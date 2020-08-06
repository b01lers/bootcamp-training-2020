#!/bin/sh

cd /challenge && ./db_create.py
exec /challenge/server.py
