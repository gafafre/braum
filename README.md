# Braum
Handles the database and its interface

```
  1 - Primeiro dar o comando docker-compose build

  2 - Em seguida executar em outro terminal -> 

  3 - Execute em outro terminal -> sudo docker exec -it braum_db_1 bash

  4 - Em seguida execute -> psql --username=postgres --password (digite a senha: docker)

  5 - Entrando no terminal do container execute o comando -> CREATE DATABASE braum_db;

  6 - Certifique-se que foi criado -> \l em seguida execute \q para sair do postgres

  7 - CTRL+C no terminal que está rodando o docker compose, execute: sudo docker-compose down e depois docker-compose up

  8 - Em outro terminal executar -> sudo docker exec -it braum_web_1 bash

  9 - Em seguida executar -> python manage.py migrate

  10 - Logo após executar -> python manage.py createsuperuser

  11 - Em seguida vai aparecer -> Username (leave blank to use 'root'): _
                                                                        L Digite -> admin

  12 - Depois Email address: _
                             L Digite -> admin@admin.com

  13 - Em Password:  e  Password (again): digite -> admin
  
  14 - Em seguida pressione "Y" e digite "exit" para sair
```
