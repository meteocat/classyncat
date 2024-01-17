
import xarray as xr


def llegeix_grib_punts(input_dir, punts1, punts2):

    # Read the grid points
    points1 = []
    points2 = []
    fp1 = open(punts1, 'Ur')
    fp2 = open(punts2, 'Ur')

    for line in fp1:
        points1.append(tuple(line.strip().split(' ')))
    for line in fp2:
        points2.append(tuple(line.strip().split(' ')))

    files_mslp = input_dir + "era5_daily_slp_*.grb"
    files_500 = input_dir+"era5_daily_500_*.grb"

    mslp_df = xr.open_mfdataset(files_mslp).to_dataframe()
    mb500_df = xr.open_mfdataset(files_500).to_dataframe()

    grid1 = {}
    grid2 = {}
    for time in mslp_df.index.get_level_values(0).unique():
        grid1[time] = []
        grid2[time] = []
        for lat, lon in points1:
            grid1[time].append(float(mslp_df['msl'].loc[time,
                               float(lat), float(lon)][0]))
        for lat, lon in points2:
            grid2[time].append(float(mb500_df['z'].loc[time,
                               float(lat), float(lon)][0]))

    return grid1, grid2
