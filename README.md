# Zeus

This is a toy project. In it I plain to experiment with on-line weather api,
    postgres, large csvs, statistical analyses, data visualizations.

# Getting started
### pull the code
    git clone https://github.com/pinkblock/zeus.git

### setup and run you venv

    mkvirtualenv zeus
    workon zeus
to stop your venv

    deactivate

### install the reqs in your venv
    
    pip install -r requirements.txt

### real-time testing

    cd zeus
    nosetests --with-watch

this will run your tests ever time you save file and give you a desktop notification

