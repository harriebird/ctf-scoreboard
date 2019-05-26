source venv/bin/activate
cd src
gunicorn -w 3 scoreboard.wsgi -b 0.0.0.0:1337 --certfile=certs/hackm3.ctf.crt --keyfile=certs/hackm3.ctf.key
