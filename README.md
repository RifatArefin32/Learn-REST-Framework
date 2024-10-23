# Create a new Django Project
- Install virtual environment: `sudo apt install python3-venv`
- Create a virtual environment: `python3 -m venv env`
- Activate the enviorment: `source env/bin/activate`
- Install Django to the environment: `pip install django`
- Check the django successfully installed: `django-admin --version`
- Create a project directory: `django-admin startproject djangorest`
- Enter into project and run the server: `cd djangorest` then `python3 manage.py runserver`
- Stop the virtual environment: `deactivate`
 
# Create a new app
- Create new app from virtual environment: `python3 manage.py startapp firstapp`
- Register the appname to the `settings.py` file's `INSTALLED_APPS` array.

# Create first model
- Create a new model `Course` at `firstapp/models.py` 
- Register the model at `firstapp/admin.py`
- Run migration `python3 manage.py migrate`
- Create Django administrator: `python3 manage.py createsuperuser`

# Make migrations
```bash
python manage.py makemigrations
python manage.py migrate
```