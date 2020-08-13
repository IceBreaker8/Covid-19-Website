from django.shortcuts import render


#import overviewPage
from pageManager.overviewPage import overviewContext


# Create your views here.

def home(request):
    return render(request, "covidHtml/home.html")


def overview(request):
    return render(request, "covidHtml/overview.html", overviewContext())


def map(request):
    return render(request, "covidHtml/map.html")


def stats(request):
    return render(request, "covidHtml/statistics.html")


def subs(request):
    return render(request, "covidHtml/subscription.html")


def about(request):
    return render(request, "covidHtml/about.html")
