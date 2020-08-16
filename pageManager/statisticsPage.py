import pandas as pd
import numpy as np

totalConfirmedUrl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
deathConfirmedUrl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
recovConfirmedUrl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'


def countryList():
    countryList = []
    confirmedGlobal = pd.read_csv(
        totalConfirmedUrl, encoding='utf-8', na_values=None)
    countryList = sorted(list(set(confirmedGlobal[confirmedGlobal.columns[1]])))

    '''xAxis'''

    dataset = confirmedPerDay(confirmedGlobal)

    context = {"countryList": countryList,
               "dataset": dataset,
               "DatesNumber": DatesNumber}

    return context


def getGraphDates(toBeParsed):
    dateList = list(toBeParsed.head(0))
    extractedDateList = []
    for i in range(DatesNumber):
        extractedDateList.append(dateList[-i - 1])
    extractedDateList.reverse()
    return extractedDateList


DatesNumber = 15


def confirmedPerDay(toBeParsed):
    confirmedGlobal = pd.read_csv(
        totalConfirmedUrl, encoding='utf-8', na_values=None)
    countryList = sorted(list(set(confirmedGlobal[confirmedGlobal.columns[1]])))

    # lastDayData =>    country : data
    finalData = []
    df3 = toBeParsed[list(toBeParsed.columns[1:2]) +
                     list(list(toBeParsed.columns.values)[-DatesNumber:])]
    # TODO dataList merge with dict
    dateList = list(list(confirmedGlobal.columns.values)[-DatesNumber:])
    #############################################################
    for c in range(len(countryList)):
        allDate = []
        for i in range(len(dateList)):
            barplot = confirmedGlobal[['Country/Region',
                                       confirmedGlobal.columns[-i - 1]]]. \
                groupby('Country/Region').sum()

            barplot = barplot.reset_index()
            barplot.columns = ['Country/Region', "values"]

            countryArray = barplot['Country/Region'].values.tolist()
            numArray = barplot['values'].values.tolist()
            # print(str(dateList[-i - 1]) + "   " + str(countryArray[c]) + "   " + str(numArray[c]))
            tempList = []
            tempList.append(dateList[-i - 1])
            tempList.append(countryArray[c])
            tempList.append(numArray[c])
            allDate.append(tempList)
        finalData.append(allDate)
    return finalData
