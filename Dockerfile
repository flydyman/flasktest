FROM python:3.9.4-slim

RUN adduser flasktest

WORKDIR /home/flasktest

COPY req.txt req.txt
RUN python -m venv venv
RUN venv/bin/pip install -r req.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY app.py config.py boot.sh ./
RUN chmod +x boot.sh
RUN chmod +x app.py

ENV FLASK_APP app.py

RUN chown -R flasktest:flasktest ./
USER flasktest

EXPOSE 5000
ENTRYPOINT ["/bin/bash", "./boot.sh"]
