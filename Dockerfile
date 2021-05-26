FROM ubuntu:20.04

MAINTAINER Kamil Marczak <kamil1marczak@gmail.com>

# Needed to be able to install python versions.
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y \
	python3.6 \
	python3.7 \
	python3.8 \
	python3.9 \
	python3-pip

WORKDIR /app

RUN python3 -m pip install -U --force-reinstall pip
RUN pip install tox