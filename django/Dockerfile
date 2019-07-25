FROM python:3.7.4
LABEL maintainer="Eduardo Rojas Tejo <eduardo.rojast@sonda.com>"

ENV PYTHONUNBUFFERED 1

RUN mkdir /config
ADD /config/requirements.pip /config/
RUN pip install -r /config/requirements.pip
RUN rm -rf /sources
RUN mkdir /sources;

WORKDIR /sources