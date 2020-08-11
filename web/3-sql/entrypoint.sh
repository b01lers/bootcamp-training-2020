#!/bin/sh

cd /var/www/3-sql && ./db_create.py
./server.py
