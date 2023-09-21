# API для проекта Yatube
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

### Реализован функционал, дающий возможность:
* Подписываться на пользователя.
* Просматривать, создавать новые, удалять и изменять посты.
* Просматривать и создавать группы.
* Комментировать, смотреть, удалять и обновлять комментарии.
* Фильтровать по полям.

### Стек:
* Python 3.9
* Django 3.2.16
* djangorestframework  3.12.4
* djangorestframework-simplejwt  4.7.2
* djoser 2.2.0

### Как запустить проект:

Склонируйте репозиторий:

```
git clone https://github.com/trsv-dev/api_final_yatube.git
```
Перейдите в папку с проектом:
```
cd api_final_yatube/
```
Установите виртуальное окружение (**если работаете в Linux**):
```
python3.9 -m venv venv
```
```
source venv/bin/activate
```
Установите виртуальное окружение (**если работаете в  Windows**):
```
python -m venv env
```
```
source env/bin/activate
```
Установите зависимости из файла **requirements.txt**:
```
pip install -r requirements.txt
```
Перейдите в папку yatube_api:
```
cd yatube_api/
```
Выполните миграции:
```
python manage.py migrate
```
Создайте суперпользователя:
```
python manage.py createsuperuser
```
В корне проекта найдите файл **.env.example**, переименуйте в **.env** и заполните своими данными.

Файл **_.env.example_** содержит следующее:
```
#Django settings:
###############################################################################
DEBUG=True
SECRET_KEY=you_need_to_set_the_secret_key
ALLOWED_HOSTS=127.0.0.1, localhost
```
Для запуска сервиса выполните команду:
```
python manage.py runserver
```
Сайт доступен по адресу http://127.0.0.1:8000

Browsable API доступно по адресу http://127.0.0.1:8000/api/v1/

Документация доступна по адресу: http://127.0.0.1:8000/redoc/


### Автор:
[trsv-dev](https://github.com/trsv-dev)