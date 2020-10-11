# Multi-DB-Router

Requirement (need install below package):
Django==3.1.2
mysqlclient 
psycopg2==2.8.6
PyMySQL==0.10.1
pytz==2020.1
sqlparse==0.4.1

or simple run the requirement.bat file

Step to Run the Application.
1. Clone the the project.
2. Install the requirement or run the requirement.bat file.
3. Install Postgresql and create two database having name 'database1' and 'database2'.
4. Install Mysql and create three database having name 'database3', 'database4' and 'database5'.
5. Open CMD and Goto \Multi_DB_Router.
6. In CMD 
      py manage.py makemigrations accounts
      py manage.py makemigrations product2
      py manage.py makemigrations product3
      py manage.py makemigrations product4
      py manage.py makemigrations product5
      
      py manage.py migrate accounts --database=default
      py manage.py migrate product2 --database=database2
      py manage.py migrate product3 --database=database3
      py manage.py migrate product4 --database=database4
      py manage.py migrate product5 --database=database5
      py manage.py migrate
7. In CMD
      py manage.py runserver
8. Also Update the Email host in settings.base.py file and Password for using Email.


**There the two setting files are present, if need to switch the "set DJANGO_SETTINGS_MODULE=Multi_DB_Router.settings.local"**
