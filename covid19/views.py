from django.shortcuts import render

# import overviewPage
from pageManager.overviewPage import overviewContext
from pageManager.statisticsPage import *


# Create your views here.

def home(request):
    return render(request, "covidHtml/home.html")


def overview(request):
    return render(request, "covidHtml/overview.html", overviewContext())


def map(request):
    return render(request, "covidHtml/map.html")


def stats(request,id):
    return render(request, "covidHtml/statistics.html", countryList(id))


def subs(request):
    return render(request, "covidHtml/subscription.html")


def about(request):
    return render(request, "covidHtml/about.html")
