import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import pandas_profiling as pp
import _strptime
from datetime import datetime as dt
from xgboost import XGBRegressor
import seaborn as sn
from sklearn.metrics import mean_squared_log_error
from sklearn import linear_model
import collections


# Part I. Mutate columns based on another column
def mutate_season(x):
    if x == 1:
        return 'Spring'
    elif x == 2:
        return 'Summer'
    elif x == 3:
        return 'Autumn'
    else:
        return 'Winter'


def mutate_workday(x):
    date_time = dt.strptime(x, '%Y-%m-%d %H:%M:%S')
    return date_time.strftime('%A')


def mutate_hour(x):
    return dt.strptime(x, '%Y-%m-%d %H:%M:%S').hour


def mutate_month(x):
    return dt.strptime(x, '%Y-%m-%d %H:%M:%S').month


def mutate_day(x):
    return dt.strptime(x, '%Y-%m-%d %H:%M:%S').day


def mutate_year(x):
    return dt.strptime(x, '%Y-%m-%d %H:%M:%S').year


def mutate_weather(x):
    if x == 1:
        return 'Clear, Few clouds, Partly cloudy, Partly cloudy'
    elif x == 2:
        return 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist'
    elif x == 3:
        return 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds'
    else:
        return 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'


class data_process:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.categorical_variables = ['season', 'weather', 'weekday']  # , 'hour', 'month']
        self.numerical_variables = ['temp', 'atemp', 'humidity', 'windspeed']

    # Part II. Wrap up functions in a nutshell, depends on Part I
    def mutate_timings(self):
        data = self.raw_data.copy()
        data['season_desc'] = data['season'].apply(lambda x: mutate_season(x))
        data['weather_desc'] = data['weather'].apply(lambda x: mutate_weather(x))
        data['weekday'] = data['datetime'].apply(lambda x: mutate_workday(x))
        data['hour'] = data['datetime'].apply(lambda x: mutate_hour(x))
        data['month'] = data['datetime'].apply(lambda x: mutate_month(x))
        data['day'] = data['datetime'].apply(lambda x: mutate_day(x))
        data['year'] = data['datetime'].apply(lambda x: mutate_year(x))
        return data

    # Part III. Change Data Types then Convert into Dummy Variables
    def change_df_column_type(self):
        data = self.raw_data.copy()
        for c in self.categorical_variables:
            data[c] = data[c].astype('object')
        for n in self.numerical_variables:
            data[n] = data[n].astype('float64')
        return data

    def mutate_dummy_variables(self):  # convert into dummy variables
        data = self.raw_data.copy()
        one_hot_target = []
        for c in self.categorical_variables:
            if (data[c].nunique() <= 4):  # tune threshold for cardinality
                one_hot_target.append(c)
        for o in one_hot_target:
            new_column = pd.get_dummies(data[o], prefix=o)
            data = pd.concat([data, new_column], axis=1)
        return data

    # Part IV. More Variables based on EDA results
    def mutate_peak(self):
        data = self.raw_data.copy()
        data['is_workday_morning_peak'] = 0
        data.loc[(data['hour'] >= 7) & (data['hour'] <= 8) & (data['holiday'] == 0), 'is_workday_morning_peak'] = 1
        data['is_workday_afternoon_peak'] = 0
        data.loc[(data['hour'] >= 17) & (data['hour'] <= 18) & (data['holiday'] == 0), 'is_workday_afternoon_peak'] = 1
        data['is_workday_night_time'] = 0
        data.loc[(data['hour'] >= 22) & (data['hour'] <= 6) & (data['holiday'] == 0), 'is_workday_night_time'] = 1
        return data

    # Wrap up all cleaning processes
    def complete_wrangling(self):
        self.raw_data = self.mutate_timings()
        self.raw_data = self.change_df_column_type()
        self.raw_data = self.mutate_dummy_variables()
        self.raw_data = self.mutate_peak()
        return self.raw_data


# Evaluate prediction
def cal_rmlse(real, pred):
    return np.sqrt(mean_squared_log_error(real, pred))