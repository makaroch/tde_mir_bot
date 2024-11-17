FROM python:3.12


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /macaroch

COPY ./requirements.txt requirements.txt
COPY ./src src
COPY ./main.py main.py
COPY .env .env
RUN pip install -r requirements.txt

CMD python main.py
