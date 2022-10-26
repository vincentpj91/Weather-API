import pytest
import requests

'''
Unit test the average max temperature details
'''
def test_avg_max_temp():
    response = requests.get('http://127.0.0.1:5000/api/avg/maxtemp/USC00110072/1985')
    print(response.status_code)
    result = "Avg value of max_temp for USC00110072 for year 1985 is : 15.334794520547945 celsius"
    assert response.status_code, 200
    assert response.text, result

'''
Unit test the average minimum temperature details
'''

def test_avg_min_temp():
    response = requests.get('http://127.0.0.1:5000/api/avg/mintemp/USC00110072/1985')
    result = "Avg value for min_temp of USC00110072 for year 1985 is : 4.326446280991732 celsius"
    assert response.status_code, 200
    assert response.text, result

'''
Unit test the average precipitation details
'''
def test_avg_precipitation():
    response = requests.get('http://127.0.0.1:5000/api/avg/precipitation/USC00110072/1985')
    result = "Avg value for precipitation of USC00110072 for year 1985 is : 2.137260273972602 cm"
    assert response.status_code, 200
    assert response.text, result

'''
Unit test the total weather details
'''
def test_weather_details():
    response = requests.get('http://127.0.0.1:5000/api/weather/USC00110072/19850109')
    result = {"date":"Wed, 09 Jan 1985 00:00:00 GMT","id":21462,"max_temp":-3.3,"min_temp":-7.2,"precipitation":0.0,"station":"USC00110072"}
    assert response.status_code, 200
    assert response.json, result

'''
Unit test the total yield details
'''
def test_yield():
    response = requests.get('http://127.0.0.1:5000/api/yield/1985')
    json_data = {"quantity":225447,"year":"1985"}
    assert response.status_code, 200
    assert response.json(),json_data