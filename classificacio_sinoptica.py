from inout.llegeix_grib_punts import llegeix_grib_punts
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
    # Calculem la latitud central que despres s'usara per J&C
    CENLAT= calcula_centre_graella(PUNTS1)
    GRID_SLP = llegeix_grib_punts(INPUT1,PUNTS1)
    GRID_500 = llegeix_grib_punts(INPUT2,PUNTS2)
    TIPUS_SFC = jenkinson_collison_sfc(GRID_SLP,CENLAT)
    TIPUS_500 = jenkinson_collison_500(GRID_500,CENLAT)
    CLASSIFICACIO= classyncat(TIPUS_SFC,TIPUS_500)
    
    
    for dia in sorted(TIPUS_500):
        #print  "%s;%s" % (dia,CLASSIFICACIO[dia])
        print ("%s;%s;%s;%s" %(dia,TIPUS_SFC[dia],TIPUS_500[dia],CLASSIFICACIO[dia]))
    pass