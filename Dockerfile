FROM python:3.7.5 AS python_env
RUN mkdir /src
COPY requirements.txt /src/
WORKDIR /src/
RUN pip3 install -r requirements.txt
COPY . .

FROM nginx/unit:1.13.0-python3.5
COPY --from=python_env /src/ /src/
