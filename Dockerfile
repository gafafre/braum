FROM python:3.6.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update -y
RUN apt-get install -y libpq-dev 
RUN apt-get install -y python3-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2
RUN pip install psycopg2-binary
COPY . /code/

CMD python manage.py runserver 0.0.0.0:$PORT