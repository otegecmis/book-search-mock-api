#!/bin/bash

source env/bin/activate
python3 app.py
deactivate

echo -e "\nApplication stopped and virtual environment deactivated."
