FROM python:alpine3.6

RUN apk add --no-cache make gcc g++

RUN mkdir -p /home/finder
WORKDIR /home/finder

ADD ./finder/requirements/requirements.txt /home/finder/requirements.txt
ADD ./finder/requirements/development.txt /home/finder/development.txt
RUN pip install -r requirements.txt
RUN pip install -r development.txt

add . /home/finder

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile=-","--reload", "-R", "--env", "PYTHONUNBUFFERED=1", "-k", "gevent", "finder:app"]
