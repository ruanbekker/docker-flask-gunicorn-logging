FROM python:3.8-slim

ENV PYTHONUNBUFFERED TRUE
COPY requirements.txt /src/requirements.txt

RUN pip3 install -r /src/requirements.txt
COPY bin/boot.sh /boot.sh
RUN chmod +x /boot.sh

ADD app /src/app
WORKDIR /src

ENTRYPOINT ["/boot.sh"]
