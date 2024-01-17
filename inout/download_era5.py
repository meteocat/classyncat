#!/usr/bin/env python
import cdsapi
import calendar
import pandas as pd
import os
import glob

import datetime as dt


def download_ERA5(date_ini, date_fi):
    cwd = os.getcwd()

    # Delete the old data
    files = glob.glob(cwd+'/data/ERA5/*')
    for f in files:
        os.remove(f)

    # We change to the directory where data will be put
    os.chdir(cwd+'/data/ERA5')

    # Call the api client
    c = cdsapi.Client()

    list_dates = pd.date_range(date_ini, date_fi, 
                               freq='BMS').strftime("%Y-%m-%d").tolist()

    if len(list_dates) == 1:
        [date1, date2] = [date_ini, date_fi]
        if (date1 != date2):
                c.retrieve('reanalysis-era5-single-levels', {
                    'product_type': 'reanalysis',
                    'area': [50, -20, 30, 10],  # North, West, South, East
                    'format': 'grib',
                    'date': date1 + '/' + date2,
                    'variable': 'mean_sea_level_pressure',
                    'time': '00:00',
                }, "era5_daily_slp_%s.grb" % date1)

                c.retrieve('reanalysis-era5-pressure-levels', {
                    'area': [50, -20, 30, 10],  # North, West, South, East.
                    'product_type': 'reanalysis',
                    'format': 'grib',
                    'variable': 'geopotential',
                    'pressure_level': '500',
                    'date': date1 + '/' + date2,
                    'time': '00:00',
                }, "era5_daily_500_%s.grb" % (date1))

    else:
        for idx in range(len(list_dates)):
            if (idx == 0):
                if (dt.datetime.strptime(list_dates[0], "%Y-%m-%d") >
                   dt.datetime.strptime(date_ini, "%Y-%m-%d")):
                    [date1, date2] = [date_ini, list_dates[1]]
                else:
                    [date1, date2] = [date_ini, list_dates[1]]
            elif (idx < len(list_dates)-1):
                [date1, date2] = [list_dates[idx], list_dates[idx+1]]
            elif (dt.datetime.strptime(list_dates[-1], "%Y-%m-%d") <
                  dt.datetime.strptime(date_fi, "%Y-%m-%d")):
                [date1, date2] = [list_dates[-1], date_fi]
            else:
                [date1, date2] = [list_dates[idx], date_fi]

            if (date1 != date2):
                c.retrieve('reanalysis-era5-single-levels', {
                    'product_type': 'reanalysis',
                    'area': [50, -20, 30, 10],  # North, West, South, East
                    'format': 'grib',
                    'date': date1 + '/' + date2,
                    'variable': 'mean_sea_level_pressure',
                    'time': '00:00',
                }, "era5_daily_slp_%s.grb" % date1)

                c.retrieve('reanalysis-era5-pressure-levels', {
                    'area': [50, -20, 30, 10],  # North, West, South, East.
                    'product_type': 'reanalysis',
                    'format': 'grib',
                    'variable': 'geopotential',
                    'pressure_level': '500',
                    'date': date1 + '/' + date2,
                    'time': '00:00',
                }, "era5_daily_500_%s.grb" % (date1))
