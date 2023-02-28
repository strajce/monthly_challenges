from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    months = list(monthly_challenges.keys())
    if (month > len(months)):
        return HttpResponseNotFound("Invalid month!!!")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported jet!!!")
    