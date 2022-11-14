# SPBU CV
Резюме-одностраничник, домашняя работа по вебу для СПбГУ

## Запуск
Нужен `docker (у меня 20.10.17)`, `docker-compose (2.10.2)`:
```shell
docker-compose up
```
Всё! После этого сайт будет доступен на http://localhost или http://127.0.0.1

## Разработка
Нужен `python (у меня 3.10)`, `pip`

Для разработки желательно установить виртуальное окружение `venv`

Установить зависимости с помощью `pip`:
```shell
cd src # Переходим в директорию с кодом

pip install -r requirements.txt
```

Запустить
```shell
flask run
```
или
```shell
python main.py
```