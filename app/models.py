from .extensions import db
from sqlalchemy_serializer import SerializerMixin

class Weather(db.Model, SerializerMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    station = db.Column(db.String)
    date = db.Column(db.Date)
    max_temp = db.Column(db.Integer)
    min_temp = db.Column(db.Integer)
    precipitation = db.Column(db.Integer)

    def __init__(self, station, date, max_temp, min_temp, precipitation):
        self.station = station
        self.date = date
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.precipitation = precipitation


class Yield(db.Model, SerializerMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    yr = db.Column(db.String(50))
    qty = db.Column(db.Integer)

    def __init__(self, yr, qty):
        self.yr = yr
        self.qty = qty

# Search results are stored
class search_results(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area_searched = db.Column(db.String)
    dt_stamp = db.Column(db.Date)
    year = db.Column(db.String)
    data = db.Column(db.String)

    def __init__(self, area_searched, dt_stamp, year, data):
        self.area_searched = area_searched
        self.dt_stamp = dt_stamp
        self.year = year
        self.data = data
