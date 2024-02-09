"""Module to read ERA5 grib data.
"""

from collections import defaultdict

import numpy as np
import xarray as xr


def get_jc_grib_points(
    grib_mslp: str | xr.Dataset,
    points_mslp: list,
    grib_z500: str | xr.Dataset,
    points_z500: list,
) -> dict:
    """Read mean sea level pressure (`grib_mlsp`) and 500 hPa geopotential height
    (`grib_z500`) gribs for specified points that will later be used for the Jenkinson
    and Collison calculations.

    Args:
        grib_mslp (str | xarray.Dataset): Mean Sea Level Pressure grib file or
            xarray.Dataset.
        points_mslp (list): Grid points (lat, lon) to calculate Jenkinson-Collison
            circulation type.
        grib_z500 (str | xarray.Dataset): Geopotential Height at 500 hPa grib file or
            xarray.Dataset.
        points_z500 (str): Grid points (lat, lon) to calculate Jenkinson-Collison
            circulation type.

    Returns:
        list: Mean Sea Level Pressure and Geopotential Height at 500 hPa data at
            specified points.
    """
    if isinstance(grib_mslp, str):
        grib_mslp = xr.open_mfdataset(grib_mslp)
    elif not isinstance(grib_mslp, xr.Dataset):
        raise ValueError(
            "`grib_mslp` must be the string path to a grib file or and "
            "xarray.Dataset."
        )

    if isinstance(grib_z500, str):
        grib_z500 = xr.open_mfdataset(grib_z500)
    elif not isinstance(grib_z500, xr.Dataset):
        raise ValueError(
            "`grib_z500` must be the string path to a grib file or and "
            "xarray.Dataset."
        )

    grid_mslp = defaultdict(list)
    grid_z500 = defaultdict(list)

    for time in np.unique(grib_mslp.time.values):
        for point_coord in points_mslp:
            grid_mslp[time].append(
                float(
                    grib_mslp["msl"]
                    .sel(
                        time=time,
                        latitude=point_coord[0],
                        longitude=point_coord[1],
                        method="nearest",
                    )
                    .values
                )
            )
        for point_coord in points_z500:
            grid_z500[time].append(
                float(
                    grib_z500["z"]
                    .sel(
                        time=time,
                        latitude=point_coord[0],
                        longitude=point_coord[1],
                        method="nearest",
                    )
                    .values
                )
            )

    return grid_mslp, grid_z500
