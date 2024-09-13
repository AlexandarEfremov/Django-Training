from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


# def january(request): #takes a request and sends back a response
#     return HttpResponse("This works!") #here we pass the data we'd like to send to the client
#
#
# def february(request):
#     return HttpResponse("Don't eat carbs")

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


def index(request):
    list_items = ""
    all_months = list(challenge_dict.keys()) #we copy the code from our dict

    for month in all_months:
        month_path = reverse("month_challenge", args=[month]) # we use reverse() to construct the URL
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a><li>" #first letter is capped

    response_date = f"<ul>{list_items}</ul>"
    return HttpResponse(response_date)


def integer_months(request, month):
    all_months = list(challenge_dict.keys())  #firstly we need a list of all the keys in the dict
    if month > len(all_months): #then we check if the month is valid
        return HttpResponseNotFound("This month is not supported")
    redirect_month = all_months[month - 1] #because the user will put 1 for january
    return HttpResponseRedirect("/challenges/" + redirect_month) #this completes the url


def monthly_challenge(request, month):  # this can dynamically enter the text
    try:
        challenge_text = challenge_dict[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")



