from .models import search_results
from .extensions import db
from .models import Weather
from datetime import datetime

def upload_search(area, year, data):
    """Thsi function is to upload Search results."""
    date_now = datetime.now()
    val = search_results(area_searched= area, dt_stamp=date_now.date(), year= year, data= data)
    db.session.add(val)
    db.session.commit()