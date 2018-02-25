#!/usr/bin/python
import sys
import Adafruit_DHT
import datetime
import time
#from flask import Flask

#app = Flask(__name__)

#@app.route("/")
#def grabExternalData():
i = 0;
listData = [];
while i < 10:
    time.sleep(5);
    humidity, temperature = Adafruit_DHT.read_retry(11, 4);
    t = datetime.datetime.now();
    currentday = t.today();
    tempString = 'Temp: {} C  Humidity: {} %  Date/time: {}'.format(temperature, humidity, t);
    listData.append(tempString);
    print tempString;
    i = i+1; 
file = open("OutputFile.txt", 'a+');
for x in range(0, len(listData)):
	file.write(listData[x]);
	file.write("\n");
file.close();
#if __name__ == "__main__":
	
	#app.run()
