***************
Installations :
***************
Command : pip install Django==1.10

(You also need Apache and MySQL)


********************
To run the project :
********************
In the folder python-blog/blog :

python manage.py makemigrations appli_blog
python manage.py migrate appli_blog
python manage.py createsuperuser
python manage.py runserver
