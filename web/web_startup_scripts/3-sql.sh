#!/bin/bash

service mysql start > /home/b00tc4mp/web/logs/3-sql.log

exec /var/www/3-sql/entrypoint.sh >> /home/b00tc4mp/web/logs/3-sql.log 2>&1 &
