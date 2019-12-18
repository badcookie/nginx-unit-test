FROM nginx/unit:1.13.0-python3.5

RUN apt-get update
RUN apt-get install -y python3-pip

RUN mkdir /src
COPY requirements.txt /src/
WORKDIR /src/
RUN pip3 install -Ur requirements.txt
COPY app.py .
COPY config.json /var/lib/unit/conf.json

EXPOSE 8000