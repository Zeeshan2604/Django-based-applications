# Step-by-Step Guide to Running the Django Project for Sorting Files

## Prerequisites
Before you start, ensure you have the following installed on your system:

*  Python 3.x 

* pip (Python package installer) 

*  Django 3.x or higher  



## Step 1: Set Up a Virtual Environment
It's a good practice to create a virtual environment for Python projects to manage dependencies.

### Create a Virtual Environment:


bash
> [!TIP]
>* python -m venv venv

### Activate the Virtual Environment:

bash
> [!TIP]
>* venv\Scripts\activate


## Step 2: Install Required Packages
### Install Django: You can install it using:

bash
> [!IMPORTANT]
>* pip install django


## Step 3: Make Migrations
### Create Database Migrations: Run the following command to create the necessary database tables based on your models:

bash
>* python manage.py makemigrations

### Apply Migrations: Apply the migrations to the database:

bash

>* python manage.py migrate


## Step 4: Create a Superuser (Admin Account)
### To access the Django admin panel, create a superuser account:

bash
>*python manage.py createsuperuser

 Follow the prompts to set up the username, email, and password.

## Step 5: Run the Development Server
### Start the Server: Run the Django development server:

bash
>* python manage.py runserver


### Access the Application: Open your web browser and go to:

>* http://127.0.0.1:8000/


Log in with your superuser credentials to manage files directly.
