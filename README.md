## **Classyncat: A Synoptic Classification Method**

*Classyncat* is a synoptic classification method based on thresholds, representing an evolution of the Jenkison-Collison classification.
This approach introduces the incorporation of the 500 hPa geopotential level. The resulting classification is achieved by combining surface
and 500 hPa types, yielding an objective synoptical classification with only 13 types, making it straightforward to use.

While primarily oriented to the northeast of the Iberian Peninsula, this classification method can be adapted for use in any location worldwide
by adjusting the types based on the most significant patterns in the region of interest.
The data used for this classification was from ERA5 reanalysis Citing the data:

*Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Thépaut, J-N. (2023): ERA5 hourly data on pressure levels from 1940 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS), DOI: 10.24381/cds.bd0915c6.*

### **How to Run**

1. **Configure Options:**
   - Edit the `config_classyncat.json` file to specify the grid points for the Jenkinson-Collison classification and the location for ERA5 data.

2. **Set Date Range:**
   - Prior to running the classification, update the variables `start_date` and `end_date` in the `synoptic_classification.py` script to define the desired period.

3. **Run the Classification:**
   - Execute the `synoptic_classification.py` script to perform the synoptic classification.

### **How to Cite**

*Miró, J. R., Pepin, N., Peña, J. C., & Martin-Vide, J. (2020). Daily atmospheric circulation patterns for Catalonia (northeast Iberian Peninsula) using a modified version of Jenkinson and Collison method. Atmospheric Research, 231, 104674.*
