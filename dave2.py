#!/usr/bin/env python3


import sys
sys.set_int_max_str_digits(0)

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

import sys
import inspect
import subprocess
import importlib

required_packages = {

    "sympy": "sympy",
    "numpy": "numpy",
    "matplotlib": "matplotlib",
    "rich": "rich",
    "pwinput": "pwinput",
    "pandas": "pandas",
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

import codecs
import pandas as pd 
import sympy as sp
import numpy as np

np.seterr(divide='raise', invalid='raise', over='raise', under='raise')

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

import statistics
import random
import readline
import pickle
import os
import atexit
import datetime
import re

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

def matrix_rank(A):
    return sp.Matrix(A).rank()

def matrix_trace(A):
    return sp.Matrix(A).trace()

def matrix_norm(A):
    return float(sp.Matrix(A).norm())

def matrix_rref(A):
    return sp.Matrix(A).rref()[0]

def matrix_nullspace(A):
    return sp.Matrix(A).nullspace()

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

def percentile(data, p):
    data = sorted(data)
    k = (len(data)-1)*(p/100)
    f = math.floor(k)
    c = math.ceil(k)

    if f == c:
        return data[int(k)]

    return data[f]*(c-k) + data[c]*(k-f)

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
    return statistics.geometric_mean(data)

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
    return distance / time

def acceleration(v1, v2, time):
    return (v2 - v1) / time

def density(mass, volume):
    return mass / volume

def pressure(force, area):
    return force / area

def work(force, distance):
    return force * distance

def power(work_done, time):
    return work_done / time

def frequency(period):
    return 1 / period

def period(freq):
    return 1 / freq

def wavelength(speed, freq):
    return speed / freq

def escape_velocity(M, R):
    G = 6.67430e-11
    return math.sqrt(2 * G * M / R)

def relativistic_ke(m, v):
    c = 299792458
    gamma = 1 / math.sqrt(1 - (v/c)**2)
    return (gamma - 1) * m * c**2

def momentum_vector(mass, velocity_vector):
    return [mass * v for v in velocity_vector]

def projectile_range(v, theta_deg, g=9.81):
    theta = math.radians(theta_deg)
    return (v**2 * math.sin(2*theta)) / g

def gravity_force(m1, m2, r):
    G = 6.67430e-11
    return G * m1 * m2 / r**2

def decay(N0, t, half_life):
    return N0 * (0.5)**(t / half_life)

def schwarzschild(mass):
    G = 6.67430e-11
    c = 299792458
    return 2 * G * mass / c**2

# ---------------- CHEMISTRY ----------------

def moles(mass, molar_mass):
    return mass / molar_mass

def mass_from_moles(moles_value, molar_mass):
    return moles_value * molar_mass

def molecules(moles_value):
    return moles_value * 6.02214076e23

def matrix_transpose(A):
    return np.array(A).T

def matrix_rank(A):
    return sp.Matrix(A).rank()

def matrix_trace(A):
    return sp.Matrix(A).trace()

def matrix_norm(A):
    return float(sp.Matrix(A).norm())

def matrix_rref(A):
    return sp.Matrix(A).rref()[0]

def matrix_nullspace(A):
    return sp.Matrix(A).nullspace()

def matrix_columnspace(A):
    return sp.Matrix(A).columnspace()

def matrix_rowspace(A):
    return sp.Matrix(A).rowspace()

def characteristic_polynomial(A):
    return sp.Matrix(A).charpoly().as_expr()

def molarity(moles_value, liters):
    return moles_value / liters

def ideal_gas_volume(n, T, P):
    R = 0.082057
    return n * R * T / P

def ideal_gas_pressure(n, T, V):
    R = 0.082057
    return n * R * T / V

def ideal_gas_temperature(P, V, n):
    R = 0.082057
    return P * V / (n * R)

def ideal_gas_moles(P, V, T):
    R = 0.082057
    return P * V / (R * T)

def protons(Z):
    return Z

def electrons(Z):
    return Z

def neutrons(A, Z):
    return A - Z

def ph(H):
    return -math.log10(H)

# ---------------- CHEMISTRY CONSTANTS ----------------

electron_mass = 9.1093837015e-31
proton_mass = 1.67262192369e-27
neutron_mass = 1.67492749804e-27

R = 8.314462618
F = 96485.33212

# ---------------- CALCULUS ----------------

def newton(expr, var, guess):
    return sp.nsolve(expr, var, guess)

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

def decimal(x):
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

    arr = np.array(m, dtype=float)

    return np.linalg.inv(arr).tolist()

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

    cos_theta = np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    return float(np.arccos(cos_theta))

def derivative(expr):

    expr = sp.sympify(expr)

    return sp.diff(expr, x)

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
    return sp.nsolve(sp.sympify(expr), guess)

def partial_x(expr):
    return sp.diff(sp.sympify(expr), x)

def partial_y(expr):
    return sp.diff(sp.sympify(expr), y)

def jacobian(exprs, vars_):
    return sp.Matrix(exprs).jacobian(vars_)

def hessian(expr):
    return sp.hessian(sp.sympify(expr), (x, y))

def newton(expr, guess, iterations=10):

    expr = sp.sympify(expr)
    deriv = sp.diff(expr, x)

    val = guess

    for _ in range(iterations):
        val = val - expr.subs(x, val) / deriv.subs(x, val)

    return sp.N(val)

def matrix_nullspace(A):
    return scipy.linalg.null_space(A)

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

def ideal_gas_pressure(n, T, V):
    R = 8.314
    return (n * R * T) / V

def ideal_gas_temperature(P, V, n):
    R = 8.314
    return (P * V) / (n * R)

def ideal_gas_volume(n, T, P):
    R = 8.314
    return (n * R * T) / P

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

def correlation_strength(x, y):
    r = np.corrcoef(x, y)[0,1]
    return {
        "r": r,
        "strength": "strong" if abs(r) > 0.7 else "weak"
    }

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

def xor_encrypt(text, key):

    return ''.join(
        chr(ord(c) ^ key)
        for c in text
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

def pretty_json(text):
    return json.dumps(json.loads(text), indent=4)

import time

start_time = None

def stopwatch_start():

    global start_time
    start_time = time.time()

def stopwatch_stop():

    return time.time() - start_time

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

def run_tests():

    tests = [

        ("2+2", 4),
        ("sqrt(81)", 9),
        ("gcd(48,18)", 6),
        ("det([[1,2],[3,4]])", -2),
    ]

    passed = 0

    for expr, expected in tests:

        try:

            result = sp.sympify(
                expr,
                locals=variables
            )

            if float(result) == float(expected):
                passed += 1

        except:
            pass

    console.print(
        f"[green]{passed}/{len(tests)} tests passed[/green]"
    )
angle_mode = "rad"

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

def electrons(s):
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

def convert(value, from_unit, to_unit):

    value = float(value)

    conversions = {

        ("kg", "lb"): 2.20462,
        ("lb", "kg"): 0.453592,

        ("m", "ft"): 3.28084,
        ("ft", "m"): 0.3048,

        ("m", "in"): 39.3701,
        ("in", "m"): 0.0254,

        ("km", "mi"): 0.621371,
        ("mi", "km"): 1.60934,

        ("g", "oz"): 0.035274,
        ("oz", "g"): 28.3495,

        ("l", "gal"): 0.264172,
        ("gal", "l"): 3.78541,
    }

    if (from_unit, to_unit) in conversions:
        return value * conversions[(from_unit, to_unit)]

    elif from_unit == "c" and to_unit == "f":
        return value * 9/5 + 32

    elif from_unit == "f" and to_unit == "c":
        return (value - 32) * 5/9

    return "Unsupported conversion"

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

        ("kg", "lb"): 2.20462,
        ("lb", "kg"): 0.453592,

        ("m", "ft"): 3.28084,
        ("ft", "m"): 0.3048,

        ("m", "in"): 39.3701,
        ("in", "m"): 0.0254,

        ("km", "mi"): 0.621371,
        ("mi", "km"): 1.60934,

        ("g", "oz"): 0.035274,
        ("oz", "g"): 28.3495,

        ("l", "gal"): 0.264172,
        ("gal", "l"): 3.78541,
    }

    if (from_unit, to_unit) in conversions:
        return value * conversions[(from_unit, to_unit)]

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

def randfloat():
    return random.random()

def choice(lst):
    return random.choice(lst)

def roots(expr):
    return sp.solve(sp.sympify(expr), x)

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
    return moles_value / liters

def ideal_gas_volume(n, T, P):
    return (n * R * T) / P

def velocity(distance, time):
    return distance / time

def acceleration(velocity_change, time):
    return velocity_change / time

def density(mass, volume):
    return mass / volume

def pressure(force_value, area):
    return force_value / area

def work(force_value, distance):
    return force_value * distance

def power(work_value, time):
    return work_value / time

def frequency(period):
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

def matrix_norm(m):
    return float(
        np.linalg.norm(
            np.array(m,dtype=float)
        )
    )

def matrix_rref(m):
    return sp.Matrix(m).rref()[0]

def matrix_columnspace(m):
    return sp.Matrix(m).columnspace()

def matrix_rowspace(m):
    return sp.Matrix(m).rowspace()

def matrix_trace(m):
    return trace(m)

def characteristic_polynomial(m):
    return sp.Matrix(m).charpoly().as_expr()

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

def skewness(data):

    arr = np.array(data)

    mean = np.mean(arr)

    std = np.std(arr)

    n = len(arr)

    return np.sum(
        ((arr-mean)/std)**3
    ) / n

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
======================== LANGUAGES ========================

English:
lang en

Spanish:
lang es

French:
lang fr

German:
lang de

Japanese:
lang jp

=========================================================
======================== HISTORY ========================

Show History:
history

Features:
- stores previous calculations
- stores answers
- readline support

=========================================================
======================== SYSTEM COMMANDS ========================

Show Help:
help

About:
about

Quit:
quit, q, or exit

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


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# =========================================================
# ASCII GRAPH
# =========================================================

def ascii_plot(expr):

    expr = sp.sympify(expr)

    f = sp.lambdify(x, expr, "math")

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

x, y, z = sp.symbols('x y z')

variables = {

    # ================= SYMBOLS =================

    "x": x,
    "y": y,
    "z": z,

    "pi": sp.pi,
    "e": sp.E,

    # ================= TRIG =================

    "sin": sin_wrapper,
    "cos": cos_wrapper,
    "tan": tan_wrapper,

    "asin": sp.asin,
    "acos": sp.acos,
    "atan": sp.atan,

    "sec": sp.sec,
    "csc": sp.csc,
    "cot": sp.cot,

    "sinh": sp.sinh,
    "cosh": sp.cosh,
    "tanh": sp.tanh,

    "radians": math.radians,
    "degrees": math.degrees,

    # ================= ALGEBRA =================

    "sqrt": sp.sqrt,
    "log": sp.log,
    "ln": sp.log,

    "expand": sp.expand,
    "expand_full": expand_full,

    "simplify": sp.simplify,
    "simplify_full": simplify_full,

    "factor": sp.factor,
    "collect": collect_terms,

    "solve": sp.solve,
    "solvefor": solvefor,

    "nsolve": nsolve_equation,

    "is_equivalent": is_equivalent,

    # ================= CALCULUS =================

    "diff": sp.diff,
    "derivative": derivative,
    "deriv": derivative,

    "integral": integral,
    "int": integral,

    "integrate": sp.integrate,
    "integral_def": definite_integral,

    "limit": limit,
    "taylor": taylor,
    "series_expansion": series_expansion,

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

    # ================= MATRIX =================

    "Matrix": sp.Matrix,

    "matrix": matrix,
    "matmul": matrix_mul,

    "det": matrix_det,
    "determinant": matrix_det,

    "inv": matrix_inv,
    "inverse": matrix_inv,

    "eig": eigenvalues,

    "matrix_power": matrix_power,
    "matrix_norm": matrix_norm,

    "matrix_rref": matrix_rref,
    "matrix_trace": matrix_trace,

    "matrix_nullspace": matrix_nullspace,
    "matrix_columnspace": matrix_columnspace,
    "matrix_rowspace": matrix_rowspace,

    "characteristic_polynomial": characteristic_polynomial,
    "transpose": matrix_transpose,
    "matrix_transpose": matrix_transpose,
    "solve_linear_system": solve_linear_system,
    "is_square": is_square,

    # Optional advanced matrix features
    "rank": matrix_rank,
    "transpose": matrix_transpose,

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

    "totient": totient,

    "prime": is_prime,
    "is_prime": is_prime,

    "primes_up_to": primes_up_to,

    "modinv": modinv,

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
    "run_tests": run_tests,

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
        console.print("[yellow]You are currently running Dave Version 1.0. Dave was made by a child who was upset that his calculator had limits. This one has none.[/yellow]")
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

            ys = f(xs)

            # Convert scalar output into array
            if np.isscalar(ys):
                ys = np.full_like(xs, ys, dtype=float)

            ys = np.array(ys, dtype=float)

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

        try:

            expr = sp.sympify(
                problem,
                locals={**variables, **user_vars}
            )

            expr = sp.simplify(expr)

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
