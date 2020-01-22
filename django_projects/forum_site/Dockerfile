FROM python:3.7

RUN apt-get update && \
    apt-get install -y \
	    nano vim binutils libproj-dev gdal-bin && \
    mkdir -p /app/logs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /requirements/
RUN pip install -r /requirements/requirements.txt

COPY . /app/

WORKDIR /app
RUN chmod +x ./manage.py ./entrypoint.sh
EXPOSE 8000

ENV USE_DOCKER yes
ENV PYTHONUNBUFFERED=0

#ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]