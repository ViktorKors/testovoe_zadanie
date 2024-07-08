# Описание проекта
API для постов.


## Технологии:
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)
![Django REST framework](https://img.shields.io/badge/-Django%20REST%20framework-ff9900?style=flat&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker&logoColor=white)

Для локальной разработки нужно:

1. Клонировать репозиторий и перейти в директорию:

```
git clone git@github.com:ViktorKors/testovoe_zadanie.git
```

```
cd postsproject
```

2. Создать и активировать виртуальное окружение:

```
python -m venv venv                      # Устанавливаем виртуальное окружение
source venv/scripts/activate             # Активируем (Windows); или
source venv/bin/activate                 # Активируем (Linux)
python -m pip install --upgrade pip      # Обновляем менеджер пакетов pip
pip install -r requirements.txt  # Устанавливаем пакеты для разработки
```


 Создать файл `.env` с переменными окружения из `.env.example`. Пример наполнения - непосредственно в `.env.example`. Значение DEBUG при локальной разработке  должно быть `True.`Вот как выглядит `.env` для разработки:

DEBUG=True


DJANGO_SECRET_KEY='p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs'



Для запуска приложения в контейнерах необходимо:

1. Заполнить `.env`:

```
DEBUG=False

DJANGO_SECRET_KEY=token

DJANGO_ALLOWED_HOSTS=127.0.0.1 localhost

DB_ENGINE=django.db.backends.postgresql_psycopg2
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432
```

2. Перейти в директорию с файлом _docker-compose.yaml_, открыть терминал и запустить docker-compose с ключом `-d`:

```
docker compose -f docker-compose.yml up -d
```

3. Выполнить миграции:

```
docker compose -f docker-compose.yml exec backend python manage.py migrate
```

4. Создать суперюзера:

```
docker compose -f docker-compose.yml exec backend python manage.py createsuperuser
```

5. Собрать статику:

```
docker compose -f docker-compose.yml exec backend python manage.py collectstatic --no-input
```

6. После успешного запуска проект станет доступен по адресу:


   http://localhost/api/v1 - Корень api

   http://localhost/admin - Админка Django

## Эндпоинты

### Список постов (`GET /api/v1/posts/`)

- **Описание**: Получение списка всех постов.
- **Метод**: `GET`
- **URL**: `/api/v1/posts/`
-  **Параметры запроса**: отсутствует
- **Пример ответа**:
  ```json
  [
    {
      "id": 1,
      "title": "Example Title",
      "content": "Example Content",
      "created_at": "2024-07-08T12:00:00Z",
      "updated_at": "2024-07-08T12:00:00Z"
    },
    {
      "id": 2,
      "title": "Another Example Title",
      "content": "Another Example Content",
      "created_at": "2024-07-08T12:00:00Z",
      "updated_at": "2024-07-08T12:00:00Z"
    }
  ]

### Детали поста (`GET /api/v1/posts/{id}/`)

- **Описание**: деталей конкретного поста по его идентификатору.
- **URL**:Детали поста (`/api/v1/posts/{id}/`)
- **Метод**: `GET`
- **Параметры запроса**:`id` (идентификатор поста)
- **Пример ответа**:
  ```json
  [
    {
      "id": 1,
      "title": "Example Title",
      "content": "Example Content",
      "created_at": "2024-07-08T12:00:00Z",
      "updated_at": "2024-07-08T12:00:00Z"
    },
  ]

### Создание поста (`POST /api/v1/posts/`)

Создание нового поста.

- **Метод**:`POST`
- **URL**:`/api/v1/posts/`

- **Тело запроса**:
  ```json
  [
    {
      "title": "Example Title",
      "content": "Example Content",
    },
  ]

### Удаление поста (`DELETE /api/v1/posts/{id}/`)

- **Описание**: Удаление поста по его идентификатору.
- **URL**:Детали поста (`/api/v1/posts/{id}/`)
- **Метод**: `DELETE`
- **Параметры запроса**:`id` (идентификатор поста)
- **Пример овтета**: `Код состояния: 204 No Content`


### Обновление поста (`PUT /api/v1/posts/{id}/`)

- **Описание**: Обновление всех данных поста по его идентификатору.
- **URL**:Детали поста (`/api/v1/posts/{id}/`)
- **Метод**: `PUT`
- **Параметры запроса**:`id` (идентификатор поста)
- **Пример овтета**:
  ```json
  [
    {
      "title": "Updated Example Title",
      "content": "Updated Example Content",
    },
  ]

## Документация API

Документация API доступна через Swagger и Redoc.

### Swagger

Вы можете ознакомиться с документацией API, используя Swagger:

- **URL**: `http://localhost/swagger/`

### Redoc

Документация также доступна через Redoc:

- **URL**: `http://localhost/redoc/`




