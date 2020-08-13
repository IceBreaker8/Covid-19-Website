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
    context = {"totalCases": totalCases, "totalRecov": totalRecov, "totalDeath": totalDeath}
    return context