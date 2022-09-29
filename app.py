
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#DATABASE#
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(engine, reflect=True) 

# Save references to each table
measurement = base.classes.measurement
station = base.classes.station

#create session to db
session = Session(engine)


#flask routes#
app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"SurfsUp Climate API</br></br></br>"
        f"Available Endpoints:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """
    Returns: precipitation data
    """
    one_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # query to retrieve the data and precipitation scores
    precip_one_year = session.query(measurement.date, measurement.prcp).filter(measurement.date >= one_year).all()

    session.close()
    #convert the query results to a dictionary
    precip = {date: prcp for date, prcp in precip_one_year}
    #returns json'ed dict
    return jsonify(precip);


@app.route("/api/v1.0/stations")
def stations():
    """
    Returns: list of station names
    """
    results = session.query(station.station).all()

    session.close()
    
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


@app.route("/api/v1.0/tobs")
def tob_yearly():
    """
    Returns: tob (temperature observed) for one year for the most active station(USC00519281)
    """
    
    one_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    
    temp_one_year = session.query(measurement.tobs).\
        filter(measurement.station == 'USC00519281').\
        filter(measurement.date >= one_year).all()

    session.close()
    temps = list(np.ravel(temp_one_year))

    # Return results
    return jsonify(temps=temps)


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def get_statistics(start, end):
    """
    Return TMIN, TAVG, and TMAX
    """
    
    selects = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]

    
    if not end:
        start = dt.datetime.strptime(start, "%m%d%Y")
        results = session.query(*selects).\
            filter(measurement.date >= start).all()

        session.close()

        temps = list(np.ravel(results))
        return jsonify(temps)

    start = dt.datetime.strptime(start, "%m%d%Y")
    end = dt.datetime.strptime(end, "%m%d%Y")

    results = session.query(*selects).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).all()

    session.close()

    temps = list(np.ravel(results))
    return jsonify(temps=temps)


if __name__ == '__main__':
    app.run()
