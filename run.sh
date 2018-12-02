source venv/bin/activate
cd src
gunicorn -w 3 scoreboard.wsgi
