from ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install python3 python3-mysqldb mysql-client mysql-server python3-pip curl php -y

RUN pip3 --no-cache-dir install flask

COPY web/. /var/www/

WORKDIR /home/b00tc4mp/

COPY web/web_startup_scripts web

RUN mkdir -p web/logs

ENTRYPOINT ["/bin/bash"]
