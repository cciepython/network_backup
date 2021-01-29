# network_backup

### How to install and run (Windows)
                
1. Install `python3`, `pip3`, `virtualenv` in your operating system
2. Create a development environment ready by using these commands
```
download https://github.com/cciepython/network_backup/archive/main.zip  
cd network_backup                                                               # go to the project DIR
python -m venv myvenv                                                           # Create virtualenv named .venv
myvenv\Scripts\activate.bat                                                     # Active virtualenv named .venv
pip install -r requirements.txt                                                 # Install project requirements in .venv
python manage.py createsuperuser                                                # create admin user and password to login admin site
python manage.py runserver                                                      # Run the project



```
3. Go to  `http://127.0.0.1:8000/admin` to use project








### How to install and run (GNU/Linux and Mac)
                
1. Install `git`,`python3`, `pip3`, `virtualenv` in your operating system
2. Create a development environment ready by using these commands
```
git clone https://github.com/cciepython/network_backup                           # clone the project
cd network_backup                                                                # go to the project DIR
virtualenv -p python3 .venv                                                      # Create virtualenv named .venv
source .venv/bin/activate                                                        # Active virtualenv named .venv
pip install -r requirements.txt                                                  # Install project requirements in .venv
python manage.py createsuperuser                                                # create admin user and password to login admin site
python manage.py runserver                                                       # Run the project
```
3. Go to  `http://127.0.0.1:8000/admin` to use project
