# django-bootcamp-geek-uni-mysql

This is a Django Bootcamp from Udemy by Geek University as a Recap where will be built 3 different applications such as a Real Time, Geo location, and Data Manipulation one, which can be seen topics like Websockets, Facebook Login, PDF Creator, Customized models and admin, tests, deploy and so on...

#### Link Application 1: https://github.com/LondonComputadores/django-bootcamp-geek-uni-sqlite

#### Link Application 2: This Repo

#### Link Application 3:


## What's going on Application 1: Django Basics Recap

Terminal's issued commands:

- $ python -m venv venv
- $ source venv/bin/activate
- $ pip install django whitenoise gunicorn django-bootstrap4 PyMySQL django-stdimage
- $ pip freeze > requirements.txt
- $ django-admin startproject django2 .
- $ python manage.py startapp app
- $ python manage.py runserver
- $ python manage.py makemigrations
- $ python manage.py migrate
- $ python manage.py createsuperuser
- $ python manage.py shell(
    - >>> from django import forms
    - >>> dir(forms)
    - >>> help(forms.CharField)
)


MySQL issues and solutions:

- Workbench won't start mysql-server neither to store connection   credentials in its system's keychain:(
    - $ apt-get remove --purge mysql-server mysql-client mysql-common
    - $ apt-get autoremove
    - $ apt-get autoclean
    - $ wget https://dev.mysql.com/get/mysql-apt-config_0.8.15-1_all.deb
    - $ dpkg -i mysql-apt-config_0.8.15-1_all.deb
    - $ apt-get update
    - $ apt-get install mysql-server
    - After that I choose Use Legecy Authentication Method (Retain Mysql 5.x) And can start mysql normally again
    - Go to Ubuntu software center
    - Search for MySQL workbench community.
    - Click on permission
    - Enable Read, add .... to on

)

- Settings just been uninstalled itself from my Ubuntu 20.04 and here is the fix so it'll ba able to access the software center to change the workbench permissions:(
     - sudo apt-get update
     - udo apt-get install --reinstall gnome-control-center
     - gnome-control-center
 )

- Won't CREATE DATABASE databasename; on workbench(
    - $ sudo mysql -u root -p
    - mysql> GRANT ALL ON *.* TO 'anynonrootusername'@'localhost';
)