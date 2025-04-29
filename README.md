# Гео-приложение Leaflet


#### Требования к развертыванию:

+ Docker

#### Как развернуть проект:

1. Клонировать репозиторий.

    ```
    1. https://github.com/Vladimir-junior/geap34.git
    2. cd greap34
    ````
2.  Запустить контейнер.

    ```
    docker compose up -d
    
    ```
2.  Применить миграции.

    ```
    1. docker compose exec web flask db init
    2. docker compose exec web flask db migrate -m "Initial migration"
    3. docker compose exec web flask db upgrade
    ```
3. Перейти на сайт по адресу.

   ```
   http://localhost:5001/ 
   
   ```
   
