<h1 align="center">
	Django Deployment with PythonAnywhere
</h1>

<h3 align="center">
	My first deployed Django app!
</h3>

<p align="center">
	<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"/>
	<img src="https://img.shields.io/github/languages/count/vicsamuel/django-deployment-app-test?color=green"/>
</p>

<h4 align="center">
	Status: ✔️ Available
</h4>

<p align="center">
	<a href="#about">About</a> •
	<a href="#tech-stack">Tech Stack</a> •
	<a href="#installation">Installation</a> •
	<a href="#usage">Usage</a> • 
	<a href="#contact">Contact</a> 
</p>

## About
Developing on my skills with Python by learning the Django framework. This project is basic, but has potential to become a full stack complete Web Application. This is not a completed application! It is a good base for building a website, which is what I may do with it in the future. This was built on a Linux machine and deployed in the PythonAnywhere virtual environment. This requires features to be installed via pip in the bash terminal. The features are Django 1.10.8, Pillow, and Argon2. These are security and file handling libraries that will help handle the flow of the site.

Website: http://v1c.pythonanywhere.com/

## Tech Stack
<img src="https://img.shields.io/badge/Bootstrap-05122A?style=flat&logo=bootstrap" alt="bootstrap Badge" height="25">&nbsp;
<img src="https://img.shields.io/badge/Django-05122A?style=flat&logo=django" alt="django Badge" height="25">&nbsp;
<img src="https://img.shields.io/badge/Html5-05122A?style=flat&logo=html5" alt="html5 Badge" height="25">&nbsp;
<img src="https://img.shields.io/badge/Python-05122A?style=flat&logo=python" alt="python Badge" height="25">&nbsp;

## Installation
To Install this project, follow the steps above:
```bash
# This project can be run in any bash terminal, but it also can be hosted live as is on services like PythonAnywhere
# It is recommended to test this in a virtual environment
# Python 3.6 is REQUIRED
# Django 1.10.8 is REQUIRED

# Clone this repository
$ git clone https://github.com/vicsamuel/django-deployment-app-test.git

# Change directory to the correct folder
$ cd django-deployment-app-test/learning_templates/

# Create a virtual environment:
$ python -m venv venv

# Activating the virtual environment:
$ source venv/bin/activate

# Install Django 1.10.8:
$ pip install django=django=1.10.8

# Install Pillow
$ pip install Pillow

# Install Argon2
$ pip install django[Argon2]
```

## Usage
To use this project, follow the steps above:
```bash
# Running the Application

$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Contact
<img align="left" src="https://avatars.githubusercontent.com/vicsamuel?size=100">

Made with ❤️ by [Victor Samuel](https://github.com/vicsamuel)!

<a href="https://www.linkedin.com/in/victor-samuel-1738a29a/" target="_blank"><img src="https://img.shields.io/badge/Contact-LinkedIn-blue" alt="LinkedIn Badge" height="25"></a>&nbsp;

<br clear="left"/>
