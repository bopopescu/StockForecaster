# StockFinalProject
Note: Before you can create the backend project, you need to install some requirements on your development machine. For Django, you need to have Python 3, PIP, and venv installed.

Bootstrap:

$cd stockforecast

$source ./bin/activate

$pip install django

$pip install djangorestframework

$pip install pymysql

$pip install django-cors-headers

and $pip install alpha-vantage

$pip install arrow

$pip install numpy

Setup MySQL Database Connection with 
Hostname: 127.0.0.1  port:3306
username: 'root' password: 'l1234567'    
Create a schema: 'ece568project'

Then hook up django with mysql database:

$cd stockForecastREST

$python manage.py migrate demo

Run up the server:

$python manage.py runserver --noreload 8080

Then use postman to test API:

1. post the historical data 
POST http://localhost:8080/api/demo/historicaldata
{
	 "symbol": "BLBL",
     "time": "2017-02-17",
     "open": 11.3,
     "high": 12.3,
     "low": 10.1,
     "close":11.3,
     "volume": 10


}

2.  get all the historical data
GET http://localhost:8080/api/demo/historicaldata

3. get the forecast data of a specific stock(e.g. GOOG) 
GET http://localhost:8080/api/forecast/historical/GOOG

4. delete all the historical data
DELETE http://localhost:8080/api/demo/historicaldata


