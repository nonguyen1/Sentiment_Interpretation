from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Greeting

import pickle
import logging

logger = logging.getLogger(__name__)

LIN_REG_SUPERVISED = "./hello/ML/lin_reg_sup.pkl"
EMOTION_LIN_REG_SUPERVISED = "./hello/ML/finalized_model_5(1).pkl"

SENTIMENT = "./hello/ML/sentiment.pkl"
EMOTION_SENTIMENT = "./hello/ML/sentiment_weights_model2.pkl"

# Import our machine learning model here.
model = pickle.load(open(LIN_REG_SUPERVISED, 'rb'))
sentiment = pickle.load(open(SENTIMENT, 'rb'))

emotion_model = pickle.load(open(EMOTION_LIN_REG_SUPERVISED, 'rb'))
emotion_sentiment = pickle.load(open(EMOTION_SENTIMENT, 'rb'))

# Use this model for prediction

def index(request):
    '''Staic page for the main model.'''
    return render(request, "index.html")

def handle_sentiment(request):
    ''' Sends back a ajax response for the sentiment analysis 
    To scale up send to worker queue to handle more requests.
    '''
    sentence = request.GET.get('sentence', None)

    sent_vec = parse_sentence(sentence)
    pred = model.predict(sent_vec)[0]

    weights = get_sentence_weights(sent_vec)
    class_bias = model.best_estimator_.intercept_ # Biases for each class.
    probs = model.predict_proba(sent_vec)[0]

    return JsonResponse({
        "sentence": sentence,
        "pred": str(pred),
        "weights": weights,
        "bias": str(class_bias),
        "probs": str(probs)
        })

def handle_emotion(request):
    ''' Sends back a ajax response for emotion analysis 
    To scale up send to worker queue to handle more requests.
    '''
    sentence = request.GET.get('sentence', None)

    # Vector transform for the emotion
    sent_vec = emotion_sentiment.transform([sentence])
    pred = emotion_model.predict(sent_vec)[0]

    class_bias = emotion_model.intercept_ # Biases for each class.
    probs = emotion_model.predict_proba(sent_vec)[0]

    weights = {}

    for index,rep in zip(sent_vec.indices,
            emotion_sentiment.inverse_transform(sent_vec)[0]):

        class_weights = []
        num_classes = len(emotion_model.classes_)

        for i in range(num_classes):
            class_weights.append(emotion_model.coef_[i][index])
        weights[str(rep)] = class_weights

    return JsonResponse({
        "sentence": sentence,
        "pred": str(pred),
        "weights": weights,
        "bias": str(class_bias),
        "probs": str(probs)
        })

def devs(request):
    ''' Developer information page '''
    return render(request, "devs.html")

def db(request):
    ''' Not used, don't need a database right now. '''
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

# ------------------------------------------
# Helper functions for sentiment analysis. Should move to external *.py file in
# the future.

def parse_sentence(sent):
    ''' Clean up the sentence for sentiment analysis '''
    sentence_vec = sentiment.count_vect.transform([sent])
    return sentence_vec

def get_sentence_weights(sent_vec):
    weights = {}

    #model.coef_
    #sent_vec.indices
    #sentiment.count_vect.inverse_transform(sent_vec) # what these indicies represent

    for index,rep in zip(sent_vec.indices,
            sentiment.count_vect.inverse_transform(sent_vec)[0]):
        weights[str(rep)] = model.best_estimator_.coef_[0][index];
        #weights[model.best_estimator_.coef_[0][index]] = str(rep);
    return weights;
