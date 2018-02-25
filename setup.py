#!/usr/bin/python
import sys
import Adafruit_DHT
import datetime
i = 0;
while i < 10:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4);
    time = datetime.datetime.now();
    currentday = time.day
    print 'Temp: {} C  Humidity: {} %  Date/time: {}'.format(temperature, humidity, currentday);
    i = i+1;