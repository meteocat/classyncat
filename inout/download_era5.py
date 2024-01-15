#!/usr/bin/env python
import cdsapi
import calendar
import os
  
cwd = os.getcwd()
os.chdir(cwd+'/data')

c = cdsapi.Client()


for year in range(2021, 2022):
    print ('YEAR ',year)
    for month in range(10,12):
        dies_calendari=calendar.monthcalendar(year,month)
        dies=[dia for dies_setmana in dies_calendari for dia in dies_setmana]

        c.retrieve('reanalysis-era5-single-levels', {
            'product_type': 'reanalysis',
            'area' : [50, -20, 30, 10], # North, West, South, East. Default: global
            'format': 'grib',
            #'grid': [5.0, 5.0], # Latitude/longitude grid: east-west (longitude) and north-south resolution (latitude). Default: 0.25 x 0.25
            'year': year,
            'variable': 'mean_sea_level_pressure',
            'month': month,
            'day': dies,
            'time': '00:00',
        },
        "era5_daily_slp_%04d%02d.grb" % (year, month))


        c.retrieve('reanalysis-era5-pressure-levels', {
            'area': [50, -20, 30, 10], # North, West, South, East. Default: global
            'product_type': 'reanalysis',
            'format': 'grib',
            #'grid': [5.0, 5.0], # Latitude/longitude grid: east-west (longitude) and north-south resolution (latitude). Default: 0.25 x 0.25
            'variable': 'geopotential',
            'pressure_level': '500',
            'year': year,
            'month': month,
            'day': dies,
            'time': '00:00',
        },
        "era5_daily_500_%04d%02d.grb" % (year, month))


