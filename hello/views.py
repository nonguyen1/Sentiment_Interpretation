from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Greeting

import pickle

# Import our machine learning model here.

model = pickle.load(open('./hello/lin_reg_unsup', 'rb'))

# Create your views here.
def index(request):
    '''Serve staic page for the main model.'''
    return render(request, "index.html")

def handle_sentiment(request):
    ''' Sends back a ajax response for the sentiment analysis
    '''
    sentence = request.GET.get('sentence', None)
#    model.
    # TODO: Perform sentiment analysis here
    return JsonResponse({"sentiment": sentence})

def devs(request):
    return render(request, "devs.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
