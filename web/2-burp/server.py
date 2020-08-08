#!/usr/bin/env python3

from flask import Flask, request, Response, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form is not None:
            username = request.form['username']
            password = request.form['password']

            if not username:
                return render_template('index.html', error='Missing username')
            elif not password:
                return render_template('index.html', error='Missing password')
            if username == 'Rick' and password == 'hunter2':
                return render_template('rrr.html')

            response = Response(render_template('index.html', error='Check your headers for a hint...'))
            response.headers['Try This In Your Browser For It To Work'] = "Username: 'Rick' & Password = 'hunter2'"
            return response

        return render_template('index.html', error='Invalid username or password')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
