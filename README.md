# CMPT354
Project for Database Systems I at Simon Fraser University

## Dependencies

0. If you don't have Python, get it.

1. Make sure you have Django installed (version 2.0.5 or later). Reference: https://docs.djangoproject.com/en/2.0/intro/tutorial01/
  - pip install django

2. MySQL version 5.7.22 is required (not latest) since mysqlclient only supports up to this. Reference: https://dev.mysql.com/doc/refman/5.7/en/
  - download the native package
  - make sure to use legacy encryption if asked

3. Download mysqlclient 1.3.12 database connector in order to use django with mysql.
 - pip install mysqlclient

This is all that is required to use django with mysql.

## Setting up the database (PLEASE REFER TO DOCUMENTATION)

After downloading the native package follow the install wizard to set things up. Refer to reference manual to create database.

To start and stop the MySQL server: 
  - To start the server:  mysqld_safe --user=mysql &
  - To stop the server:  mysqladmin -u root shutdown
  
When the MySQL server is running you can run: "mysql -u root -p" to use the MySQL shell. If you didn't set up a password no password is required.

Create database: CREATE DATABASE SubAve;

To see list of databases: SHOW databases;

To switch to a database (where you can show & create tables): USE 'database_name';

To show tables: SHOW tables;



