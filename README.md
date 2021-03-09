1. Собрать `docker-compose build`
2. Миграции `docker-compose run web python manage.py makemigrations` `docker-compose run web python manage.py migrate`
3. Запустить `docker-compose up`