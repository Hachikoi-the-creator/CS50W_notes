<style>
    body{
    color: black;
  }
  h1{
    color:#5afff7;
  }
</style>

**HTTP = Hyper Text Transfer Protocol**

# Some theory

## HTTP query example
*get command, http and it's version*

GET HTTP/1.1

---
*The page we are trying to get*

Host: www.index.com

### Response

*200 means everything went ok*

HTTP/1.1 200

---

*We got a html-text file*

Content-Type: text/html

### More status codes
|Code|Description|
|----|-----------|
|200 |         OK|
|301 |Moved Permanently|
|403 |  Forbidden (try to access without permission)|
|404 |  Not Found|
|500 |Internal Server Error|

# Virtul enviroment

Create one once you are inside the desired dir

### Create one

- **$** python3 -m venv (name of the venv)
- python -m venv (name of the venv)

### Activate it

- .\venvi\Scripts\activate

### Install Django once activated
- pip install Django

# Django

### Making a Django project

#### On console
- django-admin startproject my_django

#### Files created
- **manage.py:** No modify but we will use it later on to make changes to the rest of file
- **project/settings.py:** We will make some changes here as well
- **project/urls.py:** Basically a table of contents for all te pages on our app!
- **project/__ init __.py:** file created to tell the interpreter we are inside a module folder (pip stuff)

### Open project server, inside the Django dir
- python manage.py runserver

*may need to also run: **python manage.py migrate***

### Start an Django app
- python manage.py startapp (name of the app)
  
**All the files in here will be used**

### Add created app the the Django project

- In the Django project created at the beginning, find **settings.py**
- modify INSTALLED_APPS = [ ], whit adding the name of the new app created