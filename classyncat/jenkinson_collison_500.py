from eccodes import *
import numpy as np

from inout.llegeix_grib_punts import llegeix_grib_punts
from utils.centre_graella import calcula_centre_graella




def jenkinson_collison_500(grid_slp,cenlat):
     
    pi=4*np.arctan(1.)
    deg2rad=pi/180.
           
#   Definim constants de correcio d'escala que dependran de la latitud
#   sobre la qual tenim centrada la graella: cenlat

#      Constant que relaciona la longitut del meridia amb el paralel
#      el 2 apareix perque amb Jenkinson collison tal com l'hem definit,
#      fem anar 2 arcs de paralel per cada arc de meridia pel calcul
#      de cada una de les respectives direccions del vent 

    sfconstant=1/(2*np.cos(deg2rad*cenlat))
    
#     La mateixa constant que abans pero per la vorticitat amb la qual 
#     usem el mateix numero de meridians que de paralels pes calcular
#     les dues direccions

    zsconstant=1/(np.cos(deg2rad*cenlat))
#
#    La vorticitat zonal va multiplicada per uns factors que depenen
#    del sinus de la latitud. Se suposa que aixo es fa per compensar que
#    com mes prop del pol, l'area que hi ha entre dos meridians es menor
#    a mesura que ens acostem al pol i l'hem de compensar. El 2.5 es posa
#    perque es la meitat de la distancia en que estan separats els 
#    paralels
#    
    zwconst1=np.sin(deg2rad*cenlat)/np.sin(deg2rad*(cenlat-2.5))
    zwconst2=np.sin(deg2rad*cenlat)/np.sin(deg2rad*(cenlat+2.5))

# Calcularem el Jenkinson-Collison per cada un dels dies i ho posarem en un diccionari

    classificacio={}

    for dia in grid_slp.keys():
        # Treballem amb dam
        pres=np.array(grid_slp[dia])/10.
        
#     Calculem el vent a partir de les diferencies de pressio
        w=(1./4.)*(pres[6]+2*pres[7]+pres[8])-(1./4.)*(pres[0]+2*pres[1]+pres[2])
        s=sfconstant*((1./4.)*(pres[2]+2*pres[5]+pres[8])-(1./4.)*(pres[0]+2*pres[3]+pres[6])) 

#     Calculem l'angle i la forsa del flux        
        d=np.arctan(w/s)*(180/pi)
        f=np.sqrt(pow(w,2)+pow(s,2)) 
        
#    Calcul de la vorticitat de cisalladura a partir de les diferencies  
#    de vent al llarg de la vertical
        
        zw=zwconst1*((pres[6]+2*pres[7]+pres[8])-(pres[3]+2*pres[4]+pres[5]))-  \
           zwconst2*((pres[3]+2*pres[4]+pres[5])-(pres[0]+2*pres[1]+pres[2]))       
        
        zs=zsconstant*(0.25*(pres[2]+2*pres[5]+pres[8])-0.25*(pres[1]+2*pres[4]+pres[7])- \
                       0.25*(pres[1]+2*pres[4]+pres[7])+0.25*(pres[0]+2*pres[3]+pres[6]))
        
       
        
        z=zw+zs
        
        # Fluxos zonals
        
        if (d>=-22.5 and d<22.5):
            if (s>0):
                direccio='S'
            else:
                direccio='N'
        if (d>=22.5 and d<67.5):
            if (w>0):
                direccio='SW'
            else:
                direccio='NE'
        if (d>=67.5 and d<=112.5):
            if (w>0):
                direccio='W'
            else:
                direccio='E'
        if (d>=-67.5 and d<-22.5):
            if (w>0):
                direccio='NW'
            else:
                direccio='SE'
        if (d>=-112.5 and d<-67.5):
            if (w>0):
                direccio='W'
            else:
                direccio='E'                
#
#  El llindar per cassos anticiclonis i cassos ciclonics
#  el fem diferent, en el cas ciclonic som menys retrictius
#  i amb poca corbatura ja ho considerem ciclonic. Amb 
#  anticiclo agafem el mateix criteri que J&C original.
#

        # Cas ciclonic
        if (z>0):
            if (np.abs(z)<=(3./8.)*f):
                tipus=direccio
            tipus=direccio

        # Cas anticiclonic
        if (z<=0):
            if (np.abs(z)<=(4./3.)*f):
                tipus=direccio

        
        if (np.abs(z)>6*f):
            if (z>0):
                tipus='C'
            else:
                tipus='A'

        # Cas ciclonic
        if (z>0):
            if (np.abs(z)>(3./8.)*f and np.abs(z)<6*f):
                tipus='C'+direccio
        #Cas anticiclonic
        if (z<=0):
            if (np.abs(z)>(4./3.)*f and np.abs(z)<6*f):
                tipus='A'+direccio  
            
        #Indeterminat
        if (f<6 and np.abs(z)<6):
            tipus='U'        
            
        classificacio[dia]=tipus
    
    return classificacio  