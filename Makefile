install:
	pip install -r requirements.txt

test:
	cd ./testNuveo && python manage.py test