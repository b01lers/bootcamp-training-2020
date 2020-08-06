#!/usr/bin/env python3

import MySQLdb
import random

db = MySQLdb.connect(host='localhost', user='root', passwd='root_pass_is_toor', db='part1_db')
cur = db.cursor()
root_queries = [
    "CREATE DATABASE part2_db",
    "CREATE USER 'part1'@'localhost' IDENTIFIED BY 'pass_for_part1';",
    "CREATE USER 'part2'@'localhost' IDENTIFIED BY 'pass_for_part2';",
    "GRANT SELECT ON part1_db.* TO 'part1'@'localhost';",
    "GRANT SELECT ON part2_db.* TO 'part2'@'localhost';",
    "CREATE TABLE basic_table (id SMALLINT NOT NULL, name VARCHAR(40), age INTEGER)",
    "CREATE TABLE basic_table_names (id SMALLINT NOT NULL, four_letter_name CHAR(4))",
    "CREATE TABLE flag_table (flag CHAR(40))",
    ]

for query in root_queries:
    cur.execute(query)

four_letter_names = ['Abel', 'Abby', 'Abie', 'Adah', 'Acey', 'Adda', 'Acie', 'Adel', 'Adam', 'Aida', 'Adan', 'Aili', 'Aden', 'Alba', 'Adin', 'Alda', 'Ajay', 'Alex', 'Alan', 'Alia', 'Effa', 'Dock', 'Elba', 'Doll', 'Elda', 'Donn', 'Elia', 'Dora', 'Elin', 'Dorr', 'Ella', 'Doss', 'Elle', 'Doug', 'Elma', 'Lott', 'Maud', 'Love', 'Maya', 'Loyd', 'Maye', 'Luca', 'Meda', 'Lucy', 'Mell', 'Luis', 'Mena', 'Luka', 'Meta', 'Reid', 'Sula', 'Remy', 'Suzy', 'Rene', 'Taja', 'Reno', 'Tami', 'Rhys', 'Tana', 'Rian', 'Tara']

cur.execute("INSERT INTO flag_table (flag) VALUES ('b0ctf{you_found_the_flag!}');")

for i, name in enumerate(four_letter_names):
    cur.execute("INSERT INTO basic_table_names (id, four_letter_name) VALUES ('" + str(i) + "', '" + name + "');")

    name = ''
    age = 0
    for j in range(random.randint(20, 30)):
        age = random.randint(0, len(four_letter_names)-1)
        name += four_letter_names[age][random.randint(0, 3)]

    cur.execute("INSERT INTO basic_table (id, name, age) VALUES ('" + str(i) + "', '" + name + "', '" + str(age) + "');")

cur.close()
db.commit()
db.close()

db = MySQLdb.connect(host='localhost', user='root', passwd='root_pass_is_toor', db='part2_db')
cur = db.cursor()
cur.execute("CREATE TABLE books (id SMALLINT NOT NULL, title VARCHAR(40), author VARCHAR(40), chapters INTEGER, pages INTEGER)")
books = [
        ('David Copperfield', 'Charles Dickens', 64, 624),
        ('Hamlet', 'William Shakespeare', 5, 500),
        ('The Sun Also Rises', 'Ernest Hemingway', 19, 260),
        ('Catch 22', 'Joseph Heller', 42, 453),
        ('To Kill a Mockingbird', 'Harper Lee', 31, 296),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 9, 218),
        ('Pride and Prejudice', 'Jane Austen', 61, 432),
        ('Crime and Punishment', 'Fyodor Dostoyevsky', 38, 545),
        ('The Grapes of Wrath', 'John Steinbeck', 30, 464),
        ('Lord of the Flies', 'William Golding', 12, 224)
    ]

for i, book in enumerate(books):
    cur.execute("INSERT INTO books (id, title, author, chapters, pages) VALUES ('" + str(i) + "', '" + book[0] + "', '" + book[1] + "', '" + str(book[2]) + "', '" + str(book[3]) + "');")

cur.close()
db.commit()
db.close()
