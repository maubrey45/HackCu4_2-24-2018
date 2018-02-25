from flask import Flask, render_template
import websetup

app = Flask(__name__)

@app.route("/")
def hello():
    strout = websetup.grabExternalData()
    return strout

@app.route('/practice')
def send_practice():
        return render_template('practice.html', some_key=345)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
