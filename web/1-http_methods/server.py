#!/usr/bin/env python3

from flask import Flask, request, make_response, render_template, send_file

app = Flask(__name__)


@app.route('/', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'HEAD':
        response = make_response('')
        response.headers['flag-part2'] = 'part2_'
        return response

    elif request.method == 'POST':
        if request.data is not None:
            return render_template('post.html')
        return Flask.Response('Missing body of POST')

    elif request.method == 'PUT':
        if request.data is not None:
            return render_template('put.html')
        return Flask.Response('Missing body of PUT')

    elif request.method == 'DELETE':
        return render_template('delete.html')

    elif request.method == 'OPTIONS':
        return make_response("Methods: GET, HEAD, POST, PUT, DELETE, OPTIONS\nflag part 6: 'txt}'")


@app.route('/robots.txt')
def robots():
    return send_file('robots.txt')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
