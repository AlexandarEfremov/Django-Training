from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request): #takes a request and sends back a response
    return HttpResponse("This works!") #here we pass the data we'd like to send to the client

#