<header>
  
# Web-based Kiosk 

</header>

## Prerequisites

1. Installed Python
2. Installed MySQL

### Installation
1. If you haven't downloaded `Django` and `mysqlclient` from Python, please do so.

From Python, install Django:
   ```
   pip install django
   ```
From Python, install mysqlclient:
   ```
   pip install mysqlclient
   ```
2. After that, download this repository. From the repository's main directory,
Import SQL file to the database:
 ```
mysql -u <username> -p <databasename> < posdb.sql
 ```
Run Django:
 ```
python manage.py makemigrations
 ```
 ```
python manage.py migrate
 ```
 ```
python manage.py runserver
 ```
<br>

### Default Homepage Screen

![defaultPage](https://github.com/jaewan99/Module3/assets/68039639/e591b774-d76e-4d8f-b000-8020ff39a99e)

