from flask import Flask, render_template

from raven.contrib.flask import Sentry

app = Flask(__name__)

sentry = Sentry(app, dsn='http://6da56a15ebc0440990a428f5084cb09f:d10a08e7c2df49bba5b8101e575e6858@dev.getsentry.net:8000/2')


@app.route('/')
def hello_error():

    # 1 / 0 #ZeroDivisionError to be sent to sentry
    return render_template("hello_world.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')