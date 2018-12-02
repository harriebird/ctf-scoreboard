# ctf-scoreboard
A scoreboard made for the Capture the Flag events of Hackm3.

### Installation
1. Clone the repository of this project.
2. Run `deploy.sh` to automate the the preparation of the following:
  * Creation of virtual environment
  * Installation of the required dependencies.
  * Setting up of the initial configuration of `local_settings.py`
  * Migration of models and static collection

### Running the Application
While on the root project directory, run `run.sh` to launch the application on port 1337.

### Team or Solo Mode
This application can run in either Team or Solo Mode. By default this runs on Team Mode. To change the mode, you can modify the `TEAM_MODE` inside the `local_settings.py`. Set it to `False` if you want to use the application in Solo mode.