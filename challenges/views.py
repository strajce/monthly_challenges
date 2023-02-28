from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def january(request):
#     return HttpResponse("This Works!!!")

# def february(request):
#     return HttpResponse("February")

def monthly_challenge(request, month):
    challenge_text = None
    if (month == "january"):
        challenge_text = "This Works for January"
    elif (month == "february"):
        challenge_text = "Learn django"
    else:
        return HttpResponseNotFound("Month is not currently supported!!!")
    return HttpResponse(challenge_text)