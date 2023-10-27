#!/bin/bash
echo "Hi there! Welcome and thank you for downloading the wedding app!"
echo "Before we begin, let's make sure you the correct version of python installed" 
if ! [[ -x "$(command -v python3)" ]]
then
    echo 'Unfortunately you do not have python3 installed. Please go to https://www.python.org/downloads/ to install' >&2
    exit 1 
fi

echo "Now we need to create and activate a virtual environment" 
python3 -m venv .venv 
source .venv/bin/activate

echo "Next the dependencies for this app will be installed"
pip install -r ./requirements.txt

echo "All done! Let's get planning!"
python3 ./main.py
deactivate