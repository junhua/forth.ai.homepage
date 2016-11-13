FROM python:2.7

RUN mkdir /project
WORKDIR /project
ADD requirements.txt /project/

RUN pip install -r requirements.txt

ADD . /project

EXPOSE 80

CMD python /project/mysite/manage.py runserver 0.0.0.0:80

