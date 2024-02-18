# !/usr/bin/python3
# Make venv
python3 -m venv env
# Activate the virtual environment
source env/bin/activate
# Install the requirements
pip install -r requirements.txt

# cd into rust
cd rust
# Build the project
maturin develop
# cd out of rust
cd ..
# Run the project
python3 run.py
