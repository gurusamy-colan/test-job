# Organisation Tracker

The Organization Tracker is a Django-based application designed to manage and track datas.

## Installation

Instructions to install the project

```bash
pip install -r requirements.txt
python manage.py migrate
``` 

## To Run Server

``` bash
python manage.py runserver 8006
```

## To Run Pytest

```bash
pytest .\organization\tests.py 
```

## Superuser Credentials - Sqllite:
'''Username: admin
Email address: admin@test.com
Password: Admin@123
'''





## Steps to run the django admin user interface:
'''
1. Visit the url : http://localhost:8000/admin/
2. Enther the super amdin credentials
3. Create/Read/Edit/Delete the table values for 'Investor Type' and 'Investment Stage'
4. Logout
'''


## Steps to run the user interface:
'''
1. Visit the url : http://localhost:8000/
2. Create/Read/Edit/Delete the Organization informations'
'''

