### Assignment
***
**To run the application**

*Go to the project directory and type command: flask run*

**To upload weather data**

*Go to the project directory and type command: flask upload*

**To upload yield data**

*Go to the project directory and type command: flask upload_yield*

***
####Initial Project setup:
*drop tables from alembic.ini*

**Run the commands provided below:**

*flask db init*

*flask db migrate*

*flask upload (it will upload all the weather data)*

*flask upload_yield (it will upload all the yield data)*

*flask run (it will run the project and now ready to test the restful apis)*

***
#### List of Restful APIS:

* http://base_url/api/avg/maxtemp/<station_code>/<year>
* http://base_url/api/avg/mintemp/<station_code>/<year>
* http://base_url/api/avg/precipitation/<station_code>/<year>
* http://base_url/api/weather/<station_code>/<year>
* http://base_url/api/yield/<year>

***
#### Unit test:

######Keep the project running using flask run command and open another terminal and run below command.


*pytest -q tests/conftest.py*

***