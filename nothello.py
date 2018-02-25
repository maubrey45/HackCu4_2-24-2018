from flask import Flask, render_template
import websetup

app = Flask(__name__)

@app.route("/")
def hello():
    strout = websetup.grabExternalData()
    return strout

@app.route('/practice')
def send_practice():
        strout = websetup.grabExternalData()
        return render_template('htmltemp.html', some_key=strout)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
