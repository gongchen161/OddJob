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
* Populate data with OddJob.sql file: mysql -u root OddJob < OddJob.sql

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

    * After a customer registers and logs in, they are redirected to the Jobs page where they can view their job requests, pending jobs, and job history.
    * From the nav bar, the user can go to the job post page where they can post jobs with a specified job type, job location, and a short description.
    * The nav bar also has a link to the user profile, where they can edit their address, change their password, and change their basic information.
    * Their is also a support page where users can message admin with any issues and admin can respond from the admin portal.
    * After logging out, a user is redirected back to the home page.

    * At the home page, users can switch to the worker site where they can register/login a worker account.
    * Workers are also redirected to their job page where they can view pending, upcoming, and completed jobs.
    * Workers must have their skill set verified by admin in order to accept jobs.
        * Admin can approve skills by going to localhost:5000/admin
    * Once a worker has skills approved, they can go to the job search page to search an area for jobs that coincide with their skills.
    * A worker places their bid on a job, at which point the customer can go to their job page and accept a worker of their choice.
    * Workers also have access to a support portal where they can send admin messages.

    * localhost:5000/admin is the admin portal which contains pending skills and support messages
        * Portal is not secured for demo purposes

### Test User Logins:
* Customer
    * U: dp2387@nyu.edu		P: oddjobdev
    * U: scarface@gmail.com	P: pushittothelimit
* Worker
    * U: rob.boss@gmail.com	P: happyaccident
    * U: jazz.hands@gmail.com	P: kindofblue

### Changes from design plan:
* Instead of workers and customers rating each other, now only customers can rate workers
    * This was done to allow new customers without ratings to still have jobs fulfilled
* Customers now request jobs which workers then bid on, rather than a having a worker post a job
    * This was done to ensure specific customer needs would be met
