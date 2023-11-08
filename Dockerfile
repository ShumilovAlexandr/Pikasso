FROM python:3.10

RUN mkdir /pikasso

WORKDIR /pikasso

COPY mytest/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY mytest .

