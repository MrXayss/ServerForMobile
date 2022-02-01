FROM python:3.10.1

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED 1

ARG PROJ_DIR=/Server

RUN mkdir -p ${PROJ_DIR}
COPY . ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN pip install -U pip

COPY entry.sh /entry.sh
RUN chmod +x /entry.sh
EXPOSE 8000
ENTRYPOINT ["/entry.sh"]