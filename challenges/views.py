from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if (month > len(months)):
        return HttpResponseNotFound("Invalid month!!!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args = [redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported jet!!!")
    