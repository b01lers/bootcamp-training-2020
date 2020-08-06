#!/bin/bash

exec /var/www/2-burp/server.py > ~/web/logs/2-burp.log 2>&1 &
