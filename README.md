
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
This tutorial gives commands for running the project on Linux in the bash terminal. 

1. Download (if you do not have these already) the Rust compiler (see <https://www.rust-lang.org/tools/install>) and a Python 3 interpreter (see <https://www.python.org/downloads/>).

2. Create a virtual environment and install the required Python packages by running the following commands in the terminal. You will need to have the `venv` module installed in your Python distribution. If you do not have it, you can install it by running `sudo apt-get install python3-venv` in the terminal. Then run the following commands in the terminal to create the virtual environment and install the required packages:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Compile the Rust code and go back to the main directory by running the following commands in the terminal:

```bash
cd rust
maturin develop
cd ..
```

4. Run the program by running the following command in the terminal:

```bash
python3 run.py
```

Alternatively, run

```bash
source run_with_installs.sh
```

to run the program from complete scratch (including every install except installing Python or Rust or installing python3-venv), or run

```bash
source run_without_installs.sh
```

to run the program once everything's installed.