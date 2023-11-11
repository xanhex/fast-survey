FROM python:3.11-slim

WORKDIR /app

RUN mkdir ./fast_survey

COPY fast_survey/requirements.txt ./fast_survey

RUN pip install -U pip &&\
    pip install -r ./fast_survey/requirements.txt --no-cache-dir
