News board API

Deployed on Heroku. Link: https://django-docker-news-project.herokuapp.com/news/post/

API have a base CRUD functionality with list of news, upvote and comment post

System have CRUD API to manage post, comments, votes and post author. Include recurring job that running once a day to reset post votes count.

API created in python3.8.2, framework-Django(Django-rest-framework)

API run in docker container + PostgreSQL database run in another container and launched with docker-compose

If you want copy and run project on your machine you must: 
1. Clone this repository

2. Add file .env with your credentials in news_project/
- DEBUG=0
- SECRET_KEY=
- DB_ENGINE=django.db.backends.postgresql
- DB_TYPE=postgres
- DB_DATABASE_NAME=your_database_name  
- DB_USERNAME=your_database_username 
- DB_PASSWORD=your_database_password
- DB_HOST=db
- DB_PORT=5432

3. Add file .env-db with your credentials in news_project/
- POSTGRES_DB=your_database_name 
- POSTGRES_USER=your_database_username 
- POSTGRES_PASSWORD=your_database_password

4. Run command
- docker-compose up

API was created with the help of Postman. In postman i created collection with all useful requests for heroku production and local development server. In collection i created all requests and enviroment variables that contains development server domen and production heroku domen

Link for my collection - https://www.getpostman.com/collections/7e8177222fffb9629feb



