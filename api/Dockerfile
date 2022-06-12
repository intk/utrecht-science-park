FROM plone:5.2-python37

RUN apt update
RUN apt install -y vim build-essential

COPY custom.cfg /plone/instance
COPY src /plone/instance/src

RUN buildout -c custom.cfg
