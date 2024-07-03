FROM python:3.10

ENV LANG C.UTF-8

WORKDIR /Lu_Bot

COPY . /Lu_Bot

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
