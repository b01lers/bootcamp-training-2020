FROM mysql:5.7

RUN apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-mysqldb \
    && apt-get install -y python3-pip

RUN pip3 install flask

COPY static /challenge/static/
COPY entrypoint.sh /
COPY db_create.py server.py /challenge/
COPY templates /challenge/templates
CMD ["mysqld"]
