# Braum
Handles the database and its interface

```
  1 - Subir primeiro -> sudo docker start -a -i braum_db_1

  2 - Depois executar em outro terminal -> sudo docker start -a -i braum_web_1

  3 - Em outro terminal executar -> sudo docker braum_web_1 exec bash

  4 - Em seguida executar -> python manage.py migration

  5 - Logo após executar -> python manage.py createsuperuser

  6 - Em seguida vai aparecer -> Username (leave blank to use 'root'): _
                                                                        L Digite -> admin

  7 - Depois Email address: _
                             L Digite -> admin@admin.com

  8 - Em Password:  e  Password (again): digite -> admin
  
  9 - Em seguida pressione "Y" e digite "exit" para sair
```