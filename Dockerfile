FROM nginx/unit:1.13.0-python3.5

RUN apt-get update
RUN apt-get install -y python3-pip

RUN mkdir /src
COPY requirements.txt /src/
WORKDIR /src/
RUN pip3 install -Ur requirements.txt
COPY app/ app/
COPY config.json /var/lib/unit/conf.json

RUN chmod o+w app/
WORKDIR app/
RUN python3 manage.py makemigrations && python3 manage.py migrate

EXPOSE 8000
