Dave is a command-line calculator with standard and scientific math, symbolic algebra, and optional tools for astronomy, chemistry, biology, meteorology, physiology, and other scientific fields.

This guide is for a computer with no Python packages installed. The examples use Python 3.12 and a virtual environment so Dave’s dependencies stay separate from other software.

1. Install Python

Install Python 3.12 or newer from [python.org](https://www.python.org/downloads/).

Open Terminal then check Python is available:

python3 --version

2. Get Dave’s files

Put `dave.py` in a folder of your choice, then open a terminal in that folder. The folder should also contain this `README.md`.

3. Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

4. Install Dave’s required packages

python -m pip install mendeleev sympy numpy matplotlib rich yfinance pandas scipy deep-translator

Dave also uses Python’s built-in standard library, which does not need a separate install. Some scientific package features are optional and load only when used. Dave’s package status report can show which optional packages are available; install only the packages for the features you need.

5. Start Dave

python3 dave.py

At the prompt, enter an expression such as:

2 + 2
sqrt(81)
derivative(x**3)
absolute value of -5

Enter `help` for the in-program feature list, `selftest()` to run Dave’s checks, and `quit` to exit.

Next time

Open a terminal in Dave’s folder and activate the virtual environment again:

source .venv/bin/activate
python dave.py

Troubleshooting

- **`python` or `python3` not found:** Install Python, reopen the terminal, and check the PATH setup.
- **`No module named ...`:** Activate `.venv` and rerun the package installation command above.
- **Package installation fails:** Upgrade pip with `python -m pip 3install --upgrade pip3`. Some optional scientific packages have platform-specific requirements; Dave’s core calculator does not require installing the entire optional package catalog.
- **Geocoding or online lookups fail:** Those features require an internet connection and may rely on external services.

Note: Dave is only suitable for MacOS.
