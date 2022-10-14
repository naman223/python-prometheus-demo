FROM python:3.7-alpine
RUN mkdir /application
ADD . /application
WORKDIR /application
ADD src/requirements.txt  /application
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r /application/requirements.txt; \
	apk del .build-deps;
EXPOSE 5000
VOLUME /application
CMD uwsgi --http :5000  --manage-script-name --mount /application=flask_app:app --enable-threads --processes 1