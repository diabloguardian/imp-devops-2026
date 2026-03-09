### Stage builder
FROM python:3.14-slim AS builder

WORKDIR /app

RUN pip install --upgrade pip
#local
#COPY requirements.txt ./
#repo
COPY simple-app-py/requirements.txt ./
RUN pip install -r requirements.txt

RUN rm requirements.txt
#local
#COPY *.py ./
#repo
COPY simple-app-py/*.py ./


### Stage final

FROM python:3.14-slim

RUN adduser --disabled-password --gecos "" --no-create-home pyuser

WORKDIR /app

RUN mkdir -p /app/scripts
RUN sudo chown pyuser:pyuser /app/scripts

COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages

USER pyuser
COPY --chown=pyuser:pyuser --from=builder /app/* .

COPY --chown=pyuser:pyuser scripts/*.py /app/scripts/

EXPOSE 5000

ENV FLASK_APP=simpleapp.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python","simpleapp.py"]
