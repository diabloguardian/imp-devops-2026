FROM python:latest

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=simpleapp.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python","simpleapp.py"]
