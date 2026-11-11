# Learning Log

Учебный Django-проект для хранения тем и записей. Реализованы регистрация и вход пользователей, персональные темы, добавление и редактирование записей, админ-панель, оформление Bootstrap 4, SQLite и контейнеризация через Docker Compose (Gunicorn + WhiteNoise).

## Локальный запуск

```powershell
python -m venv ll_env
.\ll_env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Откройте `http://127.0.0.1:8000/`. Админка находится на `/admin/`. Суперпользователь создаётся командой `python manage.py createsuperuser`.

## Развёртывание на сервере через Docker Compose

1. Создайте в корне проекта файл `.env` (на основе `.env.example`):

```env
DJANGO_SECRET_KEY=replace-with-a-long-random-secret
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=192.168.1.11,localhost,127.0.0.1
DJANGO_CSRF_TRUSTED_ORIGINS=http://192.168.1.11:8000
DJANGO_USE_HTTPS=False
SQLITE_PATH=/app/data/db.sqlite3
APP_BIND_IP=0.0.0.0
APP_PORT=8000
```

2. Запустите контейнер:

```bash
docker compose up -d --build
docker compose ps
docker compose logs --tail=100 web
```

3. Создайте администратора:

```bash
docker compose exec web python manage.py createsuperuser
```

Приложение будет доступно по адресу `http://<IP_сервера>:<APP_PORT>/`.

