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
            ```
            sudo mysql -u root
            mysql> USE mysql;
            mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
            mysql> FLUSH PRIVILEGES;
            mysql> exit;
            service mysql restart
            ```
* Go to localhost:5000 to access the application

### Usage:
* Web App opens to Customer home screen, where a user can register, login, or switch to the Worker page.
* After a customer registers and logs in, they can view their pending and past jobs, post a job, and edit their account.
* After a worker registers and logs in, they can view their job history, search and accept work in a specific area, and edit their account.
* Workers must have their skill set verified by admin in order to accept jobs
    * Admin can approve skills by going to localhost:5000/admin

### Test User Logins:
* Customer
    * U: dp2387@nyu.edu		P: oddjobdev
* Worker
    * U: rob.boss@gmail.com	P: happyaccident
    * U: jazz.hands@gmail.com	P: kindofblue

### Changes:
* Instead of workers and customers rating each other, now only customers can rate workers
    * This was done to allow new customers without ratings to still have jobs fulfilled
* Customers now request jobs which workers then bid on, rather than a having a worker post a job
    * This was done to ensure specific customer needs would be met
