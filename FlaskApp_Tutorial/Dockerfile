FROM python:3.14.0-alpine3.22

COPY meme_flask.py /app/ 
COPY requirements.txt /app/
COPY templates /app/templates

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "meme_flask.py"]