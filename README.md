Welcome to Dave! This calculator is designed to be a high performance calculator running on your computers computing power. Because of this, please don’t do anything crazy or else your computer may break.



Dave version 1.0.8 requires you to install the following dependencies so run the following commands:

MacOS:


/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/yourusername/.zprofile

eval "$(/opt/homebrew/bin/brew shellenv)"

brew install python

brew install pip3

python3 -m pip install --break-system-packages --upgrade sympy numpy scipy matplotlib rich pandas yfinance deep-translator mendeleev pyreadline3 pint

To run type python3 dave2.py into your terminal. If you downloaded the file, run cd Downloads first, and then run python3 dave2.py. If anything isn't working, please add it into the comments, and I will do my best to fix it. I you have any suggestions, I will also do my best to integrate them in, so you can put those in the comments too. The first run of Dave always takes the longest.
