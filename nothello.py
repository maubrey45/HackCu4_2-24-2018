from flask import Flask
import websetup

app = Flask(__name__)

@app.route("/")
def hello():
    strout = websetup.grabExternalData()
    return strout

if __name__ == "__main__":
    app.run(host='0.0.0.0')
