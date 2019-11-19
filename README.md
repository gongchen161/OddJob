# OddJob

## Prerequisites
* Python3
* MySQL
* Flask
* PyMySQL
   <pip3 install pymysql>

## Deployment

### Database Setup:
* The default databse username used is 'root' and no password. To change the database username/password, edit them in line 15/16 of oddjob.py.
* Create database 'OddJob'
* Import tables.sql to OddJob. You can use, e.g. mysql -u root OddJob < /File/Path/OddJob/tables.sql

### Build & Run:
* Run python3 oddjob.py
    * Running script with new MySQL install on linux machine sometimes gave error:
        <pymysql.err.InternalError: (1698, "Access denied for user 'root'@'localhost'")>
        * Error was fixed with the following commands:
            ...
            > sudo mysql -u root
            mysql> USE mysql;
            mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
            mysql> FLUSH PRIVILEGES;
            mysql> exit;
            > service mysql restart
            ...
* Go to localhost:5000 to access the application
