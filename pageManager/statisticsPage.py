import pandas as pd
import numpy as np

totalConfirmedUrl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
deathConfirmedUrl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
recovConfirmedUrl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

DatesNumber = 9

id_dict = {}


def idDictGenerator(confirmedParam):
    barplot = confirmedParam[['Country/Region',
                              confirmedParam.columns[- 1]]]. \
        groupby('Country/Region').sum()

    barplot = barplot.reset_index()
    barplot.columns = ['Country/Region', "values"]

    countryArray = barplot['Country/Region'].values.tolist()

    id = 24867
    count = 0
    for i in range(id, id + len(countryArray)):
        id_dict[i] = countryArray[count]
        count += 1


def countryList(country_id):
    confirmedGlobal = pd.read_csv(
        totalConfirmedUrl, encoding='utf-8', na_values=None)

    idDictGenerator(confirmedGlobal)

    print(str(country_id) + "   " + str(id_dict[country_id]))  # for testing

    recovGlobal = pd.read_csv(
        recovConfirmedUrl)

    deathGlobal = pd.read_csv(
        deathConfirmedUrl)

    dates = getGraphDates(confirmedGlobal)

    cases = confirmedPerDay(confirmedGlobal, id_dict[country_id])
    recov = confirmedPerDay(recovGlobal, id_dict[country_id])
    deaths = confirmedPerDay(deathGlobal, id_dict[country_id])

    countryName = id_dict[country_id]
    context = {
        "countryName": countryName,
        "DatesNumber": DatesNumber,
        "dates": dates,
        "cases": cases,
        "recov": recov,
        "deaths": deaths,
        "DatesNumber": DatesNumber}

    idDictGenerator(confirmedGlobal)
    return context


def getGraphDates(toBeParsed):
    dateList = list(toBeParsed.head(0))
    extractedDateList = []
    for i in range(DatesNumber):
        extractedDateList.append(dateList[-i - 1])
    extractedDateList.reverse()
    return extractedDateList


def confirmedPerDay(confirmedParam, countryName):
    # lastDayData =>    country : data
    dateList = list(list(confirmedParam.columns.values)[-DatesNumber:])
    #############################################################

    finalData = []
    for i in range(len(dateList)):
        barplot = confirmedParam[['Country/Region',
                                  confirmedParam.columns[-i - 1]]]. \
            groupby('Country/Region').sum()

        barplot = barplot.reset_index()
        barplot.columns = ['Country/Region', "values"]

        countryArray = barplot['Country/Region'].values.tolist()
        numArray = barplot['values'].values.tolist()
        s = countryArray.index(countryName)
        finalData.append(numArray[s])
    finalData.reverse()
    return finalData


def getGraphDates(toBeParsed):
    dateList = list(toBeParsed.head(0))
    extractedDateList = []
    for i in range(DatesNumber):
        extractedDateList.append(dateList[-i - 1])
    extractedDateList.reverse()
    return extractedDateList
