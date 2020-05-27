import datetime
import os

from flask import Flask, render_template, redirect, flash, url_for

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = os.urandom(12)

@app.route('/', methods=["GET"])
def index():

    first_time = datetime.datetime(2019, 6, 28)
    current_time = datetime.datetime.now()
    work_experience = current_time - first_time

    return render_template("index.html", active="index", time=work_experience)


if __name__ == "__main__":
    app.run()