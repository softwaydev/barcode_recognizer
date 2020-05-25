FROM python:3.6

EXPOSE 8080
ENTRYPOINT ["/usr/bin/dumb-init", "--"]

VOLUME /data/
VOLUME /conf/
VOLUME /static/

RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get update && apt install -y libzbar0 dumb-init

ADD requirements.txt .
RUN pip install -r requirements.txt

COPY . /opt/app
WORKDIR /opt/app

RUN ./manage.py collectstatic --noinput && ln -s /static static

CMD gunicorn project.wsgi --bind=0.0.0.0:8080 --workers=5

