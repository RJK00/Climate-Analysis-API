### Hawaii Climate Analysis
The following project contains two parts: performing a basic climate analysis and designing a Flask API based on the queries developed during the analysis. 

#### Climate Analysis
In the analysis portion, Python, pandas, Matplotlib, and SQLAlchemy ORM queries were used to explore relevant climate statistics and visualizations.

#### Flask API
Tools used: Flask, SQLAlchemy, Python, HTML

Available Routes:
* `/api/v1.0/precipitation`
    * Timestamped precipitation data 

* `/api/v1.0/stations`
    * list of stations from the dataset.

* `/api/v1.0/tobs`
    * temperature observations(TOBS) for the previous year.

* `/api/v1.0/<start>` 
            and 
* `/api/v1.0/<start>/<end>`
    *List of the minimum temperature, the average temperature, and the maximum temperature beginning at a start date onwards or between a date range



### References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, [https://doi.org/10.1175/JTECH-D-11-00103.1](https://doi.org/10.1175/JTECH-D-11-00103.1)
