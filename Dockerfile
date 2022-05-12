FROM python:3.10.1

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED 1

ARG PROJ_DIR=/Server

RUN mkdir -p ${PROJ_DIR}
COPY . ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN pip install -U pip \
    pip install -r requirements.txt

# RUN DJANGO_SUPERUSER_PASSWORD="saw654366" python manage.py createsuperuser --username root --email s.sazono23@gmail.com --noinput
COPY entry.sh /entry.sh
RUN chmod +x /entry.sh
EXPOSE 8000
ENTRYPOINT ["/entry.sh"]
