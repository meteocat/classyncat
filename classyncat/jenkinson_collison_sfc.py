'''
Created on 14 Jun 2017

@author: jmc
'''

import numpy as np


def jenkinson_collison_sfc(grid_slp, cenlat):

    pi = 4*np.arctan(1.)
    deg2rad = pi/180.

#   Defining the scale constant depending on the latitude: cenlat
    sfconstant = 1/(2*np.cos(deg2rad*cenlat))
    zsconstant = 1/(np.cos(deg2rad*cenlat))
    zwconst1 = np.sin(deg2rad*cenlat)/np.sin(deg2rad*(cenlat-2.5))
    zwconst2 = np.sin(deg2rad*cenlat)/np.sin(deg2rad*(cenlat+2.5))

#   Calculation of Jenkinson-Collison for all the days

    classificacio = {}

    for dia in grid_slp.keys():
        # Change scale pressure (Pa -> hPa )
        pres = np.array(grid_slp[dia])/100.

        # Wind components
        w = (1./4.)*(pres[6]+2*pres[7]+pres[8]) - \
            (1./4.)*(pres[0]+2*pres[1] + pres[2])
        s = sfconstant*((1./4.)*(pres[2]+2*pres[5] + pres[8])-(1./4.) *
                        (pres[0]+2*pres[3]+pres[6]))

        # Angle and strenght of the flux
        d = np.arctan(w/s)*(180/pi)
        f = np.sqrt(pow(w, 2)+pow(s, 2))

        # Vorticity calculations
        zw = zwconst1*((pres[6]+2*pres[7]+pres[8]) -
                       (pres[3]+2*pres[4]+pres[5])) -  \
            zwconst2*((pres[3]+2*pres[4]+pres[5]) -
                      (pres[0]+2*pres[1]+pres[2]))
        zs = zsconstant*(0.25*(pres[2]+2*pres[5]+pres[8]) -
                         0.25*(pres[1]+2*pres[4]+pres[7]) -
                         0.25*(pres[1]+2*pres[4]+pres[7]) +
                         0.25*(pres[0]+2*pres[3]+pres[6]))
        z = zw+zs

        # Zonal fluxes

        if (d >= -22.5 and d < 22.5):
            if (s > 0):
                direccio = 'S'
            else:
                direccio = 'N'
        if (d >= 22.5 and d < 67.5):
            if (w > 0):
                direccio = 'SW'
            else:
                direccio = 'NE'
        if (d >= 67.5 and d <= 112.5):
            if (w > 0):
                direccio = 'W'
            else:
                direccio = 'E'
        if (d >= -67.5 and d < -22.5):
            if (w > 0):
                direccio = 'NW'
            else:
                direccio = 'SE'
        if (d >= -112.5 and d < -67.5):
            if (w > 0):
                direccio = 'W'
            else:
                direccio = 'E'

        if (np.abs(z) < f):
            tipus = direccio

        if (np.abs(z) > 2*f):
            if (z > 0):
                tipus = 'C'
            else:
                tipus = 'A'
        if (np.abs(z) > f and np.abs(z) < 2*f):
            if (z > 0):
                tipus = 'C'+direccio
            else:
                tipus = 'A'+direccio
        if (f < 6 and np.abs(z) < 6):
            tipus = 'U'

        classificacio[dia] = tipus

    return classificacio
