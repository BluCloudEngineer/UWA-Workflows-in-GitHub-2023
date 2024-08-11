FROM python:3.10.12-alpine3.18

ENV FLASK_APP=application.py

WORKDIR /webapp

COPY static/ static/
COPY templates/ templates/
COPY application.py application.py
COPY LICENSE LICENSE
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
