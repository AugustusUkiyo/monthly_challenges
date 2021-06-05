from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    'january' : "This works january!",
    'february' : "february",
    'march' : "march hello !",
    'april' : "april ??",
    'may' : "may",
    'june' : "june",
    'july' : 'july',
    'august' : 'august',
    'september' : 'september',
    'october' : "october",
    'november' : 'november',
    'december' : None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months" : months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('<h1>This month is not supported! Number must be in 1 - 12</h1>')
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month_name" : month
        })
    except:
        raise Http404()
    