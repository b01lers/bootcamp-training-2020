#!/usr/bin/env python3

from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)


def query1(search):
    db = MySQLdb.connect(host='localhost', user='part1', passwd='pass_for_part1', db='part1_db')
    cur = db.cursor()
    try:
        cur.execute(search)
        results = cur.fetchall()
        cur.close()
        db.close()
        return results
    except MySQLdb.ProgrammingError:
        return 1
    except MySQLdb.OperationalError:
        return 2


def query2(search):
    db = MySQLdb.connect(host='localhost', user='part2', passwd='pass_for_part2', db='part2_db')
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM books WHERE title LIKE '%" + search + "%' AND pages <= 400;")
        results = cur.fetchall()
        cur.close()
        db.close()
        return results
    except MySQLdb.ProgrammingError:
        return 1


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/part1', methods=['GET', 'POST'])
def part1():
    if request.method == 'POST':
        search = request.form['query']
        results = query1(search)
        if results == 1:
            return render_template('part1.html', error='Invalid sql syntax')
        elif results == 2:
            return render_template('part1.html', error='Other SQL error')

        if 'basic_table_names' in search:
            processed_results = ['basic_table_names']
        else:
            processed_results = ['basic_table']

        for each in results:
            processed_results.append(each)

        return render_template('part1.html', results=processed_results)
    return render_template('part1.html', results='none')


@app.route('/part2', methods=['GET', 'POST'])
def part2():
    if request.method == 'POST':
        search = request.form['query']
        results = query2(search)

        if results == 1:
            return render_template('part2.html', error='Invalid sql syntax')

        flag=False
        for each in results:
            if each[0] == 0:
                flag = True

        if flag:
            return render_template('part2.html', flag=flag, results=results)

        return render_template('part2.html', results=results)

    results = query2('')
    return render_template('part2.html', results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
