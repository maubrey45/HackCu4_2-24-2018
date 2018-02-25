#!/usr/bin/python
import sys
import Adafruit_DHT
import datetime
import time
i = 0;
while i < 10:

    time.sleep(30);
    humidity, temperature = Adafruit_DHT.read_retry(11, 4);
    t = datetime.datetime.now();
    currentday = t.today();
    print 'Temp: {} C  Humidity: {} %  Date/time: {}'.format(temperature, humidity, t);
    i = i+1;