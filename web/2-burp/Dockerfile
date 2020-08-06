FROM python:3.7-alpine
RUN pip3 --no-cache-dir install flask
RUN mkdir -p /challenge/templates
COPY static /challenge/static/
COPY templates /challenge/templates
COPY server.py /challenge
EXPOSE 5000
WORKDIR /challenge
CMD ["python3", "server.py"]
