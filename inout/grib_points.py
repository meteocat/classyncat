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
        input_dir (str): Data where the grib were saved.
        punts1 (str): ASCII file with the grid points for
        calculate Jenkinson and Collison at surface.
        punts2 (str): ASCII file with the grid points for
        calculate Jenkinson and Collison at 500 mb.

    Returns:
        dict: grid1 and grid2 are the dictionaries for sfc
        and 500 mb respectively.
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

    grid1 = defaultdict(list)
    grid2 = defaultdict(list)

    for time in np.unique(data_mslp.time.values):
        for lat, lon in points_mslp:
            grid1[time].append(
                float(
                    data_mslp["msl"]
                    .sel(time=time, latitude=lat, longitude=lon, method="nearest")
                    .values
                )
            )
        for lat, lon in points_z500:
            grid2[time].append(
                float(
                    data_z500["z"]
                    .sel(time=time, latitude=lat, longitude=lon, method="nearest")
                    .values
                )
            )

    print(grid2)

    return {"slp": grid1, "z500": grid2}
