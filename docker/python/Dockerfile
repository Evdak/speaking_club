FROM python:3.11

COPY ./speaking_club /srv/www/speaking_club
WORKDIR /srv/www/speaking_club
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt