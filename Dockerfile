FROM python:3.9-slim-buster

COPY ./requirements.txt ./requirements.txt

RUN apt-get update && \
    apt-get install git gcc -y -q && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache/pip/* && \
    apt-get clean

RUN mkdir /app

RUN groupadd -g 3998 endermanhelper && \
    useradd -r -u 3998 -g endermanhelper endermanhelper

RUN mkdir -p /home/endermanhelper

RUN chown -R endermanhelper:endermanhelper /home/endermanhelper

WORKDIR /app

RUN chown -R endermanhelper:endermanhelper /app

COPY cogs /app/cogs
COPY utils /app/utils
COPY main.py /app
COPY requirements.txt /app

USER endermanhelper

RUN pip install -r requirements.txt --no-cache-dir
CMD ["python", "main.py"]