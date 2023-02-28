from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Text January",
    "february": "Text February",
    "march": "Text March",
    "april": "Text April",
    "may": "Text May",
    "june": "Text June",
    "july": "Text July",
    "august": "Text August",
    "september": "Text September",
    "october": "Text October",
    "november": "Text November",
    "december": "Text December"
}

# Create your views here.

# def january(request):
#     return HttpResponse("This Works!!!")

# def february(request):
#     return HttpResponse("February")
def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    challenge_text = None
    if (month == "january"):
        challenge_text = "This Works for January"
    elif (month == "february"):
        challenge_text = "Learn django"
    else:
        return HttpResponseNotFound("Month is not currently supported!!!")
    return HttpResponse(challenge_text)