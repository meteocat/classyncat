"""Module to read ERA5 grib data.
"""
from collections import defaultdict

import numpy as np
import xarray as xr


def get_jc_grib_points(
    grib_mslp: str, points_mslp: str, grib_z500: str, points_z500: str
) -> dict:
    """Read mean sea level pressure (`grib_mlsp`) and 500 hPa geopotential height
    (`grib_z500`) gribs for specified points that will later be used for the Jenkinson
    and Collison calculations.

    Args:
        grib_mslp (str): Mean Sea Level Pressure grib file.
        points_mslp (str): ASCII file including grid points to calculate
            Jenkinson-Collison circulation type.
        grib_z500 (str): Geopotential Height at 500 hPa grib file.
        points_z500 (str): ASCII file including grid points to calculate
            Jenkinson-Collison circulation type.

    Returns:
        list: Mean Sea Level Pressure and Geopotential Height at 500 hPa data at
            specified points.
    """
    with open(points_mslp, "Ur", encoding="utf-8") as f_p:
        points_mslp = []
        for line in f_p:
            points_mslp.append(tuple(line.strip().split(" ")))

    with open(points_z500, "Ur", encoding="utf-8") as f_p:
        points_z500 = []
        for line in f_p:
            points_z500.append(tuple(line.strip().split(" ")))

    data_mslp = xr.open_mfdataset(grib_mslp)
    data_z500 = xr.open_mfdataset(grib_z500)

    grid_mslp = defaultdict(list)
    grid_z500 = defaultdict(list)

    for time in np.unique(data_mslp.time.values):
        for lat, lon in points_mslp:
            grid_mslp[time].append(
                float(
                    data_mslp["msl"]
                    .sel(time=time, latitude=lat, longitude=lon, method="nearest")
                    .values
                )
            )
        for lat, lon in points_z500:
            grid_z500[time].append(
                float(
                    data_z500["z"]
                    .sel(time=time, latitude=lat, longitude=lon, method="nearest")
                    .values
                )
            )

    return grid_mslp, grid_z500
