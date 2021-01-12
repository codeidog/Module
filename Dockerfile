FROM python:3.6-slim
ENV LOG_LEVEL=INFO


#Install the dependecies
RUN mkdir /opt/Module
WORKDIR /opt/Module
COPY ./requirements.txt /opt/Module
RUN pip3 install -r /opt/Module/requirements.txt

COPY ./main.py /opt/Module
COPY ./SubModule/*.py  /opt/Module/SubModule/

ENTRYPOINT gunicorn --bind "0.0.0.0:80" --log-level=$LOG_LEVEL --access-logfile - 'transfer:app'