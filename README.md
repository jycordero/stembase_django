# stembase_django

## Setup
To set up the inviroment you can use `requirements.txt` with `pip`

```
pip install -r requirements.txt
```

But all development and the recommended packege manager is `pipenv`

```
pip install pipenv # install
pipenv shell # creates virtual enviroment
pipenv install # installs the packages in Pipfile
```

## Django Enviroment
Once you set up the enviroment, you can set up the enviromental variables necesary to access the databases.
  * Can be hard coded
    * `DJANGO_SECRET`
    * `DJANGO_DEBUG`(This is used in the settings.py file to automatically turn off the `debug` setup in deployment.)
    * `DJANGO_GRAPHIQL`(This is used in the settings.py file to automatically turn off the `graphiql` setup in deployment.)
  * Should not be hard-coded 
    * `DB_USER` (Database user)
    * `DB_PASSWORD` (Database password)
    * `DB_HOST` (Database host)
    * `DB_PORT` (Database port)
    * `DB_NAME` (Database name)
   
## Running Django 

Make migrations 
```
python manage.py makemigrations 
python manage.py migrate
python manage.py makemigrations api
python manage.py migrate api
```

Run on local server
```
python manage.py runserver
```
