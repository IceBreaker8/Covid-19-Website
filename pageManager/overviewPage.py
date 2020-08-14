# importing pandas
import pandas as pd
import numpy as np


def overviewContext():
    # define the three variables
    confirmedGlobal = None
    confirmedDeaths = None
    confirmedRecov = None

    confirmedGlobal = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
        encoding='utf-8', na_values=None)

    deathGLobal = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

    recoverGlobal = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

    totalCases = confirmedGlobal[confirmedGlobal.columns[-1]].sum()
    totalRecov = recoverGlobal[recoverGlobal.columns[-1]].sum()
    totalDeath = deathGLobal[deathGLobal.columns[-1]].sum()

    # convertion with the commas
    totalCases = numFormatter(str(totalCases))
    totalRecov = numFormatter(str(totalRecov))
    totalDeath = numFormatter(str(totalDeath))

    # totalCaseGraph
    xAxis = getGraphDates(confirmedGlobal)
    # totalConfirmed
    yAxisConfirmed = confirmedPerDay(confirmedGlobal)
    # totalDeaths
    yAxisDeaths = confirmedPerDay(deathGLobal)
    # totalRecov
    yAxisRecov = confirmedPerDay(recoverGlobal)

    context = {"totalCases": totalCases, "totalRecov": totalRecov, "totalDeath": totalDeath,
               "xAxis": xAxis,
               "yAxisConfirmed": yAxisConfirmed,
               "yAxisDeaths": yAxisDeaths,
               "yAxisRecov": yAxisRecov}

    return context


######################################################################
# width of the xAxis
xAxisWidth = 90


######################################################################

def numFormatter(num):
    n = list(num)
    n.reverse()
    s = ""
    for i in range(0, len(n)):
        if (i % 3 == 0 and i != 0):
            s = "," + s
        s = str(n[i]) + s
    return s


def confirmedPerDay(toBeParsed):
    # lastDayData
    confirmedPerDay = []  # last 15 days
    for i in range(xAxisWidth):
        confirmedPerDay.append(toBeParsed[toBeParsed.columns[-i - 1]].sum())
    confirmedPerDay.reverse()
    return confirmedPerDay


def getGraphDates(toBeParsed):
    dateList = list(toBeParsed.head(0))
    extractedDateList = []
    for i in range(xAxisWidth):
        extractedDateList.append(dateList[-i - 1])
    extractedDateList.reverse()
    return extractedDateList
