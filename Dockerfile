FROM python:3.10

RUN mkdir /pikasso

WORKDIR /pikasso

COPY mytest/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY mytest .

RUN chmod +x  entrypoint.sh

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
