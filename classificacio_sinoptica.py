from inout.llegeix_grib_punts import llegeix_grib_punts
from inout.write_csv import write_csv
from inout.download_era5 import download_ERA5
from utils.centre_graella import calcula_centre_graella
from classyncat.jenkinson_collison_sfc import jenkinson_collison_sfc
from classyncat.jenkinson_collison_500 import jenkinson_collison_500
from classyncat.classyncat import classyncat

import numpy as np

if __name__ == '__main__':
    
    np.seterr(divide='ignore')
    INPUT1 = './data/mslp_00.grib'
    INPUT2 = './data/500mb_00.grib'
    PUNTS1 = './data/list_points_mslp'
    PUNTS2 = './data/list_points_500mb'

    INPUT_DIR = './data/ERA5/'
    DATE_INI = "2022-02-01"
    DATE_FI = "2022-05-13"
    # Calculem la latitud central que despres s'usara per J&C
    # download_ERA5(date_ini=DATE_INI, date_fi=DATE_FI, 
    #                input_dir=INPUT_DIR)
    CENLAT = calcula_centre_graella(PUNTS1)
    GRID_SLP, GRID_500 = llegeix_grib_punts(input_dir=INPUT_DIR, 
                                            punts1=PUNTS1, punts2=PUNTS2)
    TIPUS_SFC = jenkinson_collison_sfc(GRID_SLP, CENLAT)
    TIPUS_500 = jenkinson_collison_500(GRID_500, CENLAT)
    CLASSIFICACIO = classyncat(TIPUS_SFC, TIPUS_500)

    DATE_INI = DATE_INI.replace("-", "")
    DATE_FI = DATE_FI.replace("-", "")
    CSV_FILE = 'classificacio_'+DATE_INI+'_'+DATE_FI+'.csv'
    write_csv(classificacio=CLASSIFICACIO, csv_file=CSV_FILE)
