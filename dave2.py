#!/usr/bin/env python3

SAVE_FILE = "variables.pkl"
history = []

from datetime import datetime
import random
import sys
sys.set_int_max_str_digits(0)

from mendeleev import element

# =========================================================
# PYTHON VERSION CHECK
# =========================================================

MIN_VERSION = (3, 10)

if sys.version_info < MIN_VERSION:

    print(
        f"""
ERROR:
Davemrequires Python {MIN_VERSION[0]}.{MIN_VERSION[1]} or newer.

Your version:
{sys.version}

Please install a newer version of Python from:
https://www.python.org/downloads/
"""
    )

    sys.exit()

sys.set_int_max_str_digits(0)

# =========================================================
# AUTO INSTALL REQUIRED PACKAGES
# =========================================================
import scipy
import sys
import inspect
import subprocess
import importlib

required_packages = {

    "sympy": "sympy",
    "numpy": "numpy",
    "matplotlib": "matplotlib",
    "rich": "rich",
    "yfinance": "yfinance",
    "pandas": "pandas",
    "scipy": "scipy",
    "deep_translator": "deep-translator"
}

import re

def selftest():

    tests = """
2+2
sqrt(81)
factorial(5)
log(10)
ln(E)
exp(2)
abs(-5)
round(3.14159,2)
floor(3.9)
ceil(3.1)

simplify(x+x)
simplify_full((x**2-1)/(x-1))
expand((x+1)**2)
expand_full((x+1)**5)
collect(x**2+2*x+x**2)
factor(x**2-9)
solve(x**2-9)
solve(Eq(x**2,9))
solvefor(x**2+y-5,"y")
solve([x+y-5,x-y-1],[x,y])
nsolve(x**3-2,1)
roots(x**2-9)
(x**2+1).subs(x,5)
(x**2+1).evalf()
is_equivalent(x**2-1,(x-1)*(x+1))
piecewise((x**2,x<0),(x,True))

derivative(x**3)
diff(x**3)
diff(x**3,x,2)
integral(x**2)
integrate(x**2)
integral_def(x**2,0,5)
numerical_integral(x**2,0,5)
limit(sin(x)/x,0)
taylor(sin(x),0,6)
series_expansion(sin(x),0,10)
gradient(x**2+y**2+z**2)
hessian(x**2+y**2+z**2)
directional_derivative(x**2+y**2+z**2,[1,1,1],[1,0,0])
laplacian(x**2+y**2+z**2)
summation(x**2,1,10)
product(x,1,5)
newton(x**2-2,x,1)
dsolve(Derivative(y(x),x)-y(x))

sin(pi/2)
cos(pi)
tan(pi/4)
asin(1)
acos(1)
atan(1)
sinh(1)
cosh(1)
tanh(1)
radians(90)
degrees(pi)

a=10
a+5
f=x**2+1
ans

graph(x**2)
graph(sin(x))
graph(cos(x))
graph(x**3-2*x)
graph3d(x**2+y**2)
graph3d(sin(x*y))
graph3d(x**2-y**2)
graph_parametric("t","t**2")
graph_polar("theta")
intersection(x**2,x+2)
ascii_plot(x**2)

mean([1,2,3,4,5])
median([1,2,3,4,5])
mode([1,1,2,3])
variance([1,2,3,4,5])
std([1,2,3,4,5])
percentile([1,2,3,4,5],50)
correlation([1,2,3],[2,4,6])
covariance([1,2,3],[2,4,6])
range_data([1,2,3,10])
sum_data([1,2,3])
z_scores([1,2,3,4,5])
moving_average([1,2,3,4,5],3)
quartiles([1,2,3,4,5])
iqr([1,2,3,4,5])
skewness([1,2,3,4,5])
kurtosis([1,2,3,4,5])
geometric_mean([1,2,3,4])
harmonic_mean([1,2,3,4])

matrix([[1,2],[3,4]])
det([[1,2],[3,4]])
inv([[1,2],[3,4]])
transpose([[1,2],[3,4]])
trace([[1,2],[3,4]])
rank([[1,2],[3,4]])
matmul([[1,2]],[[3],[4]])
matrix_power([[1,2],[3,4]],2)
eig([[1,2],[3,4]])
solve_linear_system([[2,1],[1,3]],[5,6])
jacobian([x**2+y,y**2+x],[x,y])
matrix_norm([[1,2],[3,4]])
matrix_rref([[1,2],[3,4]])
matrix_nullspace([[1,2],[3,4]])
matrix_columnspace([[1,2],[3,4]])
matrix_rowspace([[1,2],[3,4]])
characteristic_polynomial([[1,2],[3,4]])

dot([1,2,3],[4,5,6])
cross([1,0,0],[0,1,0])
mag([3,4])
angle([1,0],[0,1])
distance([1,2],[4,6])

gcd(48,18)
lcm(12,18)
prime(17)
is_square(144)
factorint(360)
factorint_safe(360)
totient(10)
modinv(3,11)
primes_up_to(100)
ncr(5,2)
npr(5,2)

elements()
atomic_mass("Fe")
atomic_number("Fe")
element_name("Fe")
element_info("Fe")
find_element("tungsten")
molar_mass("H2O")
molar_mass("CO2")
molar_mass("C6H12O6")
moles_from_mass(18.015,"H2O")
protons("Fe")
electrons("Fe")
neutrons("Fe")
ph(1e-7)
ideal_gas_pressure(1,273,22.4)
ideal_gas_volume(1,273,1)
ideal_gas_temperature(1,22.4,1)
ideal_gas_moles(1,273,22.4)
electron_configuration("Cu")
oxidation_states("Mn")
electronegativity("O")
atomic_radius("W")
covalent_radius("C")
density_element("Os")
melting_point("Re")
boiling_point("He")
thermal_conductivity("Ag")
specific_heat("Al")
element_count("C6H12O6")
percent_composition("H2O")
empirical_formula({"C":40.0,"H":6.7,"O":53.3})
molecular_formula("CH2O",180)
balance("H2 + O2 -> H2O")
limiting_reactant("2H2 + O2 -> 2H2O",{"H2":4,"O2":1})
theoretical_yield("2H2 + O2 -> 2H2O",{"H2":4,"O2":1},"H2O")
oxidation_lookup("KMnO4")
formula("water")
find_formula("glucose")
formulas_in("C6H12O6")

ke(10,5)
momentum(10,5)
force(10,9.8)
voltage(2,10)
emc2(1)
mass_from_energy(8.9875517873681764e16)
velocity(100,5)
acceleration(20,4)
density(10,2)
pressure(100,10)
work(10,5)
power(100,10)
frequency(0.02)
period(50)
wavelength(3e8,5e14)
escape_velocity(5.97e24,6.37e6)
projectile_range(100,45)
schwarzschild(5.97e24)
decay(1000,0.693,10)
gravity_force(5.97e24,1000,6.37e6)
momentum_vector(5,[1,2,3])

convert(1,"kg","lb")
convert(1,"m","ft")
base_convert(255,10,16)
bin(42)
oct(64)
hex(255)
decimal("1010",2)
to_roman(2024)

randint(1,10)
random()
randfloat(0,1)
choice([1,2,3])
draw_card()
roll()

simple_interest(1000,0.05,2)
compound_interest(1000,0.05,2,12)
loan_payment(10000,0.05,5)

AND(True,False)
OR(True,False)
NOT(True)
XOR(True,False)

caesar_encrypt("hello",3)
caesar_decrypt("khoor",3)
rot13("hello")
md5_hash("hello")
sha1_hash("hello")
sha256_hash("hello")
sha512_hash("hello")
xor_encrypt("hello","key")
vigenere_encrypt("HELLO","KEY")
vigenere_decrypt("RIJVS","KEY")
base64_encode("hello")
base64_decode("aGVsbG8=")
rsa_encrypt("hello",65537,3233)
rsa_decrypt(2790,2753,3233)

save_note("note.txt","hello")
read_note("note.txt")

pretty_json('{"a":1}')
validate_expr("x**2+1")
explain("x**2+1")
approx(pi)

stopwatch_start()
stopwatch_stop()

system_info()

commands()

time
date
month
year

deg
rad

lang en
lang es
lang fr
lang de
lang ja

help
about
history
quit
exit
q
"""

    namespace = {}

    try:
        namespace.update(globals().get("variables", {}))
    except:
        pass

    try:
        namespace.update(globals().get("user_vars", {}))
    except:
        pass

    passed = 0
    failed = 0

    bad_strings = ["Error", "error", "None", "zoo", "nan", "ComplexInfinity"]

    print("\n===== DAVE SELF TEST =====\n")

    for test in tests.strip().splitlines():
        test = test.strip()
        if not test:
            continue

        try:
            result = eval(test, {"__builtins__": {}}, namespace)
            result_str = str(result).strip()

            bad = (
                result_str.replace(" ", "") == test.replace(" ", "")
                or result_str == ""
                or any(x in result_str for x in bad_strings)
            )

            if bad:
                print(f"[BAD ] {test}\n       Returned: {result_str}")
                failed += 1
            else:
                print(f"[PASS] {test}\n       -> {result_str}")
                passed += 1

        except Exception as e:
            print(f"[FAIL] {test}\n       {repr(e)}")
            failed += 1

    print("\nPassed:", passed)
    print("Failed:", failed)
    print("==========================")

def emc2(mass):
    """
    Calculates energy from mass using E = mc²

    mass: kilograms
    returns: joules
    """
    c = 299_792_458  # m/s

    return mass * c**2

def time():
    return datetime.now().strftime("%H:%M:%S")

def date():
    return datetime.now().strftime("%Y-%m-%d")

def month():
    return datetime.now().strftime("%B")

def year():
    return datetime.now().year

def deg():
    global angle_mode
    angle_mode = "deg"
    return "Degree mode"

def rad():
    global angle_mode
    angle_mode = "rad"
    return "Radian mode"

def mass_from_energy(energy):
    c = 299_792_458
    return energy / c**2

def limiting_reactant(reaction, available):

    reactants = reaction.split("->")[0]

    coeffs = {}

    for part in reactants.split("+"):

        part = part.strip()

        m = re.match(r"(\d*)([A-Za-z0-9()]+)", part)

        if m:

            coeff = int(m.group(1)) if m.group(1) else 1
            formula = m.group(2)

            coeffs[formula] = coeff

    ratios = {}

    for species, coeff in coeffs.items():

        if species not in available:
            raise ValueError(
                f"Missing amount for {species}"
            )

        ratios[species] = available[species] / coeff

    limiting = min(ratios, key=ratios.get)

    return {
        "limiting_reactant": limiting,
        "reaction_units": ratios
    }


def install_and_import(import_name, package_name=None):

    if package_name is None:
        package_name = import_name

    try:

        importlib.import_module(import_name)

    except ImportError:

        print(f"Installing {package_name}...")

        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            package_name
        ])

        print(f"{package_name} installed successfully.")

for import_name, package_name in required_packages.items():

    install_and_import(import_name, package_name)

# =========================================================
# OPTIONAL UPGRADE NOTICE
# =========================================================

print("All required packages are installed.")

# =========================================================
# IMPORTS
# =========================================================

print("Starting Dave...")

import math

import yfinance as yf
import codecs
import pandas as pd 
import sympy as sp
import numpy as np

np.seterr(divide='warn', invalid='warn', over='warn', under='warn')

from fractions import Fraction
import matplotlib
try:
    matplotlib.use("TkAgg")
except:
    matplotlib.use("Agg")
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print

from deep_translator import GoogleTranslator
import statistics
import random
import readline
import pickle
import os
import atexit
import datetime
import re

E = sp.E

# =========================================================
# CONSOLE
# =========================================================

console = Console()

# =========================================================
# LANGUAGES
# =========================================================

language = "en"

languages = {
    "en": {"welcome":"Welcome","about":"Calculator OS","goodbye":"Goodbye","help":"Help","result":"Result","history":"History"},
    "es": {"welcome":"Bienvenido","about":"Sistema","goodbye":"Adiós","help":"Ayuda","result":"Resultado","history":"Historial"},
    "fr": {"welcome":"Bienvenue","about":"Système","goodbye":"Au revoir","help":"Aide","result":"Résultat","history":"Historique"},
    "de": {"welcome":"Willkommen","about":"System","goodbye":"Tschüss","help":"Hilfe","result":"Ergebnis","history":"Verlauf"},
    "jp": {"welcome":"ようこそ","about":"システム","goodbye":"さようなら","help":"ヘルプ","result":"結果","history":"履歴"}
}

# =========================================================
# HISTORY FILE
# =========================================================

HISTORY_FILE = "readline_history.txt"

try:
    readline.read_history_file(HISTORY_FILE)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, HISTORY_FILE)

# =========================================================
# EXTRA FEATURES
# =========================================================

# =========================================================
# MISSING FUNCTION DEFINITIONS
# =========================================================

import sympy as sp
import numpy as np
import math
import statistics

# ---------------- MATRIX ----------------

def matrix_trace(A):
    return sp.Matrix(A).trace()

def atomic_mass(symbol):
    return element(symbol).atomic_weight

def density_element(symbol):
    return element(symbol).density

def melting_point(symbol):
    return element(symbol).melting_point

def boiling_point(symbol):
    return element(symbol).boiling_point

def electron_configuration(symbol):
    return str(element(symbol).ec)

def electronegativity(symbol):
    return element(symbol).en_pauling

def atomic_radius(symbol):
    return element(symbol).atomic_radius

def covalent_radius(symbol):
    return element(symbol).covalent_radius

def oxidation_states(symbol):
    e = element(symbol)

    try:
        return [o.oxidation_state for o in e.oxistates]
    except:
        return []

def thermal_conductivity(symbol):
    return element(symbol).thermal_conductivity

def specific_heat(symbol):
    return element(symbol).specific_heat

def element_info(symbol):

    e = element(symbol)

    return {
        "name": e.name,
        "symbol": e.symbol,
        "atomic_number": e.atomic_number,
        "atomic_mass": e.atomic_weight,
        "density": e.density,
        "melting_point": e.melting_point,
        "boiling_point": e.boiling_point,
        "electron_configuration": str(e.ec),
        "electronegativity": e.en_pauling,
        "atomic_radius": e.atomic_radius,
        "covalent_radius": e.covalent_radius,
    }

def find_element(name):

    name = name.lower()

    for z in range(1,119):

        e = element(z)

        if (
            e.name.lower() == name
            or e.symbol.lower() == name
        ):
            return e.symbol

    return None

def matrix_norm(A):
    return float(sp.Matrix(A).norm())

def matrix_rref(A):
    return sp.Matrix(A).rref()[0]

def matrix_columnspace(A):
    return sp.Matrix(A).columnspace()

def matrix_rowspace(A):
    return sp.Matrix(A).rowspace()

def characteristic_polynomial(A):
    return sp.Matrix(A).charpoly().as_expr()

# ---------------- STATISTICS ----------------

def quartiles(data):
    data = sorted(data)
    n = len(data)

    q2 = statistics.median(data)

    if n % 2 == 0:
        lower = data[:n//2]
        upper = data[n//2:]
    else:
        lower = data[:n//2]
        upper = data[n//2+1:]

    q1 = statistics.median(lower)
    q3 = statistics.median(upper)

    return (q1, q2, q3)

def iqr(data):
    q1, _, q3 = quartiles(data)
    return q3 - q1

def covariance(x, y):
    return np.cov(x, y, bias=False)[0][1]

def correlation(x, y):
    return np.corrcoef(x, y)[0][1]

def z_scores(data):
    mean = statistics.mean(data)
    std = statistics.stdev(data)
    return [(x-mean)/std for x in data]

def moving_average(data, n):
    return [
        sum(data[i:i+n])/n
        for i in range(len(data)-n+1)
    ]

def skewness(data):
    x = np.array(data)
    m = np.mean(x)
    s = np.std(x)
    return np.mean(((x-m)/s)**3)

def kurtosis(data):
    x = np.array(data)
    m = np.mean(x)
    s = np.std(x)
    return np.mean(((x-m)/s)**4) - 3

def geometric_mean(data):
    return math.prod(data) ** (1 / len(data)) if data else 0

def skewness(data):
    x = np.array(data)
    m = np.mean(x)
    s = np.std(x)

    if s == 0:
        return 0

    return np.mean(((x - m) / s) ** 3)

def kurtosis(data):
    x = np.array(data)
    m = np.mean(x)
    s = np.std(x)

    if s == 0:
        return 0

    return np.mean(((x - m) / s) ** 4) - 3

def moving_average(data, n):
    if n <= 0 or n > len(data):
        return []

    return [
        sum(data[i:i+n]) / n
        for i in range(len(data) - n + 1)
    ]

def harmonic_mean(data):
    return statistics.harmonic_mean(data)

def correlation_strength(r):
    r = abs(r)

    if r < 0.2:
        return "very weak"
    elif r < 0.4:
        return "weak"
    elif r < 0.6:
        return "moderate"
    elif r < 0.8:
        return "strong"
    else:
        return "very strong"

# ---------------- PHYSICS ----------------

def velocity(distance, time):
    if time == 0:
        return "Division by zero"
    return distance / time



def acceleration(v1, v2, time):
    return (v2 - v1) / time

def density(mass, volume):
    if volume == 0:
        return "Division by zero"
    return mass / volume

def pressure(force, area):
    if area == 0:
        return "Division by zero"
    return force / area

def work(force, distance):
    return force * distance

def power(work_done, time):
    return work_done / time

def frequency(period):
    if period == 0:
        return "Division by zero"
    return 1 / period

def period(freq):
    if freq == 0:
        return "Division by zero"
    return 1 / freq

def wavelength(speed, freq):
    if freq == 0:
        return "Division by zero"
    return speed / freq

def escape_velocity(M, R):
    G = 6.67430e-11
    return math.sqrt(2 * G * M / R)

def era(earned_runs, innings_pitched):
    return earned_runs * 9 / innings_pitched

def batting_average(hits, at_bats):
    return hits / at_bats

def obp(hits, walks, hbp, at_bats, sac_flies):
    return (hits + walks + hbp) / (at_bats + walks + hbp + sac_flies)

def slg(singles, doubles, triples, home_runs, at_bats):
    return (
        singles +
        2 * doubles +
        3 * triples +
        4 * home_runs
    ) / at_bats

def translate(text, target="es"):

    try:

        return GoogleTranslator(
            source="auto",
            target=target
        ).translate(text)

    except Exception as e:

        return f"Translation error: {e}"

def ops(singles, doubles, triples, home_runs,
        hits, walks, hbp, at_bats, sac_flies):
    return (
        slg(singles, doubles, triples, home_runs, at_bats)
        + obp(hits, walks, hbp, at_bats, sac_flies)
    )

def whip(walks, hits, innings):
    return (walks + hits) / innings

def k_per_9(strikeouts, innings):
    return strikeouts * 9 / innings

def bb_per_9(walks, innings):
    return walks * 9 / innings

def hr_per_9(home_runs, innings):
    return home_runs * 9 / innings

def fielding_percentage(putouts, assists, errors):
    return (putouts + assists) / (putouts + assists + errors)

def relativistic_ke(m, v):
    c = 299792458
    gamma = 1 / math.sqrt(1 - (v/c)**2)
    return (gamma - 1) * m * c**2

def momentum_vector(mass, velocity_vector):
    return [mass * v for v in velocity_vector]

def projectile_range(v, theta_deg, g=9.80665):
    theta = math.radians(theta_deg)
    return (v**2 * math.sin(2*theta)) / g

def stock_name(symbol):
    import yfinance as yf

    try:
        info = yf.Ticker(symbol.upper()).info

        name = info.get("longName")

        if name is None:
            name = info.get("shortName")

        if name is None:
            return "Unknown Company"

        return name

    except Exception as e:
        return f"Error: {e}"

def dividend_yield(symbol):
    import yfinance as yf

    try:
        info = yf.Ticker(symbol.upper()).info

        dy = info.get("dividendYield")

        if dy is None:
            return 0.0

        return float(dy) * 100  # return as percentage

    except Exception as e:
        return f"Error: {e}"

def market_cap(symbol):

    try:

        info = yf.Ticker(symbol).info

        value = info.get("marketCap")

        if value is None:
            return "No market cap available"

        return float(value)

    except Exception as e:

        return f"Error: {e}"

def stock_price(symbol):

    try:

        ticker = yf.Ticker(symbol.upper())
        info = ticker.info

        price = info.get("currentPrice")

        if price is None:
            return "Price unavailable"

        return float(price)

    except Exception as e:

        return f"Error: {e}"

def stock_metrics(ticker_symbol):
    try:
        ticker = yf.Ticker(str(ticker_symbol).upper())
        df = ticker.history(period="max")

        if df.empty:
            return f"No data found for ticker '{ticker_symbol}'."

        current_price = float(df["Close"].iloc[-1])

        result = []
        result.append(f"{ticker_symbol.upper()} Stock Performance")
        result.append(f"Current Price: ${current_price:.2f}")
        result.append("")

        periods = {
            "1 Day": 1,
            "1 Week": 5,
            "1 Month": 21,
            "1 Year": 252,
            "5 Years": 252 * 5,
            "Max Time": len(df) - 1
        }

        for name, offset in periods.items():

            if len(df) > offset:

                past_price = float(df["Close"].iloc[-(offset + 1)])

                change = current_price - past_price
                pct = (change / past_price) * 100

                sign = "+" if change >= 0 else ""

                result.append(
                    f"{name}: {sign}${change:.2f} ({sign}{pct:.2f}%)"
                )

            else:

                result.append(
                    f"{name}: Insufficient historical data"
                )

        return "\n".join(result)

    except Exception as e:
        return f"Stock error: {e}"

def gravity_force(m1, m2, r):
    G = 6.67430e-11
    return G * m1 * m2 / r**2

def orbital_period(radius, central_mass):
    G = 6.67430e-11
    return 2 * math.pi * math.sqrt(radius**3 / (G * central_mass))

def luminosity(radius, temperature):
    sigma = 5.670374419e-8
    return 4 * math.pi * radius**2 * sigma * temperature**4

def log(x):
    return sp.N(sp.log(x))

def redshift(emitted, observed):
    return (observed - emitted) / emitted

def distance_modulus(apparent_mag, absolute_mag):
    return 10 ** ((apparent_mag - absolute_mag + 5) / 5)

def hill_sphere(a, m, M):
    return a * (m / (3 * M)) ** (1/3)

def decay(N0, t, half_life):
    return N0 * (0.5)**(t / half_life)

def schwarzschild(mass):
    G = 6.67430e-11
    c = 299792458
    return 2 * G * mass / c**2


def stock(symbol):
    try:
        ticker = yf.Ticker(symbol.upper())
        df = ticker.history(period="max")

        if df.empty:
            return f"No data found for {symbol}"

        current_price = df["Close"].iloc[-1]

        output = []
        output.append(f"{symbol.upper()} Stock Performance")
        output.append(f"Current Price: ${current_price:.2f}")

        periods = {
            "1 Day": 1,
            "1 Week": 5,
            "1 Month": 21,
            "1 Year": 252,
            "5 Years": 252 * 5,
            "Max Time": len(df) - 1
        }

        for period_name, offset in periods.items():
            if len(df) > offset:
                past_price = df["Close"].iloc[-(offset + 1)]
                change = current_price - past_price
                pct = (change / past_price) * 100

                output.append(
                    f"{period_name}: {change:+.2f} ({pct:+.2f}%)"
                )

        return "\n".join(output)

    except Exception as e:
        return f"Error: {e}"

# ---------------- CHEMISTRY ----------------

def moles(mass, molar_mass):
    return mass / molar_mass

import random

# =========================================================
# NUMBER GUESSING GAME
# =========================================================

current_target = None
current_maximum = None


def start_guess_game(maximum=100):
    """
    Start a new guessing game.

    Example:
        start_guess_game(100)
    """
    global current_target, current_maximum

    current_maximum = int(maximum)
    current_target = random.randint(1, current_maximum)

    return f"Game started! Guess a number between 1 and {current_maximum}."


def guess(number):
    """
    Make a guess.

    Example:
        guess(50)
    """
    global current_target, current_maximum

    if current_target is None:
        return "No active game. Start one with start_guess_game(maximum)."

    number = int(number)

    if number < current_target:
        return "Too low!"
    elif number > current_target:
        return "Too high!"
    else:
        answer = current_target

        current_target = None
        current_maximum = None

        return f"Correct! The answer was {answer}."


def reveal_answer():
    """
    Reveal the current answer.
    """
    global current_target

    if current_target is None:
        return "No active game."

    return current_target


def end_guess_game():
    """
    End the current game.
    """
    global current_target, current_maximum

    current_target = None
    current_maximum = None

    return "Game ended."


def game_status():
    """
    Show current game status.
    """
    global current_target, current_maximum

    if current_target is None:
        return "No active game."

    return f"Active game: guessing between 1 and {current_maximum}."

def mass_from_moles(moles_value, molar_mass):
    return moles_value * molar_mass

def molecules(moles_value):
    return moles_value * 6.02214076e23

def matrix_transpose(A):
    return np.array(A).T

def matrix_nullspace(A):
    return sp.Matrix(A).nullspace()

def matrix_columnspace(A):
    return sp.Matrix(A).columnspace()

def matrix_rowspace(A):
    return sp.Matrix(A).rowspace()

def characteristic_polynomial(A):
    return sp.Matrix(A).charpoly().as_expr()

def pe_ratio(symbol):
    import yfinance as yf

    try:
        pe = yf.Ticker(symbol).info.get("trailingPE")

        if pe is None:
            return "No P/E ratio available"

        return float(pe)

    except Exception as e:
        return f"Error: {e}"

def molarity(moles_value, liters):
    return moles_value / liters
    if denominator == 0:
        return "Division by zero"

def ideal_gas_volume(n, T, P):
    R = 0.082057
    return n * R * T / P

def ideal_gas_temperature(P, V, n):
    R = 0.082057
    return P * V / (n * R)

def ideal_gas_moles(P, V, T):
    R = 0.082057
    return P * V / (R * T)

def quadratic(a,b,c):
    x = sp.Symbol('x')
    return sp.solve(a*x**2+b*x+c)

import random

def random_number(minimum=1, maximum=100):
    minimum = int(minimum)
    maximum = int(maximum)

    if minimum > maximum:
        return "Error: minimum cannot be larger than maximum."

    return random.randint(minimum, maximum)

def linear(a,b):
    x = sp.Symbol('x')
    return sp.solve(a*x+b)

import time

start_time = None

def stopwatch_start():
    global start_time

    start_time = time.time()

    return "Stopwatch started."

def cubic(a,b,c,d):
    x = sp.Symbol('x')
    return sp.solve(a*x**3+b*x**2+c*x+d)

def protons(Z):
    return Z

def density_material(name):
    return materials[name.lower()]["density"]

def youngs_modulus_material(name):
    return materials[name.lower()]["youngs_modulus"]

def electrons(element_symbol):
    if element_symbol not in periodic_table:
        return "Unknown element"

    return periodic_table[element_symbol]["number"]

def ph(H):

    if H <= 0:
        return "Invalid concentration"

    return -math.log10(H)

# ---------------- CHEMISTRY CONSTANTS ----------------

electron_mass = 9.1093837015e-31
proton_mass = 1.67262192369e-27
neutron_mass = 1.67492749804e-27

R = 8.314462618
F = 96485.33212

# ---------------- CALCULUS ----------------
import sympy as sp

def newton(expr, variable, guess):
    return sp.nsolve(expr, variable, guess)


def series_expansion(expr, var, point=0, order=6):
    return sp.series(expr, var, point, order)

# ---------------- NUMBER THEORY ----------------

def factor_list(n):
    return [i for i in range(1, n+1) if n % i == 0]

def largest_prime_factor(n):
    factors = sp.factorint(n)
    return max(factors.keys())

def totient(n):
    return sp.totient(n)

def decimal_from_base(x):
    return float(x)

def stats_mean(data):
    return statistics.mean(data)

def stats_median(data):
    return statistics.median(data)

def stats_mode(data):

    try:
        return statistics.mode(data)

    except:
        return statistics.multimode(data)
    
def stats_var(data):
    return statistics.variance(data)

def stats_std(data):
    return statistics.stdev(data)

def matrix_det(m):

    arr = np.array(m, dtype=float)

    return float(np.linalg.det(arr))

def matrix_inv(m):

    try:

        arr = np.array(m, dtype=float)

        return np.linalg.inv(arr).tolist()

    except np.linalg.LinAlgError:

        return "Matrix is singular."

def matrix_mul(a, b):

    A = np.array(a, dtype=float)
    B = np.array(b, dtype=float)

    return (A @ B).tolist()

def eigenvalues(m):
    return np.linalg.eigvals(np.array(m)).tolist()

def dot(a, b):
    return float(np.dot(a, b))

def cross(a, b):
    return np.cross(a, b).tolist()

def mag(v):
    return float(np.linalg.norm(v))

def angle_between(a, b):

    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)

    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)

    if na == 0 or nb == 0:
        return "Zero-length vector"

    cos_theta = np.dot(a, b)/(na*nb)

    cos_theta = np.clip(cos_theta,-1,1)

    return float(np.arccos(cos_theta))

def derivative(expr):

    expr = sp.sympify(expr)

    return sp.diff(expr, x)

dsolve = sp.dsolve
Function = sp.Function
Derivative = sp.Derivative
Eq = sp.Eq

def sinh(x):
    return float(math.sinh(x))

def cosh(x):
    return float(math.cosh(x))

def tanh(x):
    return float(math.tanh(x))

def matrix_rank(A):
    return sp.Matrix(A).rank()

def integral(expr):
    return sp.integrate(sp.sympify(expr), x)

def definite_integral(expr, a, b):
    return sp.integrate(sp.sympify(expr), (x, a, b))

def limit(expr, var_value):
    return sp.limit(sp.sympify(expr), x, var_value)

def taylor(expr, point, order):
    return sp.series(sp.sympify(expr), x, point, order).removeO()

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def prime_factors(n):
    return sp.factorint(n)

def modinv(a, m):
    return pow(a, -1, m)

def circle_area(r):
    return math.pi * r**2

def parse_list(s):
    return list(map(float, s.split(",")))

def sphere_volume(r):
    return (4/3) * math.pi * r**3

def triangle_area(a, b, c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def linear_regression(x_vals, y_vals):
    return np.polyfit(x_vals, y_vals, 1).tolist()

def poly_fit(x_vals, y_vals, degree):
    return np.polyfit(x_vals, y_vals, degree).tolist()

def nsolve_equation(expr, guess):
    return sp.nsolve(sp.sympify(expr), x, guess)

def partial_x(expr):
    return sp.diff(sp.sympify(expr), x)

def partial_y(expr):
    return sp.diff(sp.sympify(expr), y)

def jacobian(exprs, vars_):
    return sp.Matrix(exprs).jacobian(vars_)

def hessian(expr):
    return sp.hessian(sp.sympify(expr), (x, y))

def newton_nsolve(expr, guess, iterations=10):

    expr = sp.sympify(expr)
    deriv = sp.diff(expr, x)

    val = guess

    for _ in range(iterations):
        val = val - expr.subs(x, val) / deriv.subs(x, val)

    return sp.N(val)

def binary(n):
    return bin(n)

def hexadecimal(n):
    return hex(n)

def decimal(n, base):
    return int(n, base)

import inspect

def smoke_test():
    for name, func in variables.items():
        if not callable(func):
            continue

        try:
            n = len(inspect.signature(func).parameters)

            args = [1] * n

            result = func(*args)

            print(f"PASS {name}")

        except Exception as e:
            print(f"FAIL {name}: {e}")

def ncr(n,r):
    return math.comb(n,r)

def npr(n,r):
    return math.perm(n,r)

def kinetic_energy(m,v):
    return 0.5*m*v**2

def force(m,a):
    return m*a

def voltage(i,r):
    return i*r

def rank(m):
    return int(np.linalg.matrix_rank(np.array(m)))

def transpose(m):
    return np.array(m).T.tolist()

def trace(m):
    return float(np.trace(np.array(m)))

def summation(expr, start, end):

    return sp.summation(sp.sympify(expr), (x, start, end))

def product(expr, start, end):

    return sp.product(sp.sympify(expr), (x, start, end))

def ideal_gas_temperature(P, V, n):
    R = 8.314
    return (P * V) / (n * R)

def ideal_gas_volume(n, T, P):

    if P == 0:
        return "Division by zero"

    return (n * R * T) / P

def ideal_gas_temperature(P, V, n):

    if n == 0:
        return "Division by zero"

    return (P * V) / (n * R)

def ideal_gas_moles(P, V, T):

    if T == 0:
        return "Division by zero"

    return (P * V) / (R * T)

def ideal_gas_moles(P, V, T):
    R = 8.314
    return (P * V) / (R * T)

def nsolve_equation(expr, guess):

    return sp.nsolve(sp.sympify(expr), guess)
def solvefor(expr, var):

    return sp.solve(sp.sympify(expr), sp.Symbol(var))

def solve_equation(expr):
    lhs, rhs = expr.split("=")
    return sp.solve(sp.sympify(lhs) - sp.sympify(rhs), x)

def percentile(data, p):
    return np.percentile(data, p)

def correlation(x, y):
    return np.corrcoef(x, y)[0,1]

def covariance(x, y):
    return np.cov(x, y)[0,1]

def frac(n):
    return Fraction(n).limit_denominator()

def dsolve_equation(expr, func):
    return sp.dsolve(sp.sympify(expr))

def series_expansion(expr, point=0, order=6):
    return sp.series(sp.sympify(expr), x, point, order).removeO()

def is_equivalent(expr1, expr2):
    return sp.simplify(sp.sympify(expr1) - sp.sympify(expr2)) == 0

def graph_parametric(x_expr, y_expr, t_range=(-10,10)):
    t = sp.symbols('t')

    fx = sp.lambdify(t, sp.sympify(x_expr), "numpy")
    fy = sp.lambdify(t, sp.sympify(y_expr), "numpy")

    ts = np.linspace(t_range[0], t_range[1], 1000)

    plt.plot(fx(ts), fy(ts))
    plt.grid()
    plt.show()

def graph_polar(r_expr):
    theta = sp.symbols('theta')

    f = sp.lambdify(theta, sp.sympify(r_expr), "numpy")

    t = np.linspace(0, 2*np.pi, 1000)
    r = f(t)

    plt.polar(t, r)
    plt.show()

def intersection(f1, f2):
    x_sym = sp.symbols('x')
    return sp.solve(sp.sympify(f1) - sp.sympify(f2), x_sym)

def z_scores(data):
    arr = np.array(data)
    return ((arr - np.mean(arr)) / np.std(arr)).tolist()

def moving_average(data, window=3):
    arr = np.array(data)
    return np.convolve(arr, np.ones(window)/window, mode='valid').tolist()


def relativistic_ke(m, v):
    c = 299792458
    gamma = 1 / np.sqrt(1 - (v**2 / c**2))
    return (gamma - 1) * m * c**2

def momentum_vector(m, v):
    return np.array(v) * m

def factor_list(n):
    factors = sp.factorint(int(n))
    return list(factors.items())

def totient(n):
    return sp.totient(int(n))

def largest_prime_factor(n):
    return max(sp.factorint(int(n)).keys())

def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def triangle_perimeter(a, b, c):
    return a + b + c

def arc_length(r, theta):
    return r * theta

def validate_expr(expr):
    try:
        sp.sympify(expr)
        return True
    except:
        return False

def explain(expr):
    simplified = sp.simplify(expr)
    return {
        "original": expr,
        "simplified": simplified,
        "numeric": sp.N(simplified)
    }

def approx(value, digits=3):
    return round(float(value), digits)

def rot13(text):
    return codecs.decode(text, "rot_13")

import hashlib

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

import hashlib

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def sha1_hash(text):
    return hashlib.sha1(text.encode()).hexdigest()

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def sha512_hash(text):
    return hashlib.sha512(text.encode()).hexdigest()

def vigenere_encrypt(text, key):

    result = ""

    key = key.lower()
    key_index = 0

    for char in text:

        if char.isalpha():

            shift = ord(key[key_index % len(key)]) - ord('a')

            start = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char) - start + shift) % 26 + start)

            key_index += 1

        else:
            result += char

    return result


def vigenere_decrypt(text, key):

    result = ""

    key = key.lower()
    key_index = 0

    for char in text:

        if char.isalpha():

            shift = ord(key[key_index % len(key)]) - ord('a')

            start = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char) - start - shift) % 26 + start)

            key_index += 1

        else:
            result += char

    return result

def xor_encrypt(text,key):

    return ''.join(
        chr(
            ord(c) ^
            ord(key[i % len(key)])
        )
        for i,c in enumerate(text)
    )

import base64

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    return base64.b64decode(text.encode()).decode()

def rsa_encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def rsa_decrypt(cipher, d, n):
    return ''.join(chr(pow(c, d, n)) for c in cipher)

import pandas as pd

def load_csv(file):
    return pd.read_csv(file)

def corr_matrix(data):
    return data.corr()

def histogram(data):

    plt.hist(data)
    plt.show()

def scatter(x, y):

    plt.scatter(x, y)
    plt.show()

def projectile_range(v, theta):

    theta = math.radians(theta)

    return (v**2 * math.sin(2*theta)) / g

def gravity_force(m1, m2, r):

    G = 6.67430e-11

    return G * m1 * m2 / r**2

def decay(N0, half_life, t):
    return N0 * (0.5)**(t/half_life)

def ph(H):
    return -math.log10(H)

planets = {
    "earth": {
        "mass": 5.972e24,
        "radius": 6371000
    }
}

def schwarzschild(m):

    G = 6.67430e-11
    c = 299792458

    return 2*G*m/c**2

import json

def pretty_json(data):

    if isinstance(data, str):
        obj = json.loads(data)
    else:
        obj = data

    return json.dumps(
        obj,
        indent=4
    )

import time

start_time = None

def stopwatch_stop():
    global start_time

    if start_time is None:
        return "Stopwatch has not been started."

    elapsed = time.time() - start_time

    start_time = None

    return elapsed

def save_note(filename, text):
    with open(filename, "w") as f:
        f.write(text)

def read_note(filename):
    with open(filename) as f:
        return f.read()

import platform

def system_info():

    return {
        "system": platform.system(),
        "version": platform.version(),
        "machine": platform.machine()
    }

def draw_card():

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    ranks = [
        "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    return f"{random.choice(ranks)} of {random.choice(suits)}"

def roll(sides=6):
    return random.randint(1, sides)

def commands():
    for name in sorted(variables):
        print(name)

# =========================================================
# SETTINGS
# =========================================================

SAVE_FILE = "variables.pkl"
user_vars = {}

if os.path.exists(SAVE_FILE):
    try:
        with open(SAVE_FILE, "rb") as f:
            user_vars = pickle.load(f)
    except:
        user_vars = {}

history = []
last_answer = None

# =========================================================
# TRIG
# =========================================================

def _to_rad(v):
    return math.radians(v) if angle_mode == "deg" else v

def sin_wrapper(v): return sp.sin(_to_rad(v))
def cos_wrapper(v): return sp.cos(_to_rad(v))
def tan_wrapper(v): return sp.tan(_to_rad(v))

# =========================================================
# CHEMISTRY + TABLE
# =========================================================

periodic_table = {
    "H":  {"name": "Hydrogen",      "mass": 1.008,   "number": 1},
    "He": {"name": "Helium",        "mass": 4.0026,  "number": 2},
    "Li": {"name": "Lithium",       "mass": 6.94,    "number": 3},
    "Be": {"name": "Beryllium",     "mass": 9.0122,  "number": 4},
    "B":  {"name": "Boron",         "mass": 10.81,   "number": 5},
    "C":  {"name": "Carbon",        "mass": 12.011,  "number": 6},
    "N":  {"name": "Nitrogen",      "mass": 14.007,  "number": 7},
    "O":  {"name": "Oxygen",        "mass": 15.999,  "number": 8},
    "F":  {"name": "Fluorine",      "mass": 18.998,  "number": 9},
    "Ne": {"name": "Neon",          "mass": 20.180,  "number": 10},

    "Na": {"name": "Sodium",        "mass": 22.990,  "number": 11},
    "Mg": {"name": "Magnesium",     "mass": 24.305,  "number": 12},
    "Al": {"name": "Aluminum",      "mass": 26.982,  "number": 13},
    "Si": {"name": "Silicon",      "mass": 28.085,  "number": 14},
    "P":  {"name": "Phosphorus",    "mass": 30.974,  "number": 15},
    "S":  {"name": "Sulfur",        "mass": 32.06,   "number": 16},
    "Cl": {"name": "Chlorine",      "mass": 35.45,   "number": 17},
    "Ar": {"name": "Argon",         "mass": 39.948,  "number": 18},

    "K":  {"name": "Potassium",     "mass": 39.098,  "number": 19},
    "Ca": {"name": "Calcium",       "mass": 40.078,  "number": 20},
    "Sc": {"name": "Scandium",      "mass": 44.956,  "number": 21},
    "Ti": {"name": "Titanium",      "mass": 47.867,  "number": 22},
    "V":  {"name": "Vanadium",      "mass": 50.942,  "number": 23},
    "Cr": {"name": "Chromium",      "mass": 51.996,  "number": 24},
    "Mn": {"name": "Manganese",     "mass": 54.938,  "number": 25},
    "Fe": {"name": "Iron",          "mass": 55.845,  "number": 26},
    "Co": {"name": "Cobalt",        "mass": 58.933,  "number": 27},
    "Ni": {"name": "Nickel",        "mass": 58.693,  "number": 28},
    "Cu": {"name": "Copper",        "mass": 63.546,  "number": 29},
    "Zn": {"name": "Zinc",          "mass": 65.38,   "number": 30},

    "Ga": {"name": "Gallium",       "mass": 69.723,  "number": 31},
    "Ge": {"name": "Germanium",     "mass": 72.630,  "number": 32},
    "As": {"name": "Arsenic",       "mass": 74.922,  "number": 33},
    "Se": {"name": "Selenium",      "mass": 78.971,  "number": 34},
    "Br": {"name": "Bromine",       "mass": 79.904,  "number": 35},
    "Kr": {"name": "Krypton",       "mass": 83.798,  "number": 36},

    "Rb": {"name": "Rubidium",      "mass": 85.468,  "number": 37},
    "Sr": {"name": "Strontium",     "mass": 87.62,   "number": 38},
    "Y":  {"name": "Yttrium",       "mass": 88.906,  "number": 39},
    "Zr": {"name": "Zirconium",     "mass": 91.224,  "number": 40},
    "Nb": {"name": "Niobium",       "mass": 92.906,  "number": 41},
    "Mo": {"name": "Molybdenum",    "mass": 95.95,   "number": 42},
    "Tc": {"name": "Technetium",    "mass": 98,      "number": 43},
    "Ru": {"name": "Ruthenium",     "mass": 101.07,  "number": 44},
    "Rh": {"name": "Rhodium",       "mass": 102.91,  "number": 45},
    "Pd": {"name": "Palladium",     "mass": 106.42,  "number": 46},
    "Ag": {"name": "Silver",        "mass": 107.87,  "number": 47},
    "Cd": {"name": "Cadmium",       "mass": 112.41,  "number": 48},

    "In": {"name": "Indium",        "mass": 114.82,  "number": 49},
    "Sn": {"name": "Tin",           "mass": 118.71,  "number": 50},
    "Sb": {"name": "Antimony",      "mass": 121.76,  "number": 51},
    "Te": {"name": "Tellurium",     "mass": 127.60,  "number": 52},
    "I":  {"name": "Iodine",        "mass": 126.90,  "number": 53},
    "Xe": {"name": "Xenon",         "mass": 131.29,  "number": 54},

    "Cs": {"name": "Cesium",        "mass": 132.91,  "number": 55},
    "Ba": {"name": "Barium",        "mass": 137.33,  "number": 56},
    "La": {"name": "Lanthanum",     "mass": 138.91,  "number": 57},
    "Ce": {"name": "Cerium",        "mass": 140.12,  "number": 58},
    "Pr": {"name": "Praseodymium",  "mass": 140.91,  "number": 59},
    "Nd": {"name": "Neodymium",     "mass": 144.24,  "number": 60},
    "Pm": {"name": "Promethium",    "mass": 145,     "number": 61},
    "Sm": {"name": "Samarium",      "mass": 150.36,  "number": 62},
    "Eu": {"name": "Europium",      "mass": 151.96,  "number": 63},
    "Gd": {"name": "Gadolinium",    "mass": 157.25,  "number": 64},
    "Tb": {"name": "Terbium",       "mass": 158.93,  "number": 65},
    "Dy": {"name": "Dysprosium",    "mass": 162.50,  "number": 66},
    "Ho": {"name": "Holmium",       "mass": 164.93,  "number": 67},
    "Er": {"name": "Erbium",        "mass": 167.26,  "number": 68},
    "Tm": {"name": "Thulium",       "mass": 168.93,  "number": 69},
    "Yb": {"name": "Ytterbium",     "mass": 173.05,  "number": 70},
    "Lu": {"name": "Lutetium",      "mass": 174.97,  "number": 71},

    "Hf": {"name": "Hafnium",       "mass": 178.49,  "number": 72},
    "Ta": {"name": "Tantalum",      "mass": 180.95,  "number": 73},
    "W":  {"name": "Tungsten",      "mass": 183.84,  "number": 74},
    "Re": {"name": "Rhenium",       "mass": 186.21,  "number": 75},
    "Os": {"name": "Osmium",        "mass": 190.23,  "number": 76},
    "Ir": {"name": "Iridium",       "mass": 192.22,  "number": 77},
    "Pt": {"name": "Platinum",      "mass": 195.08,  "number": 78},
    "Au": {"name": "Gold",          "mass": 196.97,  "number": 79},
    "Hg": {"name": "Mercury",       "mass": 200.59,  "number": 80},
    "Tl": {"name": "Thallium",      "mass": 204.38,  "number": 81},
    "Pb": {"name": "Lead",          "mass": 207.20,  "number": 82},
    "Bi": {"name": "Bismuth",       "mass": 208.98,  "number": 83},
    "Po": {"name": "Polonium",      "mass": 209,     "number": 84},
    "At": {"name": "Astatine",      "mass": 210,     "number": 85},
    "Rn": {"name": "Radon",         "mass": 222,     "number": 86},

    "Fr": {"name": "Francium",      "mass": 223,     "number": 87},
    "Ra": {"name": "Radium",        "mass": 226,     "number": 88},
    "Ac": {"name": "Actinium",      "mass": 227,     "number": 89},
    "Th": {"name": "Thorium",       "mass": 232.04,  "number": 90},
    "Pa": {"name": "Protactinium",  "mass": 231.04,  "number": 91},
    "U":  {"name": "Uranium",       "mass": 238.03,  "number": 92},
    "Np": {"name": "Neptunium",     "mass": 237,     "number": 93},
    "Pu": {"name": "Plutonium",     "mass": 244,     "number": 94},
    "Am": {"name": "Americium",     "mass": 243,     "number": 95},
    "Cm": {"name": "Curium",        "mass": 247,     "number": 96},
    "Bk": {"name": "Berkelium",     "mass": 247,     "number": 97},
    "Cf": {"name": "Californium",   "mass": 251,     "number": 98},
    "Es": {"name": "Einsteinium",   "mass": 252,     "number": 99},
    "Fm": {"name": "Fermium",       "mass": 257,     "number": 100},
    "Md": {"name": "Mendelevium",   "mass": 258,     "number": 101},
    "No": {"name": "Nobelium",      "mass": 259,     "number": 102},
    "Lr": {"name": "Lawrencium",    "mass": 266,     "number": 103},
    "Rf": {"name": "Rutherfordium", "mass": 267,     "number": 104},
    "Db": {"name": "Dubnium",       "mass": 270,     "number": 105},
    "Sg": {"name": "Seaborgium",    "mass": 271,     "number": 106},
    "Bh": {"name": "Bohrium",       "mass": 270,     "number": 107},
    "Hs": {"name": "Hassium",       "mass": 277,     "number": 108},
    "Mt": {"name": "Meitnerium",    "mass": 278,     "number": 109},
    "Ds": {"name": "Darmstadtium",  "mass": 281,     "number": 110},
    "Rg": {"name": "Roentgenium",   "mass": 282,     "number": 111},
    "Cn": {"name": "Copernicium",   "mass": 285,     "number": 112},
    "Nh": {"name": "Nihonium",      "mass": 286,     "number": 113},
    "Fl": {"name": "Flerovium",     "mass": 289,     "number": 114},
    "Mc": {"name": "Moscovium",     "mass": 290,     "number": 115},
    "Lv": {"name": "Livermorium",   "mass": 293,     "number": 116},
    "Ts": {"name": "Tennessine",    "mass": 294,     "number": 117},
    "Og": {"name": "Oganesson",     "mass": 294,     "number": 118}
}

def elements():
    table = Table(title="Periodic Table")
    table.add_column("Symbol")
    table.add_column("Name")
    table.add_column("Atomic #")
    table.add_column("Mass")

    for s,d in periodic_table.items():
        table.add_row(s,d["name"],str(d["number"]),str(d["mass"]))

    console.print(table)

# =========================================================
# ADVANCED CALCULUS
# =========================================================

def directional_derivative(expr, point, direction):

    grad = gradient(expr)

    grad_func = [
        sp.lambdify((x, y, z), g)
        for g in grad
    ]

    gx = grad_func[0](*point)
    gy = grad_func[1](*point)
    gz = grad_func[2](*point)

    direction = np.array(direction, dtype=float)

    direction = direction / np.linalg.norm(direction)

    return gx*direction[0] + gy*direction[1] + gz*direction[2]


def laplacian(expr):

    expr = sp.sympify(expr)

    return (
        sp.diff(expr, x, 2)
        + sp.diff(expr, y, 2)
        + sp.diff(expr, z, 2)
    )

# =========================================================
# BASE CONVERSIONS
# =========================================================

def base_convert(number, from_base, to_base):

    decimal_value = int(str(number), from_base)

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if decimal_value == 0:
        return "0"

    result = ""

    while decimal_value > 0:
        result = digits[decimal_value % to_base] + result
        decimal_value //= to_base

    return result

# =========================================================
# CHEMISTRY FUNCTIONS
# =========================================================

def atomic_mass(s): return periodic_table[s]["mass"] if s in periodic_table else "Unknown"
def atomic_number(s): return periodic_table[s]["number"] if s in periodic_table else "Unknown"
def element_name(s): return periodic_table[s]["name"] if s in periodic_table else "Unknown"

def molar_mass(f):
    tokens = re.findall(r'([A-Z][a-z]?)(\d*)', f)
    total = 0
    for e,c in tokens:
        if e not in periodic_table: return "Unknown element"
        total += periodic_table[e]["mass"] * (int(c) if c else 1)
    return total

def real(z):
    return sp.re(z)

def imag(z):
    return sp.im(z)

def conjugate(z):
    return sp.conjugate(z)

def ideal_gas_pressure(n,T,V):
    return (n*8.314*T)/V

def protons(s):
    return atomic_number(s)

def neutrons(s):
    if s in periodic_table:
        return round(periodic_table[s]["mass"]) - periodic_table[s]["number"]
    return "Unknown"

def fibonacci(n):
    n = int(n)
    seq = [0,1]

    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])

    return seq[:n]

def polar_complex(r, theta):

    if angle_mode == "deg":
        theta = math.radians(theta)

    return complex(
        r * math.cos(theta),
        r * math.sin(theta)
    )


def is_prime(n):

    n = int(n)

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):

        if n % i == 0:
            return False

    return True

def primes_up_to(n):

    n = int(n)

    result = []

    for i in range(2, n + 1):

        if is_prime(i):
            result.append(i)

    return result

c = 299792458
h = 6.62607015e-34
k = 1.380649e-23
Na = 6.02214076e23
g = 9.80665
golden_ratio = (1 + math.sqrt(5)) / 2
electron_mass = 9.1093837015e-31
proton_mass = 1.67262192369e-27
neutron_mass = 1.67492749804e-27

R = 8.31446261815324
F = 96485.33212
# =========================================================
# FINANCIAL FUNCTIONS
# =========================================================

def simple_interest(p, r, t):
    return p * r * t


def compound_interest(p, r, t, n=1):
    return p * ((1 + r/n) ** (n*t))


def loan_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    payments = years * 12

    return (
        principal *
        (monthly_rate * (1 + monthly_rate)**payments)
        /
        ((1 + monthly_rate)**payments - 1)
    )

# =========================================================
# PROBABILITY
# =========================================================

def probability(successes, total):
    return successes / total


def binomial_probability(n, k, p):
    return math.comb(n, k) * (p**k) * ((1-p)**(n-k))


def permutations(n, r):
    return math.perm(n, r)


def combinations(n, r):
    return math.comb(n, r)

# =========================================================
# ADVANCED EQUATION SOLVERS
# =========================================================

def solve_quadratic(a, b, c):
    disc = b**2 - 4*a*c

    if disc >= 0:
        r1 = (-b + math.sqrt(disc)) / (2*a)
        r2 = (-b - math.sqrt(disc)) / (2*a)
    else:
        r1 = complex(-b/(2*a), math.sqrt(-disc)/(2*a))
        r2 = complex(-b/(2*a), -math.sqrt(-disc)/(2*a))

    return [r1, r2]


def solve_cubic(expr):
    return sp.solve(sp.sympify(expr), x)


def numerical_integral(expr, a, b):
    f = sp.lambdify(x, sp.sympify(expr), "numpy")
    xs = np.linspace(float(a), float(b), 10000)
    ys = f(xs)
    return np.trapz(ys, xs)

# =========================================================
# ROMAN NUMERALS
# =========================================================

def to_roman(num):

    vals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""

    for v, s in vals:

        while num >= v:
            result += s
            num -= v

    return result

# ==========================================================
# CONVERT
# ==========================================================

def convert(value, from_unit, to_unit):

    value = float(value)

    conversions = {

        ("kg","lb"):2.20462,
        ("lb","kg"):0.453592,

        ("m","ft"):3.28084,
        ("ft","m"):0.3048,

        ("m","in"):39.3701,
        ("in","m"):0.0254,

        ("km","mi"):0.621371,
        ("mi","km"):1.60934,

        ("g","oz"):0.035274,
        ("oz","g"):28.3495,

        ("l","gal"):0.264172,
        ("gal","l"):3.78541,
    }

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if (from_unit,to_unit) in conversions:
        return value * conversions[(from_unit,to_unit)]

    elif from_unit == "c" and to_unit == "f":
        return value * 9/5 + 32

    elif from_unit == "f" and to_unit == "c":
        return (value - 32) * 5/9

    return "Unsupported conversion"

def to_binary(n):
    return bin(int(n))

def to_hex(n):
    return hex(int(n))

def to_octal(n):
    return oct(int(n))

def randint(a, b):
    return random.randint(a, b)

def randfloat(a=0,b=1):
    return random.uniform(a,b)

def choice(lst):
    return random.choice(lst)

def roots(expr):
    return sp.solve(sp.sympify(expr), x)

def formula(name):
    return formulas.get(
        str(name).lower(),
        "Formula not found."
    )

def find_formula(text):

    text = text.lower()

    return [
        k for k in formulas
        if text in k
    ]

formula_categories = {

    "physics":[
        "newton",
        "kinetic energy",
        "potential energy",
        "momentum"
    ],

    "chemistry":[
        "ideal gas law",
        "molarity",
        "ph"
    ],

    "nuclear":[
        "half life",
        "activity",
        "radioactive decay"
    ]
}

def formulas_in(category):

    return formula_categories.get(
        category.lower(),
        []
    )



def data_range(data):
    return max(data) - min(data)

def data_sum(data):
    return sum(data)

def kinetic_energy(m, v):
    return 0.5 * m * v**2

def momentum(m, v):
    return m * v

def coulombs_law(q1, q2, r):
    k = 8.9875517923e9
    return k * q1 * q2 / r**2

def force(m, a):
    return m * a

def ohms_voltage(i, r):
    return i * r

def matrix(m):
    return sp.Matrix(m)

# =========================================================
# BOOLEAN LOGIC
# =========================================================

def AND(a, b):
    return bool(a and b)

def OR(a, b):
    return bool(a or b)

def NOT(a):
    return bool(not a)

def XOR(a, b):
    return bool(a) ^ bool(b)

# =========================================================
# 🔥 UPGRADES — ADDITIONAL MATH FEATURES
# =========================================================

def moles(mass, molar_mass_value):
    return mass / molar_mass_value

def mass_from_moles(moles_value, molar_mass_value):
    return moles_value * molar_mass_value

def molecules(moles_value):
    return moles_value * Na

def molarity(moles_value, liters):

    if liters == 0:
        return "Division by zero"

    return moles_value / liters

def angle(a,b):
    return angle_between(a,b)

def integral_def(expr,a,b):
    return definite_integral(expr,a,b)

def solve_linear_system(A,b):

    try:

        A = np.array(A,dtype=float)
        b = np.array(b,dtype=float)

        return np.linalg.solve(A,b).tolist()

    except Exception as e:

        return f"Error: {e}"

def matrix(data):
    return sp.Matrix(data)
    
def ideal_gas_volume(n, T, P):
    return (n * R * T) / P

def velocity(distance, time):
    return distance / time

def acceleration(v1, v2, time):

    if time == 0:
        return "Division by zero"

    return (v2 - v1) / time

def density(mass, volume):

    if volume == 0:
        return "Division by zero"

    return mass / volume

def pressure(force_value, area):

    if area == 0:
        return "Division by zero"

    return force_value / are

def work(force_value, distance):
    return force_value * distance

def power(work_done, time):

    if time == 0:
        return "Division by zero"

    return work_done / time

def frequency(period):

    if period == 0:
        return "Division by zero"

    return 1 / period

def period(freq):
    return 1 / freq

def wavelength(speed, frequency_value):
    return speed / frequency_value

def escape_velocity(mass, radius):

    G = 6.67430e-11

    return math.sqrt(
        (2 * G * mass) / radius
    )

def resistance(v, i):

    if i == 0:
        return "Division by zero"

    return v / i

def current(v, r):

    if r == 0:
        return "Division by zero"

    return v / r

def capacitance(q, v):

    if v == 0:
        return "Division by zero"

    return q / v

formulas = {

    # =========================
    # PHYSICS
    # =========================

    "newton":
        "F = m*a",

    "kinetic energy":
        "KE = 1/2*m*v^2",

    "potential energy":
        "PE = m*g*h",

    "momentum":
        "p = m*v",

    "power":
        "P = W/t",

    "work":
        "W = F*d",

    "ohms law":
        "V = I*R",

    "coulombs law":
        "F = k*q1*q2/r^2",

    "mass energy":
        "E = m*c^2",

    "gravitational force":
        "F = G*m1*m2/r^2",

    "density":
        "ρ = m/V",

    "pressure":
        "P = F/A",

    "wave speed":
        "v = f*λ",

    "frequency":
        "f = 1/T",

    "escape velocity":
        "v = sqrt(2GM/r)",

    # =========================
    # CHEMISTRY
    # =========================

    "ideal gas law":
        "PV = nRT",

    "molarity":
        "M = moles/L",

    "moles":
        "n = mass/MM",

    "percent yield":
        "%Yield = actual/theoretical * 100",

    "ph":
        "pH = -log[H+]",

    "poh":
        "pOH = -log[OH-]",

    "gibbs":
        "ΔG = ΔH - TΔS",

    "avogadro":
        "N = n*Na",

    "dilution":
        "M1V1 = M2V2",

    # =========================
    # CALCULUS
    # =========================

    "power rule":
        "d/dx(x^n)=n*x^(n-1)",

    "product rule":
        "(fg)' = f'g + fg'",

    "quotient rule":
        "(f/g)'=(f'g-fg')/g^2",

    "chain rule":
        "(f(g(x)))'=f'(g(x))*g'(x)",

    "integration by parts":
        "∫u dv = uv - ∫v du",

    # =========================
    # GEOMETRY
    # =========================

    "circle area":
        "A = πr²",

    "circle circumference":
        "C = 2πr",

    "sphere volume":
        "V = 4/3 πr³",

    "sphere area":
        "A = 4πr²",

    "cylinder volume":
        "V = πr²h",

    "cone volume":
        "V = 1/3 πr²h",

    "pythagorean":
        "a²+b²=c²",

    # =========================
    # STATISTICS
    # =========================

    "mean":
        "μ = Σx/n",

    "variance":
        "σ² = Σ(x-μ)²/n",

    "standard deviation":
        "σ = sqrt(variance)",

    "z score":
        "z=(x-μ)/σ",

    "correlation":
        "r = cov(x,y)/(σxσy)",

    # =========================
    # FINANCE
    # =========================

    "simple interest":
        "I = P*r*t",

    "compound interest":
        "A=P(1+r/n)^(nt)",

    "loan payment":
        "M=P[r(1+r)^n]/[(1+r)^n-1]",

    "roi":
        "ROI=(Gain-Cost)/Cost*100",

    # =========================
    # NUCLEAR
    # =========================

    "radioactive decay":
        "N=N0*e^(-λt)",

    "activity":
        "A=λN",

    "half life":
        "t1/2=ln(2)/λ",

    "binding energy":
        "E=Δmc²",

    # =========================
    # MATERIALS
    # =========================

    "rule of mixtures":
        "P=Σ(Vi*Pi)",

    "thermal expansion":
        "ΔL=αLΔT",

    "stress":
        "σ=F/A",

    "strain":
        "ε=ΔL/L",

    "young modulus":
        "E=σ/ε",

    "hardness ratio":
        "H≈3σy"
}

materials = {

    # =========================
    # PURE METALS
    # =========================

    "aluminum": {
        "density": 2700,
        "youngs_modulus": 69e9,
        "melting_point": 933,
        "thermal_conductivity": 237,
        "electrical_resistivity": 2.65e-8
    },

    "copper": {
        "density": 8960,
        "youngs_modulus": 117e9,
        "melting_point": 1357,
        "thermal_conductivity": 401,
        "electrical_resistivity": 1.68e-8
    },

    "silver": {
        "density": 10490,
        "youngs_modulus": 83e9,
        "melting_point": 1235,
        "thermal_conductivity": 429,
        "electrical_resistivity": 1.59e-8
    },

    "gold": {
        "density": 19320,
        "youngs_modulus": 79e9,
        "melting_point": 1337,
        "thermal_conductivity": 318,
        "electrical_resistivity": 2.44e-8
    },

    "iron": {
        "density": 7870,
        "youngs_modulus": 211e9,
        "melting_point": 1811,
        "thermal_conductivity": 80,
        "electrical_resistivity": 9.7e-8
    },

    "nickel": {
        "density": 8908,
        "youngs_modulus": 200e9,
        "melting_point": 1728,
        "thermal_conductivity": 91,
        "electrical_resistivity": 6.9e-8
    },

    "titanium": {
        "density": 4506,
        "youngs_modulus": 116e9,
        "melting_point": 1941,
        "thermal_conductivity": 21.9,
        "electrical_resistivity": 4.2e-7
    },

    "tungsten": {
        "density": 19250,
        "youngs_modulus": 411e9,
        "melting_point": 3695,
        "thermal_conductivity": 173,
        "electrical_resistivity": 5.6e-8
    },

    "molybdenum": {
        "density": 10280,
        "youngs_modulus": 329e9,
        "melting_point": 2896,
        "thermal_conductivity": 138,
        "electrical_resistivity": 5.3e-8
    },

    "chromium": {
        "density": 7190,
        "youngs_modulus": 279e9,
        "melting_point": 2180,
        "thermal_conductivity": 94,
        "electrical_resistivity": 1.25e-7
    },

    # =========================
    # STAINLESS STEELS
    # =========================

    "304 stainless": {
        "density": 8000,
        "youngs_modulus": 193e9,
        "yield_strength": 215e6,
        "thermal_conductivity": 16.2
    },

    "316 stainless": {
        "density": 8000,
        "youngs_modulus": 193e9,
        "yield_strength": 290e6,
        "thermal_conductivity": 16.3
    },

    # =========================
    # TOOL STEELS
    # =========================

    "d2 steel": {
        "density": 7700,
        "hardness_hrc": 60,
        "youngs_modulus": 210e9
    },

    "m2 steel": {
        "density": 8160,
        "hardness_hrc": 65,
        "youngs_modulus": 210e9
    },

    # =========================
    # SUPERALLOYS
    # =========================

    "inconel 718": {
        "density": 8190,
        "youngs_modulus": 200e9,
        "yield_strength": 1030e6,
        "max_service_temp": 973
    },

    "hastelloy c276": {
        "density": 8890,
        "youngs_modulus": 205e9,
        "yield_strength": 355e6
    },

    # =========================
    # CERAMICS
    # =========================

    "alumina": {
        "density": 3950,
        "youngs_modulus": 380e9,
        "melting_point": 2327
    },

    "silicon carbide": {
        "density": 3210,
        "youngs_modulus": 450e9,
        "thermal_conductivity": 120
    },

    "tungsten carbide": {
        "density": 15630,
        "youngs_modulus": 550e9,
        "hardness_gpa": 25
    },

    # =========================
    # SEMICONDUCTORS
    # =========================

    "silicon": {
        "density": 2330,
        "youngs_modulus": 130e9,
        "band_gap": 1.12
    },

    "gallium arsenide": {
        "density": 5320,
        "youngs_modulus": 85e9,
        "band_gap": 1.42
    },

    # =========================
    # CARBON MATERIALS
    # =========================

    "graphite": {
        "density": 2260,
        "youngs_modulus": 15e9,
        "thermal_conductivity": 150
    },

    "diamond": {
        "density": 3510,
        "youngs_modulus": 1200e9,
        "thermal_conductivity": 2200
    },

    "graphene": {
        "density": 2200,
        "youngs_modulus": 1000e9,
        "thermal_conductivity": 5000
    },

    # =========================
    # POLYMERS
    # =========================

    "polyethylene": {
        "density": 950,
        "youngs_modulus": 0.8e9
    },

    "ptfe": {
        "density": 2200,
        "youngs_modulus": 0.5e9
    },

    "peek": {
        "density": 1320,
        "youngs_modulus": 3.6e9
    }
}

def material_info(name):
    return materials.get(name.lower(), "Material not found")

def density_material(name):

    if name.lower() not in materials:
        return "Unknown material"

    return materials[name.lower()]["density"]

def youngs_modulus_material(name):

    if name.lower() not in materials:
        return "Unknown material"

    return materials[name.lower()]["youngs_modulus"]

def melting_material(name):
    return materials[name.lower()].get("melting_point")

def thermal_conductivity_material(name):
    return materials[name.lower()].get("thermal_conductivity")

def inductance(v, di_dt):
    return v / di_dt

def reactance(f, c):
    return 1 / (2 * math.pi * f * c)

def impedance(r, x):
    return math.sqrt(r**2 + x**2)

def power_factor(real_power, apparent_power):
    return real_power / apparent_power

def matrix_norm(m):
    return float(
        np.linalg.norm(
            np.array(m,dtype=float)
        )
    )

def matrix_rref(m):
    return sp.Matrix(m).rref()[0]

def matrix_trace(m):
    return trace(m)

def quartiles(data):

    return {
        "Q1": np.percentile(data,25),
        "Q2": np.percentile(data,50),
        "Q3": np.percentile(data,75)
    }

def iqr(data):

    return (
        np.percentile(data,75)
        -
        np.percentile(data,25)
    )

def laplace_transform_expr(expr):
    return sp.laplace_transform(expr, x, sp.Symbol('s'))

def haversine(lat1, lon1, lat2, lon2):
    R = 6371

    lat1,lon1,lat2,lon2 = map(
        math.radians,
        [lat1,lon1,lat2,lon2]
    )

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat/2)**2 +
        math.cos(lat1) *
        math.cos(lat2) *
        math.sin(dlon/2)**2
    )

    return 2 * R * math.asin(math.sqrt(a))

def inverse_laplace(expr):
    s = sp.Symbol('s')
    return sp.inverse_laplace_transform(expr, s, x)

def fourier(expr):
    return sp.fourier_transform(expr, x, sp.Symbol('k'))

def inverse_fourier(expr):
    k = sp.Symbol('k')
    return sp.inverse_fourier_transform(expr, k, x)

def transpose(m):
    return sp.Matrix(m).T

def matrix_rank(m):
    return sp.Matrix(m).rank()

def jacobian(funcs, vars):
    return sp.Matrix(funcs).jacobian(vars)

def qr(m):
    return sp.Matrix(m).QRdecomposition()

def half_life(decay_constant):
    return math.log(2) / decay_constant

def activity(n, decay_constant):
    return n * decay_constant

def mass_defect(mass_parts, mass_nucleus):
    return mass_parts - mass_nucleus

def binding_energy(delta_m):
    c = 299792458
    return delta_m * c**2

def q_value(m_before, m_after):
    c = 299792458
    return (m_before - m_after) * c**2

def lu(m):
    return sp.Matrix(m).LUdecomposition()

def projection(v, onto):
    v = sp.Matrix(v)
    onto = sp.Matrix(onto)
    return (v.dot(onto) / onto.dot(onto)) * onto

def skewness(data):

    arr = np.array(data)

    mean = np.mean(arr)

    std = np.std(arr)

    n = len(arr)

    return np.sum(
        ((arr-mean)/std)**3
    ) / n

def empirical_formula(elements):
    smallest = min(elements.values())
    ratios = {k: round(v/smallest) for k,v in elements.items()}

    result = ""
    for el,count in ratios.items():
        result += f"{el}{count if count>1 else ''}"

    return result

def weight_to_atomic(weight_percent, atomic_weights):
    moles = {}

    for e,w in weight_percent.items():
        moles[e] = w / atomic_weights[e]

    total = sum(moles.values())

    return {
        e:100*m/total
        for e,m in moles.items()
    }

def rule_of_mixtures(values, fractions):
    return sum(v*f for v,f in zip(values,fractions))

def alloy_density(densities, fractions):
    return 1 / sum(f/d for d,f in zip(densities,fractions))

def stress(force, area):
    return force / area

def strain(delta_length, original_length):
    return delta_length / original_length

def youngs_modulus(stress_value, strain_value):
    return stress_value / strain_value

def thermal_expansion(alpha, length, delta_t):
    return alpha * length * delta_t

def kurtosis(data):

    arr = np.array(data)

    mean = np.mean(arr)

    std = np.std(arr)

    n = len(arr)

    return (
        np.sum(
            ((arr-mean)/std)**4
        ) / n
    ) - 3

def present_value(fv, r, n):
    return fv / ((1+r)**n)

def future_value(pv, r, n):
    return pv * ((1+r)**n)

def npv(rate, cashflows):
    return sum(
        cf / ((1+rate)**i)
        for i,cf in enumerate(cashflows)
    )

import re

def element_count(formula):

    matches = re.findall(
        r'([A-Z][a-z]?)(\d*)',
        formula
    )

    result = {}

    for element, count in matches:

        count = int(count) if count else 1

        result[element] = (
            result.get(element,0)
            + count
        )

    return result

def percent_composition(formula):

    counts = element_count(formula)

    total = molar_mass(formula)

    result = {}

    for e,n in counts.items():

        result[e] = (
            atomic_mass(e)*n
            / total
            *100
        )

    return result

from math import gcd
from functools import reduce

def empirical_formula(counts):

    g = reduce(gcd, counts.values())

    result = ""

    for e,n in counts.items():

        n//=g

        result += e

        if n>1:
            result += str(n)

    return result

def molecular_formula(empirical, multiplier):

    counts = element_count(empirical)

    result = ""

    for e,n in counts.items():

        n*=multiplier

        result += e

        if n>1:
            result += str(n)

    return result

oxidation_rules = {

    "F":-1,
    "O":-2,
    "H":1,
    "Li":1,
    "Na":1,
    "K":1,
    "Mg":2,
    "Ca":2
}

def oxidation_lookup(element):

    return oxidation_rules.get(
        element,
        "variable"
    )

def parse_reaction(reaction):

    left,right = reaction.split("->")

    reactants = [
        x.strip()
        for x in left.split("+")
    ]

    products = [
        x.strip()
        for x in right.split("+")
    ]

    return reactants,products

import sympy as sp

def balance(reaction):

    reactants,products = parse_reaction(
        reaction
    )

    # build atom matrix

    # solve nullspace

    # return balanced equation

def moles_from_mass(mass, formula):
    return mass / molar_mass(formula)

def theoretical_yield(
    product_mm,
    product_moles
):

    return (
        product_mm
        * product_moles
    )

    return n*R*T/V

def molarity(
    moles,
    liters
):
    return moles/liters

def dilution(
    M1,V1,M2
):
    return M1*V1/M2

def heat(
    mass,
    specific_heat,
    delta_T
):
    return (
        mass
        * specific_heat
        * delta_T
    )

def activity(
    N,
    decay_constant
):
    return N*decay_constant

def half_life(
    decay_constant
):
    return math.log(2)/decay_constant



def geometric_mean(data):
    return statistics.geometric_mean(data)

def harmonic_mean(data):
    return statistics.harmonic_mean(data)

def bar_chart(labels, values):

    plt.figure()

    plt.bar(labels, values)

    plt.grid(True)

    plt.show()

def pie_chart(labels, values):

    plt.figure()

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.show()

def box_plot(data):

    plt.figure()

    plt.boxplot(data)

    plt.show()

def stem_plot(data):

    plt.figure()

    plt.stem(data)

    plt.show()

def graph_many(*expressions):

    xs = np.linspace(-10,10,1000)

    for expr in expressions:

        f = sp.lambdify(
            x,
            sp.sympify(expr),
            "numpy"
        )

        plt.plot(xs,f(xs))

    plt.grid(True)

    plt.show()



def expand_full(expr):
    return sp.expand(sp.sympify(expr))

def collect_terms(expr):
    return sp.collect(sp.sympify(expr), x)

def simplify_full(expr):
    return sp.simplify(sp.factor(sp.sympify(expr)))


# ---------------- LINEAR ALGEBRA UPGRADES ----------------

def matrix_power(m, n):
    return np.linalg.matrix_power(np.array(m), n).tolist()

def solve_linear_system(A, b):
    return np.linalg.solve(np.array(A), np.array(b)).tolist()


# ---------------- CALCULUS UPGRADES ----------------

def gradient(expr):
    expr = sp.sympify(expr)
    return [sp.diff(expr, v) for v in (x, y, z)]

def hessian_matrix(expr):
    expr = sp.sympify(expr)
    return sp.Matrix([
        [sp.diff(expr, i, j) for j in (x, y, z)]
        for i in (x, y, z)
    ])


# ---------------- NUMBER THEORY UPGRADES ----------------

def is_square(n):
    n = int(n)
    r = int(math.sqrt(n))
    return r * r == n


def factorint_safe(n):
    try:
        return sp.factorint(int(n))
    except:
        return "Invalid input"


# ---------------- PHYSICS UPGRADES ----------------

def energy_from_mass(m):
    return m * (299792458 ** 2)

def piecewise(*args):
    return sp.Piecewise(*args)

# =========================================================
# HELP
# =========================================================

def show_help():

    help_text = """

=========================================================
DAVE PRO MAX — COMPLETE EXPANDED HELP LIST
=========================================================

======================== BASIC MATH ========================

Addition:
2 + 2

Subtraction:
10 - 3

Multiplication:
5 * 8

Division:
20 / 4

Exponentiation:
2**10

Modulo:
10 % 3

Floor Division:
10 // 3

Parentheses:
(2 + 3) * 4

Absolute Value:
abs(-5)

Rounding:
round(3.14159)
round(3.14159, 2)

Square Root:
sqrt(81)

Cube Root:
27**(1/3)

Factorial:
factorial(5)

Natural Log:
log(10)

Log Base 10:
math.log10(100)

Exponential:
exp(2)

Scientific Notation:
1.23e5

Fractions:
frac(3.14159)

Approximation:
approx(pi, 5)

=========================================================
======================== SYMBOLIC ALGEBRA ========================

Simplify:
simplify(x + x)

Full Simplify:
simplify_full((x**2 - 1)/(x - 1))

Expand:
expand((x + 1)**2)

Expand Full:
expand_full((x + 1)**5)

Collect Terms:
collect(x**2 + 2*x + x**2)

Factor:
factor(x**2 - 9)

Solve Equation:
solve(x**2 - 9)

Solve Equality:
solve(Eq(x**2, 9))

Solve For Variable:
solvefor(x**2 + y - 5, "y")

Solve Systems:
solve([x+y-5, x-y-1], [x,y])

Numerical Solve:
nsolve(x**3 - 2, 1)

Roots:
roots(x**2 - 9)

Substitution:
(x**2 + 1).subs(x, 5)

Expression Evaluation:
(x**2 + 1).evalf()

Expression Comparison:
is_equivalent(x**2 - 1, (x-1)*(x+1))

Piecewise Functions:
piecewise((x**2, x < 0), (x, True))

=========================================================
======================== CALCULUS ========================

Derivative:
derivative(x**3)

Alternative:
diff(x**3)

Second Derivative:
diff(x**3, x, 2)

Integral:
integral(x**2)

Alternative:
integrate(x**2)

Definite Integral:
integral_def(x**2, 0, 5)

Numerical Integral:
numerical_integral(x**2, 0, 5)

Limit:
limit(sin(x)/x, 0)

Taylor Series:
taylor(sin(x), 0, 6)

Series Expansion:
series_expansion(sin(x), 0, 10)

Gradient:
gradient(x**2 + y**2 + z**2)

Hessian Matrix:
hessian(x**2 + y**2 + z**2)

Directional Derivative:
directional_derivative(x**2+y**2+z**2, [1,1,1], [1,0,0])

Laplacian:
laplacian(x**2+y**2+z**2)

Summation:
summation(x**2, 1, 10)

Product:
product(x, 1, 5)

Piecewise:
piecewise((x**2, x < 0), (x, True))

Newton Method:
newton(x**2 - 2, 1)

Differential Equations:
dsolve(Derivative(y(x),x)-y(x))

=========================================================
======================== TRIGONOMETRY ========================

sin(pi/2)
cos(pi)
tan(pi/4)

Inverse Trig:
asin(1)
acos(1)
atan(1)

Hyperbolic:
sinh(1)
cosh(1)
tanh(1)

Radians Conversion:
radians(90)

Degrees Conversion:
degrees(pi)

=========================================================
======================== ANGLE MODES ========================

Enable Degrees:
deg

Enable Radians:
rad

Examples:
sin(90)      # in degree mode
sin(pi/2)    # in radian mode

=========================================================
======================== VARIABLES ========================

Create Variable:
a = 10

Use Variable:
a + 5

Store Expressions:
f = x**2 + 1

Built-in Variables:
x
y
z

Last Answer:
ans

Persistent Variables:
- automatically saved
- automatically loaded

=========================================================
======================== GRAPHING ========================

2D Graph:
graph(x**2)

Examples:
graph(sin(x))
graph(cos(x))
graph(x**3 - 2*x)

3D Graph:
graph3d(x**2 + y**2)

3D Examples:
graph3d(sin(x*y))
graph3d(x**2 - y**2)

Parametric Graph:
graph_parametric("t", "t**2")

Polar Graph:
graph_polar("theta")

Intersection Finder:
intersection(x**2, x+2)

ASCII Graph:
ascii_plot(x**2)

=========================================================
======================== STATISTICS ========================

Mean:
mean([1,2,3,4,5])

Median:
median([1,2,3,4,5])

Mode:
mode([1,1,2,3])

Variance:
variance([1,2,3,4,5])

Standard Deviation:
std([1,2,3,4,5])

Percentile:
percentile([1,2,3,4,5], 50)

Correlation:
correlation([1,2,3], [2,4,6])

Covariance:
covariance([1,2,3], [2,4,6])

Range:
range_data([1,2,3,10])

Sum:
sum_data([1,2,3])

Z Scores:
z_scores([1,2,3,4,5])

Moving Average:
moving_average([1,2,3,4,5], 3)

Correlation Strength:
correlation_strength([1,2,3], [2,4,6])

=========================================================
======================== MATRICES ========================

Create Matrix:
matrix([[1,2],[3,4]])

Determinant:
det([[1,2],[3,4]])

Inverse:
inv([[1,2],[3,4]])

Transpose:
transpose([[1,2],[3,4]])

Trace:
trace([[1,2],[3,4]])

Rank:
rank([[1,2],[3,4]])

Matrix Multiplication:
matmul([[1,2]], [[3],[4]])

Matrix Power:
matrix_power([[1,2],[3,4]], 2)

Eigenvalues:
eig([[1,2],[3,4]])

Solve Linear System:
solve_linear_system([[2,1],[1,3]], [5,6])

Jacobian:
jacobian([x**2+y, y**2+x], [x,y])

=========================================================
======================== VECTORS ========================

Dot Product:
dot([1,2,3], [4,5,6])

Cross Product:
cross([1,0,0], [0,1,0])

Magnitude:
mag([3,4])

Angle Between:
angle([1,0], [0,1])

Distance:
distance([1,2], [4,6])

Momentum Vector:
momentum_vector(5, [1,2,3])

=========================================================
======================== NUMBER THEORY ========================

Greatest Common Divisor:
gcd(48,18)

Least Common Multiple:
lcm(12,18)

Prime Check:
prime(17)

Perfect Square Check:
is_square(144)

Prime Factorization:
factorint(360)

Safe Factorization:
factorint_safe(999999999)

Factor List:
factor_list(360)

Largest Prime Factor:
largest_prime_factor(360)

Euler Totient:
totient(10)

Modular Inverse:
modinv(3,11)

Combinations:
ncr(5,2)

Permutations:
npr(5,2)

Prime List:
primes_up_to(100)

Binary:
bin(42)

Hexadecimal:
hex(255)

Octal:
oct(64)

Decimal Conversion:
decimal("1010", 2)

Base Conversion:
base_convert(255, 10, 16)

Roman Numerals:
to_roman(2024)

=========================================================
======================== GEOMETRY ========================

Circle Area:
circle_area(5)

Sphere Volume:
sphere_volume(5)

Triangle Area:
triangle_area(3,4,5)

Triangle Perimeter:
triangle_perimeter(3,4,5)

Arc Length:
arc_length(5, pi)

Distance Between Points:
distance([1,2], [4,6])

=========================================================
======================== PHYSICS ========================

Kinetic Energy:
ke(10,5)

Relativistic Kinetic Energy:
relativistic_ke(1,1000000)

Momentum:
momentum(10,5)

Force:
force(10,9.8)

Voltage:
voltage(2,10)

Mass-Energy:
E_mc2(1)

Coulomb's Law:
coulombs_law(1e-6, 1e-6, 0.1)

=========================================================
======================== COMPLEX NUMBERS ========================

Complex Number:
3 + 4j

Real Part:
real(3+4j)

Imaginary Part:
imag(3+4j)

Conjugate:
conjugate(3+4j)

Magnitude:
abs(3+4j)

Polar to Complex:
polar(5,45)

=========================================================
======================== SEQUENCES ========================

Fibonacci:
fib(10)

Random Integer:
randint(1,100)

Random Float:
random()

Random Choice:
choice([1,2,3])

=========================================================
======================== REGRESSION ========================

Linear Regression:
linreg([1,2,3], [2,4,6])

Polynomial Fit:
polyfit([1,2,3], [1,4,9], 2)

=========================================================
======================== UNIT CONVERSIONS ========================

Format:
convert(value, from_unit, to_unit)

Mass:
convert(1,"kg","lb")
convert(10,"lb","kg")

Length:
convert(1,"m","ft")
convert(1,"m","in")
convert(5,"km","mi")

Temperature:
convert(100,"c","f")
convert(32,"f","c")

Volume:
convert(1,"l","gal")

=========================================================
======================== CHEMISTRY ========================

Atomic Mass:
atomic_mass("Fe")

Atomic Number:
atomic_number("Au")

Element Name:
element_name("O")

Protons:
protons("C")

Electrons:
electrons("Na")

Neutrons:
neutrons("U")

Molar Mass:
molar_mass("H2O")

Examples:
molar_mass("CO2")
molar_mass("C6H12O6")

Ideal Gas Law:
ideal_gas_pressure(1,273,22.4)

Periodic Table:
elements()

=========================================================
======================== FINANCE ========================

Simple Interest:
simple_interest(1000,0.05,2)

Compound Interest:
compound_interest(1000,0.05,2,12)

Loan Payment:
loan_payment(10000,0.05,5)

=========================================================
======================== PROBABILITY ========================

Probability:
probability(3,10)

Binomial Probability:
binomial_probability(10,3,0.5)

Permutations:
permutations(5,2)

Combinations:
combinations(5,2)

=========================================================
======================== BOOLEAN LOGIC ========================

AND(True, False)

OR(True, False)

NOT(True)

XOR(True, False)

=========================================================
======================== CRYPTOGRAPHY ========================

Caesar Encrypt:
caesar_encrypt("hello", 3)

Caesar Decrypt:
caesar_decrypt("khoor", 3)

ROT13:
rot13("hello")

SHA256 Hash:
sha256_hash("hello")

=========================================================
======================== CONSTANTS ========================

Speed of Light:
c

Planck Constant:
h

Boltzmann Constant:
k

Avogadro Number:
Na

Gravity:
g

Golden Ratio:
golden_ratio

Pi:
pi

Euler's Number:
e

=========================================================
======================== TIME / DATE ========================

Current Time:
time

Current Date:
date

Current Month:
month

Current Year:
year

=========================================================
======================== STOCK MARKET ========================
=========================================================

Stock Performance:
stock("SPY")
stock("AAPL")

Current Stock Price:
stock_price("MSFT")

Market Capitalization:
market_cap("NVDA")

P/E Ratio:
pe_ratio("AAPL")

Dividend Yield:
dividend_yield("KO")

Company Name:
stock_name("GOOG")

Examples:
stock("TSLA")
stock_price("AMD")
market_cap("AMZN")

=========================================================
======================== BASEBALL ========================
=========================================================

ERA:
era(earned_runs, innings_pitched)

Example:
era(25, 180)

Batting Average:
batting_average(hits, at_bats)

Example:
batting_average(150, 500)

On Base Percentage:
obp(hits, walks, hbp, at_bats, sacrifice_flies)

Example:
obp(150, 60, 5, 500, 4)

Slugging Percentage:
slg(singles, doubles, triples, home_runs, at_bats)

Example:
slg(90, 30, 5, 25, 500)

OPS:
ops(slg_value, obp_value)

Example:
ops(0.520, 0.380)

=========================================================
======================== ADVANCED CHEMISTRY ========================
=========================================================

Moles:
moles(18, 18.015)

Mass From Moles:
mass_from_moles(2, 18.015)

Molecules:
molecules(1)

Molarity:
molarity(0.5, 1.0)

Ideal Gas Volume:
ideal_gas_volume(1,273,1)

Ideal Gas Temperature:
ideal_gas_temperature(1,22.4,1)

Ideal Gas Moles:
ideal_gas_moles(1,273,22.4)

pH:
ph(1e-7)

Examples:
ph(0.001)
ph(1e-4)

=========================================================
======================== ADVANCED PHYSICS ========================
=========================================================

Velocity:
velocity(100,5)

Acceleration:
acceleration(20,4)

Density:
density(10,2)

Pressure:
pressure(100,10)

Work:
work(10,5)

Power:
power(100,10)

Frequency:
frequency(0.02)

Period:
period(50)

Wavelength:
wavelength(3e8,5e14)

Escape Velocity:
escape_velocity(5.97e24,6.37e6)

Projectile Range:
projectile_range(100,45)

Schwarzschild Radius:
schwarzschild(5.97e24)

Radioactive Decay:
decay(1000,0.693,10)

Gravity Force:
gravity_force(5.97e24,1000,6.37e6)

Momentum Vector:
momentum_vector(5,[1,2,3])

=========================================================
======================== ADVANCED MATRIX ========================
=========================================================

Matrix Norm:
matrix_norm([[1,2],[3,4]])

Reduced Row Echelon Form:
matrix_rref([[1,2],[3,4]])

Null Space:
matrix_nullspace([[1,2],[3,4]])

Column Space:
matrix_columnspace([[1,2],[3,4]])

Row Space:
matrix_rowspace([[1,2],[3,4]])

Characteristic Polynomial:
characteristic_polynomial([[1,2],[3,4]])

=========================================================
======================== ADVANCED STATISTICS ========================
=========================================================

Quartiles:
quartiles([1,2,3,4,5])

Interquartile Range:
iqr([1,2,3,4,5])

Skewness:
skewness([1,2,3,4,5])

Kurtosis:
kurtosis([1,2,3,4,5])

Geometric Mean:
geometric_mean([1,2,3,4])

Harmonic Mean:
harmonic_mean([1,2,3,4])

=========================================================
======================== ADVANCED GRAPHING ========================
=========================================================

Bar Chart:
bar_chart(["A","B","C"], [10,20,15])

Pie Chart:
pie_chart(["A","B","C"], [10,20,15])

Box Plot:
box_plot([1,2,3,4,5,6,7])

Stem Plot:
stem_plot([1,2,3,4,5])

Graph Multiple Functions:
graph_many(["sin(x)", "cos(x)", "x**2"])

=========================================================
======================== FILE UTILITIES ========================
=========================================================

Save Note:
save_note("my_note.txt", "Hello World")

Read Note:
read_note("my_note.txt")

=========================================================
======================== DATA ANALYSIS ========================
=========================================================

Load CSV:
load_csv("data.csv")

Correlation Matrix:
corr_matrix(data)

Histogram:
histogram([1,2,3,4,5])

Scatter Plot:
scatter([1,2,3],[4,5,6])

Pretty JSON:
pretty_json(data)

=========================================================
======================== ADVANCED CRYPTOGRAPHY ========================
=========================================================

MD5:
md5_hash("hello")

SHA1:
sha1_hash("hello")

SHA256:
sha256_hash("hello")

SHA512:
sha512_hash("hello")

Base64 Encode:
base64_encode("hello")

Base64 Decode:
base64_decode(encoded)

XOR Encrypt:
xor_encrypt("hello","key")

Vigenere Encrypt:
vigenere_encrypt("hello","key")

Vigenere Decrypt:
vigenere_decrypt(ciphertext,"key")

=========================================================
======================== GAMES ========================
=========================================================

Guessing Game:
start_guess_game(100)

Roll Dice:
roll()

Draw Card:
draw_card()

=========================================================
======================== SYSTEM COMMANDS ========================
Show History:
history

Show Help:
help

About:
about

Quit:
quit, q, or exit

=========================================================
======================== TRANSLATION ========================
=========================================================

Translate Text:
translate("Hello world", "es")

Translate To Current Language:
translate("Good morning")

Examples:
translate("I like math", "fr")
translate("How are you?", "de")
translate("The cat is sleeping", "jp")

Supported Languages:
en = English
es = Spanish
fr = French
de = German
jp = Japanese
it = Italian
pt = Portuguese
ru = Russian
zh-cn = Chinese
ar = Arabic
hi = Hindi

=========================================================
======================== ASTRONOMY ========================
=========================================================

Orbital Period:
orbital_period(1.496e11, 1.989e30)

Luminosity:
luminosity(6.96e8, 5778)

Redshift:
redshift(656.3, 700)

Distance Modulus:
distance_modulus(10, 5)

Hill Sphere:
hill_sphere(1.496e11, 5.97e24, 1.989e30)

=========================================================
======================== ELECTRONICS ========================
=========================================================

Resistance:
resistance(12, 2)

Current:
current(12, 6)

Capacitance:
capacitance(0.001, 5)

Inductance:
inductance(12, 0.5)

Reactance:
reactance(60, 1e-6)

Impedance:
impedance(100, 50)

Power Factor:
power_factor(900, 1000)

=========================================================
======================== ADVANCED MATRIX ========================
=========================================================

Transpose:
transpose([[1,2],[3,4]])

Rank:
rank([[1,2],[3,4]])

Jacobian:
jacobian([x**2+y, y**2+x], [x,y])

QR Decomposition:
qr([[1,2],[3,4]])

LU Decomposition:
lu([[1,2],[3,4]])

Projection:
projection([1,2,3], [1,0,0])

=========================================================
======================== TRANSFORMS ========================
=========================================================

Laplace Transform:
laplace_transform(sin(x))

Inverse Laplace:
inverse_laplace(1/(s+1))

Fourier Transform:
fourier_transform(exp(-x**2))

Inverse Fourier:
inverse_fourier(expr)

=========================================================
======================== ADVANCED CHEMISTRY ========================
=========================================================

Empirical Formula:
empirical_formula({
    "C":40,
    "H":6.7,
    "O":53.3
})

=========================================================
======================== NUCLEAR PHYSICS ========================
=========================================================

Half Life:
half_life(0.693)

Activity:
activity(1000, 0.693)

Mass Defect:
mass_defect(1.008+1.008, 2.014)

Binding Energy:
binding_energy(1e-30)

Q Value:
q_value(10, 9.99)

=========================================================
======================== MATERIALS SCIENCE ========================
=========================================================

Alloy Density:
alloy_density(
    [7.87,8.96],
    [0.5,0.5]
)

Rule of Mixtures:
rule_of_mixtures(
    [100,200],
    [0.4,0.6]
)

Weight % To Atomic %:
weight_to_atomic(
    {"Fe":70,"Cr":30},
    {"Fe":55.845,"Cr":51.996}
)

=========================================================
======================== ENGINEERING ========================
=========================================================

Stress:
stress(1000, 0.01)

Strain:
strain(0.001, 1)

Young's Modulus:
youngs_modulus(1e8, 0.001)

Thermal Expansion:
thermal_expansion(
    1.2e-5,
    10,
    100
)

=========================================================
======================== GEOGRAPHY ========================
=========================================================

Great Circle Distance:
haversine(
    40.7128,
    -74.0060,
    42.3601,
    -71.0589
)

=========================================================
FORMULA LIBRARY
=========================================================

Single Formula:
formula("kinetic energy")

Search:
find_formula("energy")

Category:
formulas_in("physics")

Examples:

formula("ideal gas law")
formula("ohms law")
formula("half life")
formula("young modulus")
formula("compound interest")

=========================================================
======================== ADVANCED PERIODIC TABLE ========================
=========================================================

Full Element Report:
element_info("Fe")

Electron Configuration:
electron_configuration("Cu")

Oxidation States:
oxidation_states("Mn")

Electronegativity:
electronegativity("O")

Atomic Radius:
atomic_radius("W")

Covalent Radius:
covalent_radius("C")

Density:
density_element("Os")

Melting Point:
melting_point("Re")

Boiling Point:
boiling_point("He")

Thermal Conductivity:
thermal_conductivity("Ag")

Specific Heat:
specific_heat("Al")

Find Element:
find_element("tungsten")

=========================================================
======================== ADVANCED FINANCE ========================
=========================================================

Present Value:
present_value(1000, 0.05, 10)

Future Value:
future_value(1000, 0.05, 10)

Net Present Value:
npv(
    0.08,
    [100,200,300,400]
)

=========================================================
======================== COMPUTER SCIENCE ========================
=========================================================

Quick Sort:
quick_sort([5,1,9,3,2])

Binary Search:
binary_search(
    [1,2,3,4,5],
    4
)

=========================================================
======================== ADDITIONAL GAMES ========================
=========================================================

Coin Flip:
coin_flip()

Rock Paper Scissors:
rock_paper_scissors()

Guessing Game:
start_guess_game(100)

=========================================================
======================== STOCK MARKET ========================
=========================================================

Stock Performance:
stock("SPY")

Current Price:
stock_price("AAPL")

Market Cap:
market_cap("NVDA")

P/E Ratio:
pe_ratio("MSFT")

Dividend Yield:
dividend_yield("KO")

Company Name:
stock_name("GOOG")

=========================================================
======================== BASEBALL STATISTICS ========================
=========================================================

ERA:
era(25,180)

Batting Average:
batting_average(150,500)

On Base Percentage:
obp(150,60,5,500,4)

Slugging Percentage:
slg(90,30,5,25,500)

OPS:
ops(0.520,0.380)

=========================================================
======================== SPECIAL FEATURES ========================

- symbolic algebra
- symbolic calculus
- exact fractions
- numerical evaluation
- variable persistence
- graph plotting
- ASCII graph plotting
- 3D graph plotting
- polar graph plotting
- parametric graph plotting
- chemistry tools
- periodic table viewer
- unit conversion
- statistics engine
- matrix algebra
- vector algebra
- regression analysis
- finance tools
- probability tools
- cryptography tools
- random generators
- multilingual interface
- command history
- saved variables
- rich terminal interface
- SymPy integration
- NumPy integration
- matplotlib plotting

Warning: if you try to do an impossible equation (e.g. 1/0), it will return zoo.
=========================================================
END OF HELP
=========================================================
"""

    console.print(
        Panel.fit(
            help_text,
            title="HELP MENU",
            border_style="cyan"
        )
    )
 
# =========================================================
# SIMPLE ENCRYPTION
# =========================================================

def caesar_encrypt(text, shift):

    result = ""

    for char in text:

        if char.isalpha():

            start = ord('A') if char.isupper() else ord('a')

            result += chr(
                (ord(char) - start + shift) % 26 + start
            )

        else:
            result += char

    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

def coin_flip():
    return random.choice(["Heads","Tails"])

def rock_paper_scissors():
    return random.choice([
        "Rock",
        "Paper",
        "Scissors"
    ])

def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            low = mid+1
        else:
            high = mid-1

    return -1

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def english():
    return set_language("en")

def alloy_density(densities,fractions):
    return 1/sum(
        f/d for d,f in zip(densities,fractions)
    )

def rule_of_mixtures(values,fractions):
    return sum(
        v*f for v,f in zip(values,fractions)
    )

def weight_to_atomic(weights,masses):

    moles={}

    for e in weights:
        moles[e]=weights[e]/masses[e]

    total=sum(moles.values())

    return {
        e:100*v/total
        for e,v in moles.items()
    }

def atomic_to_weight(atomic,masses):

    masses_calc={}

    for e in atomic:
        masses_calc[e]=atomic[e]*masses[e]

    total=sum(masses_calc.values())

    return {
        e:100*v/total
        for e,v in masses_calc.items()
    }



def spanish():
    return set_language("es")

def french():
    return set_language("fr")

def german():
    return set_language("de")

def japanese():
    return set_language("ja")

def half_life(decay_constant):
    return math.log(2)/decay_constant

def activity(N,lambda_):
    return N*lambda_

def decay(N0, lambda_, t):
    return N0*math.exp(-lambda_*t)

def binding_energy(delta_m):
    c = 299792458
    return delta_m*c*c

def tr(key):
    return languages.get(language, languages["en"]).get(key, key)

def set_language(lang):
    global language

    if lang in languages:
        language = lang
        return f"Language set to {lang}"

    return "Unsupported language"

# =========================================================
# ASCII GRAPH
# =========================================================

def ascii_plot(expr):

    expr = sp.sympify(expr)

    f = sp.lambdify(x, expr, modules=["numpy"])

    lines = []

    for yval in range(10, -11, -1):

        line = ""

        for xval in range(-30, 31):

            try:

                val = int(round(f(xval)))

                if val == yval:
                    line += "*"

                elif yval == 0:
                    line += "-"

                elif xval == 0:
                    line += "|"

                else:
                    line += " "

            except:
                line += " "

        lines.append(line)

    result = "\n".join(lines)

    print(result)

    return result

# =========================================================
# VARIABLES DICT
# =========================================================


language = "en"

languages = {
    "en": {
        "welcome": "Welcome",
        "goodbye": "Goodbye",
        "help": "Help",
        "answer": "Answer",
        "error": "Error",
        "enter_equation": "Enter equation here:",
        "unknown_command": "Unknown command",
    },

    "es": {
        "welcome": "Bienvenido",
        "goodbye": "Adiós",
        "help": "Ayuda",
        "answer": "Respuesta",
        "error": "Error",
        "enter_equation": "Ingrese una ecuación:",
        "unknown_command": "Comando desconocido",
    },

    "fr": {
        "welcome": "Bienvenue",
        "goodbye": "Au revoir",
        "help": "Aide",
        "answer": "Réponse",
        "error": "Erreur",
        "enter_equation": "Entrez une équation :",
        "unknown_command": "Commande inconnue",
    },

    "de": {
        "welcome": "Willkommen",
        "goodbye": "Tschüss",
        "help": "Hilfe",
        "answer": "Antwort",
        "error": "Fehler",
        "enter_equation": "Geben Sie eine Gleichung ein:",
        "unknown_command": "Unbekannter Befehl",
    },

    "ja": {
        "welcome": "ようこそ",
        "goodbye": "さようなら",
        "help": "ヘルプ",
        "answer": "答え",
        "error": "エラー",
        "enter_equation": "式を入力してください:",
        "unknown_command": "不明なコマンド",
    }
}

x, y, z = sp.symbols("x y z")

variables = {

    # ================= SYMBOLS =================
    "selftest": selftest,
    "limiting_reactant": limiting_reactant,
    "element_count": element_count,
    "E": sp.E,
    "percent_composition":
        percent_composition,
    "emc2": emc2,
    "mass_from_energy": mass_from_energy,
    "empirical_formula":
        empirical_formula,
    "dsolve": sp.dsolve,"sinh": lambda x: float(sp.sinh(x)),
    "cosh": lambda x: float(sp.cosh(x)),
    "tanh": lambda x: float(sp.tanh(x)),
    "molecular_formula":
        molecular_formula,

    "balance": balance,

    "moles_from_mass":
        moles_from_mass,

    "limiting_reactant":
        limiting_reactant,

    "theoretical_yield":
        theoretical_yield,

    "oxidation_lookup":
        oxidation_lookup,


    "formula": formula,
    "find_formula": find_formula,
    "formulas_in": formulas_in,
    "x": x,
    "y": y,
    "z": z,

    "pi": sp.pi,
    "e": sp.E,

    # ================= TRIG =================

    "set_language": set_language,
    "sin": sin_wrapper,
    "cos": cos_wrapper,
    "tan": tan_wrapper,

    "asin": sp.asin,
    "acos": sp.acos,
    "atan": sp.atan,
    "alloy_density": alloy_density,
    "rule_of_mixtures": rule_of_mixtures,
    "weight_to_atomic": weight_to_atomic,
    "atomic_to_weight": atomic_to_weight,
    "sec": sp.sec,
    "csc": sp.csc,
    "cot": sp.cot,
    "radians": math.radians,
    "degrees": math.degrees,

    # ================= ALGEBRA =================

    "sqrt": sp.sqrt,
    "log": sp.log,
    "ln": sp.log,

    "expand": sp.expand,
    "expand_full": expand_full,
    "stress": stress,
    "strain": strain,
    "youngs_modulus": youngs_modulus,
    "thermal_expansion": thermal_expansion,
    "simplify": sp.simplify,
    "simplify_full": simplify_full,

    "factor": sp.factor,
    "collect": collect_terms,
    "half_life": half_life,
    "activity": activity,
    "binding_energy": binding_energy,
    "solve": sp.solve,
    "solvefor": solvefor,
    "quick_sort": quick_sort,
    "binary_search": binary_search,
    "nsolve": nsolve_equation,
    "is_equivalent": is_equivalent,

    "material_info": material_info,
    "density_material": density_material,
    "youngs_modulus_material": youngs_modulus_material,
    "melting_material": melting_material,
    "thermal_conductivity_material": thermal_conductivity_material,

    # ================= CALCULUS =================

    "diff": sp.diff,
    "derivative": derivative,
    "deriv": derivative,

    "integral": integral,
    "int": integral,

    "integrate": sp.integrate,
    "integral_def": definite_integral,
    "translate": translate,
    "limit": limit,
    "taylor": taylor,
    "series_expansion": series_expansion,
    "coin_flip": coin_flip,
    "rock_paper_scissors": rock_paper_scissors,
    "gradient": gradient,
    "hessian": hessian_matrix,

    "directional_derivative": directional_derivative,
    "laplacian": laplacian,

    "newton": newton,

    # ================= EQUATIONS =================

    "solve_quadratic": solve_quadratic,
    "solve_cubic": solve_cubic,

    "Eq": sp.Eq,
    "Function": sp.Function,
    "Symbol": sp.Symbol,
    "Derivative": sp.Derivative,
    "quadratic": quadratic,
    "linear": linear,
    "cubic": cubic,
    # ================= MATRIX =================

    "Matrix": sp.Matrix,
    "present_value": present_value,
    "future_value": future_value,
    "npv": npv,
    "matrix": matrix,
    "matmul": matrix_mul,
    "rank": matrix_rank,
    "density_material": density_material,
    "youngs_modulus_material": youngs_modulus_material,

    "jacobian": jacobian,
    "qr": qr,
    "lu": lu,
    "projection": projection,
    "det": matrix_det,
    "determinant": matrix_det,
    "stock": stock_metrics,
    "stock_metrics": stock_metrics,
    "inv": matrix_inv,
    "inverse": matrix_inv,
    "empirical_formula": empirical_formula,
    "eig": eigenvalues,
    "weight_to_atomic": weight_to_atomic,
    "rule_of_mixtures": rule_of_mixtures,
    "alloy_density": alloy_density,
    "matrix_power": matrix_power,
    "matrix_norm": matrix_norm,
    "haversine": haversine,
    "matrix_rref": matrix_rref,
    "matrix_trace": matrix_trace,

    "matrix_nullspace": matrix_nullspace,
    "matrix_columnspace": matrix_columnspace,
    "matrix_rowspace": matrix_rowspace,
    "half_life": half_life,
    "activity": activity,
    "mass_defect": mass_defect,
    "binding_energy": binding_energy,
    "q_value": q_value,
    "characteristic_polynomial": characteristic_polynomial,
    "transpose": matrix_transpose,
    "matrix_transpose": matrix_transpose,
    "solve_linear_system": solve_linear_system,
    "is_square": is_square,
    "laplace_transform": laplace_transform_expr,
    "inverse_laplace": inverse_laplace,
    "fourier_transform": fourier,
    "inverse_fourier": inverse_fourier,
    # Optional advanced matrix features
    "rank": matrix_rank,
    "transpose": matrix_transpose,

    "element_info": element_info,

    "atomic_mass": atomic_mass,
    "atomic_number": atomic_number,
    "element_name": element_name,

    "density_element": density_element,
    "melting_point": melting_point,
    "boiling_point": boiling_point,

    "electron_configuration": electron_configuration,
    "oxidation_states": oxidation_states,

    "electronegativity": electronegativity,
    "atomic_radius": atomic_radius,
    "covalent_radius": covalent_radius,

    "thermal_conductivity": thermal_conductivity,
    "specific_heat": specific_heat,

    "find_element": find_element,

    # ================= VECTOR =================

    "dot": dot,
    "cross": cross,
    "mag": mag,
    "angle": angle_between,

    # ================= STATISTICS =================

    "mean": stats_mean,
    "avg": stats_mean,

    "median": stats_median,
    "mode": stats_mode,

    "variance": stats_var,
    "std": stats_std,

    "quartiles": quartiles,
    "iqr": iqr,

    "percentile": percentile,

    "skewness": skewness,
    "kurtosis": kurtosis,

    "geometric_mean": geometric_mean,
    "harmonic_mean": harmonic_mean,

    "correlation": correlation,
    "covariance": covariance,
    "corr_matrix": corr_matrix,

    "z_scores": z_scores,
    "moving_average": moving_average,
    "correlation_strength": correlation_strength,

    "resistance": resistance,
    "current": current,
    "capacitance": capacitance,
    "inductance": inductance,
    "reactance": reactance,
    "impedance": impedance,
    "power_factor": power_factor,

    "linreg": linear_regression,
    "polyfit": poly_fit,

    "probability": probability,
    "binomial_probability": binomial_probability,

    # ================= NUMBER THEORY =================

    "gcd": gcd,
    "lcm": lcm,

    "factorint": prime_factors,
    "factorint_safe": factorint_safe,

    "factor_list": factor_list,
    "largest_prime_factor": largest_prime_factor,
    "english": english,
    "spanish": spanish,
    "french": french,
    "german": german,
    "japanese": japanese,
    "totient": totient,

    "prime": is_prime,
    "is_prime": is_prime,

    "primes_up_to": primes_up_to,
    "orbital_period": orbital_period,
    "luminosity": luminosity,
    "redshift": redshift,
    "distance_modulus": distance_modulus,
    "hill_sphere": hill_sphere,
    "modinv": modinv,
    "distance": distance,
    "trace": trace,
    "ncr": ncr,
    "npr": npr,
    "arc_length": arc_length,
    "permutations": permutations,
    "combinations": combinations,

    "factorial": sp.factorial,

    # ================= COMPLEX =================

    "real": real,
    "imag": imag,
    "conjugate": conjugate,

    "polar": polar_complex,
    "roots": roots,

    # ================= PHYSICS =================

    "c": c,
    "h": h,
    "k": k,
    "g": g,

    "ke": kinetic_energy,
    "momentum": momentum,

    "velocity": velocity,
    "acceleration": acceleration,

    "force": force,
    "gravity_force": gravity_force,

    "density": density,
    "pressure": pressure,
    
    "start_guess_game": start_guess_game,
    "guess": guess,
    "reveal_answer": reveal_answer,
    "end_guess_game": end_guess_game, 
    "game_status": game_status,

    "work": work,
    "power": power,

    "voltage": ohms_voltage,

    "frequency": frequency,
    "period": period,
    "wavelength": wavelength,

    "escape_velocity": escape_velocity,

    "relativistic_ke": relativistic_ke,
    "momentum_vector": momentum_vector,

    "projectile_range": projectile_range,

    "stock": stock,
    "stock_price": stock_price,
    "market_cap": market_cap,
    "pe_ratio": pe_ratio,
    "dividend_yield": dividend_yield,
    "stock_name": stock_name,

    "E_mc2": energy_from_mass,

    "decay": decay,
    "schwarzschild": schwarzschild,

    # ================= CHEMISTRY =================

    "elements": elements,

    "atomic_mass": atomic_mass,
    "atomic_number": atomic_number,
    "element_name": element_name,

    "molar_mass": molar_mass,

    "moles": moles,
    "mass_from_moles": mass_from_moles,

    "molecules": molecules,
    "molarity": molarity,

    "ideal_gas_pressure": ideal_gas_pressure,
    "ideal_gas_temperature": ideal_gas_temperature,
    "ideal_gas_volume": ideal_gas_volume,
    "ideal_gas_moles": ideal_gas_moles,

    "protons": protons,
    "electrons": electrons,
    "neutrons": neutrons,

    "ph": ph,

    "electron_mass": electron_mass,
    "proton_mass": proton_mass,
    "neutron_mass": neutron_mass,

    "Na": Na,
    "R": R,
    "F": F,

    # ================= GEOMETRY =================

    "circle_area": circle_area,
    "sphere_volume": sphere_volume,
    "triangle_area": triangle_area,

    # ================= SUMS =================

    "summation": summation,
    "product": product,
    "piecewise": piecewise,

    # ================= NUMERICAL =================

    "numerical_integral": numerical_integral,

    # ================= DATA =================

    "parse": parse_list,

    "range_data": data_range,
    "sum_data": data_sum,

    "load_csv": load_csv,

    "histogram": histogram,
    "scatter": scatter,

    # ================= GRAPHING =================

    "ascii_plot": ascii_plot,
    "plot": ascii_plot,

    "bar_chart": bar_chart,
    "pie_chart": pie_chart,
    "box_plot": box_plot,
    "stem_plot": stem_plot,

    "graph_many": graph_many,

    # ================= CONVERSIONS =================

    "convert": convert,
    "base_convert": base_convert,

    "bin": to_binary,
    "oct": to_octal,
    "hex": to_hex,

    "decimal": decimal,

    "to_roman": to_roman,

    # ================= RANDOM =================

    "randint": random.randint,
    "random": random.random,
    "randfloat": randfloat,
    "choice": random.choice,

    "draw_card": draw_card,
    "roll": roll,

    # ================= FINANCE =================

    "simple_interest": simple_interest,
    "compound_interest": compound_interest,
    "loan_payment": loan_payment,

    "interest": simple_interest,

    # ================= LOGIC =================

    "AND": AND,
    "OR": OR,
    "NOT": NOT,
    "XOR": XOR,

    # ================= CRYPTO =================

    "caesar_encrypt": caesar_encrypt,
    "caesar_decrypt": caesar_decrypt,

    "rot13": rot13,

    "md5_hash": md5_hash,
    "sha1_hash": sha1_hash,
    "sha256_hash": sha256_hash,
    "sha512_hash": sha512_hash,

    "xor_encrypt": xor_encrypt,

    "vigenere_encrypt": vigenere_encrypt,
    "vigenere_decrypt": vigenere_decrypt,

    "base64_encode": base64_encode,
    "base64_decode": base64_decode,

    "rsa_encrypt": rsa_encrypt,
    "rsa_decrypt": rsa_decrypt,

    # ================= UTILITIES =================

    "round": round,
    "abs": abs,
    "whip": whip,
    "k9": k_per_9,
    "bb9": bb_per_9,
    "hr9": hr_per_9,
    "era": era,
    "batting_average": batting_average,
    "avg": batting_average,
    "obp": obp,
    "slg": slg,
    "ops": ops,"fielding_percentage": fielding_percentage,
    "floor": math.floor,
    "ceil": math.ceil,

    "exp": math.exp,

    "golden_ratio": golden_ratio,

    "pretty_json": pretty_json,

    "validate_expr": validate_expr,
    "explain": explain,
    "approx": approx,

    # ================= FILES =================

    "save_note": save_note,
    "read_note": read_note,

    # ================= STOPWATCH =================

    "stopwatch_start": stopwatch_start,
    "stopwatch_stop": stopwatch_stop,

    # ================= SYSTEM =================

    "system_info": system_info,

    # ================= HELP =================

    "commands": commands,
}

variables = {
    k: v for k, v in variables.items()
    if isinstance(k, str) and k.strip()
}

user_vars = {
    k: v for k, v in user_vars.items()
    if isinstance(k, str) and k.strip()
}

variables["ans"] = 0

# =========================================================
# MAIN LOOP
# =========================================================

while True:

    problem = input("\nType help to learn how to use Dave. Enter equation here: ").strip()

    if problem == "":
        continue

    # ---------------- HELP ----------------
    if problem.lower() == "help":
        show_help()
        continue

    # ---------------- ABOUT ----------------
    elif problem.lower() == "about":
        console.print("[yellow]You are currently running Dave Version 1.0.8. Dave was made by a child who was upset that his calculator had limits. This one has none.[/yellow]")
        continue

    # ---------------- ELEMENTS ----------------
    elif problem.strip() == "elements()":
        elements()
        continue

    # ---------------- LANGUAGE ----------------
    elif problem.startswith("lang "):

        parts = problem.split()

        if len(parts) > 1:

            lang = parts[1]

            if lang in languages:
                language = lang
                console.print(f"[green]Language {lang} set[/green]")

            else:
                console.print("[red]Unsupported language[/red]")

        continue

    # ---------------- TIME ----------------
    elif problem == "time":
        console.print(datetime.datetime.now().strftime("%H:%M:%S"))
        continue

    elif problem == "date":
        console.print(datetime.datetime.now().strftime("%Y-%m-%d"))
        continue

    elif problem == "month":
        console.print(datetime.datetime.now().strftime("%B"))
        continue

    elif problem == "year":
        console.print(datetime.datetime.now().strftime("%Y"))
        continue

    # ---------------- ANGLE MODES ----------------
    elif problem == "deg":
        angle_mode = "deg"
        console.print("[cyan]Degree mode enabled[/cyan]")
        continue

    elif problem == "rad":
        angle_mode = "rad"
        console.print("[cyan]Radian mode enabled[/cyan]")
        continue

    # ---------------- HISTORY ----------------
    elif problem == "history":

        if not history:
            console.print("[yellow]No history yet[/yellow]")

        else:
            for h in history:
                console.print(h)

        continue

        # ---------------- GRAPH ----------------
    elif problem.startswith("graph("):

        try:

            expr = problem[6:-1]

            parsed = sp.sympify(
                expr,
                locals={**variables, **user_vars}
            )

            f = sp.lambdify(x, parsed, modules=["numpy"])

            xs = np.linspace(-10, 10, 1000)

            ys = np.real(np.array(ys, dtype=np.complex128))

            # Convert scalar output into array
            if np.isscalar(ys):
                ys = np.full_like(xs, ys, dtype=float)

            plt.figure(figsize=(8,5))

            plt.plot(xs, ys)

            plt.xlabel("x")
            plt.ylabel("y")
            plt.title(f"y = {expr}")

            plt.grid(True)

            plt.show()

        except Exception as e:
            console.print(f"[red]Graph Error:[/red] {e}")

        continue

    # ---------------- GRAPH 3D ----------------
    elif problem.startswith("graph3d("):

        try:

            expr = problem[8:-1]

            f = sp.lambdify(
                (x, y),
                sp.sympify(expr, locals={**variables, **user_vars}),
                "numpy"
            )

            xs = np.linspace(-5, 5, 100)
            ys = np.linspace(-5, 5, 100)

            X, Y = np.meshgrid(xs, ys)

            Z = f(X, Y)

            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')

            ax.plot_surface(X, Y, Z)

            plt.show()

        except Exception as e:
            console.print(f"[red]3D Graph Error:[/red] {e}")

        continue
     

    # ---------------- QUIT ----------------
    elif problem.lower() in ["quit", "exit", "q"]:

        console.print("[green]Goodbye, and thank you for using Dave![/green]")
        break

    # ---------------- VARIABLE ASSIGNMENT ----------------
    elif "=" in problem and "==" not in problem and not problem.startswith("solve"):

        try:

            left, right = problem.split("=", 1)

            value = sp.sympify(
                right,
                locals={**variables, **user_vars}
            )

            var_name = left.strip()

            # Protect symbolic variables
            if var_name in ["x", "y", "z"]:

                console.print(
                    "[red]Cannot overwrite symbolic variables x, y, or z[/red]"
                )

                continue

            user_vars[var_name] = value

            with open(SAVE_FILE, "wb") as f:
                pickle.dump(user_vars, f)

            console.print(
                f"[cyan]{var_name}[/cyan] = {value}"
            )

        except Exception as e:
            console.print(f"[red]Assignment Error:[/red] {e}")

        continue

    # ---------------- NORMAL EXPRESSIONS ----------------
    else:

        # Handle text commands first
        cmd = problem.strip().lower()

        if cmd == "help":
            show_help()
            continue

        elif cmd == "about":
            show_about()
            continue

        elif cmd == "deg":
            angle_mode = "deg"
            console.print("[green]Angle mode set to degrees.[/green]")
            continue

        elif cmd == "rad":
            angle_mode = "rad"
            console.print("[green]Angle mode set to radians.[/green]")
            continue

        elif cmd in ("quit", "exit", "q"):
            break

        try:

            expr = sp.sympify(
                problem,
                locals={**variables, **user_vars}
            )

            expr = sp.simplify(expr)

            if expr.has(sp.zoo):
                raise ZeroDivisionError(
                    "Division by zero"
                )

            if hasattr(expr, "evalf") and expr.is_number:
                expr = expr.evalf()

            console.print(
                Panel.fit(
                    str(expr),
                    title="Answer",
                    border_style="green"
                )
            )

            variables["ans"] = expr
            history.append(f"{problem} = {expr}")

        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")
