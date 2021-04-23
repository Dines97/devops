FROM python:3.9.2-buster

COPY main.py requirements.txt employee.db /app/
WORKDIR /app/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
