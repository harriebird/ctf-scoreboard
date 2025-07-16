# ctf-scoreboard
A scoreboard made for the Capture the Flag events of Hackm3.

### Installation
1. Clone the repository of this project.
2. Set a `SECRET_KEY` in the settings file located at `src/scoreboard/settings.py`.
3. Run `deploy.sh` to automate the preparation of the following:
   * Creation of virtual environment
   * Installation of the required dependencies.
   * Setting up of the initial configuration of `local_settings.py`
   * Migration of models and static collection

### Running the Application
While on the root project directory, run `run.sh` to launch the application on port 1337.

To use the Administration page you must create a superuser account by using the command `python manage.py createsuperuser` on the `src` directory. Only IP addresses listed on the `ADMIN_IPS` in the `local_config.py` will be authorized to access the admin page.

### Team or Solo Mode
This application can run in either Team or Solo Mode. By default this runs on Team Mode. To change the mode, you can modify the `TEAM_MODE` inside the `local_settings.py`. Set it to `False` if you want to use the application in Solo mode.