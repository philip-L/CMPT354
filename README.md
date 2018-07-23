# CMPT354
Project for Database Systems I at Simon Fraser University

## Front end

cd CMPT354/react-dynamicform

0. npm add yarn

1. yarn

2. npm start

## Backend

These are the steps I took on a MacOS environment.

### Dependencies

0. If you don't have Python, get it.

1. Make sure you have Django installed (version 2.0.5 or later). Reference: https://docs.djangoproject.com/en/2.0/intro/tutorial01/
    
        pip install django

2. MySQL version 5.7.22 is required (not latest) since mysqlclient only supports up to this. Download page: https://dev.mysql.com/downloads/mysql/5.7.html#downloads Reference: https://dev.mysql.com/doc/refman/5.7/en/
    
        - download the native package
        - make sure to use legacy encryption if asked


3. Download mysqlclient 1.3.12 database connector in order to use django with mysql:
    
        pip install mysqlclient

4. Also need sqlparse in order to run raw sql queries in migrations
        
        pip install sqlparse


This is all that is required to use django with mysql.



### Creating the database (documentation: https://dev.mysql.com/doc/refman/5.7/en/)

After downloading the native package follow the install wizard to set things up. Refer to reference manual to create database.

You need to create a MySQL database with the following settings to match the django settings file:
       
       database name: SubAve
       user: root
       password: SubAvepwd

Useful commands:

    To start the server:  mysqld_safe --user=mysql &
    To stop the server:  mysqladmin -u root shutdown
  
When the MySQL server is running you run: 

    mysql -u root -p

When using the database shell: 
    
    CREATE DATABASE SubAve; 
    SHOW databases;
    USE SubAve;
    SHOW tables;

### Creating tables and populating the database

This is done through django. It is accomplished through migrations (https://docs.djangoproject.com/en/2.0/intro/tutorial02/):

Use these commands:
        
        To apply the migrations to populate database: python manage.py migrate
        To create a new migration for the ordering app: python manage.py makemigrations ordering
        To view the sql before applying a migration number 0001 on ordering app: python manage.py sqlmigrate ordering 0001

