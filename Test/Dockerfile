FROM python:3.6-slim
COPY ./Test /Test
COPY ./main.py /Test
COPY ./SubModule /Test/SubModule
WORKDIR /Test
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-sv", "test.py"]
CMD tail -f /dev/null