FROM python:3.11.1-alpine as builder

WORKDIR /usr/src/jks

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY .. .

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/jks/wheels -r requirements.txt

FROM python:3.11.1-alpine

RUN mkdir -p /home/jks

RUN addgroup -S app && adduser -S app -G app
ENV HOME=/home/jks
ENV APP_HOME=/home/jks/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static_back
RUN mkdir $APP_HOME/media_back
WORKDIR $APP_HOME

COPY --from=builder /usr/src/jks/wheels /wheels
COPY --from=builder /usr/src/jks/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

USER app

RUN python manage.py collectstatic --no-input;python manage.py migrate