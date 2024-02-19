# Make venv
python -m venv .venv
# Activate the virtual environment
.venv\Scripts\Activate
# Install the requirements
pip install -r requirements.txt

# cd into rust
Set-Location -Path rust
# Build the project
maturin develop --release
# cd out of rust
Set-Location -Path ..
# Run the project
python run.py