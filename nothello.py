from flask import Flask
import websetup

app = Flask(__name__)

@app.route("/")
def hello():
    strout = "Local Temperature and Humidity as of Date/Time \n" + websetup.grabExternalData()
    return strout

if __name__ == "__main__":
    app.run()