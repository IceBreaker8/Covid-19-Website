from django import views
from django.shortcuts import render, redirect

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


def stats(request, country_id):
    return render(request, "covidHtml/statistics.html", countryList(country_id))

