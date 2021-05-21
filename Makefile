install:
	pip install -r requeriments.txt

test:
	cd ./source && python manage.py test