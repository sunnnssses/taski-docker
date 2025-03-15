# Taski

## Описание проекта
Taski - это веб-приложение для планирования задач! В нём можно добавлять, редактировать и удалять задачи. Когда задача будет выполнена - можно перенести её в список "Завершённые".

## Стек
- Python
- Django
- Django REST framework
- Nginx
- Docker
- Postgres

## Как развернуть проект
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:sunnnssses/taski.git
cd taski
```
Выполнить запуск командой
```
sudo docker compose -f docker-compose.production.yml up -d
```
После запуска применить миграцию
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
```
Выполнить сбор статики
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic

sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```

## Как развернуть проект локально

В .env файле добавить `USE_SQLLITE3 = True`

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:sunnnssses/taski.git
cd taski
```
Применить миграции
```
cd backend/
python manage.py migrate
```
Запустить бэкенд
```
python manage.py runserver
```
Запустить фронтенд
```
cd ../frontend/
npm i
npm run start
```

## Заполнение .env
Для работы проекта необходимо создать и заполнить файл .env следующими переменными окружения:
- POSTGRES_DB=foodgram
- POSTGRES_USER=foodgram_user
- POSTGRES_PASSWORD=foodgram_password
- DB_HOST=db (либо DB_HOST=localhost)
- DB_PORT=5432
- SECRET_KEY='secret_key'
- ALLOWED_HOSTS='**.***.**.***,127.0.0.1,localhost'
- CSRF_TRUSTED_ORIGINS='https://*.ddns.net'
- DEBUG=False

##### Автор:  [Щеткина Елизавета](https://github.com/sunnnssses)