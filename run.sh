pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install pygame
pip install pygame-menu -U

python3 main.py

rm -r __pycache__
rm -r venv
