from ubuntu:18.04

RUN apt-get update && \
    apt-get install python3 python3-mysqldb mysql-server python3-pip curl -y

RUN pip3 --no-cache-dir install flask

COPY web/. /var/www/

RUN groupadd -r -g 666 b00tc4mp33
RUN useradd -u 666 -r -m -g b00tc4mp33 b00tc4mp33

WORKDIR /home/b00tc4mp33/

COPY web/web_startup_scripts web
RUN chown -R b00tc4mp33:b00tc4mp33 web

USER b00tc4mp33

RUN mkdir -p ~/web/logs

CMD ["/bin/bash"]
