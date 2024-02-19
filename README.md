
# yr3_panspermia_project

Project title: Panspermia in the Sun's locale

# Project Description

Litho-panspermia is the idea that life can be transferred between stellar
and planetary systems on rocks that are either directly exchanged
between stars, or are captured by one star after being ejected from
another planetary system. In this project you will estimate how many
rocks can be exchanged/captured by Sun-like stars in the Milky Way, and
then estimate how many of these rocks may harbour biological material
that could survive the harsh environs of interstellar space. The project
requires some prior knowledge/experience of coding (Python, or a compiled
language such as C or Fortran).

# Running the project 

This tutorial gives commands for running the project on Linux or Windows in the bash or powershell terminal respectively. 

Before doing anything else, download (if you do not have these already) the Rust compiler (see <https://www.rust-lang.org/tools/install>) and a Python 3 interpreter (see <https://www.python.org/downloads/>).

Then follow the instructions below to run the project.

## Run from scripts (Windows)

Run 
    
```powershell
.\scripts\run_with_installs.ps1
```

to run the program from complete scratch (including every install except from Python or Rust). Then run

```powershell
.\scripts\run_without_installs.ps1
```

if you want to run the program again once everything's installed.

## Run from scripts (Linux)

Run 

```bash
source scripts/run_with_installs.sh
```

to run the program from complete scratch (including every install except installing Python or Rust or installing python3-venv). Then run

```bash
source scripts/run_without_installs.sh
```

if you want to run the program again once everything's installed.

## Run manually (Linux - Ubuntu)

Create a virtual environment and install the required Python packages by running the following commands in the terminal. You will need to have the `venv` module installed in your Python distribution. If you do not have it, you can install it by running `sudo apt-get install python3-venv` in the terminal. Then run the following commands in the terminal to create the virtual environment and install the required packages:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Compile the Rust code and go back to the main directory by running the following commands in the terminal:

```bash
cd rust
maturin develop --release
cd ..
```

Run the program by running the following command in the terminal:

```bash
python3 python/run.py
```