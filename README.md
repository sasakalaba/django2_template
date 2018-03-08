# Django 2.0 Template

Starter project template using Django 2.0, Python 3.x and Postgres.

## Quickstart

Clone the repo from GitHub:

    git clone https://github.com/sasakalaba/django2_template.git

Create python3 virtualenv:

    apt-get install python3 python3-doc
    mkvirtualenv --python=/usr/bin/python3 <env_name>

Setup postgres:

    apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
    su - postgres
    psql

    postgres=# CREATE USER <username> WITH PASSWORD '<password>';
    postgres=# CREATE DATABASE <project_name> WITH OWNER <username>;

Navigate to project dir and install requirements:

    cd <project_name>
    pip install -r requirements.txt

Create .env file:

    cat .env_sample >> .env

Generate autokey:

    python -c "import string,random; uni=string.ascii_letters+string.digits+string.punctuation; print(repr(''.join([random.SystemRandom().choice(uni) for i in range(random.randint(45,50))])))"

Set .env values:

    nano .env

Run the migrations:

    python manage.py migrate

Create super user:

    python manage.py createsuperuser


## Setting your own project information

Make sure you change the project name in settings, and set environment variables appropriately.
Create an empty project on github.

Delete .git directory, then:

    git init
    git remote add origin git@github.com:<username>/<project_name>.git
    Replace testing_app with your own app. (Find All 'testing' in your code editor).
    Replace current templates and static files with your own.
    git add *
    git commit -m "First commit."
    git push origin master

Add licence via github.

    https://help.github.com/articles/adding-a-license-to-a-repository/


## Automated tests

To run the automated test suite:

    python manage.py test --settings=project.settings.test


## Bootstrap theme

Start Bootstrap - Resume by David Miller, Owner of Blackrock Digital

https://github.com/BlackrockDigital/startbootstrap-resume

http://davidmiller.io
