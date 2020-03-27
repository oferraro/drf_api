FROM python:3.5.7

ENV PYTHONUNBUFFERED 1

WORKDIR /drf_src

RUN ls .

COPY ./requirements.txt $WORKDIR/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r $WORKDIR/requirements.txt

EXPOSE 8080

# CMD ["ping", "google.com"]

CMD ["/usr/local/bin/python", "/drf_src/belvoapi/manage.py", "runserver", "0.0.0.0:8080"]
