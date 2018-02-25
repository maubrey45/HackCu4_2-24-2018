#!/usr/bin/python
import sys
import Adafruit_DHT
import datetime
i = 0;
while i < 10:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4);
    time = datetime.datetime.now();
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f}  Date/time: {2:0.1f}%'.format(temperature, humidity, time);
    i = i+1;