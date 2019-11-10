# OddJob

## Prerequisites
* Python3
* MySQL

## Deployment

### Database Setup:
* The default databse username used is 'root' and no password. To change the database username/password, edit them in line 15/16 of oddjob.py.
* Create database 'OddJob'
* Import tables.sql to OddJob. You can use, e.g. mysql -u root OddJob < /File/Path/OddJob/tables.sql

### Build & Run:
* Run python3 oddjob.py
* Go to localhost:5000 to access the application
