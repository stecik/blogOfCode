# blogOfCode
Simple blogging app built with django, django rest framework, vue.js 3, postgres and docker

# Installation guide
```
git clone https://github.com/stecik/blogOfCode.git blogOfCode
cd blogOfcode
docker compose up --build
docker compose exec python manage.py migrate
docker compose exec python manage.py createsuperuser
```
backend: localhost:8000

frontend: localhost:5173

go to localhost:8000/admin and create some article categories

then go to localhost:5173 and create an account and you can use the app
