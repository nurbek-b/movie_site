# Movies Site Project

The site to search and watch movies

To run this project you can clone:

```git clone git@github.com:nurbek-b/movie_site.git```

Than there will be some steps to build project:
1. First you have to build virtual environment on pipenv and install requirements
 using commands below from folder where manage.py is:

- ```pipenv shell``` 
- ```pipenv install```

2. Then you have to sync your database with models on project:
- ```python manage.py migrate```

3. Create superuser(admin):
- ```python manage.py createsuperuser```

4.Run project to see on localhost:
- ```python manage.py runserver```