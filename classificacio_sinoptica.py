from inout.llegeix_grib_punts import llegeix_grib_punts
from inout.write_csv import write_csv
from inout.download_era5 import download_ERA5
from utils.calcula_graella import calcula_graella
from classyncat.jenkinson_collison_sfc import jenkinson_collison_sfc
from classyncat.jenkinson_collison_500 import jenkinson_collison_500
from classyncat.classyncat import classyncat
from utils.load_config import load_config

import numpy as np

if __name__ == '__main__':
    
    np.seterr(divide='ignore')

    DATE_INI = "2022-02-01"
    DATE_FI = "2022-05-13"

    # Read the configuration file
    config = load_config('config_classyncat.json')
    # Grid points to be used for the Jenkinson and Collison calculations
    PUNTS1 = config["mslp_grid_points"]
    PUNTS2 = config["500mb_grid_points"]

    INPUT_DIR = config["input_dir"]
    
    # Calculate the center latitude of the grid for further calculations
    # Calculate the CENLAT for mslp grid pints
    CENLAT1, CARDINALS1 = calcula_graella(PUNTS1)
    # Calculate the CENLAT for 500 mb grid pints
    CENLAT2, CARDINALS2 = calcula_graella(PUNTS2)
    # The rectangular area to obtain from ERA5 must contain
    # the points of CARDINALS1 and CARDINALS2
    AREA = [max(CARDINALS1[0], CARDINALS2[0]),
           min(CARDINALS1[1], CARDINALS2[1]),
           min(CARDINALS1[2], CARDINALS2[2]),
           max((CARDINALS1[3], CARDINALS2[3]))]

    # Download the data from ERA5
    download_ERA5(date_ini=DATE_INI, date_fi=DATE_FI,
                  input_dir=INPUT_DIR, area=AREA)
    
    CENLAT, CARDINALS = calcula_graella(PUNTS1)
    # Read the grib generated from the data downloaded
    GRID_SLP, GRID_500 = llegeix_grib_punts(input_dir=INPUT_DIR, 
                                            punts1=PUNTS1, punts2=PUNTS2)
    # Calculate the Jenkinson & Collison for sfc
    TIPUS_SFC = jenkinson_collison_sfc(GRID_SLP, CENLAT1)
    # Calculate the types for 500 mb
    TIPUS_500 = jenkinson_collison_500(GRID_500, CENLAT2)
    # Merge both classifications for obtaining a new one
    CLASSIFICACIO = classyncat(TIPUS_SFC, TIPUS_500)

    DATE_INI = DATE_INI.replace("-", "")
    DATE_FI = DATE_FI.replace("-", "")
    CSV_FILE = 'classificacio_'+DATE_INI+'_'+DATE_FI+'.csv'
    write_csv(classificacio=CLASSIFICACIO, csv_file=CSV_FILE)
