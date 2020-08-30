import pandas as pd
import numpy as np

totalConfirmedUrl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
deathConfirmedUrl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
recovConfirmedUrl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

DatesNumber = 9

id_dict = {}

ids = ["004", "008", "012", "020", "024", "028", "032", "051", "036", "040"
    , "031", "044", "048", "050", "052", 112, "056", "084", 204, "064", "068", "070", "072", "076", "096"
    , 100, 854, "000", 108, 132, 116,
       120, 124, 140, 148, 152, 156, 170, 174, 178, 180, 188, 384, 191, 192, 196, 203, 208, 0000, 262, 212, 214, 218,
       818, 222, 226,
       232, 233, 748, 231, 242, 246, 250, 266, 270, 268, 276, 288, 300, 308, 320, 324, 624, 328, 332, 336, 340, 348,
       352, 356, 360, 364, 368, 372,
       376, 380, 388, 392, 400, 398, 404, 410, 383, 414, 417, 418, 428, 422, 426, 430, 434, 438, 440, 442, 00000, 450,
       454, 458, 462, 466, 470, 478,
       480, 484, 498, 492, 496, 499, 504, 508, 516, 524, 528, 554, 558, 562, 566, 807, 578, 512, 586, 591, 598, 600,
       604, 608, 616, 620, 634, 642, 643,
       646, 659, 662, 670, 674, 678, 682, 686, 688, 690, 694, 702, 703, 705, 706, 710, 728, 724, 144, 729, 740, 752,
       756, 760, 158, 762,
       834, 764, 626, 768, 780, 788, 792, 840, 800, 804, 784, 826, 858, 860, 862, 704, 970, 732, 887, 894, 716]


def idDictGenerator(confirmedParam):
    barplot = confirmedParam[['Country/Region',
                              confirmedParam.columns[- 1]]]. \
        groupby('Country/Region').sum()

    barplot = barplot.reset_index()
    barplot.columns = ['Country/Region', "values"]

    countryArray = barplot['Country/Region'].values.tolist()

    for i in range(len(ids)):
        id_dict[str(ids[i])] = countryArray[i]
    print(id_dict)

def countryList(country_id):
    confirmedGlobal = pd.read_csv(
        totalConfirmedUrl, encoding='utf-8', na_values=None)

    idDictGenerator(confirmedGlobal)

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
