# Aquvio
Source code of the new website of Aquvio

![](https://img.shields.io/github/license/CybSec-NITW/WeaponHEX)
![](https://img.shields.io/github/issues/CybSec-NITW/WeaponHEX)
![](https://img.shields.io/pypi/pyversions/django.svg)
![](https://img.shields.io/github/stars/CybSec-NITW/WeaponHEX)

## Important Instructions
To run this project follow these steps

```
user:~ git clone https://github.com/ankushmittal1008/Aquvio.git
user:~ cd Aquvio
user:~ pip3 install -r requirements.txt
user:~ virtualenv env
user:~ env\scripts\activate                    #(Windows) for MAC/Linux -> source env/bin/activate
user:~ python3 manage.py makemigrations
user:~ python3 manage.py migrate
user:~ python3 manage.py runserver             #It will deploy website on your localhost https://127.0.0.1:8000
```

## Admin login

Open https://127.0.0.1:8000/admin

Default credentials are

Username -> admin

Password -> admin

## A help for you
I have added a debug toolbar DjDT - Django Debug Toolbar. See right side on the website on the browser after deploying it.

## Instructions for front-end developers
Keep your html files in Aquvio/templates and your media files, css, js files in static_in_env. All your development work is related to only these folders.

## Instructions for back-end developers
Try to complete some missing parts and integrate all things. DjDT will be a major help to you. Add more tabs like about us,etc.

## Updating this repository
To update your work, follow these commands
```
user:~ git add .
user:~ git commit -m "your_unique_msg"
user:~ git pull origin master
user:~ git push origin master
```

## Note
I have given instructions in all the files in the repository in comments. Please read it before making any change.
