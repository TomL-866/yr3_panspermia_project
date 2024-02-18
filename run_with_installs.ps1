# Make venv
python3 -m venv .venv
# Activate the virtual environment
.venv\Scripts\Activate.ps1
# Install the requirements
pip install -r requirements.txt

# cd into rust
Set-Location rust
# Build the project
maturin develop --release
# cd out of rust
Set-Location ..
# Run the project
python3 run.py