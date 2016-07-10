# Location Tracker

### Developing
In order to setup your environment to run the development server and test the application, or to contribute to the project, follow the instructions below.

Open your favorite terminal and do the following:

**Clone the repository:**
```sh
$ git clone https://github.com/EKOTracking/PetManager.git
```
**Install sytem packages**

Ubuntu:
```sh
$ sudo apt-get update
$ - Enter Scripts Here
```

Mac:
```sh
$ - Enter Scripts Here
```

Links to the above packages and dependencies can be found here:

- List pakcages here

**Run the following postgres commands to setup database**

This command will run a script of sql commands
```sh
$ sudo -u postgres psql -f database.sql
```

The commands the script runs are listed below
```sh
# from ubuntu, start psql with the following. Mac - first command is "psql" only
$ sudo -u postgres psql
postgres=# CREATE DATABASE testdb;
postgres=# CREATE USER test WITH PASSWORD 'test';
postgres=# GRANT ALL PRIVILEGES ON DATABASE testdb to test;
postgres=# \connect testdb;
testdb=#\q
```

Import the test database
```sh
$ sudo -u postgres psql -U postgres testdb < dbexport.pgsql
```

**Enter the developer python environment**
```sh
$ source develop.sh
```
**Check that the server is able to run - run comman below in directory containing manage.py**
```sh
$ python manage.py runserver
```
In your webrowser, navigate to *localhost:8000* to access the home page.

***Congratulations!*** You can test out the application, and start developing.


**Testing**
COMING SOOn