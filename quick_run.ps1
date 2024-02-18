# cd into rust
Set-Location rust
# Build the project
maturin develop
# cd out of rust
Set-Location ..
# Run the project
python3 run.py