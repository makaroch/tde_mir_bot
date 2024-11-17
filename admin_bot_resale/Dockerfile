FROM python:3.12

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim


WORKDIR /macaroch

RUN mkdir ./static && mkdir ./media

COPY admin_bot_resale admin_bot_resale
COPY admin_panel admin_panel
COPY requirements.txt requirements.txt
COPY manage.py manage.py

RUN pip install -r requirements.txt


CMD bash -c "python ./manage.py collectstatic --noinput && python ./manage.py migrate && python ./manage.py createsuperuser --noinput  && gunicorn -b 0.0.0.0:8000 admin_bot_resale.wsgi:application"