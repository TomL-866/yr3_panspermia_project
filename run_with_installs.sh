# Make venv
python3 -m venv .venv
# Activate the virtual environment
source .venv/bin/activate
# Install the requirements
pip install -r requirements.txt

# cd into rust
cd rust
# Build the project
maturin develop --release
# cd out of rust
cd ..
# Run the project
python3 run.py
