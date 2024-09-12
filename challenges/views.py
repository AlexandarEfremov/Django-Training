from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


# def january(request): #takes a request and sends back a response
#     return HttpResponse("This works!") #here we pass the data we'd like to send to the client
#
#
# def february(request):
#     return HttpResponse("Don't eat carbs")


def monthly_challenge(request, month): # this can dynamically enter the text
    challenge_dict = {
        "january": "Don't eat carbs",
        "february": "Clean up the shed",
        "march": "Study more Django",
        "april": "Read one book",
        "may": "Go on a field trip",
        "june": "Star exercising",
        "july": "Go on a vacation",
        "august": "Learn a new language",
        "september": "Prepare kids for school",
        "october": "Code more",
        "november": "Go on a concert",
        "december": "Try a musical instrument"
    }
    if month in challenge_dict:
        challenge_text = challenge_dict[month]
    else:
        return HttpResponseNotFound("This month is not supported")

    return HttpResponse(challenge_text)
#