FROM python:2.7

ENV DJANGO_SETTINGS_MODULE src.settings

RUN mkdir /project
WORKDIR /project
ADD requirements.txt /project/

RUN pip install -r requirements.txt
RUN curl -LOk https://github.com/divio/django-cms-explorer/archive/master.tar.gz
RUN tar -xvzf master.tar.gz
RUN cp -nr django-cms-explorer-master/* .

ADD . /project

EXPOSE 80

CMD python manage.py runserver 0.0.0.0:80

