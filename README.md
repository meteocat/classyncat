# Classyncat #

Classyncat is a synoptic classification based on thresholds which is an evolution of the Jenkison-Collison classification adding 
the level of the 500 hPa geopotential. The resultant classification is obtained combining the surface and at 500 hPa types obtaining an objective synoptical classification
only 13 types which is straight-forward to use. The types obtained are based in the manual classification of Martin-Vide.
This classification is basically oriented to the NE of the Iberian Peninsula but could be adapted at any place in the world changing the
types to the most significative of the region of interest.
The data used are obtained from ERA5 reanalysis.

### How to install ###

* Basic installation command
* Conda environment

### How to run:

* You must configure the options in: config_classyncat.json, for indicating the grid points to use in the Jenkinson-Collison classification and the location where to put the ERA5 data.
* Before runing the classification you must change data_ini and date_end  variablles in the script synoptic_classification.py.
* For runing the classification you must run: synoptic_classification.py.
* The results obtained are saved in a csv file: "classificacio_yy1mm1dd1_yy2mm2dd2.csv  (where yy1mm1dd1 is initial data and yy2mm2dd2 is the final data)


### How to cite:

* Miró, J. R., Pepin, N., Peña, J. C., & Martin-Vide, J. (2020). Daily atmospheric circulation patterns for Catalonia (northeast Iberian Peninsula) using a modified version of Jenkinson and Collison method. Atmospheric Research, 231, 104674.
