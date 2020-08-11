#!/bin/bash

cd /var/www/4-php/
exec php -S localhost:5004 > /home/b00tc4mp/web/logs/4-php.log 2>&1 &
