[![Deploy](https://github.com/inferno681/rlt_test/actions/workflows/deploy.yaml/badge.svg)](https://github.com/inferno681/rlt_test/actions/workflows/deploy.yaml)
<br>

<div id="header" align="center">
  <img src="https://img.shields.io/badge/Python-3.12.3-F8F8FF?style=for-the-badge&logo=python&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-555555?style=for-the-badge&logo=docker&logoColor=2496ED">
  <img src="https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4">

</div>

<br>

Пример рабочего бота: [RLT_test](https://t.me/RLT_hausaufgabe_bot)

<details><summary><h1>Тестовое задание Python developer от RLT</h1></summary>

* **Задача:**
  + Написание алгоритма агрегации статистических данных о зарплатах сотрудников компании по временным промежуткам.
  + Создание телеграм бота, который будет принимать от пользователей текстовые сообщения содержащие JSON с входными данными и отдавать агрегированные данные в ответ.


</details>

<details><summary><h1>Инструкция по установке</h1></summary>

Клонируйте репозиторий и перейдите в него.
```bash
git@github.com:inferno681/rlt_test.git
```

Для установки зависимостей создайте и активируйте виртульное окружение и выполните следующую команду:
```bash
pip install -r requirements.txt
```

Создайте файл **.env**, в корневой папке проекта, с переменными окружения.

```
  BOT_TOKEN = Токен телеграм бота
  DB_HOST = db (хост)
  DB_PORT = 27017 (порт)
  MONGO_INITDB_ROOT_USERNAME = mongo_user (имя пользователя для СУБД)
  MONGO_INITDB_ROOT_PASSWORD = secret_password (пароль пользователя для СУБД)
  DB_NAME = sampleDB (название базы данных)
  COLLECTION_NAME = sample_collection (имя коллекции)

```


Импортируйте тестовые данные:
  ```
  python restore.py
  ```

Команда для запуска бота:
  ```
  python main.py
  ```


</details>

<details><summary><h1>Запуск проекта через докер</h1></summary>

- Клонируйте репозиторий.
- Перейдите в папку **infra** и создайте в ней файл **.env** с переменными окружения:
  ```
  BOT_TOKEN = Токен телеграм бота
  DB_HOST = db (хост)
  DB_PORT = 27017 (порт)
  MONGO_INITDB_ROOT_USERNAME = mongo_user (имя пользователя для СУБД)
  MONGO_INITDB_ROOT_PASSWORD = secret_password (пароль пользователя для СУБД)
  DB_NAME = sampleDB (название базы данных)
  COLLECTION_NAME = sample_collection (имя коллекции)
  ```
- Создайте папку **test_data** и скопируйте [тестовые данные](https://drive.google.com/file/d/1pcNm2TAtXHO4JIad9dkzpbNc4q7NoYkx/view?usp=sharing)
- Из папки **infra** запустите docker-compose-prod.yaml:
  ```
  ~$ docker compose -f docker-compose-prod.yaml up -d
  ```
- В контейнере **bot** выполните импорт тестовых данных:
  ```
  ~$ docker compose -f docker-compose-prod.yaml exec bot python restore.py

  ```


</details>

<details><summary>Ссылки на используемые библиотеки</summary>

- [Python](https://www.python.org/downloads/release/python-3123/)
- [MongoDB](https://www.mongodb.com/)
- [Docker](https://www.docker.com/)
- [aiogram](https://aiogram.dev//)

</details>

* **Разработчики Backend:**
  + [Василий](https://github.com/inferno681)
