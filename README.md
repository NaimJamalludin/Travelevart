Travelevart

About
This is a group project for WOC7012 - Web Based Framework Development

Prerequisites
Python 3.6.4
pip
virtualenv

Setup
Create a virtual environment in which to install Python pip packages. Virtual environment activation with virtualenv

virtualenv env
env/scripts/activate

Install development dependencies
pip install -r requirements.txt

Setup database tables
python manage.py makemigrations
python manage.py migrate

Run the web application locally
python manage.py runserver

License
MIT