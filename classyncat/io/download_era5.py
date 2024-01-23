"""Module to download data from ERA5 API.
"""
import os
from os.path import dirname, exists
from datetime import datetime

import cdsapi


def download_era5(
    start_date: datetime, end_date: datetime, area: list, output_dir: str
) -> None:
    """Download ERA5 surface and 500 hPa pressure data from Copernicus Data Store
    between two specific dates and for a specific area.

    Data: Copernicus Climate Change Service (C3S).

    Args:
        start_date (datetime): First date to download data from.
        end_date (datetime): Last date to download data from.
        area (list): Grid extension limits [North, West, South, East].
        output_dir (str): Directory where data will be downloaded.
    """
    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    out_slp_file = f"{output_dir}/era5_slp_{start_date}_{end_date}.grb"
    out_500_file = f"{output_dir}/era5_500_{start_date}_{end_date}.grb"

    if not exists(dirname(out_500_file)) or not exists(dirname(out_slp_file)):
        raise FileNotFoundError(
            f"{dirname(out_500_file)} or/and {dirname(out_slp_file)} directories"
            " do not exist."
        )

    c = cdsapi.Client()

    if os.path.exists(out_slp_file):
        print(f"{out_slp_file} already exists and SLP data is not downloaded.")
    else:
        c.retrieve(
            "reanalysis-era5-single-levels",
            {
                "product_type": "reanalysis",
                "area": area,  # North, West, South, East
                "format": "grib",
                "date": start_date + "/" + end_date,
                "variable": "mean_sea_level_pressure",
                "time": "00:00",
            },
            f"{output_dir}/era5_slp_{start_date}_{end_date}.grb",
        )

    if os.path.exists(out_500_file):
        print(f"{out_500_file} already exists and 500 hPa pressure data is "
              "not downloaded.")
    else:
        c.retrieve(
            "reanalysis-era5-pressure-levels",
            {
                "area": area,  # North, West, South, East.
                "product_type": "reanalysis",
                "format": "grib",
                "variable": "geopotential",
                "pressure_level": "500",
                "date": start_date + "/" + end_date,
                "time": "00:00",
            },
            f"era5_500_{start_date}_{end_date}.grb",
        )

    return out_slp_file, out_500_file
