FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /home/roombambar/Desktop/project_news

COPY ./requirements.txt /home/roombambar/Desktop/project_news/news_site/requirements.txt
RUN pip install -r /home/roombambar/Desktop/project_news/news_site/requirements.txt

COPY . /home/roombambar/Desktop/project_news

CMD gunicorn news_site.wsgi:application --bind 0.0.0.0:$PORT
