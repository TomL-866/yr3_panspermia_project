# cd into rust
Set-Location rust
# Build the project
maturin develop --release
# cd out of rust
Set-Location ..
# Run the project
python python/run.py
