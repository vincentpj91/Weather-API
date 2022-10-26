import sqlite3
import logging
import csv
import os
from datetime import datetime
from app.extensions import db
from app.models import Weather
logger = logging.getLogger(__name__)
starttime = datetime.now()

'''
This function will insert multiple records into sql database
'''
def insertMultipleRecords(recordList):
    try:
        CHANGE_DIR = os.chdir('../../instance')
        database_path = os.getcwd() + '/'
        print(database_path)
        sqliteConnection = sqlite3.connect(database_path+'assignment.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO weather
                          (station, date, max_temp, min_temp, precipitation) 
                          VALUES (?, ?, ?, ?, ?);"""

        cursor.executemany(sqlite_insert_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into Weather table")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

'''
This function will create list of records
'''
def createbulkdata():
    Weather.query
    CHANGE_DIR = os.chdir('data/wx_data')
    BASE_DIR = os.getcwd()
    print(BASE_DIR)
    folder_path = BASE_DIR +'/'
    all_files = os.listdir(folder_path)
    insertbulkdata = []
    for each_file in all_files:
        if each_file.endswith('.txt'):
            with open(folder_path + each_file, 'r', encoding='utf8'
                      ) as weather_file:
                tsv_reader = csv.reader(weather_file, delimiter='\t'
                                        )
                for row in tsv_reader:
                    (date_stamp, max_temp, min_temp,
                     precipitation) = row
                    date_stamp = datetime.strptime(date_stamp,
                                                   '%Y%M%d').date()
                    max_temp = (None if float(max_temp)
                                        == -9999 else float(max_temp) / 10)
                    min_temp = (None if float(min_temp)
                                        == -9999 else float(min_temp) / 10)
                    precipitation = float(precipitation) / 10
                    station = each_file[:-4:]
                    insertbulkdata.append((station, date_stamp, max_temp, min_temp, precipitation))

    return insertbulkdata

def main():
    checkinsertdata = createbulkdata()
    database_data = []
    if len(checkinsertdata) > 0:
        weather_data = Weather.query.all()
        for data in weather_data:
            database_data.append((data.station, data.date, data.max_temp, data.min_temp, data.precipitation))
        if database_data == checkinsertdata:
            logger.info(f"Weather entries created : 0 and Time taken : {datetime.now() - starttime}")
            print("No data is inserted as the data is already in database")
        else:
            insertdata = []
            for element in checkinsertdata:
                if element not in database_data:
                    insertdata.append(element)
            print(insertdata)
            insertMultipleRecords(insertdata)
            logger.info(f"Weather entries created : {len(insertdata)} and Time taken : {datetime.now() - starttime}")
            print("Data is inserted in the database")
    else:
        logger.info(f"Weather entries created : 0 and Time taken : {datetime.now() - starttime}")
        print("No data is inserted in the database")

if __name__ == "__main__":
    main()