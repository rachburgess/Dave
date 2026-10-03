Dave is a command-line calculator with standard and scientific math, symbolic algebra, and optional tools for astronomy, chemistry, biology, meteorology, physiology, and other scientific fields.

WARNING: Dave runs on your computers computing power. Because of this, be careful of what calculations you are running.

This guide starts from a computer with no Python packages installed. Keep Dave’s packages in a virtual environment where possible. The platform builds are:

| Platform | Dave file |
| --- | --- |
| macOS | `dave_macos.py` |
| Windows | `dave_windows.py` |
| Linux | `dave_linux.py` |
| Android (Termux) | `dave_android.py` |

Copy the selected file to your device and run the matching instructions below from the folder containing it.

## MacOS

1. Install Python 3.12 or newer from [python.org](https://www.python.org/downloads/).
2. Open Terminal and move to the folder containing `dave.py`.
3. Create and activate a virtual environment, then install Dave’s required packages:

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install mendeleev sympy numpy matplotlib rich yfinance pandas scipy deep-translator

4. Start Dave:

python3 dave_macos.py

## Linux

Install Python 3.12 or newer and its venv support using your distribution’s package manager. For example, on Debian or Ubuntu:

sudo apt update
sudo apt install python3 python3-venv python3-pip

From the folder containing `dave_linux.py`, create the environment and install dependencies:

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip3 install --upgrade pip
python3 -m pip3 install mendeleev sympy numpy matplotlib rich yfinance pandas scipy deep-translator

Start Dave with:

python dave_linux.py

On a Linux desktop, plots use the available Tk display backend. On a headless machine, Dave uses Matplotlib’s non-interactive Agg backend; plot windows cannot open there.

## Windows

1. Install Python 3.12 or newer from [python.org](https://www.python.org/downloads/). Select **Add Python to PATH** in the installer.
2. Open PowerShell and move to the folder containing `dave2.py`.
3. Create and activate a virtual environment, then install Dave’s required packages:

py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install mendeleev sympy numpy matplotlib rich yfinance pandas scipy deep-translator


If PowerShell blocks environment activation, run this in that PowerShell window and activate again:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

4. Start Dave:

python dave_windows.py

## Android (Termux)

The Android build is intended for [Termux](https://github.com/termux/termux-app), a terminal environment for Android. Install Termux from one official source, such as [F-Droid](https://f-droid.org/packages/com.termux/) or [the Termux GitHub releases](https://github.com/termux/termux-app/releases). Do not mix installs from different sources; their app signatures can differ. See the [Termux installation notes](https://github.com/termux/termux-app#installation).

Open Termux and install Python and the compiled scientific packages through Termux’s package manager:

pkg update
pkg upgrade
pkg install python3 python-pip3 python-numpy python-scipy python-matplotlib python-pandas

Allow access to shared storage if you plan to open the file from Downloads:

termux-setup-storage

Place `dave_android.py` in the Termux home folder. If it is in Android’s Downloads folder, copy it into Termux with:

cp ~/storage/downloads/dave_android.py ~/

Then create an environment that can see the Termux-provided compiled packages:

cd ~
python -m venv --system-site-packages .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install mendeleev sympy rich yfinance deep-translator

Launch Dave with:

python dave_android.py

Android package support varies by device and Termux repository. Termux supplies compiled packages such as NumPy, SciPy, Matplotlib, and Pandas because building these libraries with pip directly on a phone can be difficult. Optional scientific integrations may not be available on Android. Dave’s Android build uses a non-GUI plotting backend, so it cannot open desktop plot windows.

## Using Dave

At the prompt, try:

2 + 2
sqrt(81)
derivative(x**3)
absolute value of -5

Enter `help` for the in-program feature list, `selftest` to run Dave’s checks, or `quit` to exit.

## Start Dave later

Each time you open a new terminal, activate the virtual environment again before running Dave.

**macOS/Linux/Termux:**

source .venv/bin/activate

Then run the platform’s file name, for example:

python dave_linux.py

**Windows PowerShell:**

.venv\Scripts\Activate.ps1
python dave2.py

## Optional scientific packages

Dave’s required packages enable its core calculator. Other scientific integrations load only when used and may need additional packages. Use Dave’s package status report to see which optional packages are installed. You do not need the entire optional package catalog for basic calculations.

Some lookup and geocoding features also require an internet connection and an available external service.

## Troubleshooting

- **`python` or `python3` not found:** Install Python, reopen the terminal, and check that Python is on your PATH. On Windows, try `py`.
- **`No module named ...`:** Activate `.venv` and install the missing required package in the commands above.
- **PowerShell blocks activation:** Use the process-scoped execution policy command in the Windows section.
- **A pip package fails to build on Android:** Install its Termux package if one exists. Some optional packages do not support Android.
- **A plot does not open on Linux or Android:** The headless backend creates no GUI window. Run Dave on a desktop with a graphical display for interactive plots


**If anything doesn't work, or you think something could be added, please put it in the comments, and I will do my best to fix/add it.**
