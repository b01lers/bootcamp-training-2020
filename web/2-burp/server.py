#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form is not None:
            print(request.form)
            username = request.form['uname']
            password = request.form['psw']

            if not username:
                return render_template('index.html', error='Missing username')
            elif not password:
                return render_template('index.html', error='Missing password')
            if username == 'admin' and password == 'princess':
                return render_template('admin.html')
        return render_template('index.html', error='Invalid username or password')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
