from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Greeting

import pickle
import logging
import json

logger = logging.getLogger(__name__)

LIN_REG_SUPERVISED = "./hello/ML/lin_reg_sup.pkl"
SENTIMENT = "./hello/ML/sentiment.pkl"

# Import our machine learning model here.
model = pickle.load(open(LIN_REG_SUPERVISED, 'rb'))
sentiment = pickle.load(open(SENTIMENT, 'rb'))

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


    # TODO(Nate): get all the weights from the model
    weights = get_sentence_weights(sent_vec)

    return JsonResponse({
        "sentence": sentence,
        "pred": str(pred),
        "weights": weights
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
        weights[str(rep)] = model.best_estimator_.coef_[0][index]
    return weights
