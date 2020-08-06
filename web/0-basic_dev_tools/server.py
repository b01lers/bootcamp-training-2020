#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flag2.5')
def flag2():
    return render_template('flag2.5.html')


@app.route('/flag3')
def flag3():
    return render_template('flag3.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
