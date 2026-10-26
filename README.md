# Dave

Dave is a command-line calculator with standard and scientific math, symbolic algebra, and optional tools for astronomy, chemistry, biology, meteorology, physiology, and other scientific fields.

This guide starts from a computer or phone with no Python packages installed. Keep Dave's packages in a virtual environment where possible. The platform builds are:

| Platform | Dave file |
| --- | --- |
| macOS | `dave_macos.py` |
| Windows | `dave_windows.py` |
| Linux | `dave_linux.py` |
| Android (Termux) | `dave_android.py` |

Copy the selected file to your device and run the matching instructions below from the folder containing it.

## macOS

1. Install Python 3.12 or newer from [python.org](https://www.python.org/downloads/). **Note: Full compatibility with all packages requires Python 3.14 or earlier; some packages are incompatible with Python 3.15+.**
2. Open Terminal and move to the folder containing `dave_macos.py`.
3. Run Dave. On first launch, Dave automatically installs any missing required packages from `requirements.txt`:
   ```sh
   python3 dave_macos.py
   ```
   To install packages manually instead:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   python -m pip install --upgrade pip --upgrade-strategy eager
   pip install -r requirements.txt
   ```

```sh
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip --upgrade-strategy eager
pip install sympy 'sympy<1.13' numpy matplotlib rich yfinance pandas scipy deep-translator skylight astropy-iers-data astroquery bioregistry mpmath pint earthpy h5py pyarrow plotly lmfit statsmodels uncertainties xarray anndata scanpy pysam dipy nibabel bioformats jupyter jax opt_einsum equinox splot freud-analysis spopt diffrax quantecon quantities sym spreg spglmg openmm  # Note: openmm may not be available for Python 3.15+
```

### Notes on Package Compatibility

The Dave 1.0.1 wheel supports Python 3.10 through 3.15. The current Mendeleev release declares support only for Python versions below 3.15, so Dave skips that dependency on Python 3.15; element-property features that need Mendeleev are unavailable there. Other optional scientific packages have their own Python-version limits.

The following packages have known compatibility issues with Python 3.15+:

- **openmm**: No compatible versions available for Python 3.15+. Please use the latest available version (Python 3.14) or remove this dependency if not needed.
- **GUDHI**: Requires Python 3.5-3.6 only and is incompatible with Python 3.12+. If you need GUDHI, use Python 3.6.

### Complete Package List

Dave supports over 150 scientific packages across multiple domains:

**Core Dependencies:**
- `mendeleev`: Chemistry calculations (element data, molecular formulas, reactions)
- `sympy`: Symbolic mathematics
- `numpy`: Numerical computing
- `matplotlib`: Plotting
- `rich`: Console formatting and printing
- `pandas`: Data frames
- `scipy`: Scientific computing

**Astronomy:**
- `astropy`, `skyfield`, `APLpy`, `astroML`, `astroplan`, `astropy_healpix`, `astropy_iers_data`, `astroquery`, `jplephem`, `poliastro`, `pyerfa`, `pyvo`, `reproject`, `sunpy`

**Biology/Bioinformatics:**
- `biopython`, `anndata`, `biom-format`, `biotite`, `scanpy`, `dendropy`, `msprime`, `pybedtools`, `pysam`, `scikit-bio`, `tskit`

**Machine Learning/Data Science:**
- `scikit-learn`, `statsmodels`, `tensorflow`, `torchmd`, `qutip`, `quantities`, `lmfit`, `xarray`, `altair`, `pyarrow`, `dask-image`, `spglm`

**Physics/Computational Chemistry:**
- `openmm`, `pymatgen`, `mdtraj`, `bioformats`, `nlopt`, `chemicals`, `chemparse`, `gsw`, `fluids`, `equinox`, `diffrax`, `qmsolve`

**Geosciences/Remote Sensing:**
- `GDAL`, `geopandas`, `rasterio`, `earthpy`, `pyproj`, `geojson`, `mapclassify`, `spglib`, `topologicpy`

**Mathematics/Analysis:**
- `mpmath`, `freud-analysis`, `dipy`, `emcee`, `shapely`, `hdmf`, `mdapy`, `nibabel`, `pynwb`, `neurodepry`, `pnm`, `splot`

**Other Tools:**
- `yfinance`, `deep-translator`, `matplotlib-tern-mpltern`, `mpltern`, `striplog-spglib`, `spopt`, `spreg`, `spglm`, `xyztimeseries`, `xyzservices`, `yt`, `momepy`, `movingpandas`, `spint`, `splot`, `PySmeQcd`, `PIMS`, `PubChemPy`, `PuLP`, `PyAVM`, `PyWavelets`, `tobler`, `trx-python`, `welly`, `wellpathpy`

**Note:** Installation will take significant time due to the large number of packages. Consider installing dependencies incrementally and only what you need.

## Linux

1. Install Python 3.12 or newer from your package manager (e.g., `apt install python3 python3-pip`, ensure pip is up-to-date).
2. Move to the folder containing `dave_linux.py`.
3. Run Dave. On first launch, Dave automatically installs any missing required packages from `requirements.txt`:
   ```sh
   python3 dave_linux.py
   ```
   To install packages manually instead:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   python -m pip install --upgrade pip --upgrade-strategy eager
   pip install -r requirements.txt
   ```

```sh
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip --upgrade-strategy eager
pip install sympy 'sympy<1.13' numpy matplotlib rich yfinance pandas scipy deep-translator skylight astropy-iers-data astroquery bioregistry mpmath pint earthpy h5py pyarrow plotly lmfit statsmodels uncertainties xarray anndata scanpy pysam dipy nibabel bioformats jupyter jax opt_einsum equinox splot freud-analysis spopt diffrax quantecon quantities sym spreg spglmg openmm
```

### Notes on Package Compatibility

The following packages have known compatibility issues with Python 3.15+:

- **openmm**: No compatible versions available for Python 3.15+. Please use the latest available version (Python 3.14) or remove this dependency if not needed.
- **GUDHI**: Requires Python 3.5-3.6 only and is incompatible with Python 3.12+. If you need GUDHI, use Python 3.6.

## Windows

1. Install Python 3.12 or newer from [python.org](https://www.python.org/downloads/). **Note: Full compatibility with all packages requires Python 3.14 or earlier; some packages are incompatible with Python 3.15+.**
2. Open Command Prompt or PowerShell and move to the folder containing `dave_windows.py`.
3. Run Dave. On first launch, Dave automatically installs any missing required packages from `requirements.txt`:
   ```powershell
   python dave_windows.py
   ```
   To install packages manually instead:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip --upgrade-strategy eager
   pip install -r requirements.txt
   ```

```sh
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip --upgrade-strategy eager
pip install sympy 'sympy<1.13' numpy matplotlib rich yfinance pandas scipy deep-translator skylight astropy-iers-data astroquery bioregistry mpmath pint earthpy h5py pyarrow plotly lmfit statsmodels uncertainties xarray anndata scanpy pysam dipy nibabel bioformats jupyter jax opt_einsum equinox splot freud-analysis spopt diffrax quantecon quantities sym spreg spglmg openmm
```

### Notes on Package Compatibility

The following packages have known compatibility issues with Python 3.15+:

- **openmm**: No compatible versions available for Python 3.15+. Please use the latest available version (Python 3.14) or remove this dependency if not needed.
- **GUDHI**: Requires Python 3.5-3.6 only and is incompatible with Python 3.12+. If you need GUDHI, use Python 3.6.

## Android (Termux)

1. Update Termux package list.
2. Install Python 3: `pkg install python`. **Note: Python must be version 3.14 or earlier for full compatibility.**
3. Move to the folder containing `dave_android.py`.
4. Run Dave. On first launch, Dave automatically installs any missing required packages from `requirements.txt`:
   ```sh
   python dave_android.py
   ```
   To install packages manually instead:
   ```sh
   python -m venv venv
   source venv/bin/activate
   python -m pip install --upgrade pip --upgrade-strategy eager
   pip install -r requirements.txt
   ```

```sh
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip --upgrade-strategy eager
pip install sympy 'sympy<1.13' numpy matplotlib rich yfinance pandas scipy deep-translator skylight astropy-iers-data astroquery bioregistry mpmath pint earthpy h5py pyarrow plotly lmfit statsmodels uncertainties xarray anndata scanpy pysam dipy nibabel bioformats jupyter jax opt_einsum equinox splot freud-analysis spopt diffrax quantecon quantities sym spreg spglmg openmm
```

### Android-Specific Compatibility Notes

- **openmm**: No compatible versions available. This dependency cannot be installed on Termux with current package availability. Consider removing this import if not needed for your use case, or use a different Python distribution that supports openmm.
- **GUDHI**: Requires Python 3.5-3.6 only and is incompatible with Python 3.12+. If you need GUDHI, use Python 3.6 or an older compatible environment.

## Troubleshooting

### Package Installation Issues

If you encounter errors during installation:

1. **Update pip**: `python -m pip install --upgrade pip`
2. **Install in correct order**: Install core packages first (numpy, matplotlib), then scientific libraries (scipy, sympy), then optional advanced packages
3. **Python version check**: Some packages have limited Python 3.15+ compatibility. The following work but may have limitations: numpy, matplotlib, scipy, sympy, pandas, deep_translator

## Features Overview

Dave supports calculations in multiple scientific domains. Some features require specific optional packages:

- **Math & Physics**: Full suite of mathematical formulas, constants, and operations
- **Astronomy**: Planetary calculations, constellations, space data analysis (requires astropy, skyfield, etc.)
- **Chemistry**: Element properties, molecular formula balancing, chemical reactions (requires mendeleev)
- **Biology**: DNA transcription/translation, amino acid information, organism data (requires biologyns, biopython, etc.)
- **Meteorology**: Weather predictions using OpenMeteo API (requires meteopen or weatherapi)
- **Finance**: Stock analysis and market data (requires yfinance)

### Comparing Data Fits

Use `compare_fits` to fit common models to paired measurements and rank them by corrected Akaike information criterion (AICc). Lower AICc is preferred; the result also includes each model's equation, fitted parameters, RMSE, and R².

```python
compare_fits(
    [1, 2, 3, 4, 5, 6],
    [2.1, 3.9, 6.2, 7.8, 10.1, 12.2],
    ["linear", "quadratic"],
)
```

Available models are `linear`, `quadratic`, `exponential`, and `power`. Omit the model list to compare all four. The power model requires positive x values. AICc requires at least two more measurements than the number of fitted parameters. Dave requires SciPy for this command.

## Reporting Issues

If you encounter issues not covered here, report them with:
- Python version output (`python --version`)
- Full error message (including the line causing the error)
- Which Dave file you're using (macOS, Windows, Linux, Android)
- What features you were trying to use

## Supporting Dave

Please try to star Dave so that we can reach our goal of 225 stars so that we can add Dave to Homebrew. It is also helpful to add any ideas to the comments to help improve Dave for all.
