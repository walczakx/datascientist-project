FROM python:3.12-slim
#TODO run as specific user

WORKDIR /pipeline

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY *.py .

ENTRYPOINT ["python", "pipeline.py"]
