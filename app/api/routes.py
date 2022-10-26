from flask import Blueprint
import logging
from sqlalchemy import extract
from ..models import Weather, Yield
from flask import jsonify
from datetime import datetime
from ..search import upload_search


api = Blueprint('api',__name__,url_prefix='/api')
logger = logging.getLogger(__name__)

'''
Returns data from station code and date 
It shows weather details station code and date wise
'''
@api.route('/weather/<station_code>/<date>')
def weather_details(station_code, date):
    try:
        date_stamp = datetime.strptime(date,
                                '%Y%M%d').date()
        objs = Weather.query.filter((Weather.station == station_code), (Weather.date == date_stamp)).all()
        json_data = {}
        if len(objs) > 0:
            for obj in objs:
                json_data['id'] = obj.id
                json_data['station'] = obj.station
                json_data['max_temp'] = obj.max_temp
                json_data['min_temp'] = obj.min_temp
                json_data['precipitation'] = obj.precipitation
                json_data['date'] = obj.date
        return json_data
    except Exception as exc:
        return ({
            'message': "Error retrieving data. :{}".format(str(exc))
            }, 500)

"""This is the way to find avg max_temp for a year for a station code"""
@api.route('/avg/maxtemp/<station_code>/<year>')
def avg_max_temp(station_code, year):
    try:
        objs = Weather.query.filter((Weather.station == station_code)&(extract('year', Weather.date) == year)).all()
        counter, total = 0, 0
        if len(objs) > 0:
            for obj in objs:
                if obj.max_temp is not None:
                    counter += 1
                    total += obj.max_temp
            msg = f"Avg value of max_temp for {station_code} for year {year} is : {total / counter} celsius"

        else:
            msg = "No data found. Please verify the station_code and year."
        return msg
    except Exception as exc:
        logger.error(str(exc))
    finally:
        upload_search(station_code, year, "Logic from avg_max_temp method")

'''
his is the way to find avg min_temp for a year for a station code
'''
@api.route('/avg/mintemp/<station_code>/<year>')
def avg_min_temp(station_code, year):
    try:
        objs = Weather.query.filter((Weather.station == station_code)&(extract('year', Weather.date) == year)).all()
        counter, total = 0, 0
        if len(objs) > 0:
            for obj in objs:
                if obj.min_temp is not None:
                    counter += 1
                    total += obj.min_temp
            msg = f"Avg value for min_temp of {station_code} for year {year} is : {total / counter} celsius"

        else:
            msg = "No data found. Please verify the station_code and year."
        return msg
    except Exception as exc:
        logger.error(exc)
    finally:
        upload_search(station_code, year,"Logic from avg_min_temp method")
        pass


'''
This calculates the average precipitation
The function takes the station code and year as argument
This method is to find avg min_temp for a year for a area code
'''

@api.route('/avg/precipitation/<station_code>/<year>')
def avg_precipitation(station_code, year):
    try:
        objs = Weather.query.filter((Weather.station == station_code)&(extract('year', Weather.date) == year)).all()
        counter, total = 0, 0
        if len(objs) > 0:
            for obj in objs:
                if obj.precipitation is not None:
                    counter += 1
                    total += obj.precipitation
            msg = f"Avg value for precipitation of {station_code} for year {year} is : {total / counter} cm"
        else:
            msg = "No data found. Please verify the station_code and year."
        return msg
    except Exception as exc:
        logger.error(str(exc))
    finally:
        upload_search(station_code, year,"Logic from avg_precipitation method")

'''
Returns data from year
It shows the year wise total yield
'''
@api.route('yield/<year>')
def yield_details(year):
    try:
        data = Yield.query.filter_by(yr= year).all()
        json_data = {}
        if len(data) > 0:
            for obj in data:
                json_data['year'] = obj.yr
                json_data['quantity'] = obj.qty
        return json_data
    except Exception as exc:
        return ({
            'message': "Error retrieving data. :{}".format(str(exc))
            }, 500)