python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp src/local_settings.py.example src/local_settings.py
cd src
python manage.py migrate
python manage.py collectstatic
