# eliftech-project

This repository contains a test task for admission to the course by ElifTech.

## Link

https://maxrosoft.pythonanywhere.com/

## Description

The project was completed at the Middle level + page with coupons + order history.

## Installation and configuration

The following instructions will help you install and set up a project on a local device for development and testing.

### Prerequisites

[python 3.7](https://www.python.org/downloads/) must be installed on your device

### Installation

Steps to install and configure the project:

1. Clone the repository to your local device.
2. Create a virtual environment:
```bash
virtualenv env/myshop
```
3. Activate the virtual environment:
```bash
env/myshop/Scripts/activate
```
4. Change to the root folder of the project:
```bash
cd myshop/
```
5. Install the requirements:
```bash
pip install -r requirements.txt
```
6. Set up the database:

Leave the current database.

or

Create a new (empty) database:
1. Delete the current database.
2. Perform database migrations:
```bash
python manage.py migrate
```

7. Run the development server.
```bash
python manage.py runserver
```

## Contacts

maxfilipenko07@gmail.com
