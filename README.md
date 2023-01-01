# warehouse-api

##
docker-compose -f docker-compose.local.yml up -d

## test + lint
./manage.py test && flake8


./manage.py createsuperuser

./manage.py makemigrations
./manage.py migrate

pip install -r requirements.local.txt

django-admin startapp quickstart
