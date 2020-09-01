FROM python:3.7.7-slim

WORKDIR /src

ADD requirements_test.txt requirements_test.txt
ADD requirements.txt requirements.txt

RUN pip3 install -q -r requirements.txt && \
    pip3 install -q -r requirements_test.txt

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY . /src

CMD ["gunicorn", "--pythonpath", "/src", "--access-logfile", "-", "--reload", "app:app", "-b", "0.0.0.0:5000"]
