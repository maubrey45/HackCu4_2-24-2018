#!/usr/bin/python
import sys
import Adafruit_DHT
import datetime
import time
from flask import Flask

def grabExternalData():
	    humidity, temperature = Adafruit_DHT.read_retry(11, 4);
	    t = datetime.datetime.now();
	    currentday = t.today();
	    tempString = 'Temp: {} C  Humidity: {} %  Date/time: {}'.format(temperature, humidity, t);
	    return tempString;
	    
if __name__ == "__main__":
    app.run()
