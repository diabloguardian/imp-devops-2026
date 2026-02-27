### Stage builder
FROM python:3.14-slim AS builder

WORKDIR /app

RUN pip install --upgrade pip

COPY simple-app-py/requirements.txt ./
RUN pip install -r requirements.txt

COPY simple-app-py/*.py ./
RUN rm requirements.txt


### Stage final

FROM python:3.14-slim

RUN adduser --disabled-password --gecos "" --no-create-home pyuser

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages

USER pyuser
COPY --chown=pyuser:pyuser --from=builder /app/* .

EXPOSE 5000

ENV FLASK_APP=simpleapp.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python","simpleapp.py"]
