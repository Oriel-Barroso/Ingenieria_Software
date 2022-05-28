python3 -m venv .
source bin/activate
pip install --upgrade pip
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
#python manage.py createsuperuser