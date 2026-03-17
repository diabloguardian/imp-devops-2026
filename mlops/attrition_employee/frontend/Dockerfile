FROM python:3.12-slim

WORKDIR /app

COPY mlops/attrition_employee/frontend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mlops/attrition_employee/frontend/app.py .
COPY mlops/attrition_employee/frontend/static/ ./static/
COPY mlops/attrition_employee/frontend/templates/ ./templates/

EXPOSE 5000

CMD ["python", "app.py"]
