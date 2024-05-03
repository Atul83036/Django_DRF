# Implementing simple api's to model the [Trello](https://trello.com/) in  Django DRM with browsable api

## Introduction
Welcome to the project documentation for our Django Rest Framework (DRF) application with a browsable API! 
This project is inspired by Trello, a popular project management tool, and aims to provide similar functionalities through a RESTful API interface.

## Design Approach
  ### Package Requirements
  To build the Trello-like application, you'll need the following packages:
  
  **Django**: A high-level Python web framework for rapid development.
  
  **Django Rest Framework (DRF)**: A powerful toolkit for building Web APIs in Django.
## Installation
You can install Django and Django Rest Framework using pip:
`pip install django djangorestframework`

## Creating the Project
To start the project, run the following command:
`django-admin startproject backend`

## Starting the App
Navigate to the project directory and create a new app:

`cd backend`
`python manage.py startapp <app_name>`

**Don't forget to include the new app and 'rest_framework' in your settings.py file:**

`INSTALLED_APPS = [

    ...
    
    '<app_name>',
    
    'rest_framework',
    
    ...
    
]`

**Running the Server**

Run the Django development server:
`python manage.py runserver`

## Checking the API
Navigate to http://127.0.0.1:8000/ in your web browser to access the browsable API.

You should see a list of available endpoints along with interactive forms to test them out.

## Conclusion
By following this setup guide, 

you'll have the Trello-like application up and running with a RESTful API powered by Django Rest Framework. 

Feel free to explore the API and start building your project!
