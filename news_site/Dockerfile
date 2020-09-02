FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
# ENV DEBUG 0

# install psycopg2
# RUN apt-get update \
#     && apt-get install build-deps gcc python3-dev musl-dev \
#     && apt-get install postgresql-dev \
#     && pip install psycopg2 \
#     && apt-get install --reinstall build-deps

WORKDIR /home/roombambar/Desktop/project_news

COPY ./requirements.txt /home/roombambar/Desktop/project_news/news_site/requirements.txt
RUN pip install -r /home/roombambar/Desktop/project_news/news_site/requirements.txt

COPY . /home/roombambar/Desktop/project_news

# add and run as non-root user
# RUN adduser -D myuser
# USER myuser

# run gunicorn
# CMD ["python", "manage.py", "migrate"]
CMD gunicorn news_site.wsgi:application --bind 0.0.0.0:$PORT

# EXPOSE 8000
# CMD ["python", "manage.py", "migrate"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]