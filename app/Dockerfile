FROM python:3.8-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apk add --update \
        && apk add postgresql-dev gcc python3-dev musl-dev \
                build-base \
                linux-headers \
                py3-cffi \
                py3-cryptography \
                libffi-dev \
                ca-certificates \
                && update-ca-certificates \
                && pip3 install grpcio bcrypt \
                && rm -rf /var/cache/apk/*

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
