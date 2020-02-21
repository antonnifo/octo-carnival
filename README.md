## Profiles-Rest-Api  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  
### PROJECT OVERVIEW
This is a browsable, self documenting REST API built using Django, Django REST Framework, Python, Vagrant, VirtualBox, VScode, and ModHeaders. Git clone the project using the command below to get started
> git clone https://github.com/antonnifo/profiles-rest-api.git

### Create virtual environmen
> python3 -m venv env  
#### Install python packagesies
> pip install -r requirements.txt  
###  Run migrations and collectstatic
> python manage.py migrate  
> python manage.py collectstatic --noinput
#### Some of the Endpoints
| Method | Endpoint                                    | Description                                    |  
| ------ | ------------------------------------------- | ---------------------------------------------- |  
|POST    |`/api/v2/profile`                        |Adding User to system by logged in member.                                 |  
|POST    |`/api/login/`                       |user signs in here.                              |  
| GET   | `/api/profile/<int:pk>/ `                         | view a single profile data.                      | 
|PATCH  |` api/profile/<int:pk>/`      | Partially  change you account details|  
|GET |`api/feed/`                      | View all user feeds|  
|POST | `api/feed/`                    | Post a feed                           |  
|PATCH | `api/feed/<int:pk>`           | partially edit a feed               |  

