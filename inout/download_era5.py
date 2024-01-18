#!/usr/bin/env python
import cdsapi
import os
import glob

import datetime as dt


def download_ERA5(date_ini: dt.datetime,
                  date_fi: dt.datetime, input_dir) -> None:
    """Subroutine to download the ERA5 data from Copernicus
    the data will be saved in grib format and saved in the
    input_dir directory.


    Args:
        date_ini (str): Initial data
        date_fi (str): End data
        input_dir (str): Directory where the grib that will be saved.
    """

    # Delete the old data
    files = glob.glob(input_dir+'/*')
    if files != []:
        for f in files:
            os.remove(f)

    # We change to the directory where data will be put
    os.chdir(input_dir)

    # Call the api client
    c = cdsapi.Client()

    c.retrieve('reanalysis-era5-single-levels', {
        'product_type': 'reanalysis',
        'area': [50, -20, 30, 10],  # North, West, South, East
        'format': 'grib',
        'date': date_ini + '/' + date_fi,
        'variable': 'mean_sea_level_pressure',
        'time': '00:00',
    }, "era5_slp_%s_%s.grb" % (date_ini, date_fi))

    c.retrieve('reanalysis-era5-pressure-levels', {
        'area': [50, -20, 30, 10],  # North, West, South, East.
        'product_type': 'reanalysis',
        'format': 'grib',
        'variable': 'geopotential',
        'pressure_level': '500',
        'date': date_ini + '/' + date_fi,
        'time': '00:00',
    }, "era5_500_%s_%s.grb" % (date_ini, date_fi))
