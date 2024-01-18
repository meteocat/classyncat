
import xarray as xr
import numpy as np


def llegeix_grib_punts(input_dir: str, punts1: str, punts2: str) -> dict:
    """Read the gribs and calculate a grib with the data
    on the grid points that will be used for the Jenkinson
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

    # Read the grid points
    points1 = []
    points2 = []
    fp1 = open(punts1, 'Ur')
    fp2 = open(punts2, 'Ur')

    for line in fp1:
        points1.append(tuple(line.strip().split(' ')))
    for line in fp2:
        points2.append(tuple(line.strip().split(' ')))

    files_mslp = input_dir + "/era5_slp_*.grb"
    files_500 = input_dir+"/era5_500_*.grb"

    mslp_df = xr.open_mfdataset(files_mslp)
    mb500_df = xr.open_mfdataset(files_500)

    grid1 = {}
    grid2 = {}
    for time in np.unique(mslp_df.time.values):
        grid1[time] = []
        grid2[time] = []
        for lat, lon in points1:
            grid1[time].append(mslp_df['msl'].sel(time=time,
                                                  latitude=lat,
                                                  longitude=lon).values)
        for lat, lon in points2:
            grid2[time].append(mb500_df['z'].sel(time=time,
                                                 latitude=lat,
                                                 longitude=lon).values)

    return grid1, grid2
