FROM ubuntu:16.04

MAINTAINER "jamesrocker@hotmail.co.uk"
WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["src/bootststrap.sh"]