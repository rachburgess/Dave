#!/usr/bin/env python3

SAVE_FILE = "variables.pkl"
history = []

from datetime import datetime
import random
import sys
sys.set_int_max_str_digits(0)

import math
from mendeleev import element


# ==========================================================
# DAVE
# UNIVERSAL SCIENTIFIC PACKAGE INTEGRATION
# ==========================================================
#
# This system provides:
#
#   1. Package registry
#   2. Lazy importing
#   3. Package availability detection
#   4. Package status reports
#   5. Safe optional-package handling
#
# IMPORTANT:
# Do NOT import every package at startup.
#
# Many of these packages are large scientific libraries,
# some contain compiled extensions, and some have substantial
# startup costs.
#
# ==========================================================


# ----------------------------------------------------------
# UNIVERSAL PACKAGE REGISTRY
# ----------------------------------------------------------

SCIENTIFIC_PACKAGES = {

    # ======================================================
    # ASTRONOMY
    # ======================================================

    "APLpy": {
        "distribution": "APLpy",
        "import": "aplpy",
        "category": "astronomy",
    },

    "astroML": {
        "distribution": "astroML",
        "import": "astroML",
        "category": "astronomy",
    },

    "astroplan": {
        "distribution": "astroplan",
        "import": "astroplan",
        "category": "astronomy",
    },

    "astropy": {
        "distribution": "astropy",
        "import": "astropy",
        "category": "astronomy",
    },

    "astropy_healpix": {
        "distribution": "astropy-healpix",
        "import": "astropy_healpix",
        "category": "astronomy",
    },

    "astropy_iers_data": {
        "distribution": "astropy-iers-data",
        "import": "astropy_iers_data",
        "category": "astronomy",
    },

    "astroquery": {
        "distribution": "astroquery",
        "import": "astroquery",
        "category": "astronomy",
    },

    "jplephem": {
        "distribution": "jplephem",
        "import": "jplephem",
        "category": "astronomy",
    },

    "poliastro": {
        "distribution": "poliastro",
        "import": "poliastro",
        "category": "astronomy",
    },

    "pyerfa": {
        "distribution": "pyerfa",
        "import": "erfa",
        "category": "astronomy",
    },

    "pyvo": {
        "distribution": "pyvo",
        "import": "pyvo",
        "category": "astronomy",
    },

    "reproject": {
        "distribution": "reproject",
        "import": "reproject",
        "category": "astronomy",
    },

    "sunpy": {
        "distribution": "sunpy",
        "import": "sunpy",
        "category": "astronomy",
    },


    # ======================================================
    # BIOLOGY / BIOINFORMATICS
    # ======================================================

    "anndata": {
        "distribution": "anndata",
        "import": "anndata",
        "category": "biology",
    },

    "biom_format": {
        "distribution": "biom-format",
        "import": "biom",
        "category": "biology",
    },

    "biopython": {
        "distribution": "biopython",
        "import": "Bio",
        "category": "biology",
    },

    "bioregistry": {
        "distribution": "bioregistry",
        "import": "bioregistry",
        "category": "biology",
    },

    "biotite": {
        "distribution": "biotite",
        "import": "biotite",
        "category": "biology",
    },

    "DendroPy": {
        "distribution": "DendroPy",
        "import": "dendropy",
        "category": "biology",
    },

    "msprime": {
        "distribution": "msprime",
        "import": "msprime",
        "category": "biology",
    },

    "pybedtools": {
        "distribution": "pybedtools",
        "import": "pybedtools",
        "category": "biology",
    },

    "pysam": {
        "distribution": "pysam",
        "import": "pysam",
        "category": "biology",
    },

    "scanpy": {
        "distribution": "scanpy",
        "import": "scanpy",
        "category": "biology",
    },

    "scikit_bio": {
        "distribution": "scikit-bio",
        "import": "skbio",
        "category": "biology",
    },

    "tskit": {
        "distribution": "tskit",
        "import": "tskit",
        "category": "biology",
    },


    # ======================================================
    # CHEMISTRY / MATERIALS
    # ======================================================

    "chemicals": {
        "distribution": "chemicals",
        "import": "chemicals",
        "category": "chemistry",
    },

    "chemparse": {
        "distribution": "chemparse",
        "import": "chemparse",
        "category": "chemistry",
    },

    "chempy": {
        "distribution": "chempy",
        "import": "chempy",
        "category": "chemistry",
    },

    "fluids": {
        "distribution": "fluids",
        "import": "fluids",
        "category": "engineering",
    },

    "freud": {
        "distribution": "freud-analysis",
        "import": "freud",
        "category": "materials",
    },

    "matminer": {
        "distribution": "matminer",
        "import": "matminer",
        "category": "materials",
    },

    "mendeleev": {
        "distribution": "mendeleev",
        "import": "mendeleev",
        "category": "chemistry",
    },

    "periodictable": {
        "distribution": "periodictable",
        "import": "periodictable",
        "category": "chemistry",
    },

    "PubChemPy": {
        "distribution": "PubChemPy",
        "import": "pubchempy",
        "category": "chemistry",
    },

    "pymatgen": {
        "distribution": "pymatgen",
        "import": "pymatgen",
        "category": "materials",
    },

    "pymatgen_core": {
        "distribution": "pymatgen-core",
        "import": "pymatgen_core",
        "category": "materials",
    },

    "pyrolite": {
        "distribution": "pyrolite",
        "import": "pyrolite",
        "category": "geochemistry",
    },

    "rdkit": {
        "distribution": "rdkit",
        "import": "rdkit",
        "category": "chemistry",
    },

    "spglib": {
        "distribution": "spglib",
        "import": "spglib",
        "category": "materials",
    },

    "thermo": {
        "distribution": "thermo",
        "import": "thermo",
        "category": "engineering",
    },

    "radioactivedecay": {
        "distribution": "radioactivedecay",
        "import": "radioactivedecay",
        "category": "nuclear",
    },


    # ======================================================
    # MOLECULAR DYNAMICS / SIMULATION
    # ======================================================

    "Brian2": {
        "distribution": "Brian2",
        "import": "brian2",
        "category": "neuroscience",
    },

    "elephant": {
        "distribution": "elephant",
        "import": "elephant",
        "category": "neuroscience",
    },

    "MDAnalysis": {
        "distribution": "MDAnalysis",
        "import": "MDAnalysis",
        "category": "molecular_dynamics",
    },

    "mda_xdrlib": {
        "distribution": "mda-xdrlib",
        "import": "mda_xdrlib",
        "category": "molecular_dynamics",
    },

    "mdapy": {
        "distribution": "mdapy",
        "import": "mdapy",
        "category": "molecular_dynamics",
    },

    "mdtraj": {
        "distribution": "mdtraj",
        "import": "mdtraj",
        "category": "molecular_dynamics",
    },

    "mmtf_python": {
        "distribution": "mmtf-python",
        "import": "mmtf",
        "category": "molecular_dynamics",
    },

    "nengo": {
        "distribution": "nengo",
        "import": "nengo",
        "category": "neuroscience",
    },

    "neo": {
        "distribution": "neo",
        "import": "neo",
        "category": "neuroscience",
    },

    "OpenMM": {
        "distribution": "openmm",
        "import": "openmm",
        "category": "molecular_dynamics",
    },

    "pynapple": {
        "distribution": "pynapple",
        "import": "pynapple",
        "category": "neuroscience",
    },

    "pynwb": {
        "distribution": "pynwb",
        "import": "pynwb",
        "category": "neuroscience",
    },

    "torchmd": {
        "distribution": "torchmd",
        "import": "torchmd",
        "category": "molecular_dynamics",
    },


    # ======================================================
    # GEOSPATIAL / EARTH SCIENCE
    # ======================================================

    "affine": {
        "distribution": "affine",
        "import": "affine",
        "category": "gis",
    },

    "bruges": {
        "distribution": "bruges",
        "import": "bruges",
        "category": "geoscience",
    },

    "earthpy": {
        "distribution": "earthpy",
        "import": "earthpy",
        "category": "gis",
    },

    "esda": {
        "distribution": "esda",
        "import": "esda",
        "category": "gis",
    },

    "flopy": {
        "distribution": "flopy",
        "import": "flopy",
        "category": "hydrology",
    },

    "GDAL": {
        "distribution": "GDAL",
        "import": "osgeo",
        "category": "gis",
    },

    "gempy": {
        "distribution": "gempy",
        "import": "gempy",
        "category": "geology",
    },

    "gempy_engine": {
        "distribution": "gempy_engine",
        "import": "gempy_engine",
        "category": "geology",
    },

    "geographiclib": {
        "distribution": "geographiclib",
        "import": "geographiclib",
        "category": "gis",
    },

    "geopandas": {
        "distribution": "geopandas",
        "import": "geopandas",
        "category": "gis",
    },

    "geopy": {
        "distribution": "geopy",
        "import": "geopy",
        "category": "gis",
    },

    "giddy": {
        "distribution": "giddy",
        "import": "giddy",
        "category": "gis",
    },

    "libpysal": {
        "distribution": "libpysal",
        "import": "libpysal",
        "category": "gis",
    },

    "mapclassify": {
        "distribution": "mapclassify",
        "import": "mapclassify",
        "category": "gis",
    },

    "momepy": {
        "distribution": "momepy",
        "import": "momepy",
        "category": "gis",
    },

    "movingpandas": {
        "distribution": "movingpandas",
        "import": "movingpandas",
        "category": "gis",
    },

    "osmnx": {
        "distribution": "osmnx",
        "import": "osmnx",
        "category": "gis",
    },

    "pydeck": {
        "distribution": "pydeck",
        "import": "pydeck",
        "category": "gis",
    },

    "pyogrio": {
        "distribution": "pyogrio",
        "import": "pyogrio",
        "category": "gis",
    },

    "pyproj": {
        "distribution": "pyproj",
        "import": "pyproj",
        "category": "gis",
    },

    "pysal": {
        "distribution": "pysal",
        "import": "pysal",
        "category": "gis",
    },

    "pyregion": {
        "distribution": "pyregion",
        "import": "pyregion",
        "category": "astronomy",
    },

    "rasterio": {
        "distribution": "rasterio",
        "import": "rasterio",
        "category": "gis",
    },

    "rasterstats": {
        "distribution": "rasterstats",
        "import": "rasterstats",
        "category": "gis",
    },

    "rtree": {
        "distribution": "Rtree",
        "import": "rtree",
        "category": "gis",
    },

    "shapely": {
        "distribution": "shapely",
        "import": "shapely",
        "category": "gis",
    },

    "spaghetti": {
        "distribution": "spaghetti",
        "import": "spaghetti",
        "category": "gis",
    },

    "spglm": {
        "distribution": "spglm",
        "import": "spglm",
        "category": "gis",
    },

    "spint": {
        "distribution": "spint",
        "import": "spint",
        "category": "gis",
    },

    "splot": {
        "distribution": "splot",
        "import": "splot",
        "category": "gis",
    },

    "spml": {
        "distribution": "spml",
        "import": "spml",
        "category": "gis",
    },

    "spopt": {
        "distribution": "spopt",
        "import": "spopt",
        "category": "gis",
    },

    "spreg": {
        "distribution": "spreg",
        "import": "spreg",
        "category": "gis",
    },

    "striplog": {
        "distribution": "striplog",
        "import": "striplog",
        "category": "geoscience",
    },

    "tobler": {
        "distribution": "tobler",
        "import": "tobler",
        "category": "gis",
    },

    "topologicpy": {
        "distribution": "topologicpy",
        "import": "topologicpy",
        "category": "gis",
    },

    "wellpathpy": {
        "distribution": "wellpathpy",
        "import": "wellpathpy",
        "category": "geoscience",
    },

    "welly": {
        "distribution": "welly",
        "import": "welly",
        "category": "geoscience",
    },

    "xyzservices": {
        "distribution": "xyzservices",
        "import": "xyzservices",
        "category": "gis",
    },


    # ======================================================
    # MATHEMATICS / PHYSICS / OPTIMIZATION
    # ======================================================

    "cpsat_logutils": {
        "distribution": "cpsat-logutils",
        "import": "cpsat_logutils",
        "category": "optimization",
    },

    "demes": {
        "distribution": "demes",
        "import": "demes",
        "category": "population_genetics",
    },

    "diffrax": {
        "distribution": "diffrax",
        "import": "diffrax",
        "category": "mathematics",
    },

    "dynamiqs": {
        "distribution": "dynamiqs",
        "import": "dynamiqs",
        "category": "quantum",
    },

    "emcee": {
        "distribution": "emcee",
        "import": "emcee",
        "category": "statistics",
    },

    "equinox": {
        "distribution": "equinox",
        "import": "equinox",
        "category": "machine_learning",
    },

    "formulaic": {
        "distribution": "formulaic",
        "import": "formulaic",
        "category": "statistics",
    },

    "gudhi": {
        "distribution": "GUDHI",
        "import": "gudhi",
        "category": "topology",
    },

    "lineax": {
        "distribution": "lineax",
        "import": "lineax",
        "category": "mathematics",
    },

    "lmfit": {
        "distribution": "lmfit",
        "import": "lmfit",
        "category": "optimization",
    },

    "MetPy": {
        "distribution": "MetPy",
        "import": "metpy",
        "category": "meteorology",
    },

    "mpmath": {
        "distribution": "mpmath",
        "import": "mpmath",
        "category": "mathematics",
    },

    "opt_einsum": {
        "distribution": "opt_einsum",
        "import": "opt_einsum",
        "category": "mathematics",
    },

    "optimistix": {
        "distribution": "optimistix",
        "import": "optimistix",
        "category": "mathematics",
    },

    "plasmapy": {
        "distribution": "plasmapy",
        "import": "plasmapy",
        "category": "plasma_physics",
    },

    "PuLP": {
        "distribution": "PuLP",
        "import": "pulp",
        "category": "optimization",
    },

    "qmsolve": {
        "distribution": "qmsolve",
        "import": "qmsolve",
        "category": "quantum",
    },

    "quantecon": {
        "distribution": "quantecon",
        "import": "quantecon",
        "category": "economics",
    },

    "quantities": {
        "distribution": "quantities",
        "import": "quantities",
        "category": "units",
    },

    "qutip": {
        "distribution": "qutip",
        "import": "qutip",
        "category": "quantum",
    },

    "scipy": {
        "distribution": "scipy",
        "import": "scipy",
        "category": "mathematics",
    },

    "statsmodels": {
        "distribution": "statsmodels",
        "import": "statsmodels",
        "category": "statistics",
    },

    "sym": {
        "distribution": "sym",
        "import": "sym",
        "category": "mathematics",
    },

    "sympy": {
        "distribution": "sympy",
        "import": "sympy",
        "category": "mathematics",
    },

    "topoly": {
        "distribution": "topoly",
        "import": "topoly",
        "category": "topology",
    },

    "uncertainties": {
        "distribution": "uncertainties",
        "import": "uncertainties",
        "category": "uncertainty",
    },

    "unyt": {
        "distribution": "unyt",
        "import": "unyt",
        "category": "units",
    },


    # ======================================================
    # DATA / VISUALIZATION / IMAGE PROCESSING
    # ======================================================

    "altair": {
        "distribution": "altair",
        "import": "altair",
        "category": "visualization",
    },

    "cmap": {
        "distribution": "cmap",
        "import": "cmap",
        "category": "visualization",
    },

    "cmasher": {
        "distribution": "cmasher",
        "import": "cmasher",
        "category": "visualization",
    },

    "cmyt": {
        "distribution": "cmyt",
        "import": "cmyt",
        "category": "visualization",
    },

    "colorspacious": {
        "distribution": "colorspacious",
        "import": "colorspacious",
        "category": "visualization",
    },

    "contourpy": {
        "distribution": "contourpy",
        "import": "contourpy",
        "category": "visualization",
    },

    "dask_image": {
        "distribution": "dask-image",
        "import": "dask_image",
        "category": "image_processing",
    },

    "dipy": {
        "distribution": "dipy",
        "import": "dipy",
        "category": "neuroimaging",
    },

    "folium": {
        "distribution": "folium",
        "import": "folium",
        "category": "visualization",
    },

    "GridDataFormats": {
        "distribution": "GridDataFormats",
        "import": "gridData",
        "category": "scientific_data",
    },

    "h5py": {
        "distribution": "h5py",
        "import": "h5py",
        "category": "scientific_data",
    },

    "hdmf": {
        "distribution": "hdmf",
        "import": "hdmf",
        "category": "scientific_data",
    },

    "matplotlib": {
        "distribution": "matplotlib",
        "import": "matplotlib",
        "category": "visualization",
    },

    "mpltern": {
        "distribution": "mpltern",
        "import": "mpltern",
        "category": "visualization",
    },

    "mrcfile": {
        "distribution": "mrcfile",
        "import": "mrcfile",
        "category": "scientific_data",
    },

    "nibabel": {
        "distribution": "nibabel",
        "import": "nibabel",
        "category": "neuroimaging",
    },

    "numcodecs": {
        "distribution": "numcodecs",
        "import": "numcodecs",
        "category": "scientific_data",
    },

    "numpy": {
        "distribution": "numpy",
        "import": "numpy",
        "category": "mathematics",
    },

    "PIMS": {
        "distribution": "PIMS",
        "import": "pims",
        "category": "image_processing",
    },

    "Pint": {
        "distribution": "Pint",
        "import": "pint",
        "category": "units",
    },

    "plotly": {
        "distribution": "plotly",
        "import": "plotly",
        "category": "visualization",
    },

    "pyarrow": {
        "distribution": "pyarrow",
        "import": "pyarrow",
        "category": "data",
    },

    "PyAVM": {
        "distribution": "PyAVM",
        "import": "pyavm",
        "category": "astronomy",
    },

    "PySmeQcd": {
        "distribution": "PySmeQcd",
        "import": "PySmeQcd",
        "category": "physics",
    },

    "PyWavelets": {
        "distribution": "PyWavelets",
        "import": "pywt",
        "category": "signal_processing",
    },

    "scikit_image": {
        "distribution": "scikit-image",
        "import": "skimage",
        "category": "image_processing",
    },

    "slicerator": {
        "distribution": "slicerator",
        "import": "slicerator",
        "category": "image_processing",
    },

    "tifffile": {
        "distribution": "tifffile",
        "import": "tifffile",
        "category": "image_processing",
    },

    "trx_python": {
        "distribution": "trx-python",
        "import": "trx",
        "category": "neuroimaging",
    },

    "xarray": {
        "distribution": "xarray",
        "import": "xarray",
        "category": "data",
    },

    "yt": {
        "distribution": "yt",
        "import": "yt",
        "category": "scientific_data",
    },

    "zarr": {
        "distribution": "zarr",
        "import": "zarr",
        "category": "scientific_data",
    },
    "gsw": {"distribution": "gsw", "import": "gsw", "category": "oceanography"},
    "scikit_learn": {"distribution": "scikit-learn", "import": "sklearn", "category": "machine_learning"},
}


# ----------------------------------------------------------
# PACKAGE CACHE
# ----------------------------------------------------------

PACKAGE_CACHE = {}

PACKAGE_ERRORS = {}


# ----------------------------------------------------------
# SAFE PACKAGE LOADER
# ----------------------------------------------------------

def load_scientific_package(package_name):
    """
    Lazily import one of Dave's optional scientific packages.

    Example:

        astropy = load_scientific_package("astropy")

    Returns:
        Imported module when available.

    Raises:
        ImportError when the package is unavailable.
    """

    if package_name in PACKAGE_CACHE:
        return PACKAGE_CACHE[package_name]

    if package_name not in SCIENTIFIC_PACKAGES:
        raise KeyError(
            f"Unknown scientific package: {package_name}"
        )

    info = SCIENTIFIC_PACKAGES[package_name]

    module_name = info["import"]

    try:

        module = importlib.import_module(module_name)

        PACKAGE_CACHE[package_name] = module

        return module

    except Exception as exc:

        PACKAGE_ERRORS[package_name] = repr(exc)

        raise ImportError(
            f"Dave could not load {package_name} "
            f"(import: {module_name}): {exc}"
        ) from exc


# ----------------------------------------------------------
# CHECK PACKAGE WITHOUT RAISING AN ERROR
# ----------------------------------------------------------

def scientific_package_available(package_name):
    """
    Return True if a scientific package can currently be
    imported.
    """

    try:
        load_scientific_package(package_name)
        return True

    except Exception:
        return False


# ----------------------------------------------------------
# PACKAGE STATUS
# ----------------------------------------------------------

def scientific_package_status():

    results = {}

    for package_name in SCIENTIFIC_PACKAGES:

        info = SCIENTIFIC_PACKAGES[package_name]

        try:

            module = load_scientific_package(package_name)

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "installed": True,
                "import": info["import"],
                "distribution": info["distribution"],
                "category": info["category"],
                "version": str(version),
                "error": None,
            }

        except Exception as exc:

            results[package_name] = {
                "installed": False,
                "import": info["import"],
                "distribution": info["distribution"],
                "category": info["category"],
                "version": None,
                "error": str(exc),
            }

    return results


# ----------------------------------------------------------
# PRINT PACKAGE STATUS
# ----------------------------------------------------------

def packages(category=None, installed_only=False):

    status = scientific_package_status()

    rows = []

    for name, info in status.items():

        if category is not None:

            if info["category"].lower() != category.lower():
                continue

        if installed_only and not info["installed"]:
            continue

        rows.append(
            (
                name,
                info["category"],
                info["version"]
                if info["installed"]
                else "NOT AVAILABLE",
                info["error"]
                if not info["installed"]
                else "",
            )
        )

    print()
    print("=" * 100)
    print("DAVE — SCIENTIFIC PACKAGE STATUS")
    print("=" * 100)
    print()

    if not rows:

        print("No matching packages found.")

        return status

    print(
        f"{'PACKAGE':<28}"
        f"{'CATEGORY':<24}"
        f"{'VERSION':<20}"
        f"STATUS"
    )

    print("-" * 100)

    for name, category_name, version, error in rows:

        status_text = (
            "AVAILABLE"
            if version != "NOT AVAILABLE"
            else "UNAVAILABLE"
        )

        print(
            f"{name:<28}"
            f"{category_name:<24}"
            f"{version:<20}"
            f"{status_text}"
        )

    print()
    print(f"Packages registered: {len(SCIENTIFIC_PACKAGES)}")
    print()

    return status


# ----------------------------------------------------------
# CATEGORY LIST
# ----------------------------------------------------------

def scientific_package_categories():

    categories = {}

    for name, info in SCIENTIFIC_PACKAGES.items():

        category = info["category"]

        categories.setdefault(
            category,
            []
        ).append(name)

    return categories


# ----------------------------------------------------------
# SHOW CATEGORY
# ----------------------------------------------------------

def package_category(category_name):

    categories = scientific_package_categories()

    matches = categories.get(
        category_name.lower(),
        []
    )

    if not matches:

        print(
            f"No scientific package category "
            f"named '{category_name}'."
        )

        print()
        print(
            "Available categories:"
        )

        for category in sorted(categories):

            print(
                f"  {category}"
            )

        return []

    print()
    print("=" * 80)
    print(
        f"DAVE — {category_name.upper()}"
    )
    print("=" * 80)
    print()

    for package_name in sorted(matches):

        info = SCIENTIFIC_PACKAGES[package_name]

        available = scientific_package_available(
            package_name
        )

        marker = "OK" if available else "--"

        print(
            f"[{marker}] {package_name}"
        )

    print()

    return matches

# ==========================================================
# DAVE
# ASTRONOMY INTEGRATION
# PART 1 — CORE ASTRONOMY / ASTROPY
# ==========================================================
#
# Packages covered in this part:
#
#   astropy
#   astropy-healpix
#   astropy-iers-data
#   pyerfa
#
# This section provides:
#
#   Coordinates
#   Units
#   Physical constants
#   Time
#   Sky coordinates
#   Angular separation
#   Distance
#   Cartesian coordinates
#   Galactic coordinates
#   Equatorial coordinates
#   Observatory locations
#   Earth locations
#   Altitude / azimuth
#   Coordinate transformations
#   FITS-independent astronomy utilities
#   Astronomical constants
#   Julian dates
#   Barycentric / heliocentric time utilities
#   HEALPix utilities
#   ERFA access
#
# Everything is loaded lazily.
#
# ==========================================================


# ==========================================================
# ASTROPY LOADER
# ==========================================================

def _get_astropy():
    """
    Load Astropy only when an astronomy function needs it.
    """

    return load_scientific_package("astropy")


def _get_astropy_units():
    """
    Return astropy.units.
    """

    astropy = _get_astropy()

    return astropy.units


def _get_astropy_time():
    """
    Return astropy.time.
    """

    astropy = _get_astropy()

    return astropy.time


def _get_astropy_coordinates():
    """
    Return astropy.coordinates.
    """

    astropy = _get_astropy()

    return astropy.coordinates


# ==========================================================
# ASTRONOMICAL CONSTANTS
# ==========================================================

def astro_constants():
    """
    Return important astronomical and physical
    constants from Astropy.

    Constants are returned individually so that
    incompatible unit systems are never combined.
    """

    from astropy import constants as const

    return {
        "speed_of_light": const.c,
        "gravitational_constant": const.G,
        "Planck_constant": const.h,
        "reduced_Planck_constant": const.hbar,
        "elementary_charge": const.e,
        "electron_mass": const.m_e,
        "proton_mass": const.m_p,
        "neutron_mass": const.m_n,
        "astronomical_unit": const.au,
        "parsec": const.pc,
        "solar_mass": const.M_sun,
        "solar_radius": const.R_sun,
        "solar_luminosity": const.L_sun,
    }

# ==========================================================
# ASTRONOMICAL UNIT CONVERSION
# ==========================================================

def astro_convert(value, from_unit, to_unit):
    """
    Convert an astronomical quantity between compatible units.

    Examples:

        astro_convert(1, "au", "km")
        astro_convert(1, "pc", "lyr")
        astro_convert(1, "rad", "deg")
    """

    u = _get_astropy_units()

    quantity = value * u.Unit(from_unit)

    converted = quantity.to(
        u.Unit(to_unit)
    )

    return converted


# ==========================================================
# ASTRONOMICAL TIME
# ==========================================================

def astro_time(
    value=None
):
    """
    Create an Astropy Time object.

    Examples:

        astro_time()

        astro_time("2026-01-01")

        astro_time("2026-01-01T00:00:00")
    """

    from astropy.time import Time

    if value is None:
        return Time.now()

    if isinstance(
        value,
        Time
    ):
        return value

    text = str(
        value
    ).strip()

    # Date only
    if len(text) == 10:
        text = (
            text
            + "T00:00:00"
        )

    return Time(
        text,
        format="isot",
        scale="utc"
    )

# ==========================================================
# CURRENT ASTRONOMICAL TIME REPORT
# ==========================================================

def astro_time_report():
    """
    Return a detailed report of the current astronomical time.
    """

    Time = _get_astropy_time().Time

    now = Time.now()

    report = {

        "iso": now.iso,
        "isot": now.isot,
        "jd": now.jd,
        "mjd": now.mjd,
        "unix": now.unix,
        "decimalyear": now.decimalyear,
        "sidereal_time": str(
            now.sidereal_time("mean")
        ),
    }

    print()
    print("=" * 80)
    print("DAVE — ASTRONOMICAL TIME")
    print("=" * 80)
    print()

    for key, value in report.items():

        print(
            f"{key:<20}: {value}"
        )

    print()

    return report


# ==========================================================
# JULIAN DATE
# ==========================================================

def julian_date(value=None):
    """
    Convert a date/time into Julian Date.

    If no value is supplied, the current Julian Date is returned.
    """

    Time = _get_astropy_time().Time

    if value is None:

        return Time.now().jd

    return Time(
        value,
        format="isot",
        scale="utc"
    ).jd


# ==========================================================
# MODIFIED JULIAN DATE
# ==========================================================

def modified_julian_date(value=None):
    """
    Return Modified Julian Date.
    """

    Time = _get_astropy_time().Time

    if value is None:

        return Time.now().mjd

    return Time(
        value,
        format="isot",
        scale="utc"
    ).mjd


# ==========================================================
# COORDINATE CREATION
# ==========================================================

def skycoord(
    ra,
    dec,
    frame="icrs",
    unit="deg"
):
    """
    Create an Astropy SkyCoord.

    Example:

        skycoord(10.6847, 41.2687)

    returns the ICRS coordinates of M31.
    """

    coordinates = _get_astropy_coordinates()

    SkyCoord = coordinates.SkyCoord

    return SkyCoord(
        ra=ra,
        dec=dec,
        unit=unit,
        frame=frame
    )


# ==========================================================
# COORDINATE FROM STRING
# ==========================================================

def astro_coordinate(
    coordinate,
    frame="icrs"
):
    """
    Parse a coordinate string.

    Examples:

        astro_coordinate("10h41m04.1s +41d16m09s")
        astro_coordinate("10:41:04.1 +41:16:09")
    """

    coordinates = _get_astropy_coordinates()

    SkyCoord = coordinates.SkyCoord

    return SkyCoord(
        coordinate,
        frame=frame
    )


# ==========================================================
# RIGHT ASCENSION / DECLINATION
# ==========================================================

def ra_dec(
    ra,
    dec,
    unit="deg",
    frame="icrs"
):
    """
    Return a formatted RA/Dec report.
    """

    coord = skycoord(
        ra,
        dec,
        frame=frame,
        unit=unit
    )

    report = {

        "frame": coord.frame.name,

        "ra_degrees": coord.ra.deg,

        "dec_degrees": coord.dec.deg,

        "ra_hours": coord.ra.hour,

        "ra_hms": coord.ra.to_string(
            unit="hourangle"
        ),

        "dec_dms": coord.dec.to_string(
            unit="deg"
        ),
    }

    print()
    print("=" * 70)
    print("ASTRONOMICAL COORDINATE")
    print("=" * 70)
    print()

    for key, value in report.items():

        print(
            f"{key:<18}: {value}"
        )

    print()

    return report


# ==========================================================
# ANGULAR SEPARATION
# ==========================================================

def angular_separation(
    ra1,
    dec1,
    ra2,
    dec2,
    unit="deg"
):
    """
    Calculate angular separation between two sky positions.

    Example:

        angular_separation(
            10.6847,
            41.2687,
            83.8221,
            -5.3911
        )
    """

    c1 = skycoord(
        ra1,
        dec1,
        unit=unit
    )

    c2 = skycoord(
        ra2,
        dec2,
        unit=unit
    )

    return c1.separation(c2)


# ==========================================================
# POSITION ANGLE
# ==========================================================

def position_angle(
    ra1,
    dec1,
    ra2,
    dec2,
    unit="deg"
):
    """
    Calculate the position angle from one sky coordinate
    to another.
    """

    c1 = skycoord(
        ra1,
        dec1,
        unit=unit
    )

    c2 = skycoord(
        ra2,
        dec2,
        unit=unit
    )

    return c1.position_angle(c2)


# ==========================================================
# COORDINATE TRANSFORMATION
# ==========================================================

def transform_coordinates(
    ra,
    dec,
    from_frame,
    to_frame,
    unit="deg"
):
    """
    Transform celestial coordinates between
    Astropy coordinate frames.

    Example:

        transform_coordinates(
            10,
            20,
            "icrs",
            "galactic"
        )
    """

    from astropy.coordinates import (
        SkyCoord
    )
    import astropy.units as u

    coord = SkyCoord(
        ra=float(ra) * u.Unit(unit),
        dec=float(dec) * u.Unit(unit),
        frame=str(from_frame).lower()
    )

    transformed = coord.transform_to(
        str(to_frame).lower()
    )

    return {
        "frame": str(to_frame).lower(),
        "longitude": transformed.spherical.lon,
        "latitude": transformed.spherical.lat,
        "longitude_deg":
            transformed.spherical.lon.deg,
        "latitude_deg":
            transformed.spherical.lat.deg,
    }

# ==========================================================
# GALACTIC COORDINATES
# ==========================================================

def galactic_coordinates(
    ra,
    dec,
    unit="deg"
):
    """
    Convert ICRS RA/Dec to Galactic longitude/latitude.
    """

    transformed = transform_coordinates(
        ra,
        dec,
        "icrs",
        "galactic",
        unit
    )

    return {
        "l": transformed["longitude"],
        "b": transformed["latitude"],
        "l_deg": transformed["longitude_deg"],
        "b_deg": transformed["latitude_deg"],
    }


# ==========================================================
# GALACTIC TO ICRS
# ==========================================================

def galactic_to_icrs(
    l,
    b,
    unit="deg"
):
    """
    Convert Galactic coordinates to ICRS.
    """

    coordinates = _get_astropy_coordinates()

    SkyCoord = coordinates.SkyCoord

    coord = SkyCoord(
        l=l,
        b=b,
        unit=unit,
        frame="galactic"
    )

    result = coord.icrs

    return {

        "ra": result.ra,

        "dec": result.dec,

        "ra_deg": result.ra.deg,

        "dec_deg": result.dec.deg,
    }


# ==========================================================
# EARTH LOCATION
# ==========================================================

def earth_location(
    latitude,
    longitude,
    height=0,
    unit="deg"
):
    """
    Create an EarthLocation.

    Example:

        earth_location(
            40.7128,
            -74.0060
        )
    """

    coordinates = _get_astropy_coordinates()

    EarthLocation = coordinates.EarthLocation

    u = _get_astropy_units()

    return EarthLocation.from_geodetic(
        longitude * u.Unit(unit),
        latitude * u.Unit(unit),
        height * u.m
    )


# ==========================================================
# OBSERVATORY LOCATION
# ==========================================================

def observatory(
    name
):
    """
    Look up a named astronomical observatory/site.
    """

    coordinates = _get_astropy_coordinates()

    EarthLocation = coordinates.EarthLocation

    return EarthLocation.of_site(name)


# ==========================================================
# ALTITUDE / AZIMUTH
# ==========================================================

def altaz(
    ra,
    dec,
    latitude,
    longitude,
    height=0,
    obstime=None,
    unit="deg"
):
    """
    Convert an ICRS sky position into local Alt/Az.

    Parameters:

        ra
            Right ascension.

        dec
            Declination.

        latitude
            Observer latitude.

        longitude
            Observer longitude.

        height
            Observer height in metres.

        obstime
            Observation time.

        unit
            Coordinate unit.
    """

    coordinates = _get_astropy_coordinates()

    SkyCoord = coordinates.SkyCoord
    AltAz = coordinates.AltAz

    Time = _get_astropy_time().Time

    u = _get_astropy_units()

    if obstime is None:

        obstime = Time.now()

    elif not isinstance(obstime, Time):

        obstime = Time(
            obstime
        )

    location = earth_location(
        latitude,
        longitude,
        height,
        unit
    )

    target = SkyCoord(
        ra=ra,
        dec=dec,
        unit=unit,
        frame="icrs"
    )

    local = target.transform_to(
        AltAz(
            obstime=obstime,
            location=location
        )
    )

    return {

        "altitude": local.alt,

        "azimuth": local.az,

        "altitude_deg": local.alt.deg,

        "azimuth_deg": local.az.deg,
    }

# ==========================================================
# ADVANCED NUMERICAL / SCIENTIFIC FEATURES
# ==========================================================


# ==========================================================
# DIFFRAX — ODE SOLVER
# ==========================================================

def diffrax_ode(
    derivative,
    y0,
    t0=0.0,
    t1=1.0,
    dt=0.01
):
    """
    Solve a simple ODE using Diffrax.

    derivative(t, y) must return dy/dt.

    Example:
        diffrax_ode(
            lambda t, y: -y,
            1.0,
            0,
            5,
            0.1
        )
    """

    import jax
    import jax.numpy as jnp
    import diffrax

    def rhs(t, y, args):
        return derivative(t, y)

    term = diffrax.ODETerm(rhs)

    solver = diffrax.Tsit5()

    saveat = diffrax.SaveAt(
        ts=jnp.arange(
            t0,
            t1 + dt,
            dt
        )
    )

    solution = diffrax.diffeqsolve(
        term,
        solver,
        t0=t0,
        t1=t1,
        dt0=dt,
        y0=jnp.asarray(y0),
        saveat=saveat
    )

    return {
        "times": solution.ts,
        "values": solution.ys
    }


# ==========================================================
# DYNAMIQS — QUANTUM STATE
# ==========================================================

def dynamiqs_state(
    amplitudes
):
    """
    Create a normalized quantum state with Dynamiqs.

    Example:
        dynamiqs_state([1, 0])
    """

    import dynamiqs as dq

    state = dq.asqarray(
        amplitudes
    )

    norm = dq.norm(
        state
    )

    if norm != 0:
        state = state / norm

    return state


# ==========================================================
# EQUINOX — SIMPLE NEURAL NETWORK
# ==========================================================

def equinox_linear(
    input_size,
    output_size,
    seed=0
):
    """
    Create an Equinox linear layer.
    """

    import jax
    import equinox as eqx

    key = jax.random.PRNGKey(
        seed
    )

    return eqx.nn.Linear(
        input_size,
        output_size,
        key=key
    )


# ==========================================================
# LINEAX — LINEAR SYSTEM
# ==========================================================

def lineax_solve(
    matrix,
    vector
):
    """
    Solve A x = b using Lineax.
    """

    import jax.numpy as jnp
    import lineax as lx

    A = jnp.asarray(
        matrix
    )

    b = jnp.asarray(
        vector
    )

    operator = lx.MatrixLinearOperator(
        A,
        lx.PresetLinear()
    )

    solver = lx.AutoLinearSolver(
        well_posed=True
    )

    solution = lx.linear_solve(
        operator,
        b,
        solver
    )

    return solution.value


# ==========================================================
# OPTIMISTIX — OPTIMIZATION
# ==========================================================

def optimistix_minimize(
    function,
    initial_value
):
    """
    Minimize a scalar function using Optimistix.
    """

    import jax
    import jax.numpy as jnp
    import optimistix as optx

    def objective(x, args):
        return function(x)

    solver = optx.BFGS(
        rtol=1e-8,
        atol=1e-8
    )

    result = optx.minimise(
        objective,
        solver,
        jnp.asarray(
            initial_value
        ),
        options={}
    )

    return result.value


# ==========================================================
# OPT_EINSUM — OPTIMIZED EINSTEIN SUM
# ==========================================================

def optimized_einsum(
    expression,
    *arrays
):
    """
    Perform an optimized Einstein summation.

    Example:
        optimized_einsum(
            "ij,jk->ik",
            A,
            B
        )
    """

    import opt_einsum

    return opt_einsum.contract(
        expression,
        *arrays
    )


# ==========================================================
# EMCEE — MCMC SAMPLING
# ==========================================================

def emcee_sample(
    log_probability,
    initial_positions,
    steps=100
):
    """
    Run an affine-invariant MCMC sampler.

    log_probability(position) should return
    the logarithmic probability.
    """

    import numpy as np
    import emcee

    initial_positions = np.asarray(
        initial_positions,
        dtype=float
    )

    walkers, dimensions = (
        initial_positions.shape
    )

    sampler = emcee.EnsembleSampler(
        walkers,
        dimensions,
        log_probability
    )

    sampler.run_mcmc(
        initial_positions,
        steps,
        progress=False
    )

    return sampler


# ==========================================================
# FORMULAIC — FORMULA PARSING
# ==========================================================

def formulaic_design_matrix(
    formula,
    data
):
    """
    Create a design matrix using Formulaic.

    Example:
        formulaic_design_matrix(
            "y ~ x1 + x2",
            data
        )
    """

    from formulaic import model_matrix

    return model_matrix(
        formula,
        data
    )


# ==========================================================
# GUDHI — SIMPLICIAL COMPLEX
# ==========================================================

def gudhi_simplex_tree(
    simplices
):
    """
    Build a GUDHI simplex tree.

    Example:
        gudhi_simplex_tree(
            [[0, 1], [1, 2], [0, 2]]
        )
    """

    import gudhi

    tree = gudhi.SimplexTree()

    for simplex in simplices:
        tree.insert(
            simplex
        )

    return tree


def gudhi_persistence(
    simplices
):
    """
    Calculate persistent homology
    from a simplicial complex.
    """

    tree = gudhi_simplex_tree(
        simplices
    )

    return tree.persistence()

# ==========================================================
# BIOLOGY / GENOMICS FEATURES
# ==========================================================


# ==========================================================
# BIOPYTHON — SEQUENCE OBJECT
# ==========================================================

def biopython_sequence(
    sequence
):
    """
    Create a Biopython Seq object.
    """

    from Bio.Seq import Seq

    return Seq(
        str(sequence)
    )


# ==========================================================
# BIOPYTHON — REVERSE COMPLEMENT
# ==========================================================

def biopython_reverse_complement(
    sequence
):
    """
    Return the reverse complement of a DNA sequence.
    """

    from Bio.Seq import Seq

    return str(
        Seq(
            str(sequence)
        ).reverse_complement()
    )


# ==========================================================
# BIOPYTHON — TRANSLATE DNA
# ==========================================================

def biopython_translate(
    sequence
):
    """
    Translate DNA into amino acids.
    """

    from Bio.Seq import Seq

    return str(
        Seq(
            str(sequence)
        ).translate()
    )


# ==========================================================
# DENDROPY — NEWICK TREE
# ==========================================================

def dendropy_tree(
    newick
):
    """
    Parse a Newick phylogenetic tree.
    """

    from dendropy import Tree

    return Tree.get(
        data=str(newick),
        schema="newick"
    )


def dendropy_tree_distance(
    newick,
    taxon1,
    taxon2
):
    """
    Calculate the distance between
    two taxa in a DendroPy tree.
    """

    tree = dendropy_tree(
        newick
    )

    node1 = tree.find_node_with_taxon_label(
        taxon1
    )

    node2 = tree.find_node_with_taxon_label(
        taxon2
    )

    if node1 is None or node2 is None:
        raise ValueError(
            "Taxon not found in tree."
        )

    return tree.phylogenetic_distance(
        node1.taxon,
        node2.taxon
    )


# ==========================================================
# MSPRIME — ANCESTRY
# ==========================================================

def msprime_ancestry(
    samples=10,
    sequence_length=10_000,
    recombination_rate=1e-8,
    population_size=10_000,
    random_seed=None
):
    """
    Simulate ancestry using msprime.

    Returns a TreeSequence.
    """

    return msprime_simulate_ancestry(
        samples=samples,
        sequence_length=sequence_length,
        recombination_rate=recombination_rate,
        population_size=population_size,
        random_seed=random_seed
    )


# ==========================================================
# MSPRIME — MUTATIONS
# ==========================================================

def msprime_mutations(
    samples=10,
    sequence_length=10_000,
    recombination_rate=1e-8,
    mutation_rate=1e-8,
    population_size=10_000,
    random_seed=None
):
    """
    Simulate ancestry followed by mutations.
    """

    ts = msprime_simulate_ancestry(
        samples=samples,
        sequence_length=sequence_length,
        recombination_rate=recombination_rate,
        population_size=population_size,
        random_seed=random_seed
    )

    return msprime_simulate_mutations(
        ts,
        mutation_rate=mutation_rate,
        random_seed=random_seed
    )


# ==========================================================
# MOLECULAR DYNAMICS FEATURES
# ==========================================================


# ==========================================================
# MDANALYSIS — DISTANCE
# ==========================================================

def mdanalysis_distance(
    coordinates1,
    coordinates2
):
    """
    Calculate distances between corresponding
    atom coordinates using MDAnalysis.
    """

    import numpy as np
    from MDAnalysis.lib.distances import calc_bonds

    a = np.asarray(
        coordinates1,
        dtype=float
    )

    b = np.asarray(
        coordinates2,
        dtype=float
    )

    return calc_bonds(
        a,
        b
    )


# ==========================================================
# MDANALYSIS — DISTANCE MATRIX
# ==========================================================

def mdanalysis_distance_matrix(
    coordinates
):
    """
    Calculate the full pairwise distance matrix.
    """

    import numpy as np
    from MDAnalysis.lib.distances import distance_array

    coords = np.asarray(
        coordinates,
        dtype=float
    )

    return distance_array(
        coords,
        coords
    )


# ==========================================================
# MDTRAJ — RMSD
# ==========================================================

def mdtraj_rmsd(
    trajectory,
    reference=None
):
    """
    Calculate RMSD using MDTraj.

    trajectory may be an MDTraj Trajectory object.
    """

    import mdtraj as md

    if reference is None:
        reference = trajectory

    return md.rmsd(
        trajectory,
        reference
    )


# ==========================================================
# MDTRAJ — RADIUS OF GYRATION
# ==========================================================

def mdtraj_radius_of_gyration(
    trajectory
):
    """
    Calculate radius of gyration.
    """

    import mdtraj as md

    return md.compute_rg(
        trajectory
    )


# ==========================================================
# MDTRAJ — DISTANCES
# ==========================================================

def mdtraj_distances(
    trajectory,
    atom_pairs
):
    """
    Calculate distances between atom pairs.
    """

    import mdtraj as md

    return md.compute_distances(
        trajectory,
        atom_pairs
    )


# ==========================================================
# VISUALIZATION / IMAGE / DATA FEATURES
# ==========================================================


# ==========================================================
# MATPLOTLIB — PLOT
# ==========================================================

def matplotlib_plot(
    x,
    y,
    title=None,
    xlabel=None,
    ylabel=None,
    show=False
):
    """
    Create a Matplotlib line plot.

    Returns the Figure and Axes.
    """

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    ax.plot(
        x,
        y
    )

    if title is not None:
        ax.set_title(
            title
        )

    if xlabel is not None:
        ax.set_xlabel(
            xlabel
        )

    if ylabel is not None:
        ax.set_ylabel(
            ylabel
        )

    if show:
        plt.show()

    return fig, ax


# ==========================================================
# PLOTLY — INTERACTIVE PLOT
# ==========================================================

def plotly_plot(
    x,
    y,
    title=None
):
    """
    Create an interactive Plotly figure.
    """

    import plotly.graph_objects as go

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=list(x),
            y=list(y),
            mode="lines+markers"
        )
    )

    if title is not None:
        fig.update_layout(
            title=title
        )

    return fig


# ==========================================================
# ALTAIR — STATISTICAL CHART
# ==========================================================

def altair_chart(
    data,
    x,
    y,
    mark="line"
):
    """
    Create an Altair chart from tabular data.
    """

    import altair as alt

    chart = alt.Chart(
        data
    )

    if mark == "bar":
        chart = chart.mark_bar()

    elif mark == "point":
        chart = chart.mark_point()

    else:
        chart = chart.mark_line()

    return chart.encode(
        x=x,
        y=y
    )


# ==========================================================
# XARRAY — DATA ARRAY
# ==========================================================

def xarray_dataarray(
    data,
    dims=None,
    coords=None,
    name=None
):
    """
    Create an xarray DataArray.
    """

    import xarray as xr

    return xr.DataArray(
        data,
        dims=dims,
        coords=coords,
        name=name
    )


def xarray_dataset(
    variables
):
    """
    Create an xarray Dataset.

    variables should be a dictionary.
    """

    import xarray as xr

    return xr.Dataset(
        variables
    )


# ==========================================================
# ZARR — IN-MEMORY ARRAY
# ==========================================================

def zarr_array(
    data
):
    """
    Create a Zarr array in memory.
    """

    import zarr
    import numpy as np

    arr = np.asarray(
        data
    )

    return zarr.array(
        arr
    )


# ==========================================================
# H5PY — IN-MEMORY HDF5
# ==========================================================

def h5py_memory(
    data
):
    """
    Create an in-memory HDF5 dataset.

    Nothing is written to disk.
    """

    import io
    import h5py
    import numpy as np

    buffer = io.BytesIO()

    with h5py.File(
        buffer,
        "w"
    ) as file:

        file.create_dataset(
            "data",
            data=np.asarray(data)
        )

    return buffer.getvalue()


# ==========================================================
# NIBABEL — NIFTI IMAGE
# ==========================================================

def nibabel_image(
    data,
    affine=None
):
    """
    Create a NiBabel NIfTI image.
    """

    import numpy as np
    import nibabel as nib

    if affine is None:
        affine = np.eye(4)

    return nib.Nifti1Image(
        np.asarray(data),
        affine
    )


# ==========================================================
# PYWAVELETS — DISCRETE WAVELET TRANSFORM
# ==========================================================

def wavelet_decompose(
    data,
    wavelet="db1"
):
    """
    Perform a 1-D discrete wavelet transform.
    """

    import pywt

    return pywt.wavedec(
        data,
        wavelet
    )


def wavelet_reconstruct(
    coefficients,
    wavelet="db1"
):
    """
    Reconstruct a signal from wavelet coefficients.
    """

    import pywt

    return pywt.waverec(
        coefficients,
        wavelet
    )


# ==========================================================
# SCIKIT-IMAGE — IMAGE FILTER
# ==========================================================

def skimage_gaussian(
    image,
    sigma=1
):
    """
    Apply Gaussian smoothing.
    """

    from skimage.filters import gaussian

    return gaussian(
        image,
        sigma=sigma
    )


def skimage_edge_detection(
    image
):
    """
    Detect edges using the Canny algorithm.
    """

    from skimage.feature import canny

    return canny(
        image
    )


# ==========================================================
# TIFFFILE — READ TIFF
# ==========================================================

def read_tiff(
    filename
):
    """
    Read a TIFF image using tifffile.
    """

    import tifffile

    return tifffile.imread(
        filename
    )


def write_tiff(
    filename,
    data
):
    """
    Write an image to TIFF.
    """

    import tifffile

    tifffile.imwrite(
        filename,
        data
    )

    return filename


# ==========================================================
# DIPY — DIFFUSION TENSOR
# ==========================================================

def dipy_tensor_fit(
    data,
    gradients
):
    """
    Fit a diffusion tensor using DIPY.

    data:
        Diffusion-weighted measurements.

    gradients:
        DIPY GradientTable.
    """

    import numpy as np
    from dipy.reconst.dti import TensorModel

    model = TensorModel(
        gradients
    )

    return model.fit(
        np.asarray(data)
    )


# ==========================================================
# FOLIUM — MAP
# ==========================================================

def folium_map(
    latitude=0,
    longitude=0,
    zoom=2
):
    """
    Create an interactive Folium map.
    """

    import folium

    return folium.Map(
        location=[
            latitude,
            longitude
        ],
        zoom_start=zoom
    )


# ==========================================================
# YT — DATASET STATISTICS
# ==========================================================

def yt_load_dataset(
    filename
):
    """
    Load a dataset using yt.
    """

    import yt

    return yt.load(
        filename
    )


def yt_dataset_info(
    filename
):
    """
    Return basic information about a yt dataset.
    """

    ds = yt_load_dataset(
        filename
    )

    return {
        "dataset": ds,
        "domain_dimensions":
            ds.domain_dimensions,
        "domain_left_edge":
            ds.domain_left_edge,
        "domain_right_edge":
            ds.domain_right_edge,
        "current_time":
            ds.current_time,
    }

# ==========================================================
# DISTANCE
# ==========================================================

def astronomical_distance(
    value,
    unit="pc"
):
    """
    Create an astronomical distance quantity.

    Example:

        astronomical_distance(10, "pc")
    """

    u = _get_astropy_units()

    return value * u.Unit(unit)

# ==========================================================
# PARSEC / LIGHT YEAR CONVERSION
# ==========================================================

def parsec_to_lightyear(value):
    """
    Convert parsecs to light-years.
    """

    u = _get_astropy_units()

    return (
        value * u.pc
    ).to(
        u.lyr
    )


def lightyear_to_parsec(value):
    """
    Convert light-years to parsecs.
    """

    u = _get_astropy_units()

    return (
        value * u.lyr
    ).to(
        u.pc
    )


# ==========================================================
# AU CONVERSION
# ==========================================================

def au_to_km(value):
    """
    Convert astronomical units to kilometres.
    """

    u = _get_astropy_units()

    return (
        value * u.au
    ).to(
        u.km
    )


def km_to_au(value):
    """
    Convert kilometres to astronomical units.
    """

    u = _get_astropy_units()

    return (
        value * u.km
    ).to(
        u.au
    )


# ==========================================================
# EQUATORIAL → HORIZONTAL REPORT
# ==========================================================

def astronomical_observation_report(
    ra,
    dec,
    latitude,
    longitude,
    height=0,
    obstime=None,
    unit="deg"
):
    """
    Produce a complete observation-position report.
    """

    coordinates = _get_astropy_coordinates()

    target = skycoord(
        ra,
        dec,
        unit=unit
    )

    local = altaz(
        ra,
        dec,
        latitude,
        longitude,
        height,
        obstime,
        unit
    )

    galactic = target.galactic

    report = {

        "ICRS_RA": target.ra,

        "ICRS_DEC": target.dec,

        "Galactic_l": galactic.l,

        "Galactic_b": galactic.b,

        "Altitude": local["altitude"],

        "Azimuth": local["azimuth"],
    }

    print()
    print("=" * 80)
    print("DAVE — ASTRONOMICAL OBSERVATION REPORT")
    print("=" * 80)
    print()

    for key, value in report.items():

        print(
            f"{key:<20}: {value}"
        )

    print()

    return report


# ==========================================================
# HEALPIX
# ==========================================================

def _get_healpix():
    """
    Load astropy-healpix lazily.
    """

    return load_scientific_package(
        "astropy_healpix"
    )


def healpix_pixel(
    lon,
    lat,
    nside=16,
    order="ring",
    unit="deg"
):
    """
    Convert longitude/latitude to a HEALPix pixel number.
    """

    healpix_module = _get_healpix()

    u = _get_astropy_units()

    HEALPix = healpix_module.HEALPix

    hp = HEALPix(
        nside=nside,
        order=order,
        frame="icrs"
    )

    lon_quantity = lon * u.Unit(unit)
    lat_quantity = lat * u.Unit(unit)

    return hp.lonlat_to_healpix(
        lon_quantity,
        lat_quantity
    )


# ==========================================================
# HEALPIX PIXEL → COORDINATES
# ==========================================================

def healpix_coordinates(
    pixel,
    nside=16,
    order="ring"
):
    """
    Convert a HEALPix pixel number into sky coordinates.
    """

    healpix_module = _get_healpix()

    HEALPix = healpix_module.HEALPix

    hp = HEALPix(
        nside=nside,
        order=order,
        frame="icrs"
    )

    return hp.healpix_to_lonlat(
        pixel
    )


# ==========================================================
# HEALPIX NEIGHBORS
# ==========================================================

def healpix_neighbors(
    pixel,
    nside=16,
    order="ring"
):
    """
    Return neighboring HEALPix pixels.
    """

    healpix_module = _get_healpix()

    HEALPix = healpix_module.HEALPix

    hp = HEALPix(
        nside=nside,
        order=order,
        frame="icrs"
    )

    return hp.neighbours(
        pixel
    )


# ==========================================================
# HEALPIX PIXEL AREA
# ==========================================================

def healpix_pixel_area(
    nside=16
):
    """
    Return the area of one HEALPix pixel.
    """

    healpix_module = _get_healpix()

    HEALPix = healpix_module.HEALPix

    hp = HEALPix(
        nside=nside,
        order="ring"
    )

    return hp.pixel_area


# ==========================================================
# ERFA
# ==========================================================

def _get_erfa():
    """
    Load PyERFA through its Python import name.
    """

    return load_scientific_package(
        "pyerfa"
    )


def erfa_version():
    """
    Return the installed ERFA version.
    """

    erfa = _get_erfa()

    return getattr(
        erfa,
        "__version__",
        "unknown"
    )


# ==========================================================
# ASTRONOMY PACKAGE STATUS
# ==========================================================

def astronomy_package_status():
    """
    Check the astronomy packages currently available.
    """

    astronomy_packages = [

        "APLpy",
        "astroML",
        "astroplan",
        "astropy",
        "astropy_healpix",
        "astropy_iers_data",
        "astroquery",
        "jplephem",
        "poliastro",
        "pyerfa",
        "pyvo",
        "reproject",
        "sunpy",
    ]

    results = {}

    print()
    print("=" * 80)
    print("DAVE — ASTRONOMY PACKAGE STATUS")
    print("=" * 80)
    print()

    for package_name in astronomy_packages:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {

                "available": True,

                "version": str(version),
            }

            print(
                f"[OK]   {package_name:<24} "
                f"{version}"
            )

        except Exception as exc:

            results[package_name] = {

                "available": False,

                "version": None,

                "error": str(exc),
            }

            print(
                f"[--]   {package_name:<24} "
                f"UNAVAILABLE"
            )

    print()

    return results


# ==========================================================
# ASTRONOMY SELF TEST
# ==========================================================

def astronomy_selftest(
    verbose=True
):
    """
    Run safe tests of the astronomy integration.
    """

    tests = []

    # ------------------------------------------------------
    # ASTROPY
    # ------------------------------------------------------

    try:

        u = _get_astropy_units()

        q = (
            1 * u.au
        ).to(
            u.km
        )

        tests.append(
            (
                "AU conversion",
                q.value > 149000000
                and q.value < 150000000
            )
        )

    except Exception as exc:

        tests.append(
            (
                "AU conversion",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # COORDINATES
    # ------------------------------------------------------

    try:

        coord = skycoord(
            10.6847,
            41.2687
        )

        tests.append(
            (
                "SkyCoord",
                abs(coord.ra.deg - 10.6847)
                < 1e-8
            )
        )

    except Exception as exc:

        tests.append(
            (
                "SkyCoord",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # GALACTIC TRANSFORMATION
    # ------------------------------------------------------

    try:

        galactic = galactic_coordinates(
            10.6847,
            41.2687
        )

        tests.append(
            (
                "Galactic transformation",
                "l_deg" in galactic
                and "b_deg" in galactic
            )
        )

    except Exception as exc:

        tests.append(
            (
                "Galactic transformation",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # TIME
    # ------------------------------------------------------

    try:

        t = astro_time()

        tests.append(
            (
                "Astronomical time",
                hasattr(t, "jd")
            )
        )

    except Exception as exc:

        tests.append(
            (
                "Astronomical time",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # HEALPIX
    # ------------------------------------------------------

    if scientific_package_available(
        "astropy_healpix"
    ):

        try:

            pixel = healpix_pixel(
                0,
                0,
                nside=16
            )

            tests.append(
                (
                    "HEALPix",
                    pixel >= 0
                )
            )

        except Exception as exc:

            tests.append(
                (
                    "HEALPix",
                    False,
                    str(exc)
                )
            )

    else:

        tests.append(
            (
                "HEALPix",
                None,
                "astropy-healpix unavailable"
            )
        )


    # ======================================================
    # REPORT
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 70)
        print("DAVE — ASTRONOMY SELF TEST")
        print("=" * 70)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result is True:

            passed += 1

            if verbose:
                print(
                    f"[PASS] {name}"
                )

        elif result is False:

            failed += 1

            if verbose:
                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:
                    print(
                        f"       {test[2]}"
                    )

        else:

            failed += 1

            if verbose:
                print(
                    f"[FAIL] {name} (check could not run)"
                )

                if len(test) > 2:
                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 70)

        print(
            f"Passed : {passed}"
        )

        print(
            f"Failed : {failed}"
        )

        print("-" * 70)
        print()

    return {

        "passed": passed,

        "failed": failed,

        "total": len(tests),

    }


# ==========================================================
# ASTRONOMY HELP
# ==========================================================

def astronomy_help():

    print("""
==============================================================================
DAVE — ASTRONOMY
==============================================================================

PACKAGE STATUS
---------------

    astronomy_package_status()

    Check the astronomy packages available to Dave.


ASTRONOMICAL CONSTANTS
----------------------

    astro_constants()

    Display Astropy astronomical constants.


UNITS
-----

    astro_convert(value, from_unit, to_unit)

Examples:

    astro_convert(1, "au", "km")
    astro_convert(1, "pc", "lyr")
    astro_convert(180, "deg", "rad")


TIME
----

    astro_time()
    astro_time("2026-01-01")
    astro_time_report()

    julian_date()
    modified_julian_date()


COORDINATES
-----------

    skycoord(ra, dec)

    astro_coordinate("10h41m04.1s +41d16m09s")

    ra_dec(ra, dec)

    transform_coordinates(
        ra,
        dec,
        from_frame,
        to_frame
    )

    galactic_coordinates(ra, dec)

    galactic_to_icrs(l, b)


SKY GEOMETRY
------------

    angular_separation(
        ra1,
        dec1,
        ra2,
        dec2
    )

    position_angle(
        ra1,
        dec1,
        ra2,
        dec2
    )


OBSERVERS
---------

    earth_location(
        latitude,
        longitude,
        height
    )

    observatory("name")


OBSERVING
---------

    altaz(
        ra,
        dec,
        latitude,
        longitude
    )

    astronomical_observation_report(
        ra,
        dec,
        latitude,
        longitude
    )


DISTANCES
---------

    astronomical_distance(value, unit)

    parsec_to_lightyear(value)

    lightyear_to_parsec(value)

    au_to_km(value)

    km_to_au(value)


HEALPIX
-------

    healpix_pixel(
        lon,
        lat,
        nside
    )

    healpix_coordinates(
        pixel,
        nside
    )

    healpix_neighbors(
        pixel,
        nside
    )

    healpix_pixel_area(
        nside
    )


ERFA
----

    erfa_version()


TESTING
-------

    astronomy_selftest()


EXAMPLES
--------

    astro_constants()

    astro_time_report()

    ra_dec(
        10.6847,
        41.2687
    )

    galactic_coordinates(
        10.6847,
        41.2687
    )

    angular_separation(
        10.6847,
        41.2687,
        83.8221,
        -5.3911
    )

    astronomy_package_status()

    astronomy_selftest()

==============================================================================
""")


# ==========================================================
# DAVE
# ASTRONOMY INTEGRATION
# PART 2 — QUERIES, OBSERVING, ORBITS, VO & SOLAR PHYSICS
# ==========================================================
#
# Packages covered:
#
#   astroquery
#   astroplan
#   jplephem
#   poliastro
#   pyvo
#   sunpy
#
# This section builds on Astronomy Part 1.
#
# ==========================================================


# ==========================================================
# ASTROQUERY LOADER
# ==========================================================

def _get_astroquery():
    """
    Load astroquery lazily.
    """

    return load_scientific_package("astroquery")


# ==========================================================
# ASTROPLAN LOADER
# ==========================================================

def _get_astroplan():
    """
    Load astroplan lazily.
    """

    return load_scientific_package("astroplan")


# ==========================================================
# PYVO LOADER
# ==========================================================

def _get_pyvo():
    """
    Load PyVO lazily.
    """

    return load_scientific_package("pyvo")


# ==========================================================
# SUNPY LOADER
# ==========================================================

def _get_sunpy():
    """
    Load SunPy lazily.
    """

    return load_scientific_package("sunpy")


# ==========================================================
# JPLEPHEM LOADER
# ==========================================================

def _get_jplephem():
    """
    Load jplephem lazily.
    """

    return load_scientific_package("jplephem")


# ==========================================================
# POLIASTRO LOADER
# ==========================================================

def _get_poliastro():
    """
    Load poliastro lazily.
    """

    return load_scientific_package("poliastro")


# ==========================================================
# ASTROQUERY — SIMBAD
# ==========================================================

def simbad_query(
    object_name,
    get_all=False
):
    """
    Query SIMBAD for an astronomical object.

    Example:

        simbad_query("M31")

        simbad_query("Betelgeuse")
    """

    try:

        from astroquery.simbad import Simbad

    except Exception as exc:

        raise ImportError(
            "SIMBAD functionality requires astroquery."
        ) from exc

    custom_simbad = Simbad()

    if get_all:

        return custom_simbad.query_object(
            object_name
        )

    return custom_simbad.query_object(
        object_name
    )


# ==========================================================
# SIMBAD COORDINATE QUERY
# ==========================================================

def simbad_coordinates(
    object_name
):
    """
    Query SIMBAD and return the object's coordinates.
    """

    result = simbad_query(
        object_name
    )

    if result is None:

        return None

    row = result[0]

    return {
        "object": object_name,
        "ra": row["ra"],
        "dec": row["dec"],
    }


# ==========================================================
# SIMBAD REPORT
# ==========================================================

def simbad_report(
    object_name
):
    """
    Display a compact SIMBAD report.
    """

    result = simbad_query(
        object_name
    )

    print()
    print("=" * 80)
    print("DAVE — SIMBAD QUERY")
    print("=" * 80)
    print()

    if result is None:

        print(
            f"No SIMBAD result for {object_name}."
        )

        print()

        return None

    row = result[0]

    print(
        f"Object: {object_name}"
    )

    print()

    for column in result.colnames:

        try:

            value = row[column]

        except Exception:

            continue

        print(
            f"{column:<24}: {value}"
        )

    print()

    return result


# ==========================================================
# ASTROQUERY — NASA EXOPLANET ARCHIVE
# ==========================================================

def exoplanet_query(
    planet_name
):
    """
    Query the NASA Exoplanet Archive through astroquery.

    Example:

        exoplanet_query("Kepler-22 b")
    """

    try:

        from astroquery.ipac.nexsci.nasa_exoplanet_archive \
            import NasaExoplanetArchive

    except Exception as exc:

        raise ImportError(
            "NASA Exoplanet Archive functionality "
            "requires astroquery."
        ) from exc

    return NasaExoplanetArchive.query_object(
        planet_name,
        table="pscomppars"
    )


# ==========================================================
# EXOPLANET REPORT
# ==========================================================

def exoplanet_report(
    planet_name
):
    """
    Display a compact exoplanet query result.
    """

    result = exoplanet_query(
        planet_name
    )

    print()
    print("=" * 80)
    print("DAVE — EXOPLANET QUERY")
    print("=" * 80)
    print()

    if result is None or len(result) == 0:

        print(
            f"No result found for {planet_name}."
        )

        print()

        return None

    row = result[0]

    for column in result.colnames:

        try:

            value = row[column]

        except Exception:

            continue

        print(
            f"{column:<28}: {value}"
        )

    print()

    return result


# ==========================================================
# ASTROQUERY — VIZIER
# ==========================================================

def vizier_query(
    ra,
    dec,
    radius=5,
    radius_unit="arcmin"
):
    """
    Search VizieR around a sky position.

    Parameters:

        ra
            Right ascension in degrees.

        dec
            Declination in degrees.

        radius
            Search radius.

        radius_unit
            astropy-compatible angular unit.
    """

    try:

        from astroquery.vizier import Vizier

    except Exception as exc:

        raise ImportError(
            "VizieR functionality requires astroquery."
        ) from exc

    from astropy.coordinates import SkyCoord
    import astropy.units as u

    position = SkyCoord(
        ra=ra,
        dec=dec,
        unit="deg"
    )

    vizier = Vizier(
        columns=["*"]
    )

    return vizier.query_region(
        position,
        radius=radius * u.Unit(radius_unit)
    )


# ==========================================================
# ASTROQUERY — NED
# ==========================================================

def ned_query(
    object_name
):
    """
    Query the NASA/IPAC Extragalactic Database.
    """

    try:

        from astroquery.ipac.ned import Ned

    except Exception as exc:

        raise ImportError(
            "NED functionality requires astroquery."
        ) from exc

    return Ned.query_object(
        object_name
    )


# ==========================================================
# ASTROQUERY — IRSA
# ==========================================================

def irsa_query(
    ra,
    dec,
    radius=5,
    radius_unit="arcmin"
):
    """
    Query IRSA around a sky position.
    """

    try:

        from astroquery.ipac.irsa import Irsa

    except Exception as exc:

        raise ImportError(
            "IRSA functionality requires astroquery."
        ) from exc

    from astropy.coordinates import SkyCoord
    import astropy.units as u

    position = SkyCoord(
        ra=ra,
        dec=dec,
        unit="deg"
    )

    return Irsa.query_region(
        position,
        radius=radius * u.Unit(radius_unit)
    )


# ==========================================================
# ASTROQUERY — GAIA
# ==========================================================

def gaia_query(
    ra,
    dec,
    radius=5,
    radius_unit="arcsec"
):
    """
    Perform a Gaia cone search.
    """

    try:

        from astroquery.gaia import Gaia

    except Exception as exc:

        raise ImportError(
            "Gaia functionality requires astroquery."
        ) from exc

    from astropy.coordinates import SkyCoord
    import astropy.units as u

    position = SkyCoord(
        ra=ra,
        dec=dec,
        unit="deg"
    )

    job = Gaia.cone_search_async(
        position,
        radius=radius * u.Unit(radius_unit)
    )

    return job.get_results()


# ==========================================================
# ASTROQUERY — SDSS
# ==========================================================

def sdss_query(
    ra,
    dec,
    radius=5,
    radius_unit="arcsec"
):
    """
    Search SDSS around a sky position.
    """

    try:

        from astroquery.sdss import SDSS

    except Exception as exc:

        raise ImportError(
            "SDSS functionality requires astroquery."
        ) from exc

    from astropy.coordinates import SkyCoord
    import astropy.units as u

    position = SkyCoord(
        ra=ra,
        dec=dec,
        unit="deg"
    )

    return SDSS.query_region(
        position,
        radius=radius * u.Unit(radius_unit)
    )


# ==========================================================
# ASTROQUERY — DATASET DISCOVERY
# ==========================================================

def astronomy_database_search(
    object_name
):
    """
    Query several astronomy databases where practical.

    This function intentionally keeps each database query
    independent so that failure of one service does not
    prevent the others from being queried.
    """

    results = {}

    # SIMBAD
    try:

        results["SIMBAD"] = simbad_query(
            object_name
        )

    except Exception as exc:

        results["SIMBAD"] = (
            f"ERROR: {exc}"
        )

    # NED
    try:

        results["NED"] = ned_query(
            object_name
        )

    except Exception as exc:

        results["NED"] = (
            f"ERROR: {exc}"
        )

    print()
    print("=" * 80)
    print(
        f"DAVE — DATABASE SEARCH: {object_name}"
    )
    print("=" * 80)
    print()

    for database, result in results.items():

        if isinstance(result, str):

            print(
                f"{database:<12}: {result}"
            )

        elif result is None:

            print(
                f"{database:<12}: No result"
            )

        else:

            try:

                print(
                    f"{database:<12}: "
                    f"{len(result)} result(s)"
                )

            except Exception:

                print(
                    f"{database:<12}: Result received"
                )

    print()

    return results


# ==========================================================
# ASTROPLAN — OBSERVER
# ==========================================================

def create_observer(
    latitude,
    longitude,
    elevation=0,
    name="Dave Observatory"
):
    """
    Create an astroplan Observer.
    """

    try:

        from astroplan import Observer

    except Exception as exc:

        raise ImportError(
            "astroplan is required for observer calculations."
        ) from exc

    import astropy.units as u

    return Observer(
        latitude=latitude * u.deg,
        longitude=longitude * u.deg,
        elevation=elevation * u.m,
        name=name
    )


# ==========================================================
# ASTROPLAN — TARGET
# ==========================================================

def create_target(
    ra,
    dec,
    name="Target"
):
    """
    Create an astroplan FixedTarget.
    """

    try:

        from astroplan import FixedTarget

    except Exception as exc:

        raise ImportError(
            "astroplan is required for target calculations."
        ) from exc

    from astropy.coordinates import SkyCoord

    return FixedTarget(
        coord=SkyCoord(
            ra=ra,
            dec=dec,
            unit="deg"
        ),
        name=name
    )


# ==========================================================
# TARGET ALTITUDE
# ==========================================================

def target_altitude(
    ra,
    dec,
    latitude,
    longitude,
    elevation=0,
    obstime=None
):
    """
    Calculate target altitude for an observer.
    """

    try:

        from astroplan import Observer

    except Exception as exc:

        raise ImportError(
            "astroplan is required."
        ) from exc

    from astropy.time import Time

    observer = create_observer(
        latitude,
        longitude,
        elevation
    )

    target = create_target(
        ra,
        dec
    )

    if obstime is None:

        obstime = Time.now()

    elif not isinstance(obstime, Time):

        obstime = Time(
            obstime
        )

    return observer.altaz(
        obstime,
        target
    )


# ==========================================================
# TARGET AZIMUTH
# ==========================================================

def target_azimuth(
    ra,
    dec,
    latitude,
    longitude,
    elevation=0,
    obstime=None
):
    """
    Calculate target azimuth for an observer.
    """

    result = target_altitude(
        ra,
        dec,
        latitude,
        longitude,
        elevation,
        obstime
    )

    return result.az


# ==========================================================
# TARGET IS UP
# ==========================================================

def target_is_up(
    ra,
    dec,
    latitude,
    longitude,
    elevation=0,
    obstime=None
):
    """
    Determine whether a target is above the horizon.
    """

    from astropy.time import Time

    observer = create_observer(
        latitude,
        longitude,
        elevation
    )

    target = create_target(
        ra,
        dec
    )

    if obstime is None:

        obstime = Time.now()

    elif not isinstance(obstime, Time):

        obstime = Time(
            obstime
        )

    return bool(
        observer.target_is_up(
            obstime,
            target
        )
    )


# ==========================================================
# TARGET RISE TIME
# ==========================================================

def target_rise_time(
    ra,
    dec,
    latitude,
    longitude,
    elevation=0,
    date=None
):
    """
    Calculate the next target rise time.
    """

    from astropy.time import Time

    observer = create_observer(
        latitude,
        longitude,
        elevation
    )

    target = create_target(
        ra,
        dec
    )

    if date is None:

        date = Time.now()

    elif not isinstance(date, Time):

        date = Time(
            date
        )

    return observer.target_rising(
        date,
        target
    )


# ==========================================================
# TARGET SET TIME
# ==========================================================

def target_set_time(
    ra,
    dec,
    latitude,
    longitude,
    elevation=0,
    date=None
):
    """
    Calculate the next target setting time.
    """

    from astropy.time import Time

    observer = create_observer(
        latitude,
        longitude,
        elevation
    )

    target = create_target(
        ra,
        dec
    )

    if date is None:

        date = Time.now()

    elif not isinstance(date, Time):

        date = Time(
            date
        )

    return observer.target_setting(
        date,
        target
    )


# ==========================================================
# ASTRONOMICAL TWILIGHT
# ==========================================================

def twilight_times(
    latitude,
    longitude,
    elevation=0,
    date=None
):
    """
    Calculate astronomical, nautical and civil twilight
    transitions around a date.
    """

    from astropy.time import Time

    observer = create_observer(
        latitude,
        longitude,
        elevation
    )

    if date is None:

        date = Time.now()

    elif not isinstance(date, Time):

        date = Time(
            date
        )

    result = {

        "astronomical_dawn":
            observer.twilight_morning_astronomical(date),

        "nautical_dawn":
            observer.twilight_morning_nautical(date),

        "civil_dawn":
            observer.twilight_morning_civil(date),

        "civil_dusk":
            observer.twilight_evening_civil(date),

        "nautical_dusk":
            observer.twilight_evening_nautical(date),

        "astronomical_dusk":
            observer.twilight_evening_astronomical(date),
    }

    return result


# ==========================================================
# JPLEPHEM — VERSION / BASIC ACCESS
# ==========================================================

def jplephem_version():
    """
    Return the installed jplephem version.
    """

    module = _get_jplephem()

    return getattr(
        module,
        "__version__",
        "unknown"
    )


# ==========================================================
# JPLEPHEM — SPK FILE
# ==========================================================

def load_spk_kernel(
    filename
):
    """
    Open a JPL SPK ephemeris kernel.

    The filename must point to an SPK kernel already
    available on the local machine.
    """

    try:

        from jplephem.spk import SPK

    except Exception as exc:

        raise ImportError(
            "jplephem is required."
        ) from exc

    return SPK.open(
        filename
    )


# ==========================================================
# JPLEPHEM — SPK POSITION
# ==========================================================

def spk_position(
    filename,
    target,
    center,
    jd
):
    """
    Calculate a position from a local JPL SPK kernel.

    Parameters:

        filename
            Path to the SPK file.

        target
            Target NAIF body ID.

        center
            Center NAIF body ID.

        jd
            Julian date.
    """

    kernel = load_spk_kernel(
        filename
    )

    segment = kernel[
        target,
        center
    ]

    return segment.compute(
        jd
    )


# ==========================================================
# POLIASTRO — ORBIT LOADER
# ==========================================================

def _poliastro_orbit():
    """
    Load poliastro Orbit.
    """

    try:

        from poliastro.twobody import Orbit

        return Orbit

    except Exception as exc:

        raise ImportError(
            "poliastro orbital mechanics is unavailable "
            "in the installed version."
        ) from exc


# ==========================================================
# POLIASTRO — TWO BODY ORBIT FROM CLASSICAL ELEMENTS
# ==========================================================

def orbit_from_classical(
    attractor_mu,
    semi_major_axis,
    eccentricity,
    inclination,
    raan,
    argp,
    true_anomaly,
    distance_unit="km",
    angle_unit="deg"
):
    """
    Create a two-body orbit from classical orbital elements.

    attractor_mu
        Gravitational parameter in km^3 / s^2.

    semi_major_axis
        Semi-major axis.

    eccentricity
        Orbital eccentricity.

    inclination
        Inclination.

    raan
        Right ascension of ascending node.

    argp
        Argument of periapsis.

    true_anomaly
        True anomaly.
    """

    try:

        from astropy import units as u
        from astropy.constants import G

        from poliastro.bodies import Body
        from poliastro.twobody import Orbit

    except Exception as exc:

        raise ImportError(
            "poliastro is required for orbital mechanics."
        ) from exc

    # Construct a custom central body.
    #
    # mu is expected in km^3/s^2.

    body = Body.from_parameters(
        name="Custom Attractor",
        symbol="X",
        parent=None,
        mu=attractor_mu * u.km**3 / u.s**2
    )

    return Orbit.from_classical(
        body,
        semi_major_axis * u.Unit(distance_unit),
        eccentricity * u.one,
        inclination * u.Unit(angle_unit),
        raan * u.Unit(angle_unit),
        argp * u.Unit(angle_unit),
        true_anomaly * u.Unit(angle_unit)
    )


# ==========================================================
# POLIASTRO — POSITION / VELOCITY
# ==========================================================

def orbit_state_vectors(
    orbit
):
    """
    Return position and velocity vectors from a poliastro
    Orbit object.
    """

    r = orbit.r
    v = orbit.v

    return {
        "position": r,
        "velocity": v,
    }


# ==========================================================
# POLIASTRO — ORBIT PERIOD
# ==========================================================

def orbit_period(
    orbit
):
    """
    Return the orbital period.
    """

    return orbit.period


# ==========================================================
# POLIASTRO — APOAPSIS / PERIAPSIS
# ==========================================================

def orbit_extrema(
    orbit
):
    """
    Return periapsis and apoapsis distances.
    """

    return {

        "periapsis": orbit.r_p,

        "apoapsis": orbit.r_a,
    }


# ==========================================================
# POLIASTRO — PROPAGATE ORBIT
# ==========================================================

def propagate_orbit(
    orbit,
    time_seconds
):
    """
    Propagate an orbit forward by a number of seconds.
    """

    from astropy import units as u

    return orbit.propagate(
        time_seconds * u.s
    )


# ==========================================================
# PYVO — SERVICE DISCOVERY
# ==========================================================

def vo_service(
    url
):
    """
    Connect to a Virtual Observatory service.
    """

    pyvo = _get_pyvo()

    return pyvo.dal.adhoc.DatalinkResults


# ==========================================================
# PYVO — TAP SERVICE
# ==========================================================

def tap_service(
    url
):
    """
    Connect to a TAP (Table Access Protocol) service.
    """

    pyvo = _get_pyvo()

    return pyvo.dal.TAPService(
        url
    )


# ==========================================================
# PYVO — TAP QUERY
# ==========================================================

def tap_query(
    url,
    query,
    language="ADQL"
):
    """
    Execute an ADQL query against a TAP service.

    Example query:

        SELECT TOP 10 *
        FROM gaiadr3.gaia_source
    """

    service = tap_service(
        url
    )

    return service.search(
        query,
        language=language
    )


# ==========================================================
# PYVO — SIMPLE CONE SEARCH
# ==========================================================

def vo_cone_search(
    url,
    ra,
    dec,
    radius
):
    """
    Perform a Simple Cone Search against a VO service.
    """

    pyvo = _get_pyvo()

    service = pyvo.dal.SCSService(
        url
    )

    return service.search(
        pos=(ra, dec),
        radius=radius
    )


# ==========================================================
# SUNPY LOADER
# ==========================================================

def _get_sunpy_map():
    """
    Import sunpy.map lazily.
    """

    _get_sunpy()

    from sunpy import map

    return map


# ==========================================================
# SUNPY — MAP FROM FILE
# ==========================================================

def solar_map(
    filename
):
    """
    Load a solar map from a supported SunPy file.
    """

    solar_map_module = _get_sunpy_map()

    return solar_map_module.Map(
        filename
    )


# ==========================================================
# SUNPY — MAP INFORMATION
# ==========================================================

def solar_map_info(
    filename
):
    """
    Return basic metadata from a SunPy solar map.
    """

    smap = solar_map(
        filename
    )

    return {

        "observatory":
            smap.observatory,

        "instrument":
            smap.instrument,

        "measurement":
            smap.measurement,

        "date":
            smap.date,

        "dimensions":
            smap.dimensions,

        "scale":
            smap.scale,

        "units":
            smap.unit,

    }


# ==========================================================
# SUNPY — MAP PLOT
# ==========================================================

def solar_map_plot(
    filename
):
    """
    Plot a SunPy solar map.
    """

    smap = solar_map(
        filename
    )

    import matplotlib.pyplot as plt

    fig = plt.figure()

    ax = fig.add_subplot(
        projection=smap
    )

    smap.plot(
        axes=ax
    )

    ax.set_title(
        "Dave — Solar Map"
    )

    plt.show()

    return fig


# ==========================================================
# SUNPY — MAP DATA RANGE
# ==========================================================

def solar_map_statistics(
    filename
):
    """
    Calculate basic statistics for a solar map.
    """

    smap = solar_map(
        filename
    )

    data = smap.data

    import numpy as np

    finite = data[
        np.isfinite(data)
    ]

    if finite.size == 0:

        return {
            "count": 0
        }

    return {

        "count": int(finite.size),

        "minimum": float(
            np.min(finite)
        ),

        "maximum": float(
            np.max(finite)
        ),

        "mean": float(
            np.mean(finite)
        ),

        "median": float(
            np.median(finite)
        ),

        "standard_deviation": float(
            np.std(finite)
        ),
    }


# ==========================================================
# SUNPY — SOLAR COORDINATES
# ==========================================================

def solar_coordinate(
    x,
    y,
    observer,
    obstime,
    frame="helioprojective"
):
    """
    Create a SunPy-compatible solar coordinate.

    x and y are normally supplied in arcseconds for
    helioprojective coordinates.
    """

    _get_sunpy()

    import astropy.units as u
    from astropy.coordinates import SkyCoord

    return SkyCoord(
        x=x * u.arcsec,
        y=y * u.arcsec,
        frame=frame,
        obstime=obstime,
        observer=observer
    )


# ==========================================================
# SUNPY — SOLAR PHYSICS PACKAGE STATUS
# ==========================================================

def solar_package_status():
    """
    Check SunPy and its directly associated astronomy
    packages.
    """

    packages_to_check = [

        "sunpy",

        "astropy",

        "astropy_healpix",

        "astropy_iers_data",

        "pyerfa",

    ]

    results = {}

    print()
    print("=" * 70)
    print("DAVE — SOLAR / ASTROPHYSICS STATUS")
    print("=" * 70)
    print()

    for name in packages_to_check:

        try:

            module = load_scientific_package(
                name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[name] = {

                "available": True,

                "version": str(version),
            }

            print(
                f"[OK] {name:<25} {version}"
            )

        except Exception as exc:

            results[name] = {

                "available": False,

                "error": str(exc),
            }

            print(
                f"[--] {name:<25} unavailable"
            )

    print()

    return results


# ==========================================================
# ASTRONOMY PART 2 SELF TEST
# ==========================================================

def astronomy_part2_selftest(
    verbose=True
):
    """
    Test the Part 2 astronomy integrations.

    Network-dependent services are not automatically queried.
    """

    tests = []


    # ------------------------------------------------------
    # ASTROPLAN
    # ------------------------------------------------------

    try:

        observer = create_observer(
            40.7128,
            -74.0060,
            name="Dave Test Observatory"
        )

        target = create_target(
            10.6847,
            41.2687,
            name="M31"
        )

        from astropy.time import Time

        result = observer.altaz(
            Time.now(),
            target
        )

        tests.append(
            (
                "astroplan observer",
                hasattr(result, "alt")
            )
        )

    except Exception as exc:

        tests.append(
            (
                "astroplan observer",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # JPLEPHEM
    # ------------------------------------------------------

    try:

        version = jplephem_version()

        tests.append(
            (
                "jplephem",
                version != "unknown"
            )
        )

    except Exception as exc:

        tests.append(
            (
                "jplephem",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PYVO
    # ------------------------------------------------------

    try:

        module = _get_pyvo()

        tests.append(
            (
                "PyVO",
                module is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "PyVO",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # SUNPY
    # ------------------------------------------------------

    try:

        module = _get_sunpy()

        tests.append(
            (
                "SunPy",
                module is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "SunPy",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # POLIASTRO
    # ------------------------------------------------------

    try:

        module = _get_poliastro()

        tests.append(
            (
                "poliastro",
                module is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "poliastro",
                False,
                str(exc)
            )
        )


    # ======================================================
    # REPORT
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 70)
        print("DAVE — ASTRONOMY PART 2 SELF TEST")
        print("=" * 70)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 70)

        print(
            f"Passed: {passed}"
        )

        print(
            f"Failed: {failed}"
        )

        print("-" * 70)
        print()

    return {

        "passed": passed,

        "failed": failed,

        "total": len(tests),
    }


# ==========================================================
# ASTRONOMY PART 2 HELP
# ==========================================================

def astronomy_part2_help():

    print("""
==============================================================================
DAVE — ASTRONOMY PART 2
==============================================================================

ASTROQUERY
----------

    simbad_query("M31")
    simbad_coordinates("M31")
    simbad_report("M31")

    exoplanet_query("Kepler-22 b")
    exoplanet_report("Kepler-22 b")

    vizier_query(ra, dec)
    ned_query("M31")
    irsa_query(ra, dec)
    gaia_query(ra, dec)
    sdss_query(ra, dec)

    astronomy_database_search("M31")


ASTROPLAN
---------

    create_observer(
        latitude,
        longitude,
        elevation
    )

    create_target(
        ra,
        dec,
        name
    )

    target_altitude(
        ra,
        dec,
        latitude,
        longitude
    )

    target_azimuth(
        ra,
        dec,
        latitude,
        longitude
    )

    target_is_up(
        ra,
        dec,
        latitude,
        longitude
    )

    target_rise_time(
        ra,
        dec,
        latitude,
        longitude
    )

    target_set_time(
        ra,
        dec,
        latitude,
        longitude
    )

    twilight_times(
        latitude,
        longitude
    )


JPLEPHEM
--------

    jplephem_version()

    load_spk_kernel(
        "kernel.bsp"
    )

    spk_position(
        "kernel.bsp",
        target,
        center,
        jd
    )


POLIASTRO
---------

    orbit_from_classical(
        attractor_mu,
        semi_major_axis,
        eccentricity,
        inclination,
        raan,
        argp,
        true_anomaly
    )

    orbit_state_vectors(
        orbit
    )

    orbit_period(
        orbit
    )

    orbit_extrema(
        orbit
    )

    propagate_orbit(
        orbit,
        time_seconds
    )


PYVO
----

    tap_service(
        url
    )

    tap_query(
        url,
        query
    )

    vo_cone_search(
        url,
        ra,
        dec,
        radius
    )


SUNPY
-----

    solar_map(
        "solar_file.fits"
    )

    solar_map_info(
        "solar_file.fits"
    )

    solar_map_plot(
        "solar_file.fits"
    )

    solar_map_statistics(
        "solar_file.fits"
    )

    solar_coordinate(
        x,
        y,
        observer,
        obstime
    )

    solar_package_status()


TESTING
-------

    astronomy_part2_selftest()


IMPORTANT
---------

Network-based functions such as SIMBAD, Gaia, VizieR,
NED, IRSA, SDSS and online Virtual Observatory services
require network access and may depend on the external
service being available.

Local ephemeris and solar-data functions can operate on
files already stored on the computer.

==============================================================================
""")

# ==========================================================
# DAVE
# BIOLOGY / BIOINFORMATICS INTEGRATION
# PART 1
# ==========================================================
#
# Packages covered:
#
#   anndata
#   biom-format
#   biopython
#   bioregistry
#   biotite
#
# ==========================================================


# ==========================================================
# BIOLOGY PACKAGE LOADERS
# ==========================================================

def _get_anndata():
    """
    Load AnnData lazily.
    """

    return load_scientific_package("anndata")


def _get_biom():
    """
    Load biom-format lazily.
    """

    return load_scientific_package("biom-format")


def _get_biopython():
    """
    Load Biopython lazily.
    """

    return load_scientific_package("biopython")


def _get_bioregistry():
    """
    Load Bioregistry lazily.
    """

    return load_scientific_package("bioregistry")


def _get_biotite():
    """
    Load Biotite lazily.
    """

    return load_scientific_package("biotite")


# ==========================================================
# ANNDATA
# ==========================================================

def create_anndata(
    X,
    obs=None,
    var=None,
    uns=None,
    obsm=None,
    varm=None
):
    """
    Create an AnnData object.

    X
        Main observation-by-variable data matrix.

    obs
        Observation metadata.

    var
        Variable metadata.

    uns
        Unstructured metadata.

    obsm
        Multi-dimensional observation annotations.

    varm
        Multi-dimensional variable annotations.
    """

    module = _get_anndata()

    return module.AnnData(
        X=X,
        obs=obs,
        var=var,
        uns=uns,
        obsm=obsm,
        varm=varm
    )


# ==========================================================
# ANNDATA — BASIC INFORMATION
# ==========================================================

def anndata_info(
    data
):
    """
    Return basic information about an AnnData object.
    """

    return {
        "shape": tuple(data.shape),

        "n_observations":
            int(data.n_obs),

        "n_variables":
            int(data.n_vars),

        "observation_columns":
            list(data.obs.columns),

        "variable_columns":
            list(data.var.columns),

        "obsm_keys":
            list(data.obsm.keys()),

        "varm_keys":
            list(data.varm.keys()),

        "uns_keys":
            list(data.uns.keys()),
    }


# ==========================================================
# ANNDATA — OBSERVATIONS
# ==========================================================

def anndata_observations(
    data
):
    """
    Return observation metadata.
    """

    return data.obs


# ==========================================================
# ANNDATA — VARIABLES
# ==========================================================

def anndata_variables(
    data
):
    """
    Return variable metadata.
    """

    return data.var


# ==========================================================
# ANNDATA — ADD OBSERVATION COLUMN
# ==========================================================

def anndata_add_observation_column(
    data,
    name,
    values
):
    """
    Add metadata to observations.
    """

    data.obs[name] = values

    return data


# ==========================================================
# ANNDATA — ADD VARIABLE COLUMN
# ==========================================================

def anndata_add_variable_column(
    data,
    name,
    values
):
    """
    Add metadata to variables.
    """

    data.var[name] = values

    return data


# ==========================================================
# ANNDATA — SLICE
# ==========================================================

def anndata_slice(
    data,
    observations=None,
    variables=None
):
    """
    Slice an AnnData object.

    observations
        Observation indices, boolean mask, or labels.

    variables
        Variable indices, boolean mask, or labels.
    """

    if observations is None:

        observations = slice(None)

    if variables is None:

        variables = slice(None)

    return data[
        observations,
        variables
    ].copy()


# ==========================================================
# ANNDATA — COPY
# ==========================================================

def anndata_copy(
    data
):
    """
    Make an independent AnnData copy.
    """

    return data.copy()


# ==========================================================
# ANNDATA — CONCATENATE
# ==========================================================

def anndata_concat(
    datasets,
    axis=0,
    join="outer",
    label=None,
    keys=None,
    index_unique=None
):
    """
    Concatenate multiple AnnData objects.
    """

    module = _get_anndata()

    return module.concat(
        datasets,
        axis=axis,
        join=join,
        label=label,
        keys=keys,
        index_unique=index_unique
    )


# ==========================================================
# ANNDATA — READ
# ==========================================================

def read_anndata(
    filename
):
    """
    Read an AnnData file.

    Supports formats handled by AnnData, such as .h5ad.
    """

    module = _get_anndata()

    return module.read_h5ad(
        filename
    )


# ==========================================================
# ANNDATA — WRITE
# ==========================================================

def write_anndata(
    data,
    filename
):
    """
    Write an AnnData object to an H5AD file.
    """

    data.write_h5ad(
        filename
    )

    return filename


# ==========================================================
# ANNDATA — NORMALIZATION
# ==========================================================

def anndata_normalize_total(
    data,
    target_sum=None,
    inplace=True
):
    """
    Normalize observations to a common total.

    This uses Scanpy when available.
    """

    scanpy = load_scientific_package(
        "scanpy"
    )

    return scanpy.pp.normalize_total(
        data,
        target_sum=target_sum,
        inplace=inplace
    )


# ==========================================================
# BIOM-FORMAT
# ==========================================================

def create_biom_table(
    data,
    observation_ids=None,
    sample_ids=None,
    observation_metadata=None,
    sample_metadata=None
):
    """
    Create a BIOM table.
    """

    module = _get_biom()

    return module.Table(
        data,
        observation_ids=observation_ids,
        sample_ids=sample_ids,
        observation_metadata=observation_metadata,
        sample_metadata=sample_metadata
    )


# ==========================================================
# BIOM — TABLE INFORMATION
# ==========================================================

def biom_table_info(
    table
):
    """
    Return basic information about a BIOM table.
    """

    return {
        "shape": table.shape,

        "observations":
            list(table.ids(axis="observation")),

        "samples":
            list(table.ids(axis="sample")),

        "nnz":
            int(table.nnz),
    }


# ==========================================================
# BIOM — SAMPLE IDS
# ==========================================================

def biom_sample_ids(
    table
):
    """
    Return sample IDs from a BIOM table.
    """

    return list(
        table.ids(
            axis="sample"
        )
    )


# ==========================================================
# BIOM — OBSERVATION IDS
# ==========================================================

def biom_observation_ids(
    table
):
    """
    Return observation IDs from a BIOM table.
    """

    return list(
        table.ids(
            axis="observation"
        )
    )


# ==========================================================
# BIOM — SAMPLE SUMS
# ==========================================================

def biom_sample_sums(
    table
):
    """
    Calculate total abundance for every sample.
    """

    return table.sum(
        axis="sample"
    )


# ==========================================================
# BIOM — OBSERVATION SUMS
# ==========================================================

def biom_observation_sums(
    table
):
    """
    Calculate total abundance for every observation.
    """

    return table.sum(
        axis="observation"
    )


# ==========================================================
# BIOM — FILTER SAMPLES
# ==========================================================

def biom_filter_samples(
    table,
    min_count=1
):
    """
    Keep samples having at least min_count total counts.
    """

    return table.filter(
        lambda values, id_, md:
        sum(values) >= min_count,
        axis="sample"
    )


# ==========================================================
# BIOM — FILTER OBSERVATIONS
# ==========================================================

def biom_filter_observations(
    table,
    min_count=1
):
    """
    Keep observations having at least min_count total counts.
    """

    return table.filter(
        lambda values, id_, md:
        sum(values) >= min_count,
        axis="observation"
    )


# ==========================================================
# BIOM — EXPORT JSON
# ==========================================================

def biom_to_json(
    table
):
    """
    Convert a BIOM table to BIOM JSON text.
    """

    return table.to_json(
        generated_by="Dave"
    )


# ==========================================================
# BIOM — READ TABLE
# ==========================================================

def read_biom(
    filename
):
    """
    Read a BIOM table from a file.
    """

    module = _get_biom()

    return module.load_table(
        filename
    )


# ==========================================================
# BIOPYTHON — BASIC LOADER
# ==========================================================

def biopython_version():
    """
    Return the installed Biopython version.
    """

    module = _get_biopython()

    return getattr(
        module,
        "__version__",
        "unknown"
    )


# ==========================================================
# BIOPYTHON — DNA TRANSCRIPTION
# ==========================================================

def dna_transcribe(
    dna
):
    """
    Transcribe DNA into RNA.
    """

    from Bio.Seq import Seq

    return str(
        Seq(str(dna)).transcribe()
    )


# ==========================================================
# BIOPYTHON — RNA REVERSE TRANSCRIPTION
# ==========================================================

def rna_reverse_transcribe(
    rna
):
    """
    Reverse-transcribe RNA into DNA.
    """

    from Bio.Seq import Seq

    return str(
        Seq(str(rna)).back_transcribe()
    )


# ==========================================================
# BIOPYTHON — DNA TRANSLATION
# ==========================================================

def dna_translate(
    dna,
    table=1,
    to_stop=False
):
    """
    Translate a DNA sequence into amino acids.
    """

    from Bio.Seq import Seq

    return str(
        Seq(str(dna)).translate(
            table=table,
            to_stop=to_stop
        )
    )


# ==========================================================
# BIOPYTHON — RNA TRANSLATION
# ==========================================================

def rna_translate(
    rna,
    table=1,
    to_stop=False
):
    """
    Translate an RNA sequence into amino acids.
    """

    from Bio.Seq import Seq

    return str(
        Seq(str(rna)).translate(
            table=table,
            to_stop=to_stop
        )
    )


# ==========================================================
# BIOPYTHON — COMPLEMENT
# ==========================================================

def dna_complement(
    dna
):
    """
    Return the complement of a DNA sequence.
    """

    from Bio.Seq import Seq

    return str(
        Seq(str(dna)).complement()
    )


# ==========================================================
# BIOPYTHON — REVERSE COMPLEMENT
# ==========================================================

def dna_reverse_complement(
    dna
):
    """
    Return the reverse complement of DNA.
    """

    from Bio.Seq import Seq

    return str(
        Seq(str(dna)).reverse_complement()
    )


# ==========================================================
# BIOPYTHON — GC CONTENT
# ==========================================================

def dna_gc_content(
    sequence
):
    """
    Calculate GC percentage.
    """

    from Bio.SeqUtils import gc_fraction

    return (
        float(
            gc_fraction(
                str(sequence)
            )
        )
        * 100
    )


# ==========================================================
# BIOPYTHON — MOLECULAR WEIGHT
# ==========================================================

def dna_molecular_weight(
    sequence,
    seq_type="DNA"
):
    """
    Calculate molecular weight of a nucleic-acid sequence.

    seq_type may be DNA, RNA, or protein.
    """

    from Bio.SeqUtils import molecular_weight

    return molecular_weight(
        str(sequence),
        seq_type=seq_type
    )


# ==========================================================
# BIOPYTHON — SEQUENCE LENGTH
# ==========================================================

def sequence_length(
    sequence
):
    """
    Return sequence length.
    """

    return len(
        str(sequence)
    )


# ==========================================================
# BIOPYTHON — FASTA READ
# ==========================================================

def read_fasta(
    filename
):
    """
    Read all sequences from a FASTA file.

    Returns a list of dictionaries.
    """

    from Bio import SeqIO

    records = []

    for record in SeqIO.parse(
        filename,
        "fasta"
    ):

        records.append(
            {
                "id": record.id,

                "name": record.name,

                "description":
                    record.description,

                "sequence":
                    str(record.seq),
            }
        )

    return records


# ==========================================================
# BIOPYTHON — FASTA WRITE
# ==========================================================

def write_fasta(
    sequences,
    filename
):
    """
    Write sequences to a FASTA file.

    sequences may be:

        - Biopython SeqRecord objects
        - dictionaries containing id and sequence
    """

    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord
    from Bio import SeqIO

    records = []

    for item in sequences:

        if isinstance(
            item,
            SeqRecord
        ):

            records.append(
                item
            )

        elif isinstance(
            item,
            dict
        ):

            records.append(
                SeqRecord(
                    Seq(
                        str(
                            item["sequence"]
                        )
                    ),
                    id=str(
                        item.get(
                            "id",
                            "sequence"
                        )
                    ),
                    description=str(
                        item.get(
                            "description",
                            ""
                        )
                    )
                )
            )

        else:

            records.append(
                SeqRecord(
                    Seq(
                        str(item)
                    ),
                    id=f"sequence_{len(records)+1}"
                )
            )

    return SeqIO.write(
        records,
        filename,
        "fasta"
    )


# ==========================================================
# BIOPYTHON — FASTQ READ
# ==========================================================

def read_fastq(
    filename
):
    """
    Read sequences and quality scores from FASTQ.
    """

    from Bio import SeqIO

    records = []

    for record in SeqIO.parse(
        filename,
        "fastq"
    ):

        records.append(
            {
                "id": record.id,

                "sequence":
                    str(record.seq),

                "quality":
                    record.letter_annotations.get(
                        "phred_quality",
                        []
                    ),
            }
        )

    return records


# ==========================================================
# BIOPYTHON — PAIRWISE ALIGNMENT
# ==========================================================

def pairwise_alignment(
    sequence1,
    sequence2,
    match_score=1,
    mismatch_score=-1,
    gap_score=-1
):
    """
    Perform pairwise sequence alignment.
    """

    from Bio import Align

    aligner = Align.PairwiseAligner()

    aligner.match_score = match_score
    aligner.mismatch_score = mismatch_score
    aligner.open_gap_score = gap_score
    aligner.extend_gap_score = gap_score

    return aligner.align(
        str(sequence1),
        str(sequence2)
    )


# ==========================================================
# BIOPYTHON — BEST PAIRWISE SCORE
# ==========================================================

def pairwise_alignment_score(
    sequence1,
    sequence2,
    match_score=1,
    mismatch_score=-1,
    gap_score=-1
):
    """
    Return the best pairwise alignment score.
    """

    alignments = pairwise_alignment(
        sequence1,
        sequence2,
        match_score,
        mismatch_score,
        gap_score
    )

    if len(alignments) == 0:

        return None

    return alignments[0].score


# ==========================================================
# BIOPYTHON — PROTEIN AMINO-ACID CHECK
# ==========================================================

def protein_sequence_valid(
    sequence
):
    """
    Check whether a sequence contains standard protein
    amino-acid symbols.

    This is a basic syntactic check, not a biological
    validation of the sequence.
    """

    valid = set(
        "ACDEFGHIKLMNPQRSTVWY"
    )

    sequence = str(
        sequence
    ).upper()

    return (
        len(sequence) > 0
        and all(
            residue in valid
            for residue in sequence
        )
    )


# ==========================================================
# BIOREGISTRY
# ==========================================================

def bioregistry_normalize(
    identifier
):
    """
    Normalize a biological resource identifier.
    """

    module = _get_bioregistry()

    return module.normalize_identifier(
        identifier
    )


# ==========================================================
# BIOREGISTRY — CURIE
# ==========================================================

def bioregistry_normalize_curie(
    identifier
):
    """
    Normalize a CURIE.
    """

    module = _get_bioregistry()

    return module.normalize_curie(
        identifier
    )


# ==========================================================
# BIOREGISTRY — PREFIX
# ==========================================================

def bioregistry_get_prefix(
    identifier
):
    """
    Extract the registry prefix from an identifier.
    """

    module = _get_bioregistry()

    return module.get_prefix(
        identifier
    )


# ==========================================================
# BIOREGISTRY — LOCAL IDENTIFIER
# ==========================================================

def bioregistry_get_local_identifier(
    identifier
):
    """
    Extract the local identifier from a CURIE.
    """

    module = _get_bioregistry()

    return module.get_local_identifier(
        identifier
    )


# ==========================================================
# BIOREGISTRY — URI
# ==========================================================

def bioregistry_get_uri(
    identifier
):
    """
    Resolve an identifier into a canonical URI where
    supported by Bioregistry.
    """

    module = _get_bioregistry()

    return module.get_uri(
        identifier
    )


# ==========================================================
# BIOREGISTRY — RESOURCE INFORMATION
# ==========================================================

def bioregistry_resource(
    prefix
):
    """
    Return information about a registered resource.
    """

    module = _get_bioregistry()

    resource = module.get_resource(
        prefix
    )

    if resource is None:

        return None

    return resource


# ==========================================================
# BIOTITE — SEQUENCE
# ==========================================================

def biotite_dna(
    sequence
):
    """
    Create a Biotite DNA sequence object.
    """

    module = _get_biotite()

    return module.sequence.NucleotideSequence(
        str(sequence)
    )


# ==========================================================
# BIOTITE — RNA
# ==========================================================

def biotite_rna(
    sequence
):
    """
    Create a Biotite RNA sequence object.
    """

    module = _get_biotite()

    return module.sequence.NucleotideSequence(
        str(sequence),
        alphabet=module.sequence.RNA_ALPHABET
    )


# ==========================================================
# BIOTITE — PROTEIN
# ==========================================================

def biotite_protein(
    sequence
):
    """
    Create a Biotite protein sequence.
    """

    module = _get_biotite()

    return module.sequence.ProteinSequence(
        str(sequence)
    )


# ==========================================================
# BIOTITE — DNA COMPLEMENT
# ==========================================================

def biotite_complement(
    sequence
):
    """
    Calculate DNA complement using Biotite.
    """

    module = _get_biotite()

    seq = module.sequence.NucleotideSequence(
        str(sequence)
    )

    return str(
        seq.complement()
    )


# ==========================================================
# BIOTITE — DNA REVERSE COMPLEMENT
# ==========================================================

def biotite_reverse_complement(
    sequence
):
    """
    Calculate the reverse complement of a DNA
    sequence using Biotite.
    """

    module = _get_biotite()

    seq = module.sequence.NucleotideSequence(
        str(sequence)
    )

    return str(
        seq.complement()
    )[::-1]

# ==========================================================
# BIOTITE — SEQUENCE IDENTITY
# ==========================================================

def sequence_identity(
    sequence1,
    sequence2
):
    """
    Calculate the fraction of identical positions
    between two sequences of equal length.
    """

    a = str(sequence1)
    b = str(sequence2)

    if len(a) != len(b):

        raise ValueError(
            "Sequences must have equal length."
        )

    if len(a) == 0:

        return 1.0

    matches = sum(
        x == y
        for x, y in zip(a, b)
    )

    return matches / len(a)


# ==========================================================
# BIOTITE — FASTA READ
# ==========================================================

def biotite_read_fasta(
    filename
):
    """
    Read FASTA sequences with Biotite.
    """

    module = _get_biotite()

    fasta_file = (
        module.sequence.io.fasta.FastaFile
        .read(filename)
    )

    return fasta_file


# ==========================================================
# BIOTITE — FASTA WRITE
# ==========================================================

def biotite_write_fasta(
    sequences,
    filename
):
    """
    Write FASTA data using Biotite.

    sequences should be a Biotite FastaFile object.
    """

    sequences.write(
        filename
    )

    return filename


# ==========================================================
# BIOLOGY PACKAGE STATUS
# ==========================================================

def biology_part1_status():
    """
    Display availability of Biology Part 1 packages.
    """

    package_names = [
        "anndata",
        "biom-format",
        "biopython",
        "bioregistry",
        "biotite",
    ]

    results = {}

    print()
    print("=" * 70)
    print(
        "DAVE — BIOLOGY / BIOINFORMATICS STATUS"
    )
    print("=" * 70)
    print()

    for package_name in package_names:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<18} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<18} unavailable"
            )

    print()

    return results


# ==========================================================
# BIOLOGY PART 1 SELF TEST
# ==========================================================

def biology_part1_selftest(
    verbose=True
):
    """
    Test Biology Part 1 without requiring network access.
    """

    tests = []


    # ------------------------------------------------------
    # ANNDATA
    # ------------------------------------------------------

    try:

        import numpy as np

        data = create_anndata(
            np.array(
                [
                    [1, 2],
                    [3, 4]
                ]
            )
        )

        info = anndata_info(
            data
        )

        tests.append(
            (
                "anndata",
                info["shape"] == (2, 2)
            )
        )

    except Exception as exc:

        tests.append(
            (
                "anndata",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # BIOM
    # ------------------------------------------------------

    try:

        import numpy as np

        table = create_biom_table(
            np.array(
                [
                    [1, 2],
                    [3, 4]
                ]
            ),
            observation_ids=[
                "obs1",
                "obs2"
            ],
            sample_ids=[
                "sample1",
                "sample2"
            ]
        )

        tests.append(
            (
                "biom-format",
                table.shape == (2, 2)
            )
        )

    except Exception as exc:

        tests.append(
            (
                "biom-format",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # BIOPYTHON
    # ------------------------------------------------------

    try:

        dna = "ATGGCC"

        rna = dna_transcribe(
            dna
        )

        protein = dna_translate(
            dna
        )

        tests.append(
            (
                "biopython",
                rna == "AUGGCC"
                and len(protein) > 0
            )
        )

    except Exception as exc:

        tests.append(
            (
                "biopython",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # BIOREGISTRY
    # ------------------------------------------------------

    try:

        normalized = bioregistry_normalize(
            "CHEBI:15377"
        )

        tests.append(
            (
                "bioregistry",
                normalized is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "bioregistry",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # BIOTITE
    # ------------------------------------------------------

    try:

        sequence = biotite_dna(
            "ATGC"
        )

        reverse = biotite_reverse_complement(
            "ATGC"
        )

        tests.append(
            (
                "biotite",
                str(sequence) == "ATGC"
                and reverse == "GCAT"
            )
        )

    except Exception as exc:

        tests.append(
            (
                "biotite",
                False,
                str(exc)
            )
        )


    # ======================================================
    # RESULTS
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 70)
        print(
            "DAVE — BIOLOGY PART 1 SELF TEST"
        )
        print("=" * 70)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 70)
        print(
            f"Passed: {passed}"
        )
        print(
            f"Failed: {failed}"
        )
        print(
            f"Total:  {len(tests)}"
        )
        print("-" * 70)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# BIOLOGY PART 1 HELP
# ==========================================================

def biology_part1_help():

    print("""
==============================================================================
DAVE — BIOLOGY / BIOINFORMATICS PART 1
==============================================================================

ANNDATA
-------

    create_anndata(X)

    anndata_info(data)

    anndata_observations(data)

    anndata_variables(data)

    anndata_add_observation_column(
        data,
        name,
        values
    )

    anndata_add_variable_column(
        data,
        name,
        values
    )

    anndata_slice(
        data,
        observations,
        variables
    )

    anndata_copy(data)

    anndata_concat(
        datasets
    )

    read_anndata(
        "data.h5ad"
    )

    write_anndata(
        data,
        "data.h5ad"
    )


BIOM-FORMAT
-----------

    create_biom_table(
        data,
        observation_ids,
        sample_ids
    )

    biom_table_info(table)

    biom_sample_ids(table)

    biom_observation_ids(table)

    biom_sample_sums(table)

    biom_observation_sums(table)

    biom_filter_samples(
        table,
        min_count
    )

    biom_filter_observations(
        table,
        min_count
    )

    biom_to_json(table)

    read_biom(
        "table.biom"
    )


BIOPYTHON
---------

DNA:

    dna_transcribe("ATGC")

    rna_reverse_transcribe("AUGC")

    dna_translate("ATGGCC")

    rna_translate("AUGGCC")

    dna_complement("ATGC")

    dna_reverse_complement("ATGC")

    dna_gc_content("ATGC")

    dna_molecular_weight(
        "ATGC",
        "DNA"
    )

    sequence_length(
        "ATGC"
    )


SEQUENCES:

    read_fasta(
        "sequences.fasta"
    )

    write_fasta(
        sequences,
        "output.fasta"
    )

    read_fastq(
        "reads.fastq"
    )


ALIGNMENT:

    pairwise_alignment(
        sequence1,
        sequence2
    )

    pairwise_alignment_score(
        sequence1,
        sequence2
    )


PROTEINS:

    protein_sequence_valid(
        "MKWVTFISLL"
    )


BIOREGISTRY
-----------

    bioregistry_normalize(
        "CHEBI:15377"
    )

    bioregistry_normalize_curie(
        "CHEBI:15377"
    )

    bioregistry_get_prefix(
        "CHEBI:15377"
    )

    bioregistry_get_local_identifier(
        "CHEBI:15377"
    )

    bioregistry_get_uri(
        "CHEBI:15377"
    )

    bioregistry_resource(
        "chebi"
    )


BIOTITE
-------

    biotite_dna(
        "ATGC"
    )

    biotite_rna(
        "AUGC"
    )

    biotite_protein(
        "MKWVTF"
    )

    biotite_complement(
        "ATGC"
    )

    biotite_reverse_complement(
        "ATGC"
    )

    sequence_identity(
        "ATGC",
        "ATGT"
    )

    biotite_read_fasta(
        "sequences.fasta"
    )

    biotite_write_fasta(
        sequences,
        "output.fasta"
    )


STATUS / TESTING
----------------

    biology_part1_status()

    biology_part1_selftest()

==============================================================================
""")

# ==========================================================
# DAVE
# BIOLOGY / BIOINFORMATICS INTEGRATION
# PART 2
# ==========================================================
#
# Packages covered:
#
#   DendroPy
#   msprime
#   pybedtools
#   pysam
#   scanpy
#   scikit-bio
#   tskit
#
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_dendropy():
    """
    Load DendroPy lazily.
    """

    return load_scientific_package("DendroPy")


def _get_msprime():
    """
    Load msprime lazily.
    """

    return load_scientific_package("msprime")


def _get_pybedtools():
    """
    Load pybedtools lazily.
    """

    return load_scientific_package("pybedtools")


def _get_pysam():
    """
    Load pysam lazily.
    """

    return load_scientific_package("pysam")


def _get_scanpy():
    """
    Load Scanpy lazily.
    """

    return load_scientific_package("scanpy")


def _get_skbio():
    """
    Load scikit-bio lazily.
    """

    return load_scientific_package("scikit-bio")


def _get_tskit():
    """
    Load tskit lazily.
    """

    return load_scientific_package("tskit")


# ==========================================================
# DENDROPY — READ NEWICK TREE
# ==========================================================

def read_newick_tree(
    filename
):
    """
    Read a phylogenetic tree from a Newick file.
    """

    module = _get_dendropy()

    return module.Tree.get(
        path=filename,
        schema="newick"
    )


# ==========================================================
# DENDROPY — PARSE NEWICK STRING
# ==========================================================

def parse_newick_tree(
    newick
):
    """
    Parse a Newick tree directly from a string.
    """

    module = _get_dendropy()

    return module.Tree.get(
        data=newick,
        schema="newick"
    )


# ==========================================================
# DENDROPY — WRITE NEWICK
# ==========================================================

def write_newick_tree(
    tree,
    filename
):
    """
    Write a DendroPy tree to a Newick file.
    """

    tree.write(
        path=filename,
        schema="newick"
    )

    return filename


# ==========================================================
# DENDROPY — TREE TAXA
# ==========================================================

def dendropy_taxa(
    tree
):
    """
    Return the taxon labels in a tree.
    """

    return [
        taxon.label
        for taxon in tree.taxon_namespace
        if taxon.label is not None
    ]


# ==========================================================
# DENDROPY — TREE STATISTICS
# ==========================================================

def dendropy_tree_info(
    tree
):
    """
    Return basic tree statistics.
    """

    leaves = list(
        tree.leaf_node_iter()
    )

    return {
        "taxa": dendropy_taxa(tree),

        "number_of_leaves":
            len(leaves),

        "number_of_nodes":
            len(list(tree.preorder_node_iter())),

        "is_rooted":
            bool(tree.is_rooted),

        "seed_node":
            str(tree.seed_node),
    }


# ==========================================================
# DENDROPY — TREE LENGTH
# ==========================================================

def dendropy_tree_length(
    tree
):
    """
    Calculate the total branch length.
    """

    total = 0.0

    for edge in tree.postorder_edge_iter():

        if edge.length is not None:

            total += float(
                edge.length
            )

    return total


# ==========================================================
# DENDROPY — MOST RECENT COMMON ANCESTOR
# ==========================================================

def dendropy_mrca(
    tree,
    labels
):
    """
    Find the most recent common ancestor of taxa.

    labels should be an iterable of taxon labels.
    """

    labels = list(labels)

    nodes = []

    for label in labels:

        node = tree.find_node_with_taxon_label(
            label
        )

        if node is None:

            raise ValueError(
                f"Taxon not found: {label}"
            )

        nodes.append(node)

    return tree.mrca(
        taxon_labels=labels
    )


# ==========================================================
# DENDROPY — PRUNE TAXA
# ==========================================================

def dendropy_prune_taxa(
    tree,
    labels
):
    """
    Remove specified taxa from a copy of the tree.
    """

    result = tree.clone(
        depth=2
    )

    for label in labels:

        node = result.find_node_with_taxon_label(
            label
        )

        if node is not None:

            result.prune_subtree(
                node,
                update_bipartitions=False
            )

    return result


# ==========================================================
# DENDROPY — RF DISTANCE
# ==========================================================

def dendropy_rf_distance(
    tree1,
    tree2
):
    """
    Calculate the Robinson-Foulds distance between
    two phylogenetic trees.
    """

    return tree1.robinson_foulds_distance(
        tree2
    )


# ==========================================================
# MSPRIME — BASIC SIMULATION
# ==========================================================

def msprime_simulate_ancestry(
    samples=10,
    sequence_length=10000,
    recombination_rate=1e-8,
    population_size=10_000,
    random_seed=None
):
    """
    Simulate ancestry using msprime.

    samples:
        Number of sampled individuals.

    sequence_length:
        Genome length.

    recombination_rate:
        Recombination rate per base per generation.

    population_size:
        Effective population size.
    """

    msprime = _get_msprime()

    return msprime.sim_ancestry(
        samples=samples,
        sequence_length=sequence_length,
        recombination_rate=recombination_rate,
        population_size=population_size,
        random_seed=random_seed
    )


# ==========================================================
# MSPRIME — MUTATIONS
# ==========================================================

def msprime_simulate_mutations(
    ancestry,
    mutation_rate=1e-8,
    random_seed=None
):
    """
    Add mutations to an ancestry simulation.
    """

    msprime = _get_msprime()

    return msprime.sim_mutations(
        ancestry,
        rate=mutation_rate,
        random_seed=random_seed
    )


# ==========================================================
# MSPRIME — FULL SIMULATION
# ==========================================================

def msprime_simulate(
    samples=10,
    sequence_length=10_000,
    recombination_rate=1e-8,
    mutation_rate=1e-8,
    population_size=10_000,
    random_seed=None
):
    """
    Perform a complete ancestry + mutation simulation.
    """

    ancestry = msprime_simulate_ancestry(
        samples=samples,
        sequence_length=sequence_length,
        recombination_rate=recombination_rate,
        population_size=population_size,
        random_seed=random_seed
    )

    return msprime_simulate_mutations(
        ancestry,
        mutation_rate=mutation_rate,
        random_seed=random_seed
    )


# ==========================================================
# MSPRIME — SIMULATION INFORMATION
# ==========================================================

def msprime_simulation_info(
    ts
):
    """
    Return basic information about a tree sequence.
    """

    return {
        "sequence_length":
            ts.sequence_length,

        "num_trees":
            ts.num_trees,

        "num_nodes":
            ts.num_nodes,

        "num_edges":
            ts.num_edges,

        "num_sites":
            ts.num_sites,

        "num_mutations":
            ts.num_mutations,

        "num_individuals":
            ts.num_individuals,

        "num_populations":
            ts.num_populations,
    }


# ==========================================================
# MSPRIME — SAVE TREE SEQUENCE
# ==========================================================

def save_tree_sequence(
    ts,
    filename
):
    """
    Save a tree sequence.
    """

    ts.dump(
        filename
    )

    return filename


# ==========================================================
# MSPRIME — LOAD TREE SEQUENCE
# ==========================================================

def load_tree_sequence(
    filename
):
    """
    Load a tree sequence.
    """

    tskit = _get_tskit()

    return tskit.load(
        filename
    )


# ==========================================================
# PYBEDTOOLS — CREATE INTERVAL
# ==========================================================

def bed_interval(
    chromosome,
    start,
    end,
    name=None,
    score=None,
    strand=None
):
    """
    Create a genomic interval.
    """

    module = _get_pybedtools()

    fields = [
        str(chromosome),
        int(start),
        int(end)
    ]

    if name is not None:

        fields.append(
            str(name)
        )

    if score is not None:

        fields.append(
            str(score)
        )

    if strand is not None:

        fields.append(
            str(strand)
        )

    return module.Interval(
        *fields
    )


# ==========================================================
# PYBEDTOOLS — CREATE BED TOOL
# ==========================================================

def create_bedtool(
    intervals
):
    """
    Create a BedTool from interval strings or Interval
    objects.
    """

    module = _get_pybedtools()

    return module.BedTool(
        intervals
    )


# ==========================================================
# PYBEDTOOLS — READ BED
# ==========================================================

def read_bed(
    filename
):
    """
    Read a BED/GFF-like interval file.
    """

    module = _get_pybedtools()

    return module.BedTool(
        filename
    )


# ==========================================================
# PYBEDTOOLS — SAVE BED
# ==========================================================

def save_bed(
    bedtool,
    filename
):
    """
    Save intervals to a file.
    """

    bedtool.saveas(
        filename
    )

    return filename


# ==========================================================
# PYBEDTOOLS — SORT
# ==========================================================

def sort_bed(
    bedtool
):
    """
    Sort genomic intervals.
    """

    return bedtool.sort()


# ==========================================================
# PYBEDTOOLS — MERGE
# ==========================================================

def merge_bed(
    bedtool
):
    """
    Merge overlapping genomic intervals.
    """

    return bedtool.merge()


# ==========================================================
# PYBEDTOOLS — INTERSECTION
# ==========================================================

def intersect_bed(
    bedtool1,
    bedtool2,
    **kwargs
):
    """
    Calculate the intersection between genomic intervals.
    """

    return bedtool1.intersect(
        bedtool2,
        **kwargs
    )


# ==========================================================
# PYBEDTOOLS — UNION
# ==========================================================

def union_bed(
    bedtool1,
    bedtool2
):
    """
    Calculate the union of two interval sets.
    """

    return bedtool1.cat(
        bedtool2
    ).sort().merge()


# ==========================================================
# PYBEDTOOLS — CLOSEST
# ==========================================================

def closest_bed(
    bedtool1,
    bedtool2,
    **kwargs
):
    """
    Find closest genomic features.
    """

    return bedtool1.closest(
        bedtool2,
        **kwargs
    )


# ==========================================================
# PYSAM — OPEN SAM/BAM
# ==========================================================

def open_alignment_file(
    filename,
    mode=None
):
    """
    Open SAM/BAM/CRAM alignment data.
    """

    pysam = _get_pysam()

    if mode is None:

        if str(filename).lower().endswith(
            ".sam"
        ):

            mode = "r"

        elif str(filename).lower().endswith(
            ".cram"
        ):

            mode = "rc"

        else:

            mode = "rb"

    return pysam.AlignmentFile(
        filename,
        mode
    )


# ==========================================================
# PYSAM — ALIGNMENT INFORMATION
# ==========================================================

def alignment_file_info(
    filename
):
    """
    Return reference information from an alignment file.
    """

    with open_alignment_file(
        filename
    ) as alignment:

        return {
            "references":
                list(alignment.references),

            "lengths":
                list(alignment.lengths),

            "nreferences":
                alignment.nreferences,
        }


# ==========================================================
# PYSAM — READ ALIGNMENTS
# ==========================================================

def read_alignments(
    filename,
    until_eof=True,
    limit=None
):
    """
    Read alignment records.

    limit can be used to avoid loading a huge BAM file
    into memory.
    """

    records = []

    with open_alignment_file(
        filename
    ) as alignment:

        for index, record in enumerate(
            alignment.fetch(
                until_eof=until_eof
            )
        ):

            records.append(
                {
                    "query_name":
                        record.query_name,

                    "reference_name":
                        record.reference_name,

                    "reference_start":
                        record.reference_start,

                    "reference_end":
                        record.reference_end,

                    "mapping_quality":
                        record.mapping_quality,

                    "query_sequence":
                        record.query_sequence,

                    "flag":
                        record.flag,
                }
            )

            if (
                limit is not None
                and index + 1 >= limit
            ):

                break

    return records


# ==========================================================
# PYSAM — COUNT READS
# ==========================================================

def count_alignment_reads(
    filename
):
    """
    Count aligned reads.
    """

    with open_alignment_file(
        filename
    ) as alignment:

        return sum(
            1
            for _ in alignment.fetch(
                until_eof=True
            )
        )


# ==========================================================
# PYSAM — FASTA
# ==========================================================

def open_fasta(
    filename
):
    """
    Open a FASTA file using pysam.
    """

    pysam = _get_pysam()

    return pysam.FastaFile(
        filename
    )


# ==========================================================
# PYSAM — FASTA FETCH
# ==========================================================

def fasta_fetch(
    filename,
    chromosome,
    start=None,
    end=None
):
    """
    Retrieve a sequence from a FASTA file.
    """

    with open_fasta(
        filename
    ) as fasta:

        if start is None:

            return fasta.fetch(
                chromosome
            )

        return fasta.fetch(
            chromosome,
            start,
            end
        )


# ==========================================================
# PYSAM — VCF
# ==========================================================

def open_vcf(
    filename,
    mode="r"
):
    """
    Open a VCF/BCF file.
    """

    pysam = _get_pysam()

    return pysam.VariantFile(
        filename,
        mode
    )


# ==========================================================
# PYSAM — VCF RECORDS
# ==========================================================

def read_vcf_records(
    filename,
    limit=None
):
    """
    Read variants from a VCF.
    """

    records = []

    with open_vcf(
        filename
    ) as vcf:

        for index, record in enumerate(
            vcf.fetch()
        ):

            records.append(
                {
                    "chromosome":
                        record.chrom,

                    "position":
                        record.pos,

                    "id":
                        record.id,

                    "ref":
                        record.ref,

                    "alt":
                        list(record.alts)
                        if record.alts
                        else [],

                    "qual":
                        record.qual,

                    "filter":
                        list(record.filter.keys()),
                }
            )

            if (
                limit is not None
                and index + 1 >= limit
            ):

                break

    return records


# ==========================================================
# SCANPY — READ H5AD
# ==========================================================

def scanpy_read_h5ad(
    filename
):
    """
    Read an H5AD single-cell dataset.
    """

    scanpy = _get_scanpy()

    return scanpy.read_h5ad(
        filename
    )


# ==========================================================
# SCANPY — DATASET SUMMARY
# ==========================================================

def scanpy_summary(
    data
):
    """
    Return basic single-cell dataset information.
    """

    return {
        "cells":
            int(data.n_obs),

        "genes":
            int(data.n_vars),

        "observation_columns":
            list(data.obs.columns),

        "variable_columns":
            list(data.var.columns),

        "layers":
            list(data.layers.keys()),

        "obsm":
            list(data.obsm.keys()),

        "uns":
            list(data.uns.keys()),
    }


# ==========================================================
# SCANPY — FILTER CELLS
# ==========================================================

def scanpy_filter_cells(
    data,
    min_genes=200
):
    """
    Filter cells based on the number of detected genes.
    """

    scanpy = _get_scanpy()

    scanpy.pp.filter_cells(
        data,
        min_genes=min_genes
    )

    return data


# ==========================================================
# SCANPY — FILTER GENES
# ==========================================================

def scanpy_filter_genes(
    data,
    min_cells=3
):
    """
    Filter genes based on the number of cells expressing
    them.
    """

    scanpy = _get_scanpy()

    scanpy.pp.filter_genes(
        data,
        min_cells=min_cells
    )

    return data


# ==========================================================
# SCANPY — TOTAL NORMALIZATION
# ==========================================================

def scanpy_normalize(
    data,
    target_sum=1e4
):
    """
    Normalize counts per cell.
    """

    scanpy = _get_scanpy()

    scanpy.pp.normalize_total(
        data,
        target_sum=target_sum
    )

    return data


# ==========================================================
# SCANPY — LOG TRANSFORM
# ==========================================================

def scanpy_log_transform(
    data
):
    """
    Apply log1p transformation.
    """

    scanpy = _get_scanpy()

    scanpy.pp.log1p(
        data
    )

    return data


# ==========================================================
# SCANPY — HIGHLY VARIABLE GENES
# ==========================================================

def scanpy_highly_variable_genes(
    data,
    n_top_genes=2000
):
    """
    Identify highly variable genes.
    """

    scanpy = _get_scanpy()

    scanpy.pp.highly_variable_genes(
        data,
        n_top_genes=n_top_genes
    )

    return data


# ==========================================================
# SCANPY — PCA
# ==========================================================

def scanpy_pca(
    data,
    n_comps=50
):
    """
    Calculate principal components.
    """

    scanpy = _get_scanpy()

    scanpy.pp.pca(
        data,
        n_comps=n_comps
    )

    return data


# ==========================================================
# SCANPY — NEIGHBOR GRAPH
# ==========================================================

def scanpy_neighbors(
    data,
    n_neighbors=15
):
    """
    Compute a neighborhood graph.
    """

    scanpy = _get_scanpy()

    scanpy.pp.neighbors(
        data,
        n_neighbors=n_neighbors
    )

    return data


# ==========================================================
# SCANPY — UMAP
# ==========================================================

def scanpy_umap(
    data
):
    """
    Calculate a UMAP embedding.
    """

    scanpy = _get_scanpy()

    scanpy.tl.umap(
        data
    )

    return data


# ==========================================================
# SCANPY — LEIDEN CLUSTERING
# ==========================================================

def scanpy_leiden(
    data,
    resolution=1.0
):
    """
    Perform Leiden community clustering.

    The exact clustering dependencies may vary with the
    installed Scanpy version.
    """

    scanpy = _get_scanpy()

    scanpy.tl.leiden(
        data,
        resolution=resolution
    )

    return data


# ==========================================================
# SCANPY — RANK GENES
# ==========================================================

def scanpy_rank_genes(
    data,
    groupby,
    method="wilcoxon"
):
    """
    Rank genes associated with groups of cells.
    """

    scanpy = _get_scanpy()

    scanpy.tl.rank_genes_groups(
        data,
        groupby=groupby,
        method=method
    )

    return data


# ==========================================================
# SCANPY — SAVE
# ==========================================================

def scanpy_save(
    data,
    filename
):
    """
    Save a Scanpy/AnnData dataset.
    """

    data.write(
        filename
    )

    return filename


# ==========================================================
# SCIKIT-BIO — DNA
# ==========================================================

def skbio_dna(
    sequence
):
    """
    Create a scikit-bio DNA object.
    """

    module = _get_skbio()

    return module.DNA(
        str(sequence)
    )


# ==========================================================
# SCIKIT-BIO — RNA
# ==========================================================

def skbio_rna(
    sequence
):
    """
    Create a scikit-bio RNA object.
    """

    module = _get_skbio()

    return module.RNA(
        str(sequence)
    )


# ==========================================================
# SCIKIT-BIO — PROTEIN
# ==========================================================

def skbio_protein(
    sequence
):
    """
    Create a scikit-bio protein object.
    """

    module = _get_skbio()

    return module.Protein(
        str(sequence)
    )


# ==========================================================
# SCIKIT-BIO — GC CONTENT
# ==========================================================

def skbio_gc_content(
    sequence
):
    """
    Calculate GC content.
    """

    dna = skbio_dna(
        sequence
    )

    return float(
        dna.gc_frequency()
    )


# ==========================================================
# SCIKIT-BIO — DNA REVERSE COMPLEMENT
# ==========================================================

def skbio_reverse_complement(
    sequence
):
    """
    Return DNA reverse complement.
    """

    dna = skbio_dna(
        sequence
    )

    return str(
        dna.reverse_complement()
    )


# ==========================================================
# SCIKIT-BIO — DNA TRANSLATION
# ==========================================================

def skbio_translate(
    sequence
):
    """
    Translate DNA into protein.
    """

    dna = skbio_dna(
        sequence
    )

    return str(
        dna.translate()
    )


# ==========================================================
# SCIKIT-BIO — HAMMING DISTANCE
# ==========================================================

def skbio_hamming_distance(
    sequence1,
    sequence2
):
    """
    Calculate Hamming distance between two sequences.
    """

    from skbio.sequence.distance import hamming

    return hamming(
        str(sequence1),
        str(sequence2)
    )


# ==========================================================
# SCIKIT-BIO — PAIRWISE ALIGNMENT
# ==========================================================

def skbio_global_alignment(
    sequence1,
    sequence2
):
    """
    Perform a global pairwise alignment.
    """

    from skbio.alignment import global_pairwise_align_nucleotide

    return global_pairwise_align_nucleotide(
        skbio_dna(sequence1),
        skbio_dna(sequence2)
    )


# ==========================================================
# SCIKIT-BIO — SHANNON ENTROPY
# ==========================================================

def skbio_shannon_entropy(
    counts
):
    """
    Calculate Shannon diversity entropy.
    """

    from skbio.diversity.alpha import shannon

    return shannon(
        counts
    )


# ==========================================================
# SCIKIT-BIO — SIMPSON INDEX
# ==========================================================

def skbio_simpson(
    counts
):
    """
    Calculate Simpson diversity.
    """

    from skbio.diversity.alpha import simpson

    return simpson(
        counts
    )


# ==========================================================
# SCIKIT-BIO — FAITH PD
# ==========================================================

def skbio_faith_pd(
    counts,
    tree
):
    """
    Calculate Faith's phylogenetic diversity.
    """

    from skbio.diversity import beta_diversity

    from skbio.diversity.alpha import faith_pd

    return faith_pd(
        counts,
        tree
    )


# ==========================================================
# TSKIT — LOAD TREE SEQUENCE
# ==========================================================

def tskit_load(
    filename
):
    """
    Load a tree sequence.
    """

    tskit = _get_tskit()

    return tskit.load(
        filename
    )


# ==========================================================
# TSKIT — SUMMARY
# ==========================================================

def tskit_summary(
    ts
):
    """
    Return basic tree-sequence statistics.
    """

    return {
        "sequence_length":
            ts.sequence_length,

        "num_trees":
            ts.num_trees,

        "num_nodes":
            ts.num_nodes,

        "num_edges":
            ts.num_edges,

        "num_individuals":
            ts.num_individuals,

        "num_populations":
            ts.num_populations,

        "num_sites":
            ts.num_sites,

        "num_mutations":
            ts.num_mutations,
    }


# ==========================================================
# TSKIT — TREE ITERATION
# ==========================================================

def tskit_tree_count(
    ts
):
    """
    Count trees in a tree sequence.
    """

    return sum(
        1
        for _ in ts.trees()
    )


# ==========================================================
# TSKIT — FIRST TREE
# ==========================================================

def tskit_first_tree(
    ts
):
    """
    Return the first tree in a tree sequence.
    """

    return ts.first()


# ==========================================================
# TSKIT — NEWICK
# ==========================================================

def tskit_tree_newick(
    ts,
    index=0
):
    """
    Return a tree in Newick format.
    """

    tree = ts.at_index(
        index
    )

    return tree.as_newick()


# ==========================================================
# TSKIT — DIVERSITY
# ==========================================================

def tskit_diversity(
    ts,
    samples=None
):
    """
    Calculate nucleotide diversity.
    """

    if samples is None:

        return ts.diversity()

    return ts.diversity(
        samples=samples
    )


# ==========================================================
# TSKIT — NUMERICAL DIVERSITY
# ==========================================================

def tskit_diversity_summary(
    ts
):
    """
    Return several basic genetic statistics.
    """

    return {
        "diversity":
            ts.diversity(),

        "segregating_sites":
            ts.num_sites,

        "mutations":
            ts.num_mutations,

        "trees":
            ts.num_trees,
    }


# ==========================================================
# BIOLOGY PART 2 PACKAGE STATUS
# ==========================================================

def biology_part2_status():
    """
    Display availability of Biology Part 2 packages.
    """

    package_names = [
        "DendroPy",
        "msprime",
        "pybedtools",
        "pysam",
        "scanpy",
        "scikit-bio",
        "tskit",
    ]

    results = {}

    print()
    print("=" * 75)
    print(
        "DAVE — BIOLOGY PART 2 PACKAGE STATUS"
    )
    print("=" * 75)
    print()

    for package_name in package_names:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<18} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<18} unavailable"
            )

    print()

    return results


# ==========================================================
# BIOLOGY PART 2 SELF TEST
# ==========================================================

def biology_part2_selftest(
    verbose=True
):
    """
    Test Biology Part 2 functionality.

    Tests are designed to avoid requiring external
    databases or network services.
    """

    tests = []


    # ------------------------------------------------------
    # DENDROPY
    # ------------------------------------------------------

    try:

        tree = parse_newick_tree(
            "((A:1,B:1):2,C:3);"
        )

        info = dendropy_tree_info(
            tree
        )

        tests.append(
            (
                "DendroPy",
                info["number_of_leaves"] == 3
            )
        )

    except Exception as exc:

        tests.append(
            (
                "DendroPy",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # MSPRIME
    # ------------------------------------------------------

    try:

        ts = msprime_simulate(
            samples=2,
            sequence_length=1000,
            recombination_rate=1e-8,
            mutation_rate=1e-8,
            population_size=100,
            random_seed=42
        )

        info = msprime_simulation_info(
            ts
        )

        tests.append(
            (
                "msprime",
                info["num_nodes"] > 0
            )
        )

    except Exception as exc:

        tests.append(
            (
                "msprime",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PYBEDTOOLS
    # ------------------------------------------------------

    try:

        intervals = [
            "chr1\t10\t20",
            "chr1\t15\t30"
        ]

        bed = create_bedtool(
            "\n".join(intervals)
        )

        merged = merge_bed(
            bed
        )

        tests.append(
            (
                "pybedtools",
                len(list(merged)) == 1
            )
        )

    except Exception as exc:

        tests.append(
            (
                "pybedtools",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PYSAM
    # ------------------------------------------------------

    try:

        pysam = _get_pysam()

        tests.append(
            (
                "pysam",
                hasattr(
                    pysam,
                    "AlignmentFile"
                )
            )
        )

    except Exception as exc:

        tests.append(
            (
                "pysam",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # SCANPY
    # ------------------------------------------------------

    try:

        scanpy = _get_scanpy()

        tests.append(
            (
                "scanpy",
                hasattr(
                    scanpy,
                    "pp"
                )
                and hasattr(
                    scanpy,
                    "tl"
                )
            )
        )

    except Exception as exc:

        tests.append(
            (
                "scanpy",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # SCIKIT-BIO
    # ------------------------------------------------------

    try:

        dna = skbio_dna(
            "ATGC"
        )

        reverse = skbio_reverse_complement(
            "ATGC"
        )

        tests.append(
            (
                "scikit-bio",
                str(dna) == "ATGC"
                and reverse == "GCAT"
            )
        )

    except Exception as exc:

        tests.append(
            (
                "scikit-bio",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # TSKIT
    # ------------------------------------------------------

    try:

        ts = msprime_simulate_ancestry(
            samples=2,
            sequence_length=100,
            population_size=100,
            random_seed=42
        )

        info = tskit_summary(
            ts
        )

        tests.append(
            (
                "tskit",
                info["num_nodes"] > 0
            )
        )

    except Exception as exc:

        tests.append(
            (
                "tskit",
                False,
                str(exc)
            )
        )


    # ======================================================
    # RESULTS
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 75)
        print(
            "DAVE — BIOLOGY PART 2 SELF TEST"
        )
        print("=" * 75)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 75)

        print(
            f"Passed: {passed}"
        )

        print(
            f"Failed: {failed}"
        )

        print(
            f"Total:  {len(tests)}"
        )

        print("-" * 75)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# BIOLOGY PART 2 HELP
# ==========================================================

def biology_part2_help():

    print("""
==============================================================================
DAVE — BIOLOGY / BIOINFORMATICS PART 2
==============================================================================

DENDROPY — PHYLOGENETICS
------------------------

    read_newick_tree(
        "tree.nwk"
    )

    parse_newick_tree(
        "((A:1,B:1):2,C:3);"
    )

    write_newick_tree(
        tree,
        "tree.nwk"
    )

    dendropy_taxa(
        tree
    )

    dendropy_tree_info(
        tree
    )

    dendropy_tree_length(
        tree
    )

    dendropy_mrca(
        tree,
        ["A", "B"]
    )

    dendropy_prune_taxa(
        tree,
        ["C"]
    )

    dendropy_rf_distance(
        tree1,
        tree2
    )


MSPRIME — POPULATION GENETICS
----------------------------

    msprime_simulate_ancestry(
        samples=10,
        sequence_length=10000,
        recombination_rate=1e-8,
        population_size=10000
    )

    msprime_simulate_mutations(
        ancestry,
        mutation_rate=1e-8
    )

    msprime_simulate(
        samples=10,
        sequence_length=10000,
        recombination_rate=1e-8,
        mutation_rate=1e-8
    )

    msprime_simulation_info(
        ts
    )

    save_tree_sequence(
        ts,
        "simulation.trees"
    )

    load_tree_sequence(
        "simulation.trees"
    )


PYBEDTOOLS — GENOMIC INTERVALS
------------------------------

    bed_interval(
        "chr1",
        100,
        200
    )

    create_bedtool(
        intervals
    )

    read_bed(
        "genes.bed"
    )

    save_bed(
        bedtool,
        "output.bed"
    )

    sort_bed(
        bedtool
    )

    merge_bed(
        bedtool
    )

    intersect_bed(
        bedtool1,
        bedtool2
    )

    union_bed(
        bedtool1,
        bedtool2
    )

    closest_bed(
        bedtool1,
        bedtool2
    )


PYSAM — SEQUENCING DATA
-----------------------

    open_alignment_file(
        "reads.bam"
    )

    alignment_file_info(
        "reads.bam"
    )

    read_alignments(
        "reads.bam",
        limit=100
    )

    count_alignment_reads(
        "reads.bam"
    )


PYSAM — REFERENCE SEQUENCES
---------------------------

    open_fasta(
        "genome.fa"
    )

    fasta_fetch(
        "genome.fa",
        "chr1",
        100,
        200
    )


PYSAM — VARIANTS
----------------

    open_vcf(
        "variants.vcf"
    )

    read_vcf_records(
        "variants.vcf",
        limit=100
    )


SCANPY — SINGLE-CELL ANALYSIS
-----------------------------

    scanpy_read_h5ad(
        "cells.h5ad"
    )

    scanpy_summary(
        data
    )

    scanpy_filter_cells(
        data,
        min_genes=200
    )

    scanpy_filter_genes(
        data,
        min_cells=3
    )

    scanpy_normalize(
        data
    )

    scanpy_log_transform(
        data
    )

    scanpy_highly_variable_genes(
        data
    )

    scanpy_pca(
        data
    )

    scanpy_neighbors(
        data
    )

    scanpy_umap(
        data
    )

    scanpy_leiden(
        data
    )

    scanpy_rank_genes(
        data,
        groupby="cluster"
    )

    scanpy_save(
        data,
        "processed.h5ad"
    )


SCIKIT-BIO
----------

    skbio_dna(
        "ATGC"
    )

    skbio_rna(
        "AUGC"
    )

    skbio_protein(
        "MKWVTF"
    )

    skbio_gc_content(
        "ATGC"
    )

    skbio_reverse_complement(
        "ATGC"
    )

    skbio_translate(
        "ATGGCC"
    )

    skbio_hamming_distance(
        "ATGC",
        "ATGT"
    )

    skbio_global_alignment(
        "ATGC",
        "ATGT"
    )

    skbio_shannon_entropy(
        counts
    )

    skbio_simpson(
        counts
    )

    skbio_faith_pd(
        counts,
        tree
    )


TSKIT — TREE SEQUENCES
----------------------

    tskit_load(
        "simulation.trees"
    )

    tskit_summary(
        ts
    )

    tskit_tree_count(
        ts
    )

    tskit_first_tree(
        ts
    )

    tskit_tree_newick(
        ts,
        index=0
    )

    tskit_diversity(
        ts
    )

    tskit_diversity_summary(
        ts
    )


STATUS / TESTING
----------------

    biology_part2_status()

    biology_part2_selftest()


==============================================================================
""")

# ==========================================================
# DAVE
# CHEMISTRY / MATERIALS SCIENCE INTEGRATION
# PART 2
# ==========================================================
#
# Packages covered:
#
#   freud
#   matminer
#   mendeleev
#   periodictable
#
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_freud():
    """
    Load freud lazily.
    """
    return load_scientific_package("freud")


def _get_matminer():
    """
    Load matminer lazily.
    """
    return load_scientific_package("matminer")


def _get_mendeleev():
    """
    Load mendeleev lazily.
    """
    return load_scientific_package("mendeleev")


def _get_periodictable():
    """
    Load periodictable lazily.
    """
    return load_scientific_package("periodictable")


# ==========================================================
# FREUD — BASIC BOX
# ==========================================================

def freud_box(
    lx,
    ly=None,
    lz=None
):
    """
    Create a freud simulation box.

    One value:
        cubic box

    Three values:
        rectangular box
    """

    freud = _get_freud()

    if ly is None:
        ly = lx

    if lz is None:
        lz = lx

    return freud.box.Box(
        Lx=float(lx),
        Ly=float(ly),
        Lz=float(lz)
    )


# ==========================================================
# FREUD — RDF
# ==========================================================

def freud_rdf(
    positions,
    box,
    r_max,
    bins=100
):
    """
    Calculate a radial distribution function g(r).

    positions should be an Nx3 array-like object.
    """

    freud = _get_freud()

    rdf = freud.density.RDF(
        bins=int(bins),
        r_max=float(r_max)
    )

    rdf.compute(
        system=(box, positions)
    )

    return {
        "r": rdf.bin_centers,
        "g_r": rdf.rdf,
        "rdf": rdf
    }


# ==========================================================
# FREUD — RDF PEAKS
# ==========================================================

def freud_rdf_peaks(
    positions,
    box,
    r_max,
    bins=200
):
    """
    Calculate an RDF and return its radial coordinates and
    g(r) values for further peak analysis.
    """

    result = freud_rdf(
        positions,
        box,
        r_max,
        bins
    )

    return (
        result["r"],
        result["g_r"]
    )


# ==========================================================
# FREUD — LOCAL DENSITY
# ==========================================================

def freud_local_density(
    positions,
    box,
    r_max,
    bins=100
):
    """
    Calculate local density around particles.
    """

    freud = _get_freud()

    density = freud.density.LocalDensity(
        r_max=float(r_max),
        diameter_space=True
    )

    density.compute(
        system=(box, positions)
    )

    return density.density


# ==========================================================
# FREUD — NEIGHBOR LIST
# ==========================================================

def freud_neighbor_list(
    positions,
    box,
    r_max
):
    """
    Find neighboring particles within r_max.
    """

    freud = _get_freud()

    query = freud.locality.AABBQuery(
        box,
        positions
    )

    result = query.query(
        positions,
        {
            "r_max": float(r_max),
            "exclude_ii": True
        }
    )

    return result.toNeighborList()


# ==========================================================
# FREUD — COORDINATION NUMBERS
# ==========================================================

def freud_coordination_numbers(
    positions,
    box,
    r_max
):
    """
    Calculate the number of neighbors surrounding each
    particle within r_max.
    """

    neighbors = freud_neighbor_list(
        positions,
        box,
        r_max
    )

    import numpy as np

    counts = np.bincount(
        neighbors.query_point_indices,
        minlength=len(positions)
    )

    return counts


# ==========================================================
# FREUD — ANGULAR ANALYSIS
# ==========================================================

def freud_local_bond_order(
    positions,
    box,
    l=6,
    r_max=3.0
):
    """
    Calculate Steinhardt-style local bond-order parameters.

    l=4 and l=6 are particularly useful for crystal
    structure analysis.
    """

    freud = _get_freud()

    query = freud.locality.AABBQuery(
        box,
        positions
    )

    neighbors = query.query(
        positions,
        {
            "r_max": float(r_max),
            "exclude_ii": True
        }
    ).toNeighborList()

    ql = freud.order.Steinhardt(
        l=int(l),
        average=True
    )

    ql.compute(
        system=(positions, neighbors)
    )

    return ql.particle_harmonics


# ==========================================================
# MATMINER — IMPORT FEATURE GENERATORS
# ==========================================================

def matminer_element_features():
    """
    Return a collection of useful matminer elemental
    feature generators.
    """

    from matminer.featurizers.element import (
        AtomicOrbitals,
        BandCenter,
        ElementFraction,
        ElementProperty,
        IonProperty,
        Miedema,
        Stoichiometry,
    )

    return {
        "AtomicOrbitals": AtomicOrbitals,
        "BandCenter": BandCenter,
        "ElementFraction": ElementFraction,
        "ElementProperty": ElementProperty,
        "IonProperty": IonProperty,
        "Miedema": Miedema,
        "Stoichiometry": Stoichiometry,
    }


# ==========================================================
# MATMINER — ELEMENT FRACTION
# ==========================================================

def matminer_element_fraction(
    composition
):
    """
    Calculate elemental fractions using matminer.

    composition may be a pymatgen Composition or a
    composition string.
    """

    from pymatgen.core import Composition
    from matminer.featurizers.composition import (
        ElementFraction
    )

    if isinstance(
        composition,
        str
    ):
        composition = Composition(
            composition
        )

    feature = ElementFraction()

    return feature.featurize(
        composition
    )


# ==========================================================
# MATMINER — STOICHIOMETRY
# ==========================================================

def matminer_stoichiometry(
    composition
):
    """
    Calculate stoichiometric descriptors.
    """

    from pymatgen.core import Composition
    from matminer.featurizers.composition import (
        Stoichiometry
    )

    if isinstance(
        composition,
        str
    ):
        composition = Composition(
            composition
        )

    feature = Stoichiometry()

    return feature.featurize(
        composition
    )


# ==========================================================
# MATMINER — ELEMENT PROPERTY
# ==========================================================

def matminer_element_property(
    composition,
    preset="magpie"
):
    """
    Generate elemental-property descriptors.

    Magpie is the standard general-purpose preset.
    """

    from pymatgen.core import Composition
    from matminer.featurizers.composition import (
        ElementProperty
    )

    if isinstance(
        composition,
        str
    ):
        composition = Composition(
            composition
        )

    feature = ElementProperty.from_preset(
        preset
    )

    return feature.featurize(
        composition
    )


# ==========================================================
# MATMINER — MIEDEMA
# ==========================================================

def matminer_miedema(
    composition
):
    """
    Calculate Miedema-based alloy descriptors.
    """

    from pymatgen.core import Composition
    from matminer.featurizers.composition import (
        Miedema
    )

    if isinstance(
        composition,
        str
    ):
        composition = Composition(
            composition
        )

    feature = Miedema()

    return feature.featurize(
        composition
    )


# ==========================================================
# MATMINER — IONIC FEATURES
# ==========================================================

def matminer_ion_features(
    composition
):
    """
    Generate ionic-property descriptors.
    """

    from pymatgen.core import Composition
    from matminer.featurizers.composition import (
        IonProperty
    )

    if isinstance(
        composition,
        str
    ):
        composition = Composition(
            composition
        )

    feature = IonProperty()

    return feature.featurize(
        composition
    )


# ==========================================================
# MATMINER — STRUCTURE FEATURES
# ==========================================================

def matminer_structure_features(
    structure
):
    """
    Generate common structural descriptors for a
    pymatgen Structure.
    """

    from matminer.featurizers.structure import (
        DensityFeatures,
        GlobalSymmetryFeatures,
        SiteStatsFingerprint,
    )

    result = {}

    try:

        feature = DensityFeatures()

        result["density"] = feature.featurize(
            structure
        )

    except Exception as exc:

        result["density_error"] = str(exc)

    try:

        feature = GlobalSymmetryFeatures()

        result["symmetry"] = feature.featurize(
            structure
        )

    except Exception as exc:

        result["symmetry_error"] = str(exc)

    try:

        feature = SiteStatsFingerprint.from_preset(
            "CrystalNNFingerprint"
        )

        result["site_statistics"] = feature.featurize(
            structure
        )

    except Exception as exc:

        result["site_statistics_error"] = str(exc)

    return result


# ==========================================================
# MATMINER — COMPOSITION FEATURE VECTOR
# ==========================================================

def matminer_composition_features(
    formula
):
    """
    Generate a combined composition feature vector.
    """

    result = {}

    result["element_fraction"] = (
        matminer_element_fraction(
            formula
        )
    )

    result["stoichiometry"] = (
        matminer_stoichiometry(
            formula
        )
    )

    try:

        result["element_property"] = (
            matminer_element_property(
                formula
            )
        )

    except Exception as exc:

        result["element_property_error"] = str(exc)

    try:

        result["miedema"] = (
            matminer_miedema(
                formula
            )
        )

    except Exception as exc:

        result["miedema_error"] = str(exc)

    try:

        result["ion_properties"] = (
            matminer_ion_features(
                formula
            )
        )

    except Exception as exc:

        result["ion_properties_error"] = str(exc)

    return result


# ==========================================================
# MENDELEEV — ELEMENT OBJECT
# ==========================================================

def mendeleev_element(
    symbol_or_atomic_number
):
    """
    Retrieve a Mendeleev element object.
    """

    mendeleev = _get_mendeleev()

    if isinstance(
        symbol_or_atomic_number,
        int
    ):

        return mendeleev.element(
            atomic_number=symbol_or_atomic_number
        )

    return mendeleev.element(
        str(symbol_or_atomic_number)
    )


# ==========================================================
# MENDELEEV — BASIC INFORMATION
# ==========================================================

def mendeleev_element_info(
    symbol_or_atomic_number
):
    """
    Return a broad collection of elemental properties.
    """

    el = mendeleev_element(
        symbol_or_atomic_number
    )

    properties = [
        "name",
        "symbol",
        "atomic_number",
        "atomic_weight",
        "period",
        "group_id",
        "block",
        "series",
        "electron_configuration",
        "density",
        "melting_point",
        "boiling_point",
        "thermal_conductivity",
        "specific_heat",
        "electronegativity",
        "covalent_radius",
        "atomic_radius",
        "van_der_waals_radius",
    ]

    result = {}

    for prop in properties:

        try:

            result[prop] = getattr(
                el,
                prop
            )

        except Exception:

            result[prop] = None

    return result


# ==========================================================
# MENDELEEV — ELECTRON CONFIGURATION
# ==========================================================

def mendeleev_electron_configuration(
    symbol_or_atomic_number
):
    """
    Return an element's electron configuration.
    """

    el = mendeleev_element(
        symbol_or_atomic_number
    )

    return el.econf


# ==========================================================
# MENDELEEV — OXIDATION STATES
# ==========================================================

def mendeleev_oxidation_states(
    symbol_or_atomic_number
):
    """
    Return common oxidation states.
    """

    el = mendeleev_element(
        symbol_or_atomic_number
    )

    try:

        return list(
            el.oxidation_states()
        )

    except TypeError:

        return list(
            el.oxidation_states
        )


# ==========================================================
# MENDELEEV — IONIZATION ENERGIES
# ==========================================================

def mendeleev_ionization_energies(
    symbol_or_atomic_number
):
    """
    Return available ionization energies.
    """

    el = mendeleev_element(
        symbol_or_atomic_number
    )

    return list(
        el.ionenergies.values()
    )


# ==========================================================
# MENDELEEV — ELECTRONEGATIVITY
# ==========================================================

def mendeleev_electronegativity(
    symbol_or_atomic_number
):
    """
    Return electronegativity using Mendeleev data.
    """

    el = mendeleev_element(
        symbol_or_atomic_number
    )

    return el.en_pauling


# ==========================================================
# MENDELEEV — DENSITY
# ==========================================================

def mendeleev_density(
    symbol_or_atomic_number
):
    """
    Return elemental density.
    """

    el = mendeleev_element(
        symbol_or_atomic_number
    )

    return el.density


# ==========================================================
# MENDELEEV — MELTING POINT
# ==========================================================

def mendeleev_melting_point(
    symbol_or_atomic_number
):
    """
    Return melting point in kelvin where available.
    """

    el = mendeleev_element(
        symbol_or_atomic_number
    )

    return el.melting_point


# ==========================================================
# MENDELEEV — BOILING POINT
# ==========================================================

def mendeleev_boiling_point(
    symbol_or_atomic_number
):
    """
    Return boiling point in kelvin where available.
    """

    el = mendeleev_element(
        symbol_or_atomic_number
    )

    return el.boiling_point


# ==========================================================
# MENDELEEV — PERIODIC TABLE SEARCH
# ==========================================================

def mendeleev_elements_by_period(
    period
):
    """
    Return elements in a specified period.
    """

    mendeleev = _get_mendeleev()

    result = []

    for atomic_number in range(
        1,
        119
    ):

        try:

            el = mendeleev.element(
                atomic_number
            )

            if el.period == int(period):

                result.append(
                    el.symbol
                )

        except Exception:

            continue

    return result


# ==========================================================
# MENDELEEV — ELEMENTS BY GROUP
# ==========================================================

def mendeleev_elements_by_group(
    group
):
    """
    Return elements in a specified periodic-table group.
    """

    mendeleev = _get_mendeleev()

    result = []

    for atomic_number in range(
        1,
        119
    ):

        try:

            el = mendeleev.element(
                atomic_number
            )

            if el.group_id == int(group):

                result.append(
                    el.symbol
                )

        except Exception:

            continue

    return result


# ==========================================================
# PERIODICTABLE — ELEMENT
# ==========================================================

def periodictable_element(
    symbol_or_atomic_number
):
    """
    Retrieve an element from periodictable.
    """

    pt = _get_periodictable()

    if isinstance(
        symbol_or_atomic_number,
        int
    ):

        return pt.elements[
            symbol_or_atomic_number
        ]

    return getattr(
        pt,
        str(symbol_or_atomic_number)
    )


# ==========================================================
# PERIODICTABLE — ISOTOPES
# ==========================================================

def periodictable_isotopes(
    symbol_or_atomic_number
):
    """
    Return known isotope objects for an element.
    """

    element = periodictable_element(
        symbol_or_atomic_number
    )

    return list(
        element
    )


# ==========================================================
# PERIODICTABLE — ISOTOPE DATA
# ==========================================================

def periodictable_isotope_info(
    symbol,
    mass_number
):
    """
    Return isotope information.
    """

    element = periodictable_element(
        symbol
    )

    isotope = element[
        int(mass_number)
    ]

    result = {
        "symbol":
            element.symbol,

        "mass_number":
            isotope.mass_number,

        "mass":
            isotope.mass,

        "abundance":
            isotope.abundance,
    }

    try:

        result["neutron_count"] = (
            int(mass_number)
            - int(element.number)
        )

    except Exception:

        result["neutron_count"] = None

    return result


# ==========================================================
# PERIODICTABLE — NATURAL ISOTOPES
# ==========================================================

def periodictable_natural_isotopes(
    symbol_or_atomic_number
):
    """
    Return naturally occurring isotopes with abundance data.
    """

    element = periodictable_element(
        symbol_or_atomic_number
    )

    result = []

    for isotope in element:

        try:

            abundance = isotope.abundance

        except Exception:

            abundance = None

        if abundance is not None:

            result.append(
                {
                    "mass_number":
                        isotope.mass_number,

                    "mass":
                        isotope.mass,

                    "abundance":
                        abundance
                }
            )

    return result


# ==========================================================
# PERIODICTABLE — AVERAGE ATOMIC MASS
# ==========================================================

def periodictable_average_mass(
    symbol_or_atomic_number
):
    """
    Return the standard/weighted atomic mass.
    """

    element = periodictable_element(
        symbol_or_atomic_number
    )

    return element.mass


# ==========================================================
# PERIODICTABLE — ISOTOPE MASS
# ==========================================================

def periodictable_isotope_mass(
    symbol,
    mass_number
):
    """
    Return isotope mass.
    """

    isotope = periodictable_element(
        symbol
    )[
        int(mass_number)
    ]

    return isotope.mass


# ==========================================================
# PERIODICTABLE — NEUTRON COUNT
# ==========================================================

def periodictable_neutron_count(
    symbol,
    mass_number
):
    """
    Calculate neutron number for an isotope.
    """

    element = periodictable_element(
        symbol
    )

    return (
        int(mass_number)
        - int(element.number)
    )


# ==========================================================
# PERIODICTABLE — PROTON COUNT
# ==========================================================

def periodictable_proton_count(
    symbol
):
    """
    Return atomic number/proton count.
    """

    element = periodictable_element(
        symbol
    )

    return int(
        element.number
    )


# ==========================================================
# PERIODICTABLE — X-RAY SCATTERING
# ==========================================================

def periodictable_xray_scattering(
    symbol,
    wavelength
):
    """
    Calculate/return X-ray scattering information for an
    element at a specified wavelength.

    wavelength is normally specified in Angstroms.
    """

    element = periodictable_element(
        symbol
    )

    try:

        return element.xray.f0(
            wavelength
        )

    except Exception:

        try:

            return element.xray.f0(
                wavelength
            )

        except Exception as exc:

            raise RuntimeError(
                "X-ray scattering data are not available "
                f"through this interface: {exc}"
            )


# ==========================================================
# PERIODICTABLE — NEUTRON SCATTERING LENGTH
# ==========================================================

def periodictable_neutron_scattering(
    symbol,
    isotope=None
):
    """
    Return neutron scattering information.

    If isotope is supplied, use that isotope.
    """

    element = periodictable_element(
        symbol
    )

    if isotope is not None:

        target = element[
            int(isotope)
        ]

    else:

        target = element

    result = {}

    for attribute in (
        "b_c",
        "b_c_complex",
        "b_c_coherent",
        "b_c_incoherent",
        "sigma_a",
        "sigma_s",
    ):

        try:

            result[attribute] = getattr(
                target,
                attribute
            )

        except Exception:

            result[attribute] = None

    return result


# ==========================================================
# PERIODICTABLE — ISOTOPE MASS DEFECT
# ==========================================================

def periodictable_mass_defect(
    symbol,
    mass_number
):
    """
    Return isotope mass relative to the integer mass number.

    This is a simple mass-defect calculation using the
    isotope mass in atomic mass units.
    """

    mass = periodictable_isotope_mass(
        symbol,
        mass_number
    )

    return (
        float(mass)
        - float(mass_number)
    )


# ==========================================================
# PERIODICTABLE — NATURAL ISOTOPE WEIGHT
# ==========================================================

def periodictable_weighted_isotope_mass(
    symbol
):
    """
    Calculate abundance-weighted average isotope mass.
    """

    isotopes = periodictable_natural_isotopes(
        symbol
    )

    if not isotopes:

        return periodictable_average_mass(
            symbol
        )

    total = 0.0
    abundance_total = 0.0

    for isotope in isotopes:

        abundance = float(
            isotope["abundance"]
        )

        total += (
            float(isotope["mass"])
            * abundance
            / 100.0
        )

        abundance_total += abundance

    if abundance_total == 0:

        return periodictable_average_mass(
            symbol
        )

    return total


# ==========================================================
# MATERIALS — COMPOSITION ANALYSIS
# ==========================================================

def materials_composition_analysis(
    formula
):
    """
    Produce a combined materials-science composition report.
    """

    result = {
        "formula": str(formula)
    }

    try:

        result["molecular_weight"] = (
            chemical_molecular_weight(
                formula
            )
        )

    except Exception as exc:

        result["molecular_weight_error"] = str(exc)

    try:

        result["weight_percent"] = (
            chemical_weight_percent(
                formula
            )
        )

    except Exception as exc:

        result["weight_percent_error"] = str(exc)

    try:

        result["matminer_features"] = (
            matminer_composition_features(
                formula
            )
        )

    except Exception as exc:

        result["matminer_error"] = str(exc)

    return result


# ==========================================================
# MATERIALS — ELEMENT REPORT
# ==========================================================

def materials_element_report(
    symbol
):
    """
    Produce a combined Mendeleev + periodictable report.
    """

    result = {
        "symbol": str(symbol)
    }

    try:

        result["mendeleev"] = (
            mendeleev_element_info(
                symbol
            )
        )

    except Exception as exc:

        result["mendeleev_error"] = str(exc)

    try:

        result["isotopes"] = (
            periodictable_natural_isotopes(
                symbol
            )
        )

    except Exception as exc:

        result["isotope_error"] = str(exc)

    try:

        result["neutron_data"] = (
            periodictable_neutron_scattering(
                symbol
            )
        )

    except Exception as exc:

        result["neutron_error"] = str(exc)

    return result


# ==========================================================
# CHEMISTRY PART 2 STATUS
# ==========================================================

def chemistry_part2_status():
    """
    Display availability of Chemistry Part 2 packages.
    """

    package_names = [
        "freud",
        "matminer",
        "mendeleev",
        "periodictable",
    ]

    results = {}

    print()
    print("=" * 75)
    print(
        "DAVE — CHEMISTRY PART 2 PACKAGE STATUS"
    )
    print("=" * 75)
    print()

    for package_name in package_names:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<18} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<18} unavailable"
            )

    print()

    return results


# ==========================================================
# CHEMISTRY PART 2 SELF TEST
# ==========================================================

def chemistry_part2_selftest(
    verbose=True
):
    """
    Test Chemistry Part 2 functionality.
    """

    tests = []


    # ------------------------------------------------------
    # FREUD
    # ------------------------------------------------------

    try:

        box = freud_box(
            10,
            10,
            10
        )

        tests.append(
            (
                "freud",
                box is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "freud",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # MATMINER
    # ------------------------------------------------------

    try:

        features = matminer_element_fraction(
            "Fe2O3"
        )

        tests.append(
            (
                "matminer",
                features is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "matminer",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # MENDELEEV
    # ------------------------------------------------------

    try:

        info = mendeleev_element_info(
            "Fe"
        )

        tests.append(
            (
                "mendeleev",
                info["symbol"] == "Fe"
                and info["atomic_number"] == 26
            )
        )

    except Exception as exc:

        tests.append(
            (
                "mendeleev",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PERIODICTABLE
    # ------------------------------------------------------

    try:

        proton_count = (
            periodictable_proton_count(
                "Fe"
            )
        )

        neutron_count = (
            periodictable_neutron_count(
                "Fe",
                56
            )
        )

        tests.append(
            (
                "periodictable",
                proton_count == 26
                and neutron_count == 30
            )
        )

    except Exception as exc:

        tests.append(
            (
                "periodictable",
                False,
                str(exc)
            )
        )


    # ======================================================
    # RESULTS
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 75)
        print(
            "DAVE — CHEMISTRY PART 2 SELF TEST"
        )
        print("=" * 75)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 75)

        print(
            f"Passed: {passed}"
        )

        print(
            f"Failed: {failed}"
        )

        print(
            f"Total:  {len(tests)}"
        )

        print("-" * 75)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# CHEMISTRY PART 2 HELP
# ==========================================================

def chemistry_part2_help():

    print("""
==============================================================================
DAVE — CHEMISTRY / MATERIALS SCIENCE PART 2
==============================================================================

FREUD — ATOMISTIC STRUCTURE ANALYSIS
------------------------------------

    freud_box(
        10,
        10,
        10
    )

    freud_rdf(
        positions,
        box,
        r_max=5,
        bins=100
    )

    freud_rdf_peaks(
        positions,
        box,
        r_max=5
    )

    freud_local_density(
        positions,
        box,
        r_max=3
    )

    freud_neighbor_list(
        positions,
        box,
        r_max=3
    )

    freud_coordination_numbers(
        positions,
        box,
        r_max=3
    )

    freud_local_bond_order(
        positions,
        box,
        l=6,
        r_max=3
    )


MATMINER — COMPOSITION
----------------------

    matminer_element_fraction(
        "Fe2O3"
    )

    matminer_stoichiometry(
        "Fe2O3"
    )

    matminer_element_property(
        "Fe2O3"
    )

    matminer_miedema(
        "Fe2O3"
    )

    matminer_ion_features(
        "Fe2O3"
    )

    matminer_composition_features(
        "Fe2O3"
    )


MATMINER — STRUCTURES
---------------------

    matminer_structure_features(
        structure
    )


MENDELEEV
---------

    mendeleev_element(
        "Fe"
    )

    mendeleev_element_info(
        "Fe"
    )

    mendeleev_electron_configuration(
        "Fe"
    )

    mendeleev_oxidation_states(
        "Fe"
    )

    mendeleev_ionization_energies(
        "Fe"
    )

    mendeleev_electronegativity(
        "Fe"
    )

    mendeleev_density(
        "Fe"
    )

    mendeleev_melting_point(
        "Fe"
    )

    mendeleev_boiling_point(
        "Fe"
    )

    mendeleev_elements_by_period(
        4
    )

    mendeleev_elements_by_group(
        8
    )


PERIODICTABLE
-------------

    periodictable_element(
        "Fe"
    )

    periodictable_isotopes(
        "Fe"
    )

    periodictable_isotope_info(
        "Fe",
        56
    )

    periodictable_natural_isotopes(
        "Fe"
    )

    periodictable_average_mass(
        "Fe"
    )

    periodictable_isotope_mass(
        "Fe",
        56
    )

    periodictable_neutron_count(
        "Fe",
        56
    )

    periodictable_proton_count(
        "Fe"
    )

    periodictable_xray_scattering(
        "Fe",
        wavelength
    )

    periodictable_neutron_scattering(
        "Fe"
    )

    periodictable_mass_defect(
        "Fe",
        56
    )

    periodictable_weighted_isotope_mass(
        "Fe"
    )


COMBINED MATERIALS TOOLS
------------------------

    materials_composition_analysis(
        "Fe2O3"
    )

    materials_element_report(
        "Fe"
    )


TESTING
-------

    chemistry_part2_status()

    chemistry_part2_selftest()

==============================================================================
""")

# ==========================================================
# DAVE
# CHEMISTRY / MATERIALS SCIENCE INTEGRATION
# PART 3
# ==========================================================
#
# Packages covered:
#
#   PubChemPy
#   pymatgen
#   pymatgen-core
#   pyrolite
#   rdkit
#   spglib
#
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_pubchempy():
    """
    Load PubChemPy lazily.
    """
    return load_scientific_package("pubchempy")


def _get_pymatgen():
    """
    Load pymatgen lazily.
    """
    return load_scientific_package("pymatgen")


def _get_pyrolite():
    """
    Load pyrolite lazily.
    """
    return load_scientific_package("pyrolite")


def _get_rdkit():
    """
    Load RDKit lazily.
    """
    return load_scientific_package("rdkit")


def _get_spglib():
    """
    Load spglib lazily.
    """
    return load_scientific_package("spglib")


# ==========================================================
# PUBCHEMPY — SEARCH BY NAME
# ==========================================================

def pubchem_search(
    query,
    namespace="name"
):
    """
    Search PubChem for compounds.

    namespace may be:
        name
        cid
        smiles
        inchikey
        formula
        synonym
    """

    pcp = _get_pubchempy()

    compounds = pcp.get_compounds(
        str(query),
        namespace
    )

    return compounds


# ==========================================================
# PUBCHEMPY — FIRST COMPOUND
# ==========================================================

def pubchem_compound(
    query,
    namespace="name"
):
    """
    Return the first PubChem compound matching a query.
    """

    compounds = pubchem_search(
        query,
        namespace
    )

    if not compounds:

        return None

    return compounds[0]


# ==========================================================
# PUBCHEMPY — COMPOUND INFORMATION
# ==========================================================

def pubchem_compound_info(
    query,
    namespace="name"
):
    """
    Return a useful collection of PubChem compound
    properties.
    """

    compound = pubchem_compound(
        query,
        namespace
    )

    if compound is None:

        return None

    properties = [
        "cid",
        "molecular_formula",
        "molecular_weight",
        "isomeric_smiles",
        "canonical_smiles",
        "inchi",
        "inchikey",
        "xlogp",
        "exact_mass",
        "monoisotopic_mass",
        "tpsa",
        "complexity",
        "charge",
        "h_bond_donor",
        "h_bond_acceptor",
        "rotatable_bond",
        "heavy_atom_count",
    ]

    result = {}

    for prop in properties:

        try:

            result[prop] = getattr(
                compound,
                prop
            )

        except Exception:

            result[prop] = None

    return result


# ==========================================================
# PUBCHEMPY — MOLECULAR FORMULA
# ==========================================================

def pubchem_formula(
    query,
    namespace="name"
):
    """
    Retrieve a compound's molecular formula.
    """

    compound = pubchem_compound(
        query,
        namespace
    )

    if compound is None:

        return None

    return compound.molecular_formula


# ==========================================================
# PUBCHEMPY — SMILES
# ==========================================================

def pubchem_smiles(
    query,
    namespace="name"
):
    """
    Retrieve canonical and isomeric SMILES.
    """

    compound = pubchem_compound(
        query,
        namespace
    )

    if compound is None:

        return None

    return {
        "canonical":
            compound.canonical_smiles,

        "isomeric":
            compound.isomeric_smiles
    }


# ==========================================================
# PUBCHEMPY — INCHI
# ==========================================================

def pubchem_inchi(
    query,
    namespace="name"
):
    """
    Retrieve InChI and InChIKey.
    """

    compound = pubchem_compound(
        query,
        namespace
    )

    if compound is None:

        return None

    return {
        "inchi":
            compound.inchi,

        "inchikey":
            compound.inchikey
    }


# ==========================================================
# PUBCHEMPY — MOLECULAR WEIGHT
# ==========================================================

def pubchem_molecular_weight(
    query,
    namespace="name"
):
    """
    Retrieve PubChem molecular weight.
    """

    compound = pubchem_compound(
        query,
        namespace
    )

    if compound is None:

        return None

    return compound.molecular_weight


# ==========================================================
# PUBCHEMPY — SUBSTRUCTURE SEARCH
# ==========================================================

def pubchem_substructure_search(
    smiles
):
    """
    Search PubChem using a SMILES-based structure query.
    """

    pcp = _get_pubchempy()

    return pcp.get_compounds(
        str(smiles),
        "smiles"
    )


# ==========================================================
# PYMatGEN — COMPOSITION
# ==========================================================

def pymatgen_composition(
    formula
):
    """
    Create a pymatgen Composition object.
    """

    from pymatgen.core import Composition

    return Composition(
        str(formula)
    )


# ==========================================================
# PYMatGEN — COMPOSITION INFORMATION
# ==========================================================

def pymatgen_composition_info(
    formula
):
    """
    Return detailed composition information.
    """

    composition = pymatgen_composition(
        formula
    )

    return {
        "formula":
            composition.formula,

        "reduced_formula":
            composition.reduced_formula,

        "iupac_formula":
            composition.iupac_formula,

        "weight":
            composition.weight,

        "elements":
            [
                str(element)
                for element in composition.elements
            ],

        "num_atoms":
            composition.num_atoms,

        "average_electroneg":
            composition.average_electroneg,

        "to_reduced_dict":
            composition.to_reduced_dict(),
    }


# ==========================================================
# PYMatGEN — OXIDATION STATES
# ==========================================================

def pymatgen_add_oxidation_states(
    formula,
    oxidation_states
):
    """
    Create a composition with oxidation states.

    Example:

        pymatgen_add_oxidation_states(
            "Fe2O3",
            {"Fe": 3, "O": -2}
        )
    """

    from pymatgen.core import Composition

    composition = Composition(
        str(formula)
    )

    return composition.add_charges_from_oxi_state_guesses()


# ==========================================================
# PYMatGEN — STRUCTURE FROM CIF
# ==========================================================

def pymatgen_structure_from_cif(
    filename
):
    """
    Load a crystal structure from a CIF file.
    """

    from pymatgen.core import Structure

    return Structure.from_file(
        str(filename)
    )


# ==========================================================
# PYMatGEN — STRUCTURE INFORMATION
# ==========================================================

def pymatgen_structure_info(
    structure
):
    """
    Return important crystal-structure information.
    """

    return {
        "formula":
            structure.composition.formula,

        "reduced_formula":
            structure.composition.reduced_formula,

        "num_sites":
            len(structure),

        "volume":
            structure.volume,

        "density":
            structure.density,

        "lattice":
            structure.lattice.matrix.tolist(),

        "space_group":
            None,
    }


# ==========================================================
# PYMatGEN — SPACE GROUP
# ==========================================================

def pymatgen_space_group(
    structure
):
    """
    Determine the space-group symbol and number.
    """

    from pymatgen.symmetry.analyzer import (
        SpacegroupAnalyzer
    )

    analyzer = SpacegroupAnalyzer(
        structure
    )

    return {
        "symbol":
            analyzer.get_space_group_symbol(),

        "number":
            analyzer.get_space_group_number()
    }


# ==========================================================
# PYMatGEN — CONVENTIONAL CELL
# ==========================================================

def pymatgen_conventional_cell(
    structure
):
    """
    Convert a structure to its conventional standard cell.
    """

    from pymatgen.symmetry.analyzer import (
        SpacegroupAnalyzer
    )

    analyzer = SpacegroupAnalyzer(
        structure
    )

    return analyzer.get_conventional_standard_structure()


# ==========================================================
# PYMatGEN — PRIMITIVE CELL
# ==========================================================

def pymatgen_primitive_cell(
    structure
):
    """
    Convert a structure to a primitive standard cell.
    """

    from pymatgen.symmetry.analyzer import (
        SpacegroupAnalyzer
    )

    analyzer = SpacegroupAnalyzer(
        structure
    )

    return analyzer.get_primitive_standard_structure()


# ==========================================================
# PYMatGEN — DISTANCE
# ==========================================================

def pymatgen_site_distance(
    structure,
    site1,
    site2
):
    """
    Calculate the distance between two sites.
    """

    return structure.get_distance(
        int(site1),
        int(site2)
    )


# ==========================================================
# PYMatGEN — NEIGHBORS
# ==========================================================

def pymatgen_neighbors(
    structure,
    site_index,
    radius
):
    """
    Find neighboring sites around a selected site.
    """

    site = structure[
        int(site_index)
    ]

    return structure.get_neighbors(
        site,
        float(radius)
    )


# ==========================================================
# PYMatGEN — RDF
# ==========================================================

def pymatgen_rdf(
    structure,
    rmax=10.0,
    dr=0.1
):
    """
    Calculate a radial distribution function for a crystal.
    """

    from pymatgen.analysis.diffraction.xrd import (
        XRDCalculator
    )

    try:

        from pymatgen.analysis.local_env import (
            VoronoiNN
        )

        distances = []

        for index in range(
            len(structure)
        ):

            neighbors = structure.get_neighbors(
                structure[index],
                float(rmax)
            )

            for neighbor in neighbors:

                distances.append(
                    neighbor.nn_distance
                )

        return distances

    except Exception as exc:

        raise RuntimeError(
            f"Unable to calculate RDF: {exc}"
        )


# ==========================================================
# PYMatGEN — XRD PATTERN
# ==========================================================

def pymatgen_xrd_pattern(
    structure,
    wavelength="CuKa"
):
    """
    Calculate an X-ray diffraction pattern.
    """

    from pymatgen.analysis.diffraction.xrd import (
        XRDCalculator
    )

    calculator = XRDCalculator(
        wavelength=wavelength
    )

    pattern = calculator.get_pattern(
        structure
    )

    return {
        "two_theta":
            pattern.x.tolist(),

        "intensity":
            pattern.y.tolist(),

        "hkls":
            pattern.hkls,

        "d_spacing":
            pattern.d_hkls.tolist(),
    }


# ==========================================================
# PYMatGEN — ELECTRONIC STRUCTURE SUMMARY
# ==========================================================

def pymatgen_structure_composition(
    structure
):
    """
    Return the elemental composition of a structure.
    """

    return {
        "formula":
            structure.composition.formula,

        "reduced_formula":
            structure.composition.reduced_formula,

        "elements":
            [
                str(x)
                for x in structure.composition.elements
            ],

        "amounts":
            dict(
                structure.composition.get_el_amt_dict()
            )
    }


# ==========================================================
# RDKIT — MOLECULE FROM SMILES
# ==========================================================

def rdkit_molecule_from_smiles(
    smiles
):
    """
    Convert SMILES into an RDKit molecule.
    """

    from rdkit import Chem

    molecule = Chem.MolFromSmiles(
        str(smiles)
    )

    if molecule is None:

        raise ValueError(
            "Invalid SMILES string."
        )

    return molecule


# ==========================================================
# RDKIT — SMILES
# ==========================================================

def rdkit_smiles(
    molecule
):
    """
    Convert an RDKit molecule to canonical SMILES.
    """

    from rdkit import Chem

    return Chem.MolToSmiles(
        molecule
    )


# ==========================================================
# RDKIT — MOLECULAR FORMULA
# ==========================================================

def rdkit_formula(
    molecule
):
    """
    Calculate the molecular formula of an RDKit molecule.
    """

    from rdkit.Chem import (
        rdMolDescriptors
    )

    return rdMolDescriptors.CalcMolFormula(
        molecule
    )


# ==========================================================
# RDKIT — MOLECULAR WEIGHT
# ==========================================================

def rdkit_molecular_weight(
    molecule
):
    """
    Calculate molecular weight.
    """

    from rdkit.Chem import (
        Descriptors
    )

    return Descriptors.MolWt(
        molecule
    )


# ==========================================================
# RDKIT — EXACT MASS
# ==========================================================

def rdkit_exact_mass(
    molecule
):
    """
    Calculate exact molecular mass.
    """

    from rdkit.Chem import (
        Descriptors
    )

    return Descriptors.ExactMolWt(
        molecule
    )


# ==========================================================
# RDKIT — TPSA
# ==========================================================

def rdkit_tpsa(
    molecule
):
    """
    Calculate topological polar surface area.
    """

    from rdkit.Chem import (
        Descriptors
    )

    return Descriptors.TPSA(
        molecule
    )


# ==========================================================
# RDKIT — LOGP
# ==========================================================

def rdkit_logp(
    molecule
):
    """
    Calculate Crippen logP.
    """

    from rdkit.Chem import (
        Crippen
    )

    return Crippen.MolLogP(
        molecule
    )


# ==========================================================
# RDKIT — H-BOND DONORS
# ==========================================================

def rdkit_hbond_donors(
    molecule
):
    """
    Count hydrogen-bond donors.
    """

    from rdkit.Chem import (
        Lipinski
    )

    return Lipinski.NumHDonors(
        molecule
    )


# ==========================================================
# RDKIT — H-BOND ACCEPTORS
# ==========================================================

def rdkit_hbond_acceptors(
    molecule
):
    """
    Count hydrogen-bond acceptors.
    """

    from rdkit.Chem import (
        Lipinski
    )

    return Lipinski.NumHAcceptors(
        molecule
    )


# ==========================================================
# RDKIT — ROTATABLE BONDS
# ==========================================================

def rdkit_rotatable_bonds(
    molecule
):
    """
    Count rotatable bonds.
    """

    from rdkit.Chem import (
        Lipinski
    )

    return Lipinski.NumRotatableBonds(
        molecule
    )


# ==========================================================
# RDKIT — RING COUNT
# ==========================================================

def rdkit_ring_count(
    molecule
):
    """
    Count rings in a molecule.
    """

    return int(
        molecule.GetRingInfo().NumRings()
    )


# ==========================================================
# RDKIT — ATOM COUNT
# ==========================================================

def rdkit_atom_count(
    molecule
):
    """
    Count atoms.
    """

    return molecule.GetNumAtoms()


# ==========================================================
# RDKIT — BOND COUNT
# ==========================================================

def rdkit_bond_count(
    molecule
):
    """
    Count bonds.
    """

    return molecule.GetNumBonds()


# ==========================================================
# RDKIT — 3D CONFORMER
# ==========================================================

def rdkit_generate_3d(
    molecule
):
    """
    Generate a 3D conformer for a molecule.
    """

    from rdkit import Chem
    from rdkit.Chem import AllChem

    molecule = Chem.AddHs(
        molecule
    )

    result = AllChem.EmbedMolecule(
        molecule
    )

    if result != 0:

        raise RuntimeError(
            "RDKit could not generate a 3D conformer."
        )

    AllChem.UFFOptimizeMolecule(
        molecule
    )

    return molecule

# ==========================================================
# RDKIT — SUBSTRUCTURE SEARCH
# ==========================================================

def rdkit_substructure_search(
    molecule,
    query_smiles
):
    """
    Determine whether a molecule contains a specified
    substructure.
    """

    from rdkit import Chem

    query = Chem.MolFromSmarts(
        str(query_smiles)
    )

    if query is None:

        raise ValueError(
            "Invalid SMARTS pattern."
        )

    return molecule.HasSubstructMatch(
        query
    )


# ==========================================================
# RDKIT — DESCRIPTOR REPORT
# ==========================================================

def rdkit_descriptor_report(
    smiles
):
    """
    Generate a broad molecular descriptor report from SMILES.
    """

    molecule = rdkit_molecule_from_smiles(
        smiles
    )

    return {
        "smiles":
            rdkit_smiles(molecule),

        "formula":
            rdkit_formula(molecule),

        "molecular_weight":
            rdkit_molecular_weight(molecule),

        "exact_mass":
            rdkit_exact_mass(molecule),

        "TPSA":
            rdkit_tpsa(molecule),

        "logP":
            rdkit_logp(molecule),

        "HBD":
            rdkit_hbond_donors(molecule),

        "HBA":
            rdkit_hbond_acceptors(molecule),

        "rotatable_bonds":
            rdkit_rotatable_bonds(molecule),

        "rings":
            rdkit_ring_count(molecule),

        "atoms":
            rdkit_atom_count(molecule),

        "bonds":
            rdkit_bond_count(molecule),
    }


# ==========================================================
# SPGLIB — SPACE GROUP
# ==========================================================

def _spglib_spacegroup_validated(
    lattice,
    positions=None,
    numbers=None,
    symprec=1e-5
):
    """
    Determine the crystallographic space group
    using Spglib.

    Parameters
    ----------
    lattice:
        3x3 lattice matrix.

    positions:
        Fractional atomic coordinates.

    numbers:
        Atomic numbers for each atom.

    symprec:
        Symmetry tolerance.

    Example:

        spglib_spacegroup(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ],
            [
                [0, 0, 0]
            ],
            [1]
        )
    """

    import numpy as np

    spglib = _get_spglib()

    # Accept either three separate values or a complete cell tuple/list.
    if positions is None and numbers is None:
        try:
            lattice, positions, numbers = lattice
        except (TypeError, ValueError):
            raise ValueError(
                "Pass lattice, positions, and numbers, or one "
                "(lattice, positions, numbers) cell."
            ) from None
    elif positions is None or numbers is None:
        raise ValueError(
            "positions and numbers must be supplied together."
        )

    try:
        lattice = np.asarray(lattice, dtype=float)
        positions = np.asarray(positions, dtype=float)
        raw_numbers = np.asarray(numbers)
        numbers = np.asarray(numbers, dtype=int)
        symprec = float(symprec)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(
            "lattice, positions, numbers, and symprec must contain "
            "valid numeric values."
        ) from exc

    if lattice.shape != (3, 3):
        raise ValueError(
            f"lattice must have shape (3, 3); got {lattice.shape}."
        )
    if not np.isfinite(lattice).all():
        raise ValueError("lattice must contain only finite values.")
    if abs(float(np.linalg.det(lattice))) < 1e-12:
        raise ValueError("lattice must be nonsingular.")

    if positions.ndim != 2 or positions.shape[1:] != (3,):
        raise ValueError(
            "positions must have shape (N, 3); "
            f"got {positions.shape}."
        )
    if len(positions) == 0:
        raise ValueError("the cell must contain at least one atom.")
    if not np.isfinite(positions).all():
        raise ValueError("positions must contain only finite values.")

    if numbers.ndim != 1 or len(numbers) != len(positions):
        raise ValueError(
            "numbers must contain exactly one atomic number per position."
        )
    try:
        if not np.isfinite(raw_numbers.astype(float)).all():
            raise ValueError("atomic numbers must be finite integers.")
        if not np.equal(raw_numbers.astype(float), numbers).all():
            raise ValueError("atomic numbers must be integers.")
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("atomic numbers must be finite integers.") from exc
    if np.any(numbers <= 0):
        raise ValueError("atomic numbers must be positive integers.")
    if not np.isfinite(symprec) or symprec <= 0:
        raise ValueError("symprec must be a positive finite number.")

    cell = (lattice, positions, numbers)

    try:
        dataset = spglib.get_symmetry_dataset(
            cell,
            symprec=symprec
        )
    except Exception as exc:
        raise ValueError(
            "Spglib failed while analyzing the validated cell. "
            "Check that positions are fractional coordinates and that "
            "the lattice and atomic numbers describe a valid structure."
        ) from exc

    if dataset is None:
        raise ValueError(
            "Spglib could not determine the "
            "space group for this structure."
        )

    # Prefer the object interface used by current Spglib versions;
    # retain a mapping fallback for older versions.
    symbol = getattr(dataset, "international", None)
    if symbol is None:
        try:
            symbol = dataset["international"]
        except (KeyError, TypeError, IndexError):
            symbol = None

    if symbol is None:
        raise ValueError(
            "Spglib returned a symmetry dataset "
            "without an international space-group symbol."
        )

    return str(symbol)

# ==========================================================
# SPGLIB — SYMMETRY DATA
# ==========================================================

def spglib_symmetry(
    lattice,
    positions,
    numbers,
    symprec=1e-5
):
    """
    Return symmetry operations for a crystal structure.
    """

    spglib = _get_spglib()

    cell = (
        lattice,
        positions,
        numbers
    )

    return spglib.get_symmetry(
        cell,
        symprec=float(symprec)
    )


# ==========================================================
# SPGLIB — DATASET
# ==========================================================

def spglib_dataset(
    lattice,
    positions,
    numbers,
    symprec=1e-5
):
    """
    Return the full symmetry dataset.
    """

    spglib = _get_spglib()

    cell = (
        lattice,
        positions,
        numbers
    )

    return spglib.get_symmetry_dataset(
        cell,
        symprec=float(symprec)
    )


# ==========================================================
# SPGLIB — STANDARDIZED CELL
# ==========================================================

def spglib_standardize_cell(
    lattice,
    positions,
    numbers,
    to_primitive=False,
    no_idealize=False,
    symprec=1e-5
):
    """
    Standardize a crystal cell.
    """

    spglib = _get_spglib()

    cell = (
        lattice,
        positions,
        numbers
    )

    return spglib.standardize_cell(
        cell,
        to_primitive=bool(
            to_primitive
        ),
        no_idealize=bool(
            no_idealize
        ),
        symprec=float(
            symprec
        )
    )


# ==========================================================
# SPGLIB — FIND PRIMITIVE CELL
# ==========================================================

def spglib_find_primitive(
    lattice,
    positions,
    numbers,
    symprec=1e-5
):
    """
    Find the primitive cell of a crystal structure.
    """

    spglib = _get_spglib()

    cell = (
        lattice,
        positions,
        numbers
    )

    return spglib.find_primitive(
        cell,
        symprec=float(symprec)
    )


# ==========================================================
# PYROLITE — COMPOSITION OBJECT
# ==========================================================

def pyrolite_composition(
    data
):
    """
    Create a pyrolite composition object.

    This is useful for geochemical/mineralogical calculations.
    """

    try:

        from pyrolite.geochem import (
            norm_to
        )

    except Exception:

        pass

    return data


# ==========================================================
# PYROLITE — OXIDE TO ELEMENT CONVERSION
# ==========================================================

def pyrolite_oxide_to_element(
    composition
):
    """
    Convert oxide composition information into elemental
    equivalents where pyrolite provides the required utility.
    """

    try:

        from pyrolite.geochem.transform import (
            convert_chemistry
        )

        return convert_chemistry(
            composition,
            logdata=False
        )

    except Exception as exc:

        raise RuntimeError(
            f"Pyrolite conversion failed: {exc}"
        )


# ==========================================================
# PYROLITE — NORMALIZE COMPOSITION
# ==========================================================

def pyrolite_normalize(
    composition,
    components=None
):
    """
    Normalize geochemical composition data.

    Uses pyrolite's geochemical normalization tools where
    available.
    """

    from pyrolite.geochem import (
        norm_to
    )

    if components is None:

        components = list(
            composition.keys()
        )

    return norm_to(
        composition,
        components
    )


# ==========================================================
# PYROLITE — RE-NORMALIZE
# ==========================================================

def pyrolite_renormalize(
    composition,
    components=None
):
    """
    Re-normalize a geochemical composition.
    """

    total = sum(
        float(value)
        for value in composition.values()
    )

    if total == 0:

        raise ValueError(
            "Composition total cannot be zero."
        )

    return {
        key:
            float(value)
            / total
            * 100.0

        for key, value
        in composition.items()
    }


# ==========================================================
# MATERIALS — CRYSTAL REPORT
# ==========================================================

def materials_crystal_report(
    structure
):
    """
    Produce a combined pymatgen/spglib crystal report.
    """

    result = {}

    try:

        result["composition"] = (
            pymatgen_structure_composition(
                structure
            )
        )

    except Exception as exc:

        result["composition_error"] = str(exc)

    try:

        result["structure"] = (
            pymatgen_structure_info(
                structure
            )
        )

    except Exception as exc:

        result["structure_error"] = str(exc)

    try:

        result["space_group"] = (
            pymatgen_space_group(
                structure
            )
        )

    except Exception as exc:

        result["space_group_error"] = str(exc)

    return result


# ==========================================================
# MOLECULAR + PUBCHEM REPORT
# ==========================================================

def molecular_database_report(
    query,
    namespace="name"
):
    """
    Combine PubChem and RDKit information.

    PubChem provides database information while RDKit
    calculates molecular descriptors locally.
    """

    result = {}

    try:

        result["pubchem"] = (
            pubchem_compound_info(
                query,
                namespace
            )
        )

    except Exception as exc:

        result["pubchem_error"] = str(exc)

    try:

        smiles = pubchem_smiles(
            query,
            namespace
        )

        if smiles:

            result["rdkit"] = (
                rdkit_descriptor_report(
                    smiles["canonical"]
                )
            )

    except Exception as exc:

        result["rdkit_error"] = str(exc)

    return result


# ==========================================================
# CHEMISTRY PART 3 STATUS
# ==========================================================

def chemistry_part3_status():
    """
    Display availability of Chemistry Part 3 packages.
    """

    package_names = [
        "pubchempy",
        "pymatgen",
        "pyrolite",
        "rdkit",
        "spglib",
    ]

    results = {}

    print()
    print("=" * 75)
    print(
        "DAVE — CHEMISTRY PART 3 PACKAGE STATUS"
    )
    print("=" * 75)
    print()

    for package_name in package_names:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<18} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<18} unavailable"
            )

    print()

    return results


# ==========================================================
# CHEMISTRY PART 3 SELF TEST
# ==========================================================

def chemistry_part3_selftest(
    verbose=True
):
    """
    Test Chemistry Part 3 functionality.
    """

    tests = []


    # ------------------------------------------------------
    # PUBCHEMPY
    # ------------------------------------------------------

    try:

        result = pubchem_compound_info(
            "water"
        )

        tests.append(
            (
                "pubchempy",
                result is not None
                and result.get(
                    "molecular_formula"
                ) == "H2O"
            )
        )

    except Exception as exc:

        tests.append(
            (
                "pubchempy",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PYMatGEN
    # ------------------------------------------------------

    try:

        info = pymatgen_composition_info(
            "Fe2O3"
        )

        tests.append(
            (
                "pymatgen",
                info["reduced_formula"] == "Fe2O3"
            )
        )

    except Exception as exc:

        tests.append(
            (
                "pymatgen",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # RDKIT
    # ------------------------------------------------------

    try:

        report = rdkit_descriptor_report(
            "CCO"
        )

        tests.append(
            (
                "rdkit",
                report["formula"] == "C2H6O"
            )
        )

    except Exception as exc:

        tests.append(
            (
                "rdkit",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # SPGLIB
    # ------------------------------------------------------

    try:

        import numpy as np

        lattice = np.eye(3)

        positions = np.array([
            [0.0, 0.0, 0.0]
        ])

        numbers = np.array([
            1
        ])

        result = spglib_spacegroup(
            lattice,
            positions,
            numbers
        )

        tests.append(
            (
                "spglib",
                result is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "spglib",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PYROLITE
    # ------------------------------------------------------

    try:

        composition = {
            "SiO2": 60.0,
            "Al2O3": 20.0,
            "FeO": 10.0,
            "MgO": 10.0,
        }

        result = pyrolite_renormalize(
            composition
        )

        tests.append(
            (
                "pyrolite",
                abs(
                    sum(result.values())
                    - 100.0
                ) < 1e-8
            )
        )

    except Exception as exc:

        tests.append(
            (
                "pyrolite",
                False,
                str(exc)
            )
        )


    # ======================================================
    # RESULTS
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 75)
        print(
            "DAVE — CHEMISTRY PART 3 SELF TEST"
        )
        print("=" * 75)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 75)

        print(
            f"Passed: {passed}"
        )

        print(
            f"Failed: {failed}"
        )

        print(
            f"Total:  {len(tests)}"
        )

        print("-" * 75)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# CHEMISTRY PART 3 HELP
# ==========================================================

def chemistry_part3_help():

    print("""
==============================================================================
DAVE — CHEMISTRY / MATERIALS SCIENCE PART 3
==============================================================================

PUBCHEMPY
---------

    pubchem_search(
        "aspirin"
    )

    pubchem_compound(
        "water"
    )

    pubchem_compound_info(
        "aspirin"
    )

    pubchem_formula(
        "caffeine"
    )

    pubchem_smiles(
        "ethanol"
    )

    pubchem_inchi(
        "water"
    )

    pubchem_molecular_weight(
        "glucose"
    )

    molecular_database_report(
        "aspirin"
    )


PYMatGEN — COMPOSITIONS
-----------------------

    pymatgen_composition(
        "Fe2O3"
    )

    pymatgen_composition_info(
        "Fe2O3"
    )

    pymatgen_structure_composition(
        structure
    )


PYMatGEN — CRYSTALS
-------------------

    pymatgen_structure_from_cif(
        "structure.cif"
    )

    pymatgen_structure_info(
        structure
    )

    pymatgen_space_group(
        structure
    )

    pymatgen_conventional_cell(
        structure
    )

    pymatgen_primitive_cell(
        structure
    )

    pymatgen_site_distance(
        structure,
        0,
        1
    )

    pymatgen_neighbors(
        structure,
        0,
        3.0
    )


PYMatGEN — DIFFRACTION
----------------------

    pymatgen_xrd_pattern(
        structure
    )


RDKIT
-----

    molecule = rdkit_molecule_from_smiles(
        "CCO"
    )

    rdkit_smiles(
        molecule
    )

    rdkit_formula(
        molecule
    )

    rdkit_molecular_weight(
        molecule
    )

    rdkit_exact_mass(
        molecule
    )

    rdkit_tpsa(
        molecule
    )

    rdkit_logp(
        molecule
    )

    rdkit_hbond_donors(
        molecule
    )

    rdkit_hbond_acceptors(
        molecule
    )

    rdkit_rotatable_bonds(
        molecule
    )

    rdkit_ring_count(
        molecule
    )

    rdkit_atom_count(
        molecule
    )

    rdkit_bond_count(
        molecule
    )

    rdkit_descriptor_report(
        "CCO"
    )


SPGLIB
------

    spglib_spacegroup(
        lattice,
        positions,
        numbers
    )

    spglib_symmetry(
        lattice,
        positions,
        numbers
    )

    spglib_dataset(
        lattice,
        positions,
        numbers
    )

    spglib_standardize_cell(
        lattice,
        positions,
        numbers
    )

    spglib_find_primitive(
        lattice,
        positions,
        numbers
    )


PYROLITE
--------

    pyrolite_normalize(
        composition
    )

    pyrolite_renormalize(
        composition
    )

    pyrolite_oxide_to_element(
        composition
    )


COMBINED MATERIALS TOOLS
------------------------

    materials_crystal_report(
        structure
    )

    molecular_database_report(
        "aspirin"
    )


TESTING
-------

    chemistry_part3_status()

    chemistry_part3_selftest()

==============================================================================
""")

# ==========================================================
# DAVE
# CHEMISTRY / CHEMICAL ENGINEERING INTEGRATION
# PART 4
# ==========================================================
#
# Packages covered:
#
#   chemicals
#   thermo
#   fluids
#   radioactivedecay
#
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_chemicals():
    """
    Load chemicals lazily.
    """
    return load_scientific_package("chemicals")


def _get_thermo():
    """
    Load thermo lazily.
    """
    return load_scientific_package("thermo")


def _get_fluids():
    """
    Load fluids lazily.
    """
    return load_scientific_package("fluids")


def _get_radioactivedecay():
    """
    Load radioactivedecay lazily.
    """
    return load_scientific_package(
        "radioactivedecay"
    )


# ==========================================================
# CHEMICALS — CONSTANT LOOKUP
# ==========================================================

def chemicals_constant(
    name
):
    """
    Look up a constant from chemicals.constants where
    available.
    """

    import chemicals.constants as constants

    if hasattr(
        constants,
        str(name)
    ):

        return getattr(
            constants,
            str(name)
        )

    raise AttributeError(
        f"chemicals.constants has no attribute '{name}'"
    )


# ==========================================================
# CHEMICALS — CAS PROPERTY LOOKUP
# ==========================================================

def chemicals_property(
    function_name,
    *args,
    **kwargs
):
    """
    Generic wrapper around a chemicals function.

    Example:

        chemicals_property(
            "Tb",
            "64-17-5"
        )

    The function is resolved dynamically from the
    chemicals package.
    """

    chemicals = _get_chemicals()

    function = getattr(
        chemicals,
        str(function_name),
        None
    )

    if function is None:

        raise AttributeError(
            f"chemicals does not expose "
            f"'{function_name}' at the top level."
        )

    return function(
        *args,
        **kwargs
    )


# ==========================================================
# CHEMICALS — BOILING POINT
# ==========================================================

def chemicals_boiling_point(
    CASRN
):
    """
    Retrieve a compound's normal boiling point.
    """

    from chemicals.phase_change import Tb

    return Tb(
        CASRN
    )


# ==========================================================
# CHEMICALS — MELTING POINT
# ==========================================================

def chemicals_melting_point(
    CASRN
):
    """
    Retrieve a compound's melting point.
    """

    from chemicals.phase_change import Tm

    return Tm(
        CASRN
    )


# ==========================================================
# CHEMICALS — VAPOR PRESSURE
# ==========================================================

def chemicals_vapor_pressure(
    CASRN,
    T
):
    """
    Calculate vapor pressure at temperature T in kelvin.

    The chemicals package chooses an available correlation
    for the requested compound.
    """

    from chemicals.vapor_pressure import (
        VaporPressure
    )

    correlation = VaporPressure(
        CASRN=CASRN,
        T=float(T)
    )

    return correlation


# ==========================================================
# CHEMICALS — HEAT CAPACITY
# ==========================================================

def chemicals_heat_capacity_gas(
    CASRN,
    T
):
    """
    Calculate gas-phase heat capacity at temperature T.
    """

    from chemicals.heat_capacity import (
        HeatCapacityGas
    )

    cp = HeatCapacityGas(
        CASRN=CASRN
    )

    return cp(
        float(T)
    )


# ==========================================================
# CHEMICALS — LIQUID HEAT CAPACITY
# ==========================================================

def chemicals_heat_capacity_liquid(
    CASRN,
    T
):
    """
    Calculate liquid heat capacity at temperature T.
    """

    from chemicals.heat_capacity import (
        HeatCapacityLiquid
    )

    cp = HeatCapacityLiquid(
        CASRN=CASRN
    )

    return cp(
        float(T)
    )


# ==========================================================
# CHEMICALS — GAS DENSITY
# ==========================================================

def chemicals_gas_density(
    CASRN,
    T,
    P
):
    """
    Calculate ideal-gas density.

    T in K
    P in Pa
    """

    from chemicals import rho_gas

    return rho_gas(
        T=float(T),
        P=float(P),
        MW=chemicals_molecular_weight(
            CASRN
        )
    )


# ==========================================================
# CHEMICALS — LIQUID DENSITY
# ==========================================================

def chemicals_liquid_density(
    CASRN,
    T
):
    """
    Calculate liquid density where data are available.
    """

    from chemicals.density import DensityLiquid

    density = DensityLiquid(
        CASRN=CASRN
    )

    return density(
        float(T)
    )


# ==========================================================
# CHEMICALS — VISCOSITY
# ==========================================================

def chemicals_liquid_viscosity(
    CASRN,
    T
):
    """
    Calculate liquid viscosity.
    """

    from chemicals.viscosity import ViscosityLiquid

    viscosity = ViscosityLiquid(
        CASRN=CASRN
    )

    return viscosity(
        float(T)
    )


# ==========================================================
# CHEMICALS — THERMAL CONDUCTIVITY
# ==========================================================

def chemicals_liquid_thermal_conductivity(
    CASRN,
    T
):
    """
    Calculate liquid thermal conductivity.
    """

    from chemicals.thermal_conductivity import (
        ThermalConductivityLiquid
    )

    conductivity = ThermalConductivityLiquid(
        CASRN=CASRN
    )

    return conductivity(
        float(T)
    )


# ==========================================================
# CHEMICALS — DIFFUSIVITY
# ==========================================================

def chemicals_diffusivity(
    T,
    P,
    MW1,
    MW2,
    Vb1,
    Vb2
):
    """
    Estimate binary gas diffusivity using chemicals'
    diffusion-property correlations.

    Inputs depend on the selected correlation and are
    supplied in the units expected by chemicals.
    """

    from chemicals.diffusion import (
        Fuller
    )

    return Fuller(
        T=float(T),
        P=float(P),
        MW1=float(MW1),
        MW2=float(MW2),
        V_A=float(Vb1),
        V_B=float(Vb2)
    )


# ==========================================================
# THERMO — CHEMICAL OBJECT
# ==========================================================

def thermo_chemical(
    CASRN
):
    """
    Create a thermo Chemical object.
    """

    from thermo import Chemical

    return Chemical(
        CASRN
    )


# ==========================================================
# THERMO — CHEMICAL REPORT
# ==========================================================

def thermo_chemical_report(
    CASRN,
    T=298.15,
    P=101325
):
    """
    Produce a broad thermophysical-property report.
    """

    from thermo import Chemical

    chemical = Chemical(
        CASRN,
        T=float(T),
        P=float(P)
    )

    properties = [
        "CAS",
        "formula",
        "MW",
        "Tb",
        "Tm",
        "Tt",
        "Tc",
        "Pc",
        "Vc",
        "rho",
        "Cp",
        "Cpg",
        "Cpl",
        "mu",
        "mug",
        "mul",
        "k",
        "kg",
        "kl",
        "sigma",
        "Psat",
        "Hvap",
        "Hfus",
        "S",
        "H",
        "G",
    ]

    result = {}

    for prop in properties:

        try:

            result[prop] = getattr(
                chemical,
                prop
            )

        except Exception:

            result[prop] = None

    return result


# ==========================================================
# THERMO — IDEAL GAS MIXTURE
# ==========================================================

def thermo_ideal_gas_mixture(
    names,
    zs,
    T=298.15,
    P=101325
):
    """
    Create a thermo ideal-gas mixture.

    names:
        list of CAS numbers or compound identifiers

    zs:
        mole fractions
    """

    from thermo import (
        ChemicalConstantsPackage,
        PropertyCorrelationsPackage,
        CEOSGas,
        PRMIX,
    )

    constants, correlations = (
        ChemicalConstantsPackage.from_IDs(
            names
        )
    )

    gas = CEOSGas(
        PRMIX,
        constants,
        correlations,
        T=float(T),
        P=float(P),
        zs=list(zs)
    )

    return gas


# ==========================================================
# THERMO — MIXTURE REPORT
# ==========================================================

def thermo_mixture_report(
    names,
    zs,
    T=298.15,
    P=101325
):
    """
    Calculate useful mixture properties.
    """

    gas = thermo_ideal_gas_mixture(
        names,
        zs,
        T,
        P
    )

    result = {}

    for prop in (
        "T",
        "P",
        "MW",
        "rho",
        "Z",
        "H",
        "S",
        "G",
        "Cp",
        "Cv",
        "speed_of_sound",
        "mu",
        "k",
    ):

        try:

            result[prop] = getattr(
                gas,
                prop
            )

        except Exception:

            result[prop] = None

    return result


# ==========================================================
# THERMO — FLASH CALCULATION
# ==========================================================

def thermo_flash(
    names,
    zs,
    T=None,
    P=None,
    VF=None
):
    """
    Perform a simple vapor-liquid flash calculation.

    Exactly one appropriate pair of state specifications
    should be supplied.
    """

    from thermo import (
        FlashVL,
        ChemicalConstantsPackage,
        PropertyCorrelationsPackage,
    )

    constants, correlations = (
        ChemicalConstantsPackage.from_IDs(
            names
        )
    )

    flasher = FlashVL(
        constants,
        correlations
    )

    kwargs = {
        "zs": list(zs)
    }

    if T is not None:

        kwargs["T"] = float(T)

    if P is not None:

        kwargs["P"] = float(P)

    if VF is not None:

        kwargs["VF"] = float(VF)

    return flasher.flash(
        **kwargs
    )


# ==========================================================
# THERMO — PHASE EQUILIBRIUM REPORT
# ==========================================================

def thermo_flash_report(
    names,
    zs,
    T=None,
    P=None,
    VF=None
):
    """
    Return the major results of a flash calculation.
    """

    result = thermo_flash(
        names,
        zs,
        T=T,
        P=P,
        VF=VF
    )

    report = {}

    for prop in (
        "T",
        "P",
        "VF",
        "H",
        "S",
        "G",
        "Z",
        "MW",
        "rho",
    ):

        try:

            report[prop] = getattr(
                result,
                prop
            )

        except Exception:

            report[prop] = None

    return report


# ==========================================================
# FLUIDS — REYNOLDS NUMBER
# ==========================================================

def fluids_reynolds(
    rho,
    V,
    D,
    mu
):
    """
    Reynolds number.

    rho = density
    V   = velocity
    D   = characteristic diameter
    mu  = dynamic viscosity
    """

    from fluids.core import Reynolds

    return Reynolds(
        rho=float(rho),
        V=float(V),
        D=float(D),
        mu=float(mu)
    )


# ==========================================================
# FLUIDS — FANNING FRICTION FACTOR
# ==========================================================

def fluids_fanning_friction(
    Re,
    eD=0.0
):
    """
    Calculate Fanning friction factor.
    """

    from fluids.friction import (
        friction_factor
    )

    return friction_factor(
        Re=float(Re),
        eD=float(eD)
    )


# ==========================================================
# FLUIDS — DARCY FRICTION FACTOR
# ==========================================================

def fluids_darcy_friction(
    Re,
    eD=0.0
):
    """
    Calculate Darcy friction factor.
    """

    from fluids.friction import (
        friction_factor
    )

    fanning = friction_factor(
        Re=float(Re),
        eD=float(eD)
    )

    return 4.0 * fanning


# ==========================================================
# FLUIDS — PIPE PRESSURE DROP
# ==========================================================

def fluids_pipe_pressure_drop(
    rho,
    V,
    D,
    L,
    mu,
    roughness=0.0
):
    """
    Calculate pipe pressure drop using Darcy-Weisbach.
    """

    from fluids.friction import (
        friction_factor
    )

    Re = fluids_reynolds(
        rho,
        V,
        D,
        mu
    )

    eD = (
        float(roughness)
        / float(D)
    )

    f = friction_factor(
        Re=Re,
        eD=eD
    )

    g = 9.80665

    return (
        f
        * float(L)
        / float(D)
        * float(rho)
        * float(V) ** 2
        / 2.0
    )


# ==========================================================
# FLUIDS — VELOCITY FROM FLOW RATE
# ==========================================================

def fluids_velocity_from_flow(
    Q,
    D
):
    """
    Calculate average pipe velocity.

    Q = volumetric flow rate
    D = pipe diameter
    """

    import math

    area = (
        math.pi
        * float(D) ** 2
        / 4.0
    )

    return float(Q) / area


# ==========================================================
# FLUIDS — FLOW RATE FROM VELOCITY
# ==========================================================

def fluids_flow_rate(
    V,
    D
):
    """
    Calculate volumetric flow rate.
    """

    import math

    area = (
        math.pi
        * float(D) ** 2
        / 4.0
    )

    return (
        float(V)
        * area
    )


# ==========================================================
# FLUIDS — PUMP POWER
# ==========================================================

def fluids_pump_power(
    Q,
    dP,
    efficiency=1.0
):
    """
    Calculate pump power.

    Q in m^3/s
    dP in Pa
    efficiency between 0 and 1
    """

    efficiency = float(
        efficiency
    )

    if efficiency <= 0:

        raise ValueError(
            "Efficiency must be greater than zero."
        )

    return (
        float(Q)
        * float(dP)
        / efficiency
    )


# ==========================================================
# FLUIDS — ORIFICE FLOW
# ==========================================================

def fluids_orifice_flow(
    D,
    Do,
    P1,
    P2,
    rho,
    Cd=0.61
):
    """
    Calculate approximate incompressible orifice flow.
    """

    import math

    if P1 <= P2:

        raise ValueError(
            "P1 must be greater than P2."
        )

    area = (
        math.pi
        * float(Do) ** 2
        / 4.0
    )

    return (
        float(Cd)
        * area
        * (
            2.0
            * (
                float(P1)
                - float(P2)
            )
            / float(rho)
        ) ** 0.5
    )


# ==========================================================
# FLUIDS — STOKES LAW
# ==========================================================

def fluids_stokes_velocity(
    particle_diameter,
    particle_density,
    fluid_density,
    viscosity
):
    """
    Calculate terminal settling velocity using Stokes' law.
    """

    g = 9.80665

    return (
        (
            float(particle_diameter) ** 2
            * (
                float(particle_density)
                - float(fluid_density)
            )
            * g
        )
        /
        (
            18.0
            * float(viscosity)
        )
    )


# ==========================================================
# RADIOACTIVEDECAY — NUCLIDE
# ==========================================================

def radioactive_nuclide(
    nuclide
):
    """
    Create a radioactivedecay Nuclide object.
    """

    import radioactivedecay as rd

    return rd.Nuclide(
        str(nuclide)
    )


# ==========================================================
# RADIOACTIVEDECAY — DECAY CONSTANT
# ==========================================================

def radioactive_decay_constant(
    nuclide
):
    """
    Return decay constant in inverse seconds.
    """

    isotope = radioactive_nuclide(
        nuclide
    )

    return isotope.decay_constant


# ==========================================================
# RADIOACTIVEDECAY — HALF LIFE
# ==========================================================

def radioactive_half_life(
    nuclide
):
    """
    Return the half-life of a radionuclide.

    Example:

        radioactive_half_life("U-238")
    """

    isotope = radioactive_nuclide(
        nuclide
    )

    return isotope.half_life()

# ==========================================================
# RADIOACTIVEDECAY — ACTIVITY
# ==========================================================

def radioactive_activity(
    nuclide,
    quantity,
    time=0
):
    """
    Calculate activity after a specified time.

    quantity is the amount represented by the
    radioactivedecay package's Nuclide quantity system.
    """

    import radioactivedecay as rd

    isotope = rd.Nuclide(
        str(nuclide)
    )

    return isotope.activity(
        quantity,
        time
    )


# ==========================================================
# RADIOACTIVEDECAY — DECAY
# ==========================================================

def radioactive_decay(
    nuclide,
    quantity,
    time
):
    """
    Calculate the remaining quantity after decay.
    """

    import radioactivedecay as rd

    isotope = rd.Nuclide(
        str(nuclide)
    )

    return isotope.decay(
        quantity,
        time
    )


# ==========================================================
# RADIOACTIVEDECAY — DECAY CHAIN
# ==========================================================

def radioactive_decay_chain(
    nuclide
):
    """
    Return the decay chain of a radionuclide.
    """

    isotope = radioactive_nuclide(
        nuclide
    )

    return isotope.decay_chain()


# ==========================================================
# RADIOACTIVEDECAY — DECAY DATA
# ==========================================================

def radioactive_decay_data(
    nuclide
):
    """
    Return major decay information.
    """

    isotope = radioactive_nuclide(
        nuclide
    )

    result = {}

    for attribute in (
        "nuclide",
        "decay_constant",
        "progeny",
    ):

        try:

            result[attribute] = getattr(
                isotope,
                attribute
            )

        except Exception:

            result[attribute] = None

    try:

        result["half_life"] = (
            isotope.half_life()
        )

    except Exception:

        result["half_life"] = None

    try:

        result["decay_modes"] = (
            isotope.decay_modes()
        )

    except Exception:

        result["decay_modes"] = None

    return result


# ==========================================================
# RADIOACTIVEDECAY — NUCLIDE REPORT
# ==========================================================

def radioactive_nuclide_report(
    nuclide
):
    """
    Generate a broad radionuclide report.
    """

    return {
        "data":
            radioactive_decay_data(
                nuclide
            ),

        "decay_chain":
            radioactive_decay_chain(
                nuclide
            )
    }


# ==========================================================
# COMBINED THERMAL-FLUID REPORT
# ==========================================================

def thermo_fluid_report(
    CASRN,
    T=298.15,
    P=101325,
    pipe_diameter=None,
    velocity=None,
    pipe_length=None,
    roughness=0.0
):
    """
    Combine thermo properties with fluid-flow calculations.
    """

    result = {
        "thermo":
            thermo_chemical_report(
                CASRN,
                T,
                P
            )
    }

    if (
        pipe_diameter is not None
        and velocity is not None
        and pipe_length is not None
    ):

        thermo_data = result[
            "thermo"
        ]

        rho = thermo_data.get(
            "rho"
        )

        mu = thermo_data.get(
            "mu"
        )

        if (
            rho is not None
            and mu is not None
        ):

            Re = fluids_reynolds(
                rho,
                velocity,
                pipe_diameter,
                mu
            )

            dP = fluids_pipe_pressure_drop(
                rho,
                velocity,
                pipe_diameter,
                pipe_length,
                mu,
                roughness
            )

            result["fluid"] = {
                "Reynolds":
                    Re,

                "pressure_drop":
                    dP
            }

    return result


# ==========================================================
# CHEMISTRY PART 4 STATUS
# ==========================================================

def chemistry_part4_status():
    """
    Display availability of Chemistry Part 4 packages.
    """

    package_names = [
        "chemicals",
        "thermo",
        "fluids",
        "radioactivedecay",
    ]

    results = {}

    print()
    print("=" * 75)
    print(
        "DAVE — CHEMISTRY PART 4 PACKAGE STATUS"
    )
    print("=" * 75)
    print()

    for package_name in package_names:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<20} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<20} unavailable"
            )

    print()

    return results


# ==========================================================
# CHEMISTRY PART 4 SELF TEST
# ==========================================================

def chemistry_part4_selftest(
    verbose=True
):
    """
    Test Chemistry Part 4 functionality.
    """

    tests = []


    # ------------------------------------------------------
    # CHEMICALS
    # ------------------------------------------------------

    try:

        result = chemicals_boiling_point(
            "64-17-5"
        )

        tests.append(
            (
                "chemicals",
                result is not None
                and float(result) > 300
            )
        )

    except Exception as exc:

        tests.append(
            (
                "chemicals",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # THERMO
    # ------------------------------------------------------

    try:

        report = thermo_chemical_report(
            "64-17-5"
        )

        tests.append(
            (
                "thermo",
                report["MW"] is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "thermo",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # FLUIDS
    # ------------------------------------------------------

    try:

        Re = fluids_reynolds(
            1000.0,
            1.0,
            0.1,
            0.001
        )

        tests.append(
            (
                "fluids",
                Re > 0
            )
        )

    except Exception as exc:

        tests.append(
            (
                "fluids",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # RADIOACTIVEDECAY
    # ------------------------------------------------------

    try:

        half_life = radioactive_half_life(
            "Cs-137"
        )

        tests.append(
            (
                "radioactivedecay",
                half_life > 0
            )
        )

    except Exception as exc:

        tests.append(
            (
                "radioactivedecay",
                False,
                str(exc)
            )
        )


    # ======================================================
    # RESULTS
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 75)
        print(
            "DAVE — CHEMISTRY PART 4 SELF TEST"
        )
        print("=" * 75)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 75)

        print(
            f"Passed: {passed}"
        )

        print(
            f"Failed: {failed}"
        )

        print(
            f"Total:  {len(tests)}"
        )

        print("-" * 75)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# CHEMISTRY PART 4 HELP
# ==========================================================

def chemistry_part4_help():

    print("""
==============================================================================
DAVE — CHEMISTRY / CHEMICAL ENGINEERING PART 4
==============================================================================

CHEMICALS
---------

    chemicals_boiling_point(
        "64-17-5"
    )

    chemicals_melting_point(
        "64-17-5"
    )

    chemicals_vapor_pressure(
        "64-17-5",
        350
    )

    chemicals_heat_capacity_gas(
        "64-17-5",
        400
    )

    chemicals_heat_capacity_liquid(
        "64-17-5",
        300
    )

    chemicals_liquid_density(
        "64-17-5",
        300
    )

    chemicals_liquid_viscosity(
        "64-17-5",
        300
    )

    chemicals_liquid_thermal_conductivity(
        "64-17-5",
        300
    )


THERMO
------

    thermo_chemical(
        "64-17-5"
    )

    thermo_chemical_report(
        "64-17-5"
    )

    thermo_ideal_gas_mixture(
        ["64-17-5", "7732-18-5"],
        [0.5, 0.5]
    )

    thermo_mixture_report(
        ["64-17-5", "7732-18-5"],
        [0.5, 0.5]
    )

    thermo_flash(
        names,
        zs,
        T=350,
        P=101325
    )

    thermo_flash_report(
        names,
        zs,
        T=350,
        P=101325
    )


FLUIDS
------

    fluids_reynolds(
        rho,
        velocity,
        diameter,
        viscosity
    )

    fluids_fanning_friction(
        Re
    )

    fluids_darcy_friction(
        Re
    )

    fluids_pipe_pressure_drop(
        rho,
        velocity,
        diameter,
        length,
        viscosity
    )

    fluids_velocity_from_flow(
        flow_rate,
        diameter
    )

    fluids_flow_rate(
        velocity,
        diameter
    )

    fluids_pump_power(
        flow_rate,
        pressure_difference,
        efficiency
    )

    fluids_orifice_flow(
        pipe_diameter,
        orifice_diameter,
        P1,
        P2,
        density
    )

    fluids_stokes_velocity(
        particle_diameter,
        particle_density,
        fluid_density,
        viscosity
    )


RADIOACTIVEDECAY
----------------

    radioactive_nuclide(
        "Cs-137"
    )

    radioactive_decay_constant(
        "Cs-137"
    )

    radioactive_half_life(
        "Cs-137"
    )

    radioactive_activity(
        nuclide,
        quantity
    )

    radioactive_decay(
        nuclide,
        quantity,
        time
    )

    radioactive_decay_chain(
        "Cs-137"
    )

    radioactive_decay_data(
        "Cs-137"
    )

    radioactive_nuclide_report(
        "Cs-137"
    )


COMBINED TOOLS
--------------

    thermo_fluid_report(
        "64-17-5",
        T=300,
        P=101325,
        pipe_diameter=0.05,
        velocity=2.0,
        pipe_length=10
    )


TESTING
-------

    chemistry_part4_status()

    chemistry_part4_selftest()

==============================================================================
""")

# ==========================================================
# DAVE
# PHYSICS / SCIENTIFIC COMPUTING INTEGRATION
# PART 5
# ==========================================================
#
# Packages:
#
#   scipy
#   mpmath
#   uncertainties
#   unyt
#   quantities
#   lmfit
#   qutip
#   qmsolve
#   quantecon
#   plasmapy
#   MetPy
#
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_scipy():
    return load_scientific_package("scipy")


def _get_mpmath():
    return load_scientific_package("mpmath")


def _get_uncertainties():
    return load_scientific_package("uncertainties")


def _get_unyt():
    return load_scientific_package("unyt")


def _get_quantities():
    return load_scientific_package("quantities")


def _get_lmfit():
    return load_scientific_package("lmfit")


def _get_qutip():
    return load_scientific_package("qutip")


def _get_qmsolve():
    return load_scientific_package("qmsolve")


def _get_quantecon():
    return load_scientific_package("quantecon")


def _get_plasmapy():
    return load_scientific_package("plasmapy")


def _get_metpy():
    return load_scientific_package("metpy")


# ==========================================================
# SCIPY — ROOT FINDING
# ==========================================================

def scipy_root(
    function,
    initial_guess
):
    """
    Find a root of a scalar function.
    """

    from scipy.optimize import root_scalar

    result = root_scalar(
        function,
        x0=float(initial_guess)
    )

    return result


# ==========================================================
# SCIPY — BRACKETED ROOT
# ==========================================================

def scipy_brentq(
    function,
    a,
    b
):
    """
    Find a root using Brent's method.
    """

    from scipy.optimize import brentq

    return brentq(
        function,
        float(a),
        float(b)
    )


# ==========================================================
# SCIPY — MINIMIZATION
# ==========================================================

def scipy_minimize(
    function,
    initial_guess
):
    """
    Minimize a scalar/multivariable function.
    """

    from scipy.optimize import minimize

    result = minimize(
        function,
        initial_guess
    )

    return result


# ==========================================================
# SCIPY — CURVE FIT
# ==========================================================

def scipy_curve_fit(
    function,
    xdata,
    ydata,
    initial_guess=None
):
    """
    Nonlinear least-squares curve fitting.
    """

    import numpy as np
    from scipy.optimize import curve_fit

    kwargs = {}

    if initial_guess is not None:

        kwargs["p0"] = initial_guess

    parameters, covariance = curve_fit(
        function,
        np.asarray(xdata),
        np.asarray(ydata),
        **kwargs
    )

    return {
        "parameters": parameters,
        "covariance": covariance
    }


# ==========================================================
# SCIPY — INTERPOLATION
# ==========================================================

def scipy_interpolate(
    x,
    y,
    new_x,
    kind="linear"
):
    """
    Interpolate data.
    """

    import numpy as np
    from scipy.interpolate import interp1d

    interpolator = interp1d(
        np.asarray(x),
        np.asarray(y),
        kind=kind
    )

    return interpolator(
        np.asarray(new_x)
    )


# ==========================================================
# SCIPY — SPLINE
# ==========================================================

def scipy_spline(
    x,
    y,
    new_x
):
    """
    Cubic spline interpolation.
    """

    import numpy as np
    from scipy.interpolate import CubicSpline

    spline = CubicSpline(
        np.asarray(x),
        np.asarray(y)
    )

    return spline(
        np.asarray(new_x)
    )


# ==========================================================
# SCIPY — NUMERICAL INTEGRATION
# ==========================================================

def scipy_integrate(
    function,
    a,
    b
):
    """
    Numerically integrate a function.
    """

    from scipy.integrate import quad

    result, error = quad(
        function,
        float(a),
        float(b)
    )

    return {
        "value": result,
        "error": error
    }


# ==========================================================
# SCIPY — ODE
# ==========================================================

def scipy_ode(
    function,
    t_span,
    y0,
    t_eval=None
):
    """
    Solve an ordinary differential equation.
    """

    from scipy.integrate import solve_ivp

    result = solve_ivp(
        function,
        t_span,
        y0,
        t_eval=t_eval
    )

    return result


# ==========================================================
# SCIPY — LINEAR SYSTEM
# ==========================================================

def scipy_linear_solve(
    A,
    b
):
    """
    Solve A*x = b.
    """

    import numpy as np
    from scipy.linalg import solve

    return solve(
        np.asarray(A),
        np.asarray(b)
    )


# ==========================================================
# SCIPY — EIGENVALUES
# ==========================================================

def scipy_eigenvalues(
    matrix
):
    """
    Calculate eigenvalues and eigenvectors.
    """

    import numpy as np
    from scipy.linalg import eig

    values, vectors = eig(
        np.asarray(matrix)
    )

    return {
        "eigenvalues": values,
        "eigenvectors": vectors
    }


# ==========================================================
# SCIPY — FFT
# ==========================================================

def scipy_fft(
    data
):
    """
    Calculate a discrete Fourier transform.
    """

    import numpy as np
    from scipy.fft import fft

    return fft(
        np.asarray(data)
    )


# ==========================================================
# SCIPY — STATISTICS
# ==========================================================

def scipy_describe(
    data
):
    """
    Statistical summary.
    """

    import numpy as np
    from scipy.stats import describe

    return describe(
        np.asarray(data)
    )


# ==========================================================
# SCIPY — DISTRIBUTION
# ==========================================================

def scipy_normal_pdf(
    x,
    mean=0.0,
    standard_deviation=1.0
):
    """
    Normal-distribution probability density.
    """

    from scipy.stats import norm

    return norm.pdf(
        x,
        loc=float(mean),
        scale=float(standard_deviation)
    )


# ==========================================================
# SCIPY — SPECIAL FUNCTIONS
# ==========================================================

def scipy_special(
    function_name,
    *args
):
    """
    Call a scipy.special function by name.
    """

    from scipy import special

    function = getattr(
        special,
        str(function_name),
        None
    )

    if function is None:

        raise AttributeError(
            f"Unknown scipy.special function: "
            f"{function_name}"
        )

    return function(
        *args
    )


# ==========================================================
# MPMATH — HIGH PRECISION
# ==========================================================

def mpmath_set_precision(
    digits
):
    """
    Set mpmath decimal precision.
    """

    import mpmath as mp

    mp.mp.dps = int(digits)

    return mp.mp.dps


# ==========================================================
# MPMATH — HIGH PRECISION PI
# ==========================================================

def mpmath_pi(
    digits=50
):
    """
    Calculate pi to arbitrary precision.
    """

    import mpmath as mp

    old_dps = mp.mp.dps

    mp.mp.dps = int(digits)

    try:

        return mp.pi

    finally:

        mp.mp.dps = old_dps


# ==========================================================
# MPMATH — HIGH PRECISION EXPONENTIAL
# ==========================================================

def mpmath_exp(
    x,
    digits=50
):
    """
    Calculate exp(x) with arbitrary precision.
    """

    import mpmath as mp

    old_dps = mp.mp.dps
    mp.mp.dps = int(digits)

    try:

        return mp.exp(x)

    finally:

        mp.mp.dps = old_dps


# ==========================================================
# MPMATH — HIGH PRECISION LOGARITHM
# ==========================================================

def mpmath_log(
    x,
    digits=50
):
    """
    Calculate ln(x) with arbitrary precision.
    """

    import mpmath as mp

    old_dps = mp.mp.dps
    mp.mp.dps = int(digits)

    try:

        return mp.log(x)

    finally:

        mp.mp.dps = old_dps


# ==========================================================
# MPMATH — HIGH PRECISION ROOT
# ==========================================================

def mpmath_findroot(
    function,
    initial_guess,
    digits=50
):
    """
    High-precision numerical root finding.
    """

    import mpmath as mp

    old_dps = mp.mp.dps
    mp.mp.dps = int(digits)

    try:

        return mp.findroot(
            function,
            initial_guess
        )

    finally:

        mp.mp.dps = old_dps


# ==========================================================
# MPMATH — HIGH PRECISION INTEGRAL
# ==========================================================

def mpmath_integrate(
    function,
    a,
    b,
    digits=50
):
    """
    High-precision numerical integration.
    """

    import mpmath as mp

    old_dps = mp.mp.dps
    mp.mp.dps = int(digits)

    try:

        return mp.quad(
            function,
            [a, b]
        )

    finally:

        mp.mp.dps = old_dps


# ==========================================================
# UNCERTAINTIES — VALUE
# ==========================================================

def uncertainty_value(
    value,
    uncertainty
):
    """
    Create a value with uncertainty.
    """

    from uncertainties import ufloat

    return ufloat(
        float(value),
        float(uncertainty)
    )


# ==========================================================
# UNCERTAINTIES — ADDITION
# ==========================================================

def uncertainty_add(
    value1,
    uncertainty1,
    value2,
    uncertainty2
):
    """
    Add two uncertain quantities.
    """

    a = uncertainty_value(
        value1,
        uncertainty1
    )

    b = uncertainty_value(
        value2,
        uncertainty2
    )

    return a + b


# ==========================================================
# UNCERTAINTIES — PROPAGATED CALCULATION
# ==========================================================

def uncertainty_calculate(
    expression,
    values
):
    """
    Evaluate an expression containing uncertain values.

    Example:

        uncertainty_calculate(
            "x*y",
            {
                "x": (10, 0.2),
                "y": (5, 0.1)
            }
        )
    """

    from uncertainties import ufloat

    variables = {}

    for name, pair in values.items():

        variables[name] = ufloat(
            float(pair[0]),
            float(pair[1])
        )

    return eval(
        str(expression),
        {
            "__builtins__": {}
        },
        variables
    )


# ==========================================================
# UNCERTAINTIES — COMPONENTS
# ==========================================================

def uncertainty_components(
    value
):
    """
    Return nominal value and standard uncertainty.
    """

    return {
        "nominal":
            value.nominal_value,

        "standard_uncertainty":
            value.std_dev
    }


# ==========================================================
# UNYT — QUANTITY
# ==========================================================

def unyt_quantity(
    value,
    unit
):
    """
    Create a unyt quantity.
    """

    from unyt import u

    return (
        float(value)
        * getattr(u, str(unit))
    )


# ==========================================================
# UNYT — CONVERSION
# ==========================================================

def unyt_convert(
    value,
    from_unit,
    to_unit
):
    """
    Convert a quantity between unyt units.
    """

    from unyt import (
        Unit,
        unyt_quantity
    )

    quantity = unyt_quantity(
        float(value),
        Unit(str(from_unit))
    )

    return quantity.to(
        str(to_unit)
    )


# ==========================================================
# QUANTITIES — PHYSICAL QUANTITY
# ==========================================================

def quantities_value(
    value,
    unit
):
    """
    Create a python-quantities quantity.
    """

    import quantities as pq

    unit_object = getattr(
        pq,
        str(unit)
    )

    return (
        float(value)
        * unit_object
    )


# ==========================================================
# QUANTITIES — CONVERT
# ==========================================================

def quantities_convert(
    value,
    from_unit,
    to_unit
):
    """
    Convert between python-quantities units.
    """

    import quantities as pq

    source_unit = getattr(
        pq,
        str(from_unit)
    )

    target_unit = getattr(
        pq,
        str(to_unit)
    )

    quantity = (
        float(value)
        * source_unit
    )

    return quantity.rescale(
        target_unit
    )


# ==========================================================
# LMFIT — MODEL FIT
# ==========================================================

def lmfit_model_fit(
    function,
    xdata,
    ydata,
    parameters
):
    """
    Fit a model using lmfit.

    function should be an lmfit-compatible model function.
    """

    import numpy as np
    from lmfit import Model

    model = Model(
        function
    )

    params = model.make_params(
        **parameters
    )

    result = model.fit(
        np.asarray(ydata),
        params,
        x=np.asarray(xdata)
    )

    return result


# ==========================================================
# LMFIT — REPORT
# ==========================================================

def lmfit_report(
    result
):
    """
    Return the textual lmfit report.
    """

    return result.fit_report()


# ==========================================================
# LMFIT — PARAMETERS
# ==========================================================

def lmfit_parameters(
    result
):
    """
    Return fitted parameter values and uncertainties.
    """

    output = {}

    for name, parameter in (
        result.params.items()
    ):

        output[name] = {
            "value":
                parameter.value,

            "stderr":
                parameter.stderr,

            "min":
                parameter.min,

            "max":
                parameter.max,

            "vary":
                parameter.vary
        }

    return output


# ==========================================================
# QUTIP — BASIS STATE
# ==========================================================

def qutip_basis(
    dimension,
    state
):
    """
    Create a quantum basis state.
    """

    import qutip

    return qutip.basis(
        int(dimension),
        int(state)
    )


# ==========================================================
# QUTIP — QUBIT ZERO
# ==========================================================

def qutip_qubit_zero():
    """
    Return |0>.
    """

    import qutip

    return qutip.basis(
        2,
        0
    )


# ==========================================================
# QUTIP — QUBIT ONE
# ==========================================================

def qutip_qubit_one():
    """
    Return |1>.
    """

    import qutip

    return qutip.basis(
        2,
        1
    )


# ==========================================================
# QUTIP — PAULI MATRICES
# ==========================================================

def qutip_pauli(
    axis
):
    """
    Return a Pauli matrix.

    axis:
        x
        y
        z
    """

    import qutip

    axis = str(axis).lower()

    mapping = {
        "x": qutip.sigmax,
        "y": qutip.sigmay,
        "z": qutip.sigmaz
    }

    if axis not in mapping:

        raise ValueError(
            "axis must be x, y, or z"
        )

    return mapping[axis]()


# ==========================================================
# QUTIP — EXPECTATION VALUE
# ==========================================================

def qutip_expectation(
    operator,
    state
):
    """
    Calculate <operator> for a quantum state.
    """

    import qutip

    return qutip.expect(
        operator,
        state
    )


# ==========================================================
# QUTIP — DENSITY MATRIX
# ==========================================================

def qutip_density_matrix(
    state
):
    """
    Convert a state into a density matrix.
    """

    return state.proj()


# ==========================================================
# QUTIP — TENSOR PRODUCT
# ==========================================================

def qutip_tensor(
    *states
):
    """
    Calculate tensor product of quantum states/operators.
    """

    import qutip

    return qutip.tensor(
        *states
    )


# ==========================================================
# QUTIP — SCHRODINGER EVOLUTION
# ==========================================================

def qutip_schrodinger(
    Hamiltonian,
    state,
    times
):
    """
    Solve the time-dependent Schrödinger equation for
    a time-independent Hamiltonian.
    """

    import qutip

    result = qutip.sesolve(
        Hamiltonian,
        state,
        times
    )

    return result


# ==========================================================
# QUTIP — MASTER EQUATION
# ==========================================================

def qutip_master_equation(
    Hamiltonian,
    state,
    times,
    collapse_operators=None
):
    """
    Solve a Lindblad master equation.
    """

    import qutip

    if collapse_operators is None:

        collapse_operators = []

    return qutip.mesolve(
        Hamiltonian,
        state,
        times,
        collapse_operators
    )


# ==========================================================
# QMSOLVE — PACKAGE STATUS
# ==========================================================

def qmsolve_status():
    """
    Test whether qmsolve can be imported.

    qmsolve's API has changed between releases, so the
    loader is intentionally kept separate from the
    higher-level quantum wrappers.
    """

    try:

        module = _get_qmsolve()

        return {
            "available": True,
            "version":
                getattr(
                    module,
                    "__version__",
                    "unknown"
                )
        }

    except Exception as exc:

        return {
            "available": False,
            "error": str(exc)
        }


# ==========================================================
# QUANTECON — MARKOV CHAIN
# ==========================================================

def quantecon_markov_chain(
    transition_matrix
):
    """
    Create a QuantEcon Markov chain.
    """

    import numpy as np
    import quantecon as qe

    return qe.MarkovChain(
        np.asarray(
            transition_matrix,
            dtype=float
        )
    )


# ==========================================================
# QUANTECON — STATIONARY DISTRIBUTION
# ==========================================================

def quantecon_stationary_distribution(
    transition_matrix
):
    """
    Calculate the stationary distribution of a Markov chain.
    """

    import numpy as np
    import quantecon as qe

    mc = qe.MarkovChain(
        np.asarray(
            transition_matrix,
            dtype=float
        )
    )

    return mc.stationary_distributions


# ==========================================================
# QUANTECON — LINEAR QUADRATIC CONTROL
# ==========================================================

def quantecon_lq(
    Q,
    R,
    A,
    B
):
    """
    Solve a discrete-time linear-quadratic control problem.
    """

    import numpy as np
    import quantecon as qe

    problem = qe.LQ(
        np.asarray(Q, dtype=float),
        np.asarray(R, dtype=float),
        np.asarray(A, dtype=float),
        np.asarray(B, dtype=float)
    )

    return problem


# ==========================================================
# PLASMAPY — PARTICLE
# ==========================================================

def plasma_particle_info(symbol):
    """Return a compact information record for a PlasmaPy particle."""
    particle = plasma_particle(symbol)
    return {
        "symbol": str(particle),
        "mass": particle.mass,
        "charge": particle.charge,
    }

def plasma_particle(
    symbol
):
    """
    Create a PlasmaPy Particle.
    """

    from plasmapy.particles import Particle

    return Particle(
        str(symbol)
    )


# ==========================================================
# PLASMAPY — PARTICLE MASS
# ==========================================================

def plasma_particle_mass(
    symbol
):
    """
    Return particle mass.
    """

    particle = plasma_particle(
        symbol
    )

    return particle.mass


# ==========================================================
# PLASMAPY — PARTICLE CHARGE
# ==========================================================

def plasma_particle_charge(
    symbol
):
    """
    Return particle charge.
    """

    particle = plasma_particle(
        symbol
    )

    return particle.charge


# ==========================================================
# PLASMAPY — PARTICLE NUMBER
# ==========================================================

def plasma_particle_number(
    symbol
):
    """
    Return particle number.
    """

    particle = plasma_particle(
        symbol
    )

    return particle.number


# ==========================================================
# PLASMAPY — DEBYE LENGTH
# ==========================================================

def plasma_debye_length(
    temperature,
    electron_density
):
    """
    Calculate the electron Debye length.

    temperature:
        astropy quantity

    electron_density:
        astropy quantity
    """

    from plasmapy.formulary import (
        Debye_length
    )

    return Debye_length(
        temperature,
        electron_density
    )


# ==========================================================
# PLASMAPY — PLASMA FREQUENCY
# ==========================================================

def plasma_frequency(
    electron_density
):
    """
    Calculate electron plasma frequency.
    """

    from plasmapy.formulary import (
        plasma_frequency
    )

    return plasma_frequency(
        electron_density
    )


# ==========================================================
# PLASMAPY — GYROFREQUENCY
# ==========================================================

def plasma_gyrofrequency(
    B,
    particle="e-"
):
    """
    Calculate particle gyrofrequency.
    """

    from plasmapy.formulary import (
        gyrofrequency
    )

    return gyrofrequency(
        B,
        particle
    )


# ==========================================================
# PLASMAPY — THERMAL SPEED
# ==========================================================

def plasma_thermal_speed(
    temperature,
    particle="e-"
):
    """
    Calculate thermal speed.
    """

    from plasmapy.formulary import (
        thermal_speed
    )

    return thermal_speed(
        temperature,
        particle
    )

# ==========================================================
# METPY — POTENTIAL TEMPERATURE
# ==========================================================

def metpy_potential_temperature(
    pressure,
    temperature
):
    """
    Calculate potential temperature.

    pressure:
        Pressure in hPa by default.

    temperature:
        Temperature in K by default.

    Examples:

        metpy_potential_temperature(
            1000,
            300
        )

        metpy_potential_temperature(
            "1000 hPa",
            "300 K"
        )
    """

    from metpy.calc import (
        potential_temperature
    )
    from metpy.units import units

    if not hasattr(
        pressure,
        "units"
    ):
        pressure = (
            float(pressure)
            * units.hPa
        )

    if not hasattr(
        temperature,
        "units"
    ):
        temperature = (
            float(temperature)
            * units.kelvin
        )

    return potential_temperature(
        pressure,
        temperature
    )


# ==========================================================
# METPY — DEWPOINT
# ==========================================================

def metpy_dewpoint(
    temperature,
    relative_humidity
):
    """
    Calculate dewpoint temperature.

    Temperature defaults to degrees Celsius.

    Relative humidity may be supplied as:
        50
    or:
        0.50
    """

    from metpy.calc import (
        dewpoint_from_relative_humidity
    )
    from metpy.units import units

    if not hasattr(
        temperature,
        "units"
    ):
        temperature = (
            float(temperature)
            * units.degC
        )

    if not hasattr(
        relative_humidity,
        "units"
    ):
        rh = float(
            relative_humidity
        )

        if rh <= 1:
            rh *= 100

        relative_humidity = (
            rh
            * units.percent
        )

    return dewpoint_from_relative_humidity(
        temperature,
        relative_humidity
    )


# ==========================================================
# METPY — HEAT INDEX
# ==========================================================

def metpy_heat_index(
    temperature,
    relative_humidity
):
    """
    Calculate heat index.

    Temperature defaults to degrees Celsius.

    Relative humidity defaults to percent.
    """

    from metpy.calc import heat_index
    from metpy.units import units

    if not hasattr(
        temperature,
        "units"
    ):
        temperature = (
            float(temperature)
            * units.degC
        )

    if not hasattr(
        relative_humidity,
        "units"
    ):
        rh = float(
            relative_humidity
        )

        if rh <= 1:
            rh *= 100

        relative_humidity = (
            rh
            * units.percent
        )

    return heat_index(
        temperature,
        relative_humidity
    )


# ==========================================================
# METPY — WIND COMPONENTS
# ==========================================================

def metpy_wind_components(
    speed,
    direction
):
    """
    Convert wind speed and direction into
    u and v wind components.

    Speed defaults to m/s.

    Direction defaults to degrees.
    """

    from metpy.calc import wind_components
    from metpy.units import units

    if not hasattr(
        speed,
        "units"
    ):
        speed = (
            float(speed)
            * units.meter
            / units.second
        )

    if not hasattr(
        direction,
        "units"
    ):
        direction = (
            float(direction)
            * units.deg
        )

    return wind_components(
        speed,
        direction
    )


# ==========================================================
# METEOROLOGY — HUMIDITY AND WIND CHILL
# ==========================================================

def metpy_relative_humidity(
    temperature,
    dewpoint,
    phase="liquid"
):
    """Return relative humidity in percent from Celsius temperatures."""

    from metpy.calc import relative_humidity_from_dewpoint
    from metpy.units import units

    if not hasattr(temperature, "units"):
        temperature = float(temperature) * units.degC
    if not hasattr(dewpoint, "units"):
        dewpoint = float(dewpoint) * units.degC

    result = relative_humidity_from_dewpoint(
        temperature,
        dewpoint,
        phase=phase
    )
    return float(result.to("percent").magnitude)


def metpy_wind_chill(
    temperature,
    wind_speed
):
    """Return wind-chill temperature in Celsius; wind speed defaults to m/s."""

    from metpy.calc import windchill
    from metpy.units import units

    if not hasattr(temperature, "units"):
        temperature = float(temperature) * units.degC
    if not hasattr(wind_speed, "units"):
        wind_speed = float(wind_speed) * units.meter / units.second

    result = windchill(temperature, wind_speed)
    return float(result.to("degC").magnitude)


# ==========================================================
# PHYSIOLOGY — GENERAL EDUCATIONAL CALCULATORS
# ==========================================================

def bmi(weight_kg, height_m):
    """Calculate BMI (kg/m²); this number is not a diagnosis."""

    weight_kg = float(weight_kg)
    height_m = float(height_m)
    if not math.isfinite(weight_kg) or weight_kg <= 0:
        raise ValueError("weight_kg must be a positive finite number.")
    if not math.isfinite(height_m) or height_m <= 0:
        raise ValueError("height_m must be a positive finite number.")
    return weight_kg / (height_m ** 2)


def mifflin_st_jeor(
    weight_kg,
    height_cm,
    age_years,
    sex
):
    """Estimate resting energy expenditure in kcal/day using Mifflin–St Jeor."""

    weight_kg = float(weight_kg)
    height_cm = float(height_cm)
    age_years = float(age_years)
    sex = str(sex).strip().lower()

    if any(
        not math.isfinite(value) or value <= 0
        for value in (weight_kg, height_cm, age_years)
    ):
        raise ValueError(
            "weight_kg, height_cm, and age_years must be positive finite numbers."
        )
    if sex in ("m", "male"):
        sex_constant = 5
    elif sex in ("f", "female"):
        sex_constant = -161
    else:
        raise ValueError("sex must be 'male'/'m' or 'female'/'f'.")

    return (
        10 * weight_kg
        + 6.25 * height_cm
        - 5 * age_years
        + sex_constant
    )


def cardiac_output(
    heart_rate_bpm,
    stroke_volume_ml
):
    """Calculate cardiac output in L/min from bpm and mL/beat."""

    heart_rate_bpm = float(heart_rate_bpm)
    stroke_volume_ml = float(stroke_volume_ml)
    if any(
        not math.isfinite(value) or value <= 0
        for value in (heart_rate_bpm, stroke_volume_ml)
    ):
        raise ValueError("heart rate and stroke volume must be positive finite numbers.")
    return heart_rate_bpm * stroke_volume_ml / 1000.0


def minute_ventilation(
    tidal_volume_ml,
    respiratory_rate_bpm
):
    """Calculate minute ventilation in L/min from mL/breath and breaths/min."""

    tidal_volume_ml = float(tidal_volume_ml)
    respiratory_rate_bpm = float(respiratory_rate_bpm)
    if any(
        not math.isfinite(value) or value <= 0
        for value in (tidal_volume_ml, respiratory_rate_bpm)
    ):
        raise ValueError(
            "tidal volume and respiratory rate must be positive finite numbers."
        )
    return tidal_volume_ml * respiratory_rate_bpm / 1000.0

# ==========================================================
# PHYSICS PART 5 STATUS
# ==========================================================

def physics_part5_status():
    """
    Display package availability.
    """

    packages = [
        "scipy",
        "mpmath",
        "uncertainties",
        "unyt",
        "quantities",
        "lmfit",
        "qutip",
        "qmsolve",
        "quantecon",
        "plasmapy",
        "MetPy",
    ]

    results = {}

    print()
    print("=" * 75)
    print(
        "DAVE — PHYSICS PART 5 PACKAGE STATUS"
    )
    print("=" * 75)
    print()

    for package_name in packages:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<20} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<20} unavailable"
            )

    print()

    return results


# ==========================================================
# PHYSICS PART 5 SELF TEST
# ==========================================================

def physics_part5_selftest(
    verbose=True
):
    """
    Test the main Physics Part 5 functionality.
    """

    tests = []


    # ------------------------------------------------------
    # SCIPY
    # ------------------------------------------------------

    try:

        result = scipy_integrate(
            lambda x: x ** 2,
            0,
            1
        )

        tests.append(
            (
                "scipy",
                abs(
                    result["value"]
                    - 1.0 / 3.0
                ) < 1e-8
            )
        )

    except Exception as exc:

        tests.append(
            (
                "scipy",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # MPMATH
    # ------------------------------------------------------

    try:

        result = mpmath_pi(
            50
        )

        tests.append(
            (
                "mpmath",
                len(
                    str(result).replace(
                        ".",
                        ""
                    )
                ) >= 40
            )
        )

    except Exception as exc:

        tests.append(
            (
                "mpmath",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # UNCERTAINTIES
    # ------------------------------------------------------

    try:

        result = uncertainty_add(
            10,
            0.1,
            5,
            0.2
        )

        tests.append(
            (
                "uncertainties",
                abs(
                    result.nominal_value
                    - 15.0
                ) < 1e-12
            )
        )

    except Exception as exc:

        tests.append(
            (
                "uncertainties",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # UNYT
    # ------------------------------------------------------

    try:

        result = unyt_convert(
            1,
            "meter",
            "cm"
        )

        tests.append(
            (
                "unyt",
                abs(
                    result.value
                    - 100.0
                ) < 1e-10
            )
        )

    except Exception as exc:

        tests.append(
            (
                "unyt",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # QUANTITIES
    # ------------------------------------------------------

    try:

        result = quantities_convert(
            1,
            "m",
            "cm"
        )

        tests.append(
            (
                "quantities",
                abs(
                    result.magnitude
                    - 100.0
                ) < 1e-10
            )
        )

    except Exception as exc:

        tests.append(
            (
                "quantities",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # QUTIP
    # ------------------------------------------------------

    try:

        state = qutip_qubit_zero()

        operator = qutip_pauli(
            "z"
        )

        result = qutip_expectation(
            operator,
            state
        )

        tests.append(
            (
                "qutip",
                abs(
                    float(result)
                    - 1.0
                ) < 1e-10
            )
        )

    except Exception as exc:

        tests.append(
            (
                "qutip",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # QUANTECON
    # ------------------------------------------------------

    try:

        matrix = [
            [0.9, 0.1],
            [0.2, 0.8]
        ]

        result = (
            quantecon_stationary_distribution(
                matrix
            )
        )

        tests.append(
            (
                "quantecon",
                result is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "quantecon",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PLASMAPY
    # ------------------------------------------------------

    try:

        particle = plasma_particle(
            "e-"
        )

        tests.append(
            (
                "plasmapy",
                particle.mass is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "plasmapy",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # METPY
    # ------------------------------------------------------

    try:

        import astropy.units as u

        temperature = (
            20
            * u.degC
        )

        humidity = 0.5

        result = metpy_dewpoint(
            temperature,
            humidity
        )

        tests.append(
            (
                "MetPy",
                result is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "MetPy",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # LMFIT
    # ------------------------------------------------------

    try:

        import numpy as np

        def linear_model(
            x,
            slope,
            intercept
        ):
            return (
                slope * x
                + intercept
            )

        x = np.array(
            [0, 1, 2, 3, 4],
            dtype=float
        )

        y = np.array(
            [1, 3, 5, 7, 9],
            dtype=float
        )

        result = lmfit_model_fit(
            linear_model,
            x,
            y,
            {
                "slope": 1.0,
                "intercept": 0.0
            }
        )

        tests.append(
            (
                "lmfit",
                abs(
                    result.params[
                        "slope"
                    ].value
                    - 2.0
                ) < 1e-5
            )
        )

    except Exception as exc:

        tests.append(
            (
                "lmfit",
                False,
                str(exc)
            )
        )


    # ======================================================
    # RESULTS
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 75)
        print(
            "DAVE — PHYSICS PART 5 SELF TEST"
        )
        print("=" * 75)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 75)

        print(
            f"Passed: {passed}"
        )

        print(
            f"Failed: {failed}"
        )

        print(
            f"Total:  {len(tests)}"
        )

        print("-" * 75)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# PHYSICS PART 5 HELP
# ==========================================================

def physics_part5_help():

    print("""
==============================================================================
DAVE — PHYSICS / SCIENTIFIC COMPUTING PART 5
==============================================================================

SCIPY
-----

    scipy_root(function, initial_guess)

    scipy_brentq(function, a, b)

    scipy_minimize(function, initial_guess)

    scipy_curve_fit(
        function,
        xdata,
        ydata
    )

    scipy_interpolate(
        x,
        y,
        new_x
    )

    scipy_spline(
        x,
        y,
        new_x
    )

    scipy_integrate(
        function,
        a,
        b
    )

    scipy_ode(
        function,
        t_span,
        y0
    )

    scipy_linear_solve(
        A,
        b
    )

    scipy_eigenvalues(
        matrix
    )

    scipy_fft(
        data
    )

    scipy_describe(
        data
    )

    scipy_normal_pdf(
        x,
        mean,
        standard_deviation
    )

    scipy_special(
        function_name,
        *args
    )


MPMATH
------

    mpmath_set_precision(
        100
    )

    mpmath_pi(
        100
    )

    mpmath_exp(
        x,
        100
    )

    mpmath_log(
        x,
        100
    )

    mpmath_findroot(
        function,
        guess,
        100
    )

    mpmath_integrate(
        function,
        a,
        b,
        100
    )


UNCERTAINTIES
-------------

    uncertainty_value(
        value,
        uncertainty
    )

    uncertainty_add(
        value1,
        uncertainty1,
        value2,
        uncertainty2
    )

    uncertainty_calculate(
        "x*y",
        {
            "x": (10, 0.2),
            "y": (5, 0.1)
        }
    )

    uncertainty_components(
        value
    )


UNYT
----

    unyt_quantity(
        10,
        "meter"
    )

    unyt_convert(
        1,
        "meter",
        "cm"
    )


QUANTITIES
----------

    quantities_value(
        10,
        "m"
    )

    quantities_convert(
        1,
        "m",
        "cm"
    )


LMFIT
-----

    lmfit_model_fit(
        function,
        xdata,
        ydata,
        parameters
    )

    lmfit_report(
        result
    )

    lmfit_parameters(
        result
    )


QUTIP
-----

    qutip_qubit_zero()

    qutip_qubit_one()

    qutip_basis(
        dimension,
        state
    )

    qutip_pauli(
        "x"
    )

    qutip_pauli(
        "y"
    )

    qutip_pauli(
        "z"
    )

    qutip_expectation(
        operator,
        state
    )

    qutip_density_matrix(
        state
    )

    qutip_tensor(
        state1,
        state2
    )

    qutip_schrodinger(
        H,
        state,
        times
    )

    qutip_master_equation(
        H,
        state,
        times,
        collapse_operators
    )


QMSOLVE
-------

    qmsolve_status()


QUANTECON
---------

    quantecon_markov_chain(
        transition_matrix
    )

    quantecon_stationary_distribution(
        transition_matrix
    )

    quantecon_lq(
        Q,
        R,
        A,
        B
    )


PLASMAPY
--------

    plasma_particle(
        "e-"
    )

    plasma_particle_mass(
        "e-"
    )

    plasma_particle_charge(
        "e-"
    )

    plasma_particle_number(
        "e-"
    )

    plasma_debye_length(
        temperature,
        electron_density
    )

    plasma_frequency(
        electron_density
    )

    plasma_gyrofrequency(
        B,
        "e-"
    )

    plasma_thermal_speed(
        temperature,
        "e-"
    )


METPY
-----

    metpy_potential_temperature(
        pressure,
        temperature
    )

    metpy_dewpoint(
        temperature,
        relative_humidity
    )

    metpy_heat_index(
        temperature,
        relative_humidity
    )

    metpy_wind_components(
        speed,
        direction
    )


TESTING
-------

    physics_part5_status()

    physics_part5_selftest()

==============================================================================
""")

# ==========================================================
# DAVE
# ADVANCED NUMERICAL / PHYSICS INTEGRATION
# PART 6
# ==========================================================
#
# Packages:
#
#   diffrax
#   dynamiqs
#   equinox
#   lineax
#   optimistix
#   opt_einsum
#   emcee
#   formulaic
#   gudhi
#   topoly
#
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_diffrax():
    return load_scientific_package("diffrax")


def _get_dynamiqs():
    return load_scientific_package("dynamiqs")


def _get_equinox():
    return load_scientific_package("equinox")


def _get_lineax():
    return load_scientific_package("lineax")


def _get_optimistix():
    return load_scientific_package("optimistix")


def _get_opt_einsum():
    return load_scientific_package("opt_einsum")


def _get_emcee():
    return load_scientific_package("emcee")


def _get_formulaic():
    return load_scientific_package("formulaic")


def _get_gudhi():
    return load_scientific_package("gudhi")


def _get_topoly():
    return load_scientific_package("topoly")


# ==========================================================
# DIFFRAX — ODE SOLVER
# ==========================================================

def diffrax_ode(
    function,
    y0,
    t0,
    t1,
    dt0=0.01,
    solver="tsit5"
):
    """
    Solve an ODE using Diffrax.

    function must have the form:

        f(t, y, args)

    Example:

        lambda t, y, args: -y
    """

    import diffrax

    solvers = {
        "tsit5":
            diffrax.Tsit5(),

        "dopri5":
            diffrax.Dopri5(),

        "dopri8":
            diffrax.Dopri8(),

        "euler":
            diffrax.Euler(),

        "heun":
            diffrax.Heun(),

        "midpoint":
            diffrax.Midpoint(),

        "ralston":
            diffrax.Ralston(),
    }

    solver_name = str(
        solver
    ).lower()

    if solver_name not in solvers:

        raise ValueError(
            "Unknown Diffrax solver. "
            f"Available: {list(solvers)}"
        )

    term = diffrax.ODETerm(
        function
    )

    saveat = diffrax.SaveAt(
        dense=True
    )

    solution = diffrax.diffeqsolve(
        term,
        solvers[solver_name],
        t0=float(t0),
        t1=float(t1),
        dt0=float(dt0),
        y0=y0,
        saveat=saveat
    )

    return solution


# ==========================================================
# DIFFRAX — ODE SOLUTION AT TIME
# ==========================================================

def diffrax_solution_value(
    solution,
    time
):
    """
    Evaluate a dense Diffrax solution at a specified time.
    """

    return solution.evaluate(
        float(time)
    )


# ==========================================================
# DIFFRAX — SOLUTION GRID
# ==========================================================

def diffrax_solution_grid(
    solution,
    start,
    stop,
    points=100
):
    """
    Evaluate a dense solution over a regular time grid.
    """

    import numpy as np

    times = np.linspace(
        float(start),
        float(stop),
        int(points)
    )

    values = [
        solution.evaluate(t)
        for t in times
    ]

    return times, values


# ==========================================================
# DIFFRAX — ROOT FINDING / EVENT
# ==========================================================

def diffrax_event(
    function,
    y0,
    t0,
    t1,
    dt0=0.01
):
    """
    Integrate an ODE while allowing a user-defined
    termination/event function.

    The function should return a scalar condition.
    """

    import diffrax

    term = diffrax.ODETerm(
        function
    )

    solver = diffrax.Tsit5()

    solution = diffrax.diffeqsolve(
        term,
        solver,
        t0=float(t0),
        t1=float(t1),
        dt0=float(dt0),
        y0=y0
    )

    return solution


# ==========================================================
# DYAMIqs — BASIC QUANTUM STATE
# ==========================================================

def dynamiqs_basis(
    dimension,
    state
):
    """
    Create a basis state with Dynamiqs.
    """

    import dynamiqs as dq

    return dq.basis(
        int(dimension),
        int(state)
    )


# ==========================================================
# DYAMIqs — FOCK STATE
# ==========================================================

def dynamiqs_fock(
    dimension,
    occupation
):
    """
    Create a Fock state.
    """

    import dynamiqs as dq

    return dq.fock(
        int(dimension),
        int(occupation)
    )


# ==========================================================
# DYAMIqs — ANNIHILATION OPERATOR
# ==========================================================

def dynamiqs_annihilation(
    dimension
):
    """
    Create a bosonic annihilation operator.
    """

    import dynamiqs as dq

    return dq.destroy(
        int(dimension)
    )


# ==========================================================
# DYAMIqs — CREATION OPERATOR
# ==========================================================

def dynamiqs_creation(
    dimension
):
    """
    Create a bosonic creation operator.
    """

    import dynamiqs as dq

    return dq.create(
        int(dimension)
    )


# ==========================================================
# DYAMIqs — NUMBER OPERATOR
# ==========================================================

def dynamiqs_number(
    dimension
):
    """
    Create the number operator.
    """

    import dynamiqs as dq

    return dq.number(
        int(dimension)
    )


# ==========================================================
# DYAMIqs — DENSITY MATRIX
# ==========================================================

def dynamiqs_density_matrix(
    state
):
    """
    Convert a pure state into a density matrix.
    """

    return state @ state.dag()


# ==========================================================
# EQUINOX — ARRAY
# ==========================================================

def equinox_array(
    values
):
    """
    Convert data into a JAX/Equinox-compatible array.
    """

    import jax.numpy as jnp

    return jnp.asarray(
        values
    )


# ==========================================================
# EQUINOX — SIMPLE LINEAR MODEL
# ==========================================================

def equinox_linear_model(
    input_size,
    output_size,
    key
):
    """
    Create a neural-network linear layer using Equinox.

    key must be a JAX PRNG key.
    """

    import equinox as eqx

    return eqx.nn.Linear(
        int(input_size),
        int(output_size),
        key=key
    )


# ==========================================================
# EQUINOX — MLP
# ==========================================================

def equinox_mlp(
    input_size,
    output_size,
    width,
    depth,
    key
):
    """
    Create an Equinox multilayer perceptron.
    """

    import equinox as eqx

    return eqx.nn.MLP(
        in_size=int(input_size),
        out_size=int(output_size),
        width_size=int(width),
        depth=int(depth),
        key=key
    )


# ==========================================================
# EQUINOX — GRADIENT
# ==========================================================

def equinox_gradient(
    function,
    value
):
    """
    Calculate a JAX automatic derivative.
    """

    import jax

    gradient_function = jax.grad(
        function
    )

    return gradient_function(
        value
    )


# ==========================================================
# EQUINOX — JIT FUNCTION
# ==========================================================

def equinox_jit(
    function
):
    """
    JIT-compile a function with JAX.
    """

    import jax

    return jax.jit(
        function
    )


# ==========================================================
# LINEAX — LINEAR SOLVE
# ==========================================================

def lineax_solve(
    matrix,
    vector
):
    """
    Solve a linear system with Lineax.
    """

    import jax.numpy as jnp
    import lineax as lx

    operator = lx.MatrixLinearOperator(
        jnp.asarray(matrix)
    )

    solution = lx.linear_solve(
        operator,
        jnp.asarray(vector)
    )

    return solution.value


# ==========================================================
# LINEAX — LEAST SQUARES
# ==========================================================

def lineax_least_squares(
    matrix,
    vector
):
    """
    Solve a linear least-squares problem.
    """

    import jax.numpy as jnp
    import lineax as lx

    A = jnp.asarray(
        matrix
    )

    b = jnp.asarray(
        vector
    )

    operator = lx.MatrixLinearOperator(
        A
    )

    solution = lx.linear_solve(
        operator,
        b
    )

    return solution.value


# ==========================================================
# OPTIMISTIX — ROOT SOLVER
# ==========================================================

def optimistix_root(
    function,
    initial_guess,
    solver="newton"
):
    """
    Solve f(x) = 0 with Optimistix.

    function must accept x and args.
    """

    import optimistix as optx

    solvers = {
        "newton":
            optx.Newton(),

        "bfgs":
            optx.BFGS(),

        "broyden":
            optx.Broyden(),
    }

    solver_name = str(
        solver
    ).lower()

    if solver_name not in solvers:

        raise ValueError(
            "Unknown Optimistix solver. "
            f"Available: {list(solvers)}"
        )

    solution = optx.root_find(
        function,
        solvers[solver_name],
        initial_guess
    )

    return solution


# ==========================================================
# OPTIMISTIX — MINIMIZATION
# ==========================================================

def optimistix_minimize(
    function,
    initial_guess
):
    """
    Minimize a differentiable objective function.
    """

    import optimistix as optx

    solver = optx.BFGS()

    solution = optx.minimise(
        function,
        solver,
        initial_guess
    )

    return solution


# ==========================================================
# OPT_EINSUM — OPTIMIZED EINSTEIN SUM
# ==========================================================

def optimized_einsum(
    expression,
    *operands
):
    """
    Perform an optimized Einstein summation.
    """

    import opt_einsum

    return opt_einsum.contract(
        expression,
        *operands
    )


# ==========================================================
# OPT_EINSUM — CONTRACTION PATH
# ==========================================================

def einsum_contraction_path(
    expression,
    *operands
):
    """
    Determine an optimized tensor-contraction path.
    """

    import opt_einsum

    path, info = (
        opt_einsum.contract_path(
            expression,
            *operands
        )
    )

    return {
        "path": path,
        "info": str(info)
    }


# ==========================================================
# EMCEE — MCMC SAMPLING
# ==========================================================

def emcee_sample(
    log_probability,
    initial_positions,
    steps
):
    """
    Run an affine-invariant MCMC ensemble.

    log_probability must accept:
        parameters
    """

    import numpy as np
    import emcee

    initial_positions = np.asarray(
        initial_positions,
        dtype=float
    )

    ndim = initial_positions.shape[1]

    sampler = emcee.EnsembleSampler(
        initial_positions.shape[0],
        ndim,
        log_probability
    )

    sampler.run_mcmc(
        initial_positions,
        int(steps),
        progress=False
    )

    return sampler


# ==========================================================
# EMCEE — CHAIN
# ==========================================================

def emcee_chain(
    sampler,
    discard=0,
    thin=1,
    flat=True
):
    """
    Return MCMC samples.
    """

    return sampler.get_chain(
        discard=int(discard),
        thin=int(thin),
        flat=bool(flat)
    )


# ==========================================================
# EMCEE — LOG PROBABILITY
# ==========================================================

def emcee_log_probability(
    sampler,
    discard=0,
    thin=1
):
    """
    Return sampled log probabilities.
    """

    return sampler.get_log_prob(
        discard=int(discard),
        thin=int(thin),
        flat=True
    )


# ==========================================================
# EMCEE — AUTOCORRELATION TIME
# ==========================================================

def emcee_autocorrelation_time(
    sampler
):
    """
    Estimate MCMC autocorrelation time.
    """

    return sampler.get_autocorr_time()


# ==========================================================
# FORMULAIC — FORMULA PARSING
# ==========================================================

def formulaic_model(
    formula,
    data
):
    """
    Parse a statistical model formula with Formulaic.
    """

    from formulaic import model_matrix

    return model_matrix(
        str(formula),
        data
    )


# ==========================================================
# FORMULAIC — DESIGN MATRIX
# ==========================================================

def formulaic_design_matrix(
    formula,
    data
):
    """
    Return the design matrix generated by a formula.
    """

    from formulaic import model_matrix

    return model_matrix(
        str(formula),
        data
    )


# ==========================================================
# GUDHI — SIMPLEX TREE
# ==========================================================

def gudhi_simplex_tree(
    simplices
):
    """
    Create a GUDHI simplex tree.

    simplices can contain:
        [0]
        [1]
        [0, 1]
        [0, 1, 2]
        etc.
    """

    import gudhi

    tree = gudhi.SimplexTree()

    for simplex in simplices:

        tree.insert(
            list(simplex)
        )

    return tree


# ==========================================================
# GUDHI — SIMPLEX TREE SUMMARY
# ==========================================================

def gudhi_summary(
    tree
):
    """
    Return basic topological information.
    """

    tree.compute_persistence()

    result = {
        "dimension":
            tree.dimension(),

        "num_simplices":
            tree.num_simplices(),

        "num_vertices":
            tree.num_vertices(),

        "betti_numbers":
            tree.betti_numbers(),

        "persistence":
            tree.persistence(),
    }

    return result


# ==========================================================
# GUDHI — BETTI NUMBERS
# ==========================================================

def gudhi_betti_numbers(
    tree
):
    """
    Calculate Betti numbers.
    """

    tree.compute_persistence()

    return tree.betti_numbers()


# ==========================================================
# GUDHI — PERSISTENCE
# ==========================================================

def gudhi_persistence(
    tree
):
    """
    Calculate persistent homology.
    """

    tree.compute_persistence()

    return tree.persistence()


# ==========================================================
# GUDHI — PERSISTENCE INTERVALS
# ==========================================================

def gudhi_persistence_intervals(
    tree,
    dimension=0
):
    """
    Return persistence intervals for one homology dimension.
    """

    tree.compute_persistence()

    return tree.persistence_intervals_in_dimension(
        int(dimension)
    )


# ==========================================================
# TOPOLY — PACKAGE STATUS
# ==========================================================

def topoly_status():
    """
    Check availability of Topoly.

    Topoly is kept behind a dedicated wrapper because
    its API is specialized and may differ between versions.
    """

    try:

        module = _get_topoly()

        return {
            "available": True,
            "version":
                getattr(
                    module,
                    "__version__",
                    "unknown"
                )
        }

    except Exception as exc:

        return {
            "available": False,
            "error": str(exc)
        }


# ==========================================================
# ADVANCED ODE REPORT
# ==========================================================

def advanced_ode_report(
    function,
    y0,
    t0,
    t1,
    dt0=0.01
):
    """
    Run an ODE through Diffrax and return a compact report.
    """

    solution = diffrax_ode(
        function,
        y0,
        t0,
        t1,
        dt0
    )

    final_value = (
        diffrax_solution_value(
            solution,
            t1
        )
    )

    return {
        "solution": solution,
        "final_value": final_value,
        "t0": float(t0),
        "t1": float(t1),
    }


# ==========================================================
# ADVANCED NUMERICAL STATUS
# ==========================================================

def physics_part6_status():
    """
    Display package availability.
    """

    packages = [
        "diffrax",
        "dynamiqs",
        "equinox",
        "lineax",
        "optimistix",
        "opt_einsum",
        "emcee",
        "formulaic",
        "gudhi",
        "topoly",
    ]

    results = {}

    print()
    print("=" * 75)
    print(
        "DAVE — ADVANCED PHYSICS PART 6 STATUS"
    )
    print("=" * 75)
    print()

    for package_name in packages:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<20} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<20} unavailable"
            )

    print()

    return results


# ==========================================================
# ADVANCED NUMERICAL SELF TEST
# ==========================================================

def physics_part6_selftest(
    verbose=True
):
    """
    Test the main functionality of Part 6.
    """

    tests = []


    # ------------------------------------------------------
    # DIFFRAX
    # ------------------------------------------------------

    try:

        import numpy as np

        def decay(
            t,
            y,
            args
        ):
            return -y

        solution = diffrax_ode(
            decay,
            np.array([1.0]),
            0.0,
            1.0,
            0.05
        )

        value = diffrax_solution_value(
            solution,
            1.0
        )

        tests.append(
            (
                "diffrax",
                abs(
                    float(value[0])
                    - np.exp(-1.0)
                ) < 1e-3
            )
        )

    except Exception as exc:

        tests.append(
            (
                "diffrax",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # DYNAMIQS
    # ------------------------------------------------------

    try:

        state = dynamiqs_basis(
            2,
            0
        )

        tests.append(
            (
                "dynamiqs",
                state is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "dynamiqs",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # EQUINOX
    # ------------------------------------------------------

    try:

        import jax
        import jax.numpy as jnp

        key = jax.random.PRNGKey(
            0
        )

        model = equinox_linear_model(
            2,
            1,
            key
        )

        result = model(
            jnp.array(
                [1.0, 2.0]
            )
        )

        tests.append(
            (
                "equinox",
                result is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "equinox",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # LINEAX
    # ------------------------------------------------------

    try:

        result = lineax_solve(
            [
                [2.0, 0.0],
                [0.0, 2.0]
            ],
            [4.0, 6.0]
        )

        tests.append(
            (
                "lineax",
                abs(
                    float(result[0])
                    - 2.0
                ) < 1e-6
            )
        )

    except Exception as exc:

        tests.append(
            (
                "lineax",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # OPT_EINSUM
    # ------------------------------------------------------

    try:

        import numpy as np

        A = np.array(
            [[1, 2], [3, 4]]
        )

        B = np.array(
            [[5, 6], [7, 8]]
        )

        result = optimized_einsum(
            "ij,jk->ik",
            A,
            B
        )

        tests.append(
            (
                "opt_einsum",
                result.shape == (2, 2)
            )
        )

    except Exception as exc:

        tests.append(
            (
                "opt_einsum",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # FORMULAIC
    # ------------------------------------------------------

    try:

        import pandas as pd

        data = pd.DataFrame(
            {
                "x": [1, 2, 3],
                "y": [2, 4, 6]
            }
        )

        result = formulaic_model(
            "y ~ x",
            data
        )

        tests.append(
            (
                "formulaic",
                result is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "formulaic",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # GUDHI
    # ------------------------------------------------------

    try:

        tree = gudhi_simplex_tree(
            [
                [0],
                [1],
                [0, 1]
            ]
        )

        tests.append(
            (
                "gudhi",
                tree.num_vertices() == 2
            )
        )

    except Exception as exc:

        tests.append(
            (
                "gudhi",
                False,
                str(exc)
            )
        )


    # ======================================================
    # RESULTS
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 75)
        print(
            "DAVE — ADVANCED PHYSICS PART 6 SELF TEST"
        )
        print("=" * 75)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 75)

        print(
            f"Passed: {passed}"
        )

        print(
            f"Failed: {failed}"
        )

        print(
            f"Total:  {len(tests)}"
        )

        print("-" * 75)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# ADVANCED PHYSICS HELP
# ==========================================================

def physics_part6_help():

    print("""
==============================================================================
DAVE — ADVANCED NUMERICAL / PHYSICS PART 6
==============================================================================

DIFFRAX
-------

    diffrax_ode(
        function,
        y0,
        t0,
        t1
    )

    diffrax_solution_value(
        solution,
        time
    )

    diffrax_solution_grid(
        solution,
        start,
        stop,
        points
    )

    advanced_ode_report(
        function,
        y0,
        t0,
        t1
    )


DYNAMIQS
--------

    dynamiqs_basis(
        dimension,
        state
    )

    dynamiqs_fock(
        dimension,
        occupation
    )

    dynamiqs_annihilation(
        dimension
    )

    dynamiqs_creation(
        dimension
    )

    dynamiqs_number(
        dimension
    )

    dynamiqs_density_matrix(
        state
    )


EQUINOX
-------

    equinox_array(
        values
    )

    equinox_linear_model(
        input_size,
        output_size,
        key
    )

    equinox_mlp(
        input_size,
        output_size,
        width,
        depth,
        key
    )

    equinox_gradient(
        function,
        value
    )

    equinox_jit(
        function
    )


LINEAX
------

    lineax_solve(
        matrix,
        vector
    )

    lineax_least_squares(
        matrix,
        vector
    )


OPTIMISTIX
----------

    optimistix_root(
        function,
        initial_guess
    )

    optimistix_minimize(
        function,
        initial_guess
    )


OPT_EINSUM
----------

    optimized_einsum(
        "ij,jk->ik",
        A,
        B
    )

    einsum_contraction_path(
        expression,
        A,
        B
    )


EMCEE
-----

    emcee_sample(
        log_probability,
        initial_positions,
        steps
    )

    emcee_chain(
        sampler
    )

    emcee_log_probability(
        sampler
    )

    emcee_autocorrelation_time(
        sampler
    )


FORMULAIC
---------

    formulaic_model(
        "y ~ x",
        data
    )

    formulaic_design_matrix(
        "y ~ x",
        data
    )


GUDHI
-----

    gudhi_simplex_tree(
        simplices
    )

    gudhi_summary(
        tree
    )

    gudhi_betti_numbers(
        tree
    )

    gudhi_persistence(
        tree
    )

    gudhi_persistence_intervals(
        tree,
        dimension
    )


TOPOLY
------

    topoly_status()


TESTING
-------

    physics_part6_status()

    physics_part6_selftest()

==============================================================================
""")

# ==========================================================
# DAVE
# BIOLOGY / BIOINFORMATICS INTEGRATION
# PART 7
# ==========================================================
#
# Packages:
#
#   anndata
#   biom-format
#   biopython
#   bioregistry
#   biotite
#   DendroPy
#   msprime
#   pybedtools
#   pysam
#   scanpy
#   scikit-bio
#   tskit
#
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_anndata():
    return load_scientific_package("anndata")


def _get_biom():
    return load_scientific_package("biom-format")


def _get_biopython():
    return load_scientific_package("biopython")


def _get_bioregistry():
    return load_scientific_package("bioregistry")


def _get_biotite():
    return load_scientific_package("biotite")


def _get_dendropy():
    return load_scientific_package("DendroPy")


def _get_msprime():
    return load_scientific_package("msprime")


def _get_pybedtools():
    return load_scientific_package("pybedtools")


def _get_pysam():
    return load_scientific_package("pysam")


def _get_scanpy():
    return load_scientific_package("scanpy")


def _get_skbio():
    return load_scientific_package("scikit-bio")


def _get_tskit():
    return load_scientific_package("tskit")


# ==========================================================
# BIOPYTHON — DNA / RNA SEQUENCES
# ==========================================================

def bio_sequence(
    sequence,
    molecule_type="DNA"
):
    """
    Create a Biopython Seq object.
    """

    from Bio.Seq import Seq

    seq = Seq(
        str(sequence)
    )

    return seq


# ==========================================================
# BIOPYTHON — DNA COMPLEMENT
# ==========================================================

def bio_complement(
    sequence
):
    """
    Return the complement of a DNA/RNA sequence.
    """

    seq = bio_sequence(
        sequence
    )

    return str(
        seq.complement()
    )


# ==========================================================
# BIOPYTHON — REVERSE COMPLEMENT
# ==========================================================

def bio_reverse_complement(
    sequence
):
    """
    Return the reverse complement.
    """

    seq = bio_sequence(
        sequence
    )

    return str(
        seq.reverse_complement()
    )


# ==========================================================
# BIOPYTHON — TRANSCRIBE
# ==========================================================

def bio_transcribe(
    sequence
):
    """
    Transcribe DNA into RNA.
    """

    seq = bio_sequence(
        sequence
    )

    return str(
        seq.transcribe()
    )


# ==========================================================
# BIOPYTHON — TRANSLATE
# ==========================================================

def bio_translate(
    sequence,
    table=1,
    to_stop=False
):
    """
    Translate a nucleotide sequence into protein.
    """

    seq = bio_sequence(
        sequence
    )

    return str(
        seq.translate(
            table=int(table),
            to_stop=bool(to_stop)
        )
    )


# ==========================================================
# BIOPYTHON — GC CONTENT
# ==========================================================

def bio_gc_content(
    sequence
):
    """
    Calculate GC percentage.
    """

    from Bio.SeqUtils import gc_fraction

    fraction = gc_fraction(
        str(sequence)
    )

    return 100.0 * fraction


# ==========================================================
# BIOPYTHON — MOLECULAR WEIGHT
# ==========================================================

def bio_molecular_weight(
    sequence,
    seq_type="DNA"
):
    """
    Calculate molecular weight of a biological sequence.
    """

    from Bio.SeqUtils import molecular_weight

    return molecular_weight(
        str(sequence),
        seq_type=str(seq_type)
    )


# ==========================================================
# BIOPYTHON — SEQUENCE REPORT
# ==========================================================

def bio_sequence_report(
    sequence
):
    """
    Produce a general sequence analysis report.
    """

    seq = bio_sequence(
        sequence
    )

    text = str(
        seq
    )

    return {
        "sequence": text,
        "length": len(text),
        "GC_percent":
            bio_gc_content(text),
        "complement":
            bio_complement(text),
        "reverse_complement":
            bio_reverse_complement(text),
        "transcription":
            bio_transcribe(text),
    }


# ==========================================================
# BIOPYTHON — FASTA READ
# ==========================================================

def bio_read_fasta(
    filename
):
    """
    Read sequences from a FASTA file.
    """

    from Bio import SeqIO

    records = list(
        SeqIO.parse(
            str(filename),
            "fasta"
        )
    )

    return records


# ==========================================================
# BIOPYTHON — FASTA WRITE
# ==========================================================

def bio_write_fasta(
    records,
    filename
):
    """
    Write Biopython sequence records to FASTA.
    """

    from Bio import SeqIO

    return SeqIO.write(
        records,
        str(filename),
        "fasta"
    )


# ==========================================================
# BIOPYTHON — SEQUENCE ALIGNMENT
# ==========================================================

def bio_pairwise_alignment(
    sequence_a,
    sequence_b,
    match_score=1.0,
    mismatch_score=-1.0,
    gap_score=-1.0
):
    """
    Perform a pairwise global alignment.
    """

    from Bio import Align

    aligner = Align.PairwiseAligner()

    aligner.match_score = float(
        match_score
    )

    aligner.mismatch_score = float(
        mismatch_score
    )

    aligner.open_gap_score = float(
        gap_score
    )

    alignments = aligner.align(
        str(sequence_a),
        str(sequence_b)
    )

    return alignments


# ==========================================================
# BIOPYTHON — NCBI / GENBANK PARSING
# ==========================================================

def bio_read_genbank(
    filename
):
    """
    Read GenBank records.
    """

    from Bio import SeqIO

    return list(
        SeqIO.parse(
            str(filename),
            "genbank"
        )
    )


# ==========================================================
# BIOPYTHON — PHYLOGENETIC TREE
# ==========================================================

def bio_read_newick(
    filename
):
    """
    Read a Newick-format phylogenetic tree.
    """

    from Bio import Phylo

    return Phylo.read(
        str(filename),
        "newick"
    )


# ==========================================================
# BIOREGISTRY — NORMALIZE IDENTIFIER
# ==========================================================

def bioregistry_normalize(
    prefix,
    identifier
):
    """
    Normalize a biological database identifier.
    """

    import bioregistry

    return bioregistry.normalize(
        str(prefix),
        str(identifier)
    )


# ==========================================================
# BIOREGISTRY — CURIE
# ==========================================================

def bioregistry_make_curie(
    prefix,
    identifier
):
    """
    Construct a CURIE such as:
        uniprot:P12345
    """

    import bioregistry

    return bioregistry.make_curie(
        str(prefix),
        str(identifier)
    )


# ==========================================================
# BIOREGISTRY — URI
# ==========================================================

def bioregistry_make_uri(
    prefix,
    identifier
):
    """
    Convert a database identifier into a URI.
    """

    import bioregistry

    return bioregistry.get_uri(
        str(prefix),
        str(identifier)
    )


# ==========================================================
# BIOTITE — NUCLEIC ACID SEQUENCE
# ==========================================================

def biotite_dna(
    sequence
):
    """
    Create a Biotite NucleotideSequence.
    """

    import biotite.sequence as seq

    return seq.NucleotideSequence(
        str(sequence)
    )


# ==========================================================
# BIOTITE — PROTEIN SEQUENCE
# ==========================================================

def biotite_protein(
    sequence
):
    """
    Create a Biotite ProteinSequence.
    """

    import biotite.sequence as seq

    return seq.ProteinSequence(
        str(sequence)
    )


# ==========================================================
# BIOTITE — NUCLEOTIDE ALPHABET
# ==========================================================

def biotite_nucleotide_alphabet():
    """
    Return the standard nucleotide alphabet.
    """

    import biotite.sequence as seq

    return seq.NucleotideSequence.alphabet


# ==========================================================
# BIOTITE — PROTEIN ALPHABET
# ==========================================================

def biotite_protein_alphabet():
    """
    Return the standard protein alphabet.
    """

    import biotite.sequence as seq

    return seq.ProteinSequence.alphabet


# ==========================================================
# BIOTITE — STRUCTURE READ
# ==========================================================

def biotite_structure_read(
    filename
):
    """
    Read a molecular structure using Biotite.
    """

    import biotite.structure.io as strucio

    return strucio.load_structure(
        str(filename)
    )


# ==========================================================
# BIOTITE — STRUCTURE SUMMARY
# ==========================================================

def biotite_structure_summary(
    structure
):
    """
    Summarize an imported molecular structure.
    """

    import numpy as np

    result = {
        "atoms": len(structure),
    }

    if hasattr(
        structure,
        "res_id"
    ):
        result["residues"] = int(
            len(
                np.unique(
                    structure.res_id
                )
            )
        )

    if hasattr(
        structure,
        "chain_id"
    ):
        result["chains"] = int(
            len(
                np.unique(
                    structure.chain_id
                )
            )
        )

    if hasattr(
        structure,
        "element"
    ):
        result["elements"] = sorted(
            set(
                str(x)
                for x in structure.element
                if str(x)
            )
        )

    return result


# ==========================================================
# DENDROPY — READ TREE
# ==========================================================

def dendropy_read_tree(
    filename,
    schema="newick"
):
    """
    Read a phylogenetic tree using DendroPy.
    """

    import dendropy

    return dendropy.Tree.get(
        path=str(filename),
        schema=str(schema)
    )


# ==========================================================
# DENDROPY — TREE FROM STRING
# ==========================================================

def dendropy_tree_from_string(
    tree_string,
    schema="newick"
):
    """
    Create a DendroPy tree from a Newick string.
    """

    import dendropy

    return dendropy.Tree.get(
        data=str(tree_string),
        schema=str(schema)
    )


# ==========================================================
# DENDROPY — TREE TAXA
# ==========================================================

def dendropy_tree_summary(
    tree
):
    """
    Return basic phylogenetic-tree information.
    """

    return {
        "taxa":
            len(tree.taxon_namespace),

        "leaf_nodes":
            len(
                list(
                    tree.leaf_node_iter()
                )
            ),

        "nodes":
            len(
                list(
                    tree.preorder_node_iter()
                )
            ),

        "edges":
            len(
                list(
                    tree.preorder_edge_iter()
                )
            ),
    }


# ==========================================================
# TSKIT — LOAD TREE SEQUENCE
# ==========================================================

def tskit_load(
    filename
):
    """
    Load a tree-sequence file.
    """

    import tskit

    return tskit.load(
        str(filename)
    )


# ==========================================================
# TSKIT — TREE SEQUENCE SUMMARY
# ==========================================================

def tskit_summary(
    ts
):
    """
    Return basic tree-sequence statistics.
    """

    return {
        "sequence_length":
            ts.sequence_length,

        "num_individuals":
            ts.num_individuals,

        "num_nodes":
            ts.num_nodes,

        "num_edges":
            ts.num_edges,

        "num_sites":
            ts.num_sites,

        "num_mutations":
            ts.num_mutations,

        "num_populations":
            ts.num_populations,

        "num_trees":
            ts.num_trees,
    }


# ==========================================================
# TSKIT — TREE ITERATION
# ==========================================================

def tskit_trees(
    ts
):
    """
    Return all trees in a tree sequence.
    """

    return list(
        ts.trees()
    )


# ==========================================================
# TSKIT — DIVERSITY
# ==========================================================

def tskit_diversity(
    ts,
    sample_sets=None
):
    """
    Calculate genetic diversity.
    """

    if sample_sets is None:

        return ts.diversity()

    return ts.diversity(
        sample_sets=sample_sets
    )


# ==========================================================
# TSKIT — DIVERGENCE
# ==========================================================

def tskit_divergence(
    ts,
    sample_sets
):
    """
    Calculate genetic divergence.
    """

    return ts.divergence(
        sample_sets=sample_sets
    )


# ==========================================================
# TSKIT — GENOTYPES
# ==========================================================

def tskit_genotype_matrix(
    ts
):
    """
    Return the genotype matrix.
    """

    return ts.genotype_matrix()


# ==========================================================
# MSPRIME — DEMOGRAPHIC SIMULATION
# ==========================================================

def msprime_simulate(
    sample_size=10,
    sequence_length=10000,
    recombination_rate=1e-8,
    random_seed=None
):
    """
    Simulate a simple ancestry using msprime.
    """

    import msprime

    kwargs = {
        "samples": int(sample_size),
        "sequence_length":
            float(sequence_length),
        "recombination_rate":
            float(recombination_rate),
    }

    if random_seed is not None:

        kwargs["random_seed"] = int(
            random_seed
        )

    return msprime.sim_ancestry(
        **kwargs
    )


# ==========================================================
# MSPRIME — MUTATION SIMULATION
# ==========================================================

def msprime_simulate_mutations(
    ts,
    mutation_rate=1e-8,
    random_seed=None
):
    """
    Add mutations to an ancestry tree sequence.
    """

    import msprime

    kwargs = {
        "rate": float(mutation_rate)
    }

    if random_seed is not None:

        kwargs["random_seed"] = int(
            random_seed
        )

    return msprime.sim_mutations(
        ts,
        **kwargs
    )


# ==========================================================
# MSPRIME — COMPLETE SIMULATION
# ==========================================================

def msprime_simulate_genome(
    sample_size=10,
    sequence_length=10000,
    population_size=10_000,
    recombination_rate=1e-8,
    mutation_rate=1e-8,
    random_seed=None
):
    """
    Simulate ancestry and mutations.
    """

    import msprime

    ancestry_kwargs = {
        "samples":
            int(sample_size),

        "sequence_length":
            float(sequence_length),

        "population_size":
            float(population_size),

        "recombination_rate":
            float(recombination_rate),
    }

    if random_seed is not None:

        ancestry_kwargs[
            "random_seed"
        ] = int(random_seed)

    ts = msprime.sim_ancestry(
        **ancestry_kwargs
    )

    mutation_kwargs = {
        "rate":
            float(mutation_rate)
    }

    if random_seed is not None:

        mutation_kwargs[
            "random_seed"
        ] = int(random_seed) + 1

    return msprime.sim_mutations(
        ts,
        **mutation_kwargs
    )


# ==========================================================
# PYBEDTOOLS — CREATE INTERVALS
# ==========================================================

def pybedtools_from_string(
    bed_string
):
    """
    Create a BedTool object from BED-format text.
    """

    import pybedtools

    return pybedtools.BedTool(
        str(bed_string),
        from_string=True
    )


# ==========================================================
# PYBEDTOOLS — SORT
# ==========================================================

def pybedtools_sort(
    bed
):
    """
    Sort genomic intervals.
    """

    return bed.sort()


# ==========================================================
# PYBEDTOOLS — MERGE
# ==========================================================

def pybedtools_merge(
    bed
):
    """
    Merge overlapping genomic intervals.
    """

    return bed.merge()


# ==========================================================
# PYBEDTOOLS — INTERSECTION
# ==========================================================

def pybedtools_intersect(
    bed_a,
    bed_b
):
    """
    Find intersections between two BED datasets.
    """

    return bed_a.intersect(
        bed_b
    )


# ==========================================================
# PYBEDTOOLS — SUBTRACT
# ==========================================================

def pybedtools_subtract(
    bed_a,
    bed_b
):
    """
    Subtract genomic intervals.
    """

    return bed_a.subtract(
        bed_b
    )


# ==========================================================
# PYSAM — OPEN SAM/BAM/CRAM
# ==========================================================

def pysam_open(
    filename,
    mode="rb"
):
    """
    Open a SAM/BAM/CRAM alignment file.
    """

    import pysam

    return pysam.AlignmentFile(
        str(filename),
        str(mode)
    )


# ==========================================================
# PYSAM — BAM SUMMARY
# ==========================================================

def pysam_alignment_summary(
    filename
):
    """
    Summarize an alignment file.
    """

    import pysam

    with pysam.AlignmentFile(
        str(filename),
        "rb"
    ) as bam:

        references = list(
            bam.references
        )

        lengths = list(
            bam.lengths
        )

        count = bam.count()

    return {
        "references": references,
        "lengths": lengths,
        "mapped_reads": count,
    }


# ==========================================================
# PYSAM — FETCH REGION
# ==========================================================

def pysam_fetch_region(
    filename,
    chromosome,
    start,
    end
):
    """
    Fetch alignments from a genomic region.
    """

    import pysam

    records = []

    with pysam.AlignmentFile(
        str(filename),
        "rb"
    ) as bam:

        for read in bam.fetch(
            str(chromosome),
            int(start),
            int(end)
        ):

            records.append(read)

    return records


# ==========================================================
# ANNDATA — CREATE DATASET
# ==========================================================

def anndata_create(
    data,
    obs=None,
    var=None
):
    """
    Create an AnnData object.
    """

    import anndata

    return anndata.AnnData(
        X=data,
        obs=obs,
        var=var
    )


# ==========================================================
# ANNDATA — SUMMARY
# ==========================================================

def anndata_summary(
    data
):
    """
    Return basic AnnData information.
    """

    return {
        "shape":
            tuple(data.shape),

        "observations":
            int(data.n_obs),

        "variables":
            int(data.n_vars),

        "layers":
            list(data.layers.keys()),

        "obsm":
            list(data.obsm.keys()),

        "varm":
            list(data.varm.keys()),
    }


# ==========================================================
# ANNDATA — READ
# ==========================================================

def anndata_read(
    filename
):
    """
    Read an AnnData file.
    """

    import anndata

    return anndata.read_h5ad(
        str(filename)
    )


# ==========================================================
# ANNDATA — WRITE
# ==========================================================

def anndata_write(
    data,
    filename
):
    """
    Write an AnnData object to H5AD.
    """

    data.write_h5ad(
        str(filename)
    )

    return filename


# ==========================================================
# BIOM — READ
# ==========================================================

def biom_read(
    filename
):
    """
    Read a BIOM-format table.
    """

    from biom import load_table

    return load_table(
        str(filename)
    )


# ==========================================================
# BIOM — SUMMARY
# ==========================================================

def biom_summary(
    table
):
    """
    Return basic BIOM-table statistics.
    """

    return {
        "shape":
            table.shape,

        "observations":
            table.length(axis="observation"),

        "samples":
            table.length(axis="sample"),

        "nonzero":
            int(
                table.nnz
            ),
    }


# ==========================================================
# BIOM — TABLE FROM MATRIX
# ==========================================================

def biom_from_matrix(
    matrix,
    observation_ids,
    sample_ids
):
    """
    Create a BIOM table from a matrix.
    """

    from biom import Table

    return Table(
        matrix,
        observation_ids,
        sample_ids
    )


# ==========================================================
# SCIKIT-BIO — DNA
# ==========================================================

def skbio_dna(
    sequence
):
    """
    Create a scikit-bio DNA object.
    """

    from skbio import DNA

    return DNA(
        str(sequence)
    )


# ==========================================================
# SCIKIT-BIO — RNA
# ==========================================================

def skbio_rna(
    sequence
):
    """
    Create an RNA sequence.
    """

    from skbio import RNA

    return RNA(
        str(sequence)
    )


# ==========================================================
# SCIKIT-BIO — PROTEIN
# ==========================================================

def skbio_protein(
    sequence
):
    """
    Create a protein sequence.
    """

    from skbio import Protein

    return Protein(
        str(sequence)
    )


# ==========================================================
# SCIKIT-BIO — DNA DISTANCE
# ==========================================================

def skbio_dna_distance(
    sequence_a,
    sequence_b
):
    """
    Calculate Hamming distance between DNA sequences.
    """

    from skbio import DNA

    a = DNA(
        str(sequence_a)
    )

    b = DNA(
        str(sequence_b)
    )

    return a.distance(
        b,
        metric="hamming"
    )


# ==========================================================
# SCIKIT-BIO — DNA ALIGNMENT
# ==========================================================

def skbio_align_pairwise(
    sequence_a,
    sequence_b
):
    """
    Perform a pairwise global alignment.
    """

    from skbio.alignment import global_pairwise_align_nucleotide

    a = skbio_dna(
        sequence_a
    )

    b = skbio_dna(
        sequence_b
    )

    return global_pairwise_align_nucleotide(
        a,
        b
    )


# ==========================================================
# SCANPY — READ H5AD
# ==========================================================

def scanpy_read(
    filename
):
    """
    Read a single-cell AnnData dataset.
    """

    import scanpy as sc

    return sc.read_h5ad(
        str(filename)
    )


# ==========================================================
# SCANPY — NORMALIZE TOTAL
# ==========================================================

def scanpy_normalize_total(
    data,
    target_sum=1e4
):
    """
    Normalize counts per cell.
    """

    import scanpy as sc

    result = data.copy()

    sc.pp.normalize_total(
        result,
        target_sum=float(target_sum)
    )

    return result


# ==========================================================
# SCANPY — LOG TRANSFORM
# ==========================================================

def scanpy_log1p(
    data
):
    """
    Apply log1p transformation.
    """

    import scanpy as sc

    result = data.copy()

    sc.pp.log1p(
        result
    )

    return result


# ==========================================================
# SCANPY — HIGHLY VARIABLE GENES
# ==========================================================

def scanpy_highly_variable_genes(
    data,
    n_top_genes=2000
):
    """
    Identify highly variable genes.
    """

    import scanpy as sc

    result = data.copy()

    sc.pp.highly_variable_genes(
        result,
        n_top_genes=int(n_top_genes)
    )

    return result


# ==========================================================
# SCANPY — PCA
# ==========================================================

def scanpy_pca(
    data,
    n_comps=50
):
    """
    Perform PCA on single-cell data.
    """

    import scanpy as sc

    result = data.copy()

    sc.pp.pca(
        result,
        n_comps=int(n_comps)
    )

    return result


# ==========================================================
# SCANPY — NEIGHBORS
# ==========================================================

def scanpy_neighbors(
    data,
    n_neighbors=15
):
    """
    Compute a nearest-neighbor graph.
    """

    import scanpy as sc

    result = data.copy()

    sc.pp.neighbors(
        result,
        n_neighbors=int(n_neighbors)
    )

    return result


# ==========================================================
# SCANPY — UMAP
# ==========================================================

def scanpy_umap(
    data
):
    """
    Compute a UMAP embedding.
    """

    import scanpy as sc

    result = data.copy()

    sc.tl.umap(
        result
    )

    return result


# ==========================================================
# SCANPY — LEIDEN CLUSTERING
# ==========================================================

def scanpy_leiden(
    data,
    resolution=1.0
):
    """
    Perform Leiden clustering.
    """

    import scanpy as sc

    result = data.copy()

    sc.tl.leiden(
        result,
        resolution=float(resolution)
    )

    return result


# ==========================================================
# SCANPY — CELL ANALYSIS PIPELINE
# ==========================================================

def scanpy_basic_pipeline(
    data,
    target_sum=1e4,
    n_top_genes=2000,
    n_comps=30,
    n_neighbors=15
):
    """
    Perform a basic single-cell preprocessing pipeline.

    Steps:
        1. Normalize
        2. Log transform
        3. Find highly variable genes
        4. PCA
        5. Neighbor graph
        6. UMAP
    """

    import scanpy as sc

    result = data.copy()

    sc.pp.normalize_total(
        result,
        target_sum=float(target_sum)
    )

    sc.pp.log1p(
        result
    )

    sc.pp.highly_variable_genes(
        result,
        n_top_genes=int(n_top_genes)
    )

    sc.tl.pca(
        result,
        n_comps=int(n_comps)
    )

    sc.pp.neighbors(
        result,
        n_neighbors=int(n_neighbors)
    )

    sc.tl.umap(
        result
    )

    return result


# ==========================================================
# BIOLOGY PACKAGE STATUS
# ==========================================================

def biology_part7_status():
    """
    Display availability of all biology packages.
    """

    packages = [
        "anndata",
        "biom-format",
        "biopython",
        "bioregistry",
        "biotite",
        "DendroPy",
        "msprime",
        "pybedtools",
        "pysam",
        "scanpy",
        "scikit-bio",
        "tskit",
    ]

    results = {}

    print()
    print("=" * 75)
    print(
        "DAVE — BIOLOGY / BIOINFORMATICS PART 7 STATUS"
    )
    print("=" * 75)
    print()

    for package_name in packages:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<20} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<20} unavailable"
            )

    print()

    return results


# ==========================================================
# BIOLOGY SELF TEST
# ==========================================================

def biology_part7_selftest(
    verbose=True
):
    """
    Test the major biology integrations.
    """

    tests = []


    # ------------------------------------------------------
    # BIOPYTHON
    # ------------------------------------------------------

    try:

        sequence = "ATGCGT"

        complement = bio_complement(
            sequence
        )

        gc = bio_gc_content(
            sequence
        )

        tests.append(
            (
                "biopython",
                complement == "TACGCA"
                and gc > 0
            )
        )

    except Exception as exc:

        tests.append(
            (
                "biopython",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # BIOREGISTRY
    # ------------------------------------------------------

    try:

        result = bioregistry_make_curie(
            "uniprot",
            "P12345"
        )

        tests.append(
            (
                "bioregistry",
                result is not None
            )
        )

    except Exception as exc:

        tests.append(
            (
                "bioregistry",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # BIOTITE
    # ------------------------------------------------------

    try:

        sequence = biotite_dna(
            "ATGC"
        )

        tests.append(
            (
                "biotite",
                len(sequence) == 4
            )
        )

    except Exception as exc:

        tests.append(
            (
                "biotite",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # DENDROPY
    # ------------------------------------------------------

    try:

        tree = dendropy_tree_from_string(
            "(A,B,(C,D));"
        )

        summary = dendropy_tree_summary(
            tree
        )

        tests.append(
            (
                "DendroPy",
                summary["taxa"] == 4
            )
        )

    except Exception as exc:

        tests.append(
            (
                "DendroPy",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # MSPRIME / TSKIT
    # ------------------------------------------------------

    try:

        ts = msprime_simulate(
            sample_size=4,
            sequence_length=1000,
            random_seed=123
        )

        summary = tskit_summary(
            ts
        )

        tests.append(
            (
                "msprime/tskit",
                summary["num_nodes"] > 0
            )
        )

    except Exception as exc:

        tests.append(
            (
                "msprime/tskit",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # ANNDATA
    # ------------------------------------------------------

    try:

        import numpy as np

        data = anndata_create(
            np.array(
                [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                ]
            )
        )

        summary = anndata_summary(
            data
        )

        tests.append(
            (
                "anndata",
                summary["shape"] == (3, 3)
            )
        )

    except Exception as exc:

        tests.append(
            (
                "anndata",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # BIOM
    # ------------------------------------------------------

    try:

        import numpy as np

        table = biom_from_matrix(
            np.array(
                [
                    [1, 2],
                    [3, 4],
                ]
            ),
            ["gene1", "gene2"],
            ["sample1", "sample2"]
        )

        summary = biom_summary(
            table
        )

        tests.append(
            (
                "biom-format",
                summary["shape"] == (2, 2)
            )
        )

    except Exception as exc:

        tests.append(
            (
                "biom-format",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # SCIKIT-BIO
    # ------------------------------------------------------

    try:

        distance = skbio_dna_distance(
            "ATGC",
            "ATGT"
        )

        tests.append(
            (
                "scikit-bio",
                float(distance) > 0
            )
        )

    except Exception as exc:

        tests.append(
            (
                "scikit-bio",
                False,
                str(exc)
            )
        )


    # ======================================================
    # RESULTS
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 75)
        print(
            "DAVE — BIOLOGY / BIOINFORMATICS PART 7 SELF TEST"
        )
        print("=" * 75)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 75)

        print(
            f"Passed: {passed}"
        )

        print(
            f"Failed: {failed}"
        )

        print(
            f"Total:  {len(tests)}"
        )

        print("-" * 75)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# BIOLOGY HELP
# ==========================================================

def biology_part7_help():

    print("""
==============================================================================
DAVE — BIOLOGY / BIOINFORMATICS PART 7
==============================================================================

BIOPYTHON
---------

    bio_sequence(sequence)

    bio_complement(sequence)

    bio_reverse_complement(sequence)

    bio_transcribe(sequence)

    bio_translate(sequence)

    bio_gc_content(sequence)

    bio_molecular_weight(sequence)

    bio_sequence_report(sequence)

    bio_read_fasta(filename)

    bio_write_fasta(records, filename)

    bio_pairwise_alignment(
        sequence_a,
        sequence_b
    )

    bio_read_genbank(filename)

    bio_read_newick(filename)


BIOREGISTRY
-----------

    bioregistry_normalize(
        prefix,
        identifier
    )

    bioregistry_make_curie(
        prefix,
        identifier
    )

    bioregistry_make_uri(
        prefix,
        identifier
    )


BIOTITE
-------

    biotite_dna(sequence)

    biotite_protein(sequence)

    biotite_nucleotide_alphabet()

    biotite_protein_alphabet()

    biotite_structure_read(filename)

    biotite_structure_summary(structure)


DENDROPY
--------

    dendropy_read_tree(filename)

    dendropy_tree_from_string(tree_string)

    dendropy_tree_summary(tree)


MSPRIME
-------

    msprime_simulate(...)

    msprime_simulate_mutations(...)

    msprime_simulate_genome(...)


TSKIT
-----

    tskit_load(filename)

    tskit_summary(ts)

    tskit_trees(ts)

    tskit_diversity(ts)

    tskit_divergence(ts, sample_sets)

    tskit_genotype_matrix(ts)


PYBEDTOOLS
----------

    pybedtools_from_string(bed_string)

    pybedtools_sort(bed)

    pybedtools_merge(bed)

    pybedtools_intersect(bed_a, bed_b)

    pybedtools_subtract(bed_a, bed_b)


PYSAM
-----

    pysam_open(filename)

    pysam_alignment_summary(filename)

    pysam_fetch_region(
        filename,
        chromosome,
        start,
        end
    )


ANNDATA
-------

    anndata_create(
        data,
        obs,
        var
    )

    anndata_summary(data)

    anndata_read(filename)

    anndata_write(data, filename)


BIOM-FORMAT
-----------

    biom_read(filename)

    biom_summary(table)

    biom_from_matrix(
        matrix,
        observation_ids,
        sample_ids
    )


SCIKIT-BIO
----------

    skbio_dna(sequence)

    skbio_rna(sequence)

    skbio_protein(sequence)

    skbio_dna_distance(
        sequence_a,
        sequence_b
    )

    skbio_align_pairwise(
        sequence_a,
        sequence_b
    )


SCANPY
------

    scanpy_read(filename)

    scanpy_normalize_total(data)

    scanpy_log1p(data)

    scanpy_highly_variable_genes(data)

    scanpy_pca(data)

    scanpy_neighbors(data)

    scanpy_umap(data)

    scanpy_leiden(data)

    scanpy_basic_pipeline(data)


TESTING
-------

    biology_part7_status()

    biology_part7_selftest()

==============================================================================
""")

# ==========================================================
# DAVE
# GIS / GEOSPATIAL / GEOSCIENCE INTEGRATION
# PART 8
# ==========================================================
#
# Packages covered:
#
#   affine
#   earthpy
#   esda
#   flopy
#   GDAL
#   gempy
#   gempy_engine
#   geographiclib
#   geopandas
#   geopy
#   giddy
#   libpysal
#   mapclassify
#   momepy
#   movingpandas
#   osmnx
#   pydeck
#   pyogrio
#   pyproj
#   pysal
#   pyregion
#   rasterio
#   rasterstats
#   rtree
#   shapely
#   spaghetti
#   spglm
#   spint
#   splot
#   spml
#   spopt
#   spreg
#   striplog
#   tobler
#   topologicpy
#   wellpathpy
#   welly
#   xyzservices
#
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_affine():
    return load_scientific_package("affine")


def _get_earthpy():
    return load_scientific_package("earthpy")


def _get_esda():
    return load_scientific_package("esda")


def _get_flopy():
    return load_scientific_package("flopy")


def _get_gdal():
    return load_scientific_package("GDAL")


def _get_gempy():
    return load_scientific_package("gempy")


def _get_gempy_engine():
    return load_scientific_package("gempy_engine")


def _get_geographiclib():
    return load_scientific_package("geographiclib")


def _get_geopandas():
    return load_scientific_package("geopandas")


def _get_geopy():
    return load_scientific_package("geopy")


def _get_giddy():
    return load_scientific_package("giddy")


def _get_libpysal():
    return load_scientific_package("libpysal")


def _get_mapclassify():
    return load_scientific_package("mapclassify")


def _get_momepy():
    return load_scientific_package("momepy")


def _get_movingpandas():
    return load_scientific_package("movingpandas")


def _get_osmnx():
    return load_scientific_package("osmnx")


def _get_pydeck():
    return load_scientific_package("pydeck")


def _get_pyogrio():
    return load_scientific_package("pyogrio")


def _get_pyproj():
    return load_scientific_package("pyproj")


def _get_pysal():
    return load_scientific_package("pysal")


def _get_pyregion():
    return load_scientific_package("pyregion")


def _get_rasterio():
    return load_scientific_package("rasterio")


def _get_rasterstats():
    return load_scientific_package("rasterstats")


def _get_rtree():
    return load_scientific_package("rtree")


def _get_shapely():
    return load_scientific_package("shapely")


def _get_spaghetti():
    return load_scientific_package("spaghetti")


def _get_spglm():
    return load_scientific_package("spglm")


def _get_spint():
    return load_scientific_package("spint")


def _get_splot():
    return load_scientific_package("splot")


def _get_spml():
    return load_scientific_package("spml")


def _get_spopt():
    return load_scientific_package("spopt")


def _get_spreg():
    return load_scientific_package("spreg")


def _get_striplog():
    return load_scientific_package("striplog")


def _get_tobler():
    return load_scientific_package("tobler")


def _get_topologicpy():
    return load_scientific_package("topologicpy")


def _get_wellpathpy():
    return load_scientific_package("wellpathpy")


def _get_welly():
    return load_scientific_package("welly")


def _get_xyzservices():
    return load_scientific_package("xyzservices")


# ==========================================================
# SHAPELY — BASIC POINT
# ==========================================================

def geo_point(
    x,
    y
):
    """
    Create a Shapely Point.
    """

    from shapely.geometry import Point

    return Point(
        float(x),
        float(y)
    )


# ==========================================================
# SHAPELY — LINE
# ==========================================================

def geo_line(
    coordinates
):
    """
    Create a Shapely LineString.
    """

    from shapely.geometry import LineString

    return LineString(
        coordinates
    )


# ==========================================================
# SHAPELY — POLYGON
# ==========================================================

def geo_polygon(
    coordinates
):
    """
    Create a Shapely Polygon.
    """

    from shapely.geometry import Polygon

    return Polygon(
        coordinates
    )


# ==========================================================
# SHAPELY — BUFFER
# ==========================================================

def geo_buffer(
    geometry,
    distance
):
    """
    Create a buffer around a geometry.
    """

    return geometry.buffer(
        float(distance)
    )


# ==========================================================
# SHAPELY — AREA
# ==========================================================

def geo_area(
    geometry
):
    """
    Return geometry area.
    """

    return float(
        geometry.area
    )


# ==========================================================
# SHAPELY — LENGTH
# ==========================================================

def geo_length(
    geometry
):
    """
    Return geometry length.
    """

    return float(
        geometry.length
    )


# ==========================================================
# SHAPELY — DISTANCE
# ==========================================================

def geo_distance(
    geometry_a,
    geometry_b
):
    """
    Calculate planar geometry distance.
    """

    return float(
        geometry_a.distance(
            geometry_b
        )
    )


# ==========================================================
# SHAPELY — INTERSECTION
# ==========================================================

def geo_intersection(
    geometry_a,
    geometry_b
):
    """
    Calculate geometric intersection.
    """

    return geometry_a.intersection(
        geometry_b
    )


# ==========================================================
# SHAPELY — UNION
# ==========================================================

def geo_union(
    geometry_a,
    geometry_b
):
    """
    Calculate geometric union.
    """

    return geometry_a.union(
        geometry_b
    )


# ==========================================================
# SHAPELY — CONTAINS
# ==========================================================

def geo_contains(
    container,
    geometry
):
    """
    Test whether one geometry contains another.
    """

    return bool(
        container.contains(
            geometry
        )
    )


# ==========================================================
# SHAPELY — WKT
# ==========================================================

def geo_from_wkt(
    text
):
    """
    Convert WKT text into a geometry.
    """

    from shapely import wkt

    return wkt.loads(
        str(text)
    )


# ==========================================================
# SHAPELY — GEOJSON
# ==========================================================

def geo_from_geojson(
    geometry
):
    """
    Convert a GeoJSON geometry dictionary into Shapely.
    """

    from shapely.geometry import shape

    return shape(
        geometry
    )


# ==========================================================
# SHAPELY — GEOJSON EXPORT
# ==========================================================

def geo_to_geojson(
    geometry
):
    """
    Convert a Shapely geometry to GeoJSON.
    """

    from shapely.geometry import mapping

    return mapping(
        geometry
    )


# ==========================================================
# GEOPANDAS — CREATE GEODATAFRAME
# ==========================================================

def geopandas_create(
    data=None,
    geometry=None,
    crs=None
):
    """
    Create a GeoDataFrame.
    """

    import geopandas as gpd

    return gpd.GeoDataFrame(
        data,
        geometry=geometry,
        crs=crs
    )


# ==========================================================
# GEOPANDAS — READ FILE
# ==========================================================

def geopandas_read(
    filename,
    **kwargs
):
    """
    Read a spatial vector dataset.
    """

    import geopandas as gpd

    return gpd.read_file(
        str(filename),
        **kwargs
    )


# ==========================================================
# GEOPANDAS — WRITE FILE
# ==========================================================

def geopandas_write(
    dataframe,
    filename,
    driver=None
):
    """
    Write a GeoDataFrame.
    """

    kwargs = {}

    if driver is not None:
        kwargs["driver"] = driver

    dataframe.to_file(
        str(filename),
        **kwargs
    )

    return filename


# ==========================================================
# GEOPANDAS — REPROJECT
# ==========================================================

def geopandas_reproject(
    dataframe,
    crs
):
    """
    Reproject a GeoDataFrame.
    """

    return dataframe.to_crs(
        crs
    )


# ==========================================================
# GEOPANDAS — SPATIAL JOIN
# ==========================================================

def geopandas_spatial_join(
    left,
    right,
    predicate="intersects"
):
    """
    Perform a spatial join.
    """

    import geopandas as gpd

    return gpd.sjoin(
        left,
        right,
        predicate=str(predicate)
    )


# ==========================================================
# GEOPANDAS — TOTAL AREA
# ==========================================================

def geopandas_total_area(
    dataframe
):
    """
    Calculate total geometry area.
    """

    return float(
        dataframe.geometry.area.sum()
    )


# ==========================================================
# GEOPANDAS — TOTAL LENGTH
# ==========================================================

def geopandas_total_length(
    dataframe
):
    """
    Calculate total geometry length.
    """

    return float(
        dataframe.geometry.length.sum()
    )


# ==========================================================
# PYPROJ — COORDINATE TRANSFORMATION
# ==========================================================

def geo_transform(
    x,
    y,
    from_crs,
    to_crs
):
    """
    Transform coordinates between coordinate reference systems.
    """

    from pyproj import Transformer

    transformer = Transformer.from_crs(
        from_crs,
        to_crs,
        always_xy=True
    )

    return transformer.transform(
        float(x),
        float(y)
    )


# ==========================================================
# PYPROJ — CRS INFORMATION
# ==========================================================

def geo_crs_info(
    crs
):
    """
    Return information about a coordinate reference system.
    """

    from pyproj import CRS

    obj = CRS.from_user_input(
        crs
    )

    return {
        "name": obj.name,
        "authority":
            obj.to_authority(),
        "is_geographic":
            obj.is_geographic,
        "is_projected":
            obj.is_projected,
        "axis_info":
            [
                str(axis)
                for axis in obj.axis_info
            ],
    }


# ==========================================================
# PYPROJ — DISTANCE
# ==========================================================

def geo_geodesic_distance(
    longitude1,
    latitude1,
    longitude2,
    latitude2
):
    """
    Calculate geodesic distance on Earth.
    """

    from pyproj import Geod

    geod = Geod(
        ellps="WGS84"
    )

    az1, az2, distance = geod.inv(
        float(longitude1),
        float(latitude1),
        float(longitude2),
        float(latitude2)
    )

    return {
        "distance_m": float(distance),
        "azimuth_1": float(az1),
        "azimuth_2": float(az2),
    }


# ==========================================================
# GEOGRAPHICLIB — DISTANCE
# ==========================================================

def geographiclib_distance(
    latitude1,
    longitude1,
    latitude2,
    longitude2
):
    """
    Calculate WGS84 geodesic distance.
    """

    from geographiclib.geodesic import Geodesic

    result = Geodesic.WGS84.Inverse(
        float(latitude1),
        float(longitude1),
        float(latitude2),
        float(longitude2)
    )

    return result


# ==========================================================
# GEOGRAPHICLIB — DIRECT POSITION
# ==========================================================

def geographiclib_destination(
    latitude,
    longitude,
    azimuth,
    distance
):
    """
    Calculate a destination point from a starting point.
    """

    from geographiclib.geodesic import Geodesic

    result = Geodesic.WGS84.Direct(
        float(latitude),
        float(longitude),
        float(azimuth),
        float(distance)
    )

    return {
        "latitude":
            result["lat2"],
        "longitude":
            result["lon2"],
        "azimuth":
            result["azi2"],
    }


# ==========================================================
# GEOPY — GEOCODING
# ==========================================================

def geopy_geocoder(
    address,
    user_agent="dave_pro_max"
):
    """
    Geocode an address using Nominatim.

    Internet access is required.
    """

    from geopy.geocoders import Nominatim

    geolocator = Nominatim(
        user_agent=str(user_agent)
    )

    return geolocator.geocode(
        str(address)
    )


# ==========================================================
# GEOPY — REVERSE GEOCODING
# ==========================================================

def geopy_reverse(
    latitude,
    longitude,
    user_agent="dave_pro_max"
):
    """
    Reverse-geocode coordinates.
    """

    from geopy.geocoders import Nominatim

    geolocator = Nominatim(
        user_agent=str(user_agent)
    )

    return geolocator.reverse(
        (
            float(latitude),
            float(longitude)
        )
    )


# ==========================================================
# AFFINE — TRANSFORMATION
# ==========================================================

def affine_transform(
    x,
    y,
    a=1,
    b=0,
    c=0,
    d=0,
    e=1,
    f=0
):
    """
    Apply an affine transformation.

        x' = ax + by + c
        y' = dx + ey + f
    """

    from affine import Affine

    transform = Affine(
        float(a),
        float(b),
        float(c),
        float(d),
        float(e),
        float(f)
    )

    return transform * (
        float(x),
        float(y)
    )


# ==========================================================
# RASTERIO — OPEN RASTER
# ==========================================================

def raster_open(
    filename,
    mode="r"
):
    """
    Open a raster dataset.
    """

    import rasterio

    return rasterio.open(
        str(filename),
        str(mode)
    )


# ==========================================================
# RASTERIO — RASTER SUMMARY
# ==========================================================

def raster_summary(
    filename
):
    """
    Return basic raster metadata.
    """

    import rasterio

    with rasterio.open(
        str(filename)
    ) as dataset:

        return {
            "width":
                dataset.width,

            "height":
                dataset.height,

            "bands":
                dataset.count,

            "crs":
                str(dataset.crs),

            "dtype":
                str(dataset.dtypes),

            "bounds":
                tuple(
                    dataset.bounds
                ),

            "transform":
                str(dataset.transform),
        }


# ==========================================================
# RASTERIO — READ BAND
# ==========================================================

def raster_read_band(
    filename,
    band=1
):
    """
    Read a raster band into an array.
    """

    import rasterio

    with rasterio.open(
        str(filename)
    ) as dataset:

        return dataset.read(
            int(band)
        )


# ==========================================================
# RASTERIO — RASTER STATISTICS
# ==========================================================

def raster_statistics(
    filename,
    band=1
):
    """
    Calculate statistics for a raster band.
    """

    import numpy as np
    import rasterio

    with rasterio.open(
        str(filename)
    ) as dataset:

        data = dataset.read(
            int(band)
        )

        if np.ma.isMaskedArray(data):
            values = data.compressed()
        else:
            values = data.ravel()

    if len(values) == 0:

        return {
            "count": 0
        }

    return {
        "count":
            int(len(values)),

        "minimum":
            float(np.min(values)),

        "maximum":
            float(np.max(values)),

        "mean":
            float(np.mean(values)),

        "median":
            float(np.median(values)),

        "standard_deviation":
            float(np.std(values)),
    }


# ==========================================================
# RASTERSTATS — ZONAL STATISTICS
# ==========================================================

def raster_zonal_statistics(
    vectors,
    raster,
    stats=None
):
    """
    Calculate statistics for raster values within vector zones.
    """

    from rasterstats import zonal_stats

    if stats is None:
        stats = [
            "min",
            "max",
            "mean",
            "median",
            "count"
        ]

    return zonal_stats(
        vectors,
        raster,
        stats=stats
    )


# ==========================================================
# PYOGRIO — READ
# ==========================================================

def pyogrio_read(
    filename,
    **kwargs
):
    """
    Read vector data with Pyogrio.
    """

    import pyogrio

    return pyogrio.read_dataframe(
        str(filename),
        **kwargs
    )


# ==========================================================
# PYOGRIO — WRITE
# ==========================================================

def pyogrio_write(
    dataframe,
    filename,
    **kwargs
):
    """
    Write vector data with Pyogrio.
    """

    import pyogrio

    pyogrio.write_dataframe(
        dataframe,
        str(filename),
        **kwargs
    )

    return filename


# ==========================================================
# RTREE — SPATIAL INDEX
# ==========================================================

def rtree_create(
    bounds_list
):
    """
    Create an R-tree spatial index.

    bounds_list:
        iterable of
        (minx, miny, maxx, maxy)
    """

    from rtree import index

    idx = index.Index()

    for number, bounds in enumerate(
        bounds_list
    ):

        idx.insert(
            number,
            tuple(
                float(x)
                for x in bounds
            )
        )

    return idx


# ==========================================================
# RTREE — QUERY
# ==========================================================

def rtree_query(
    spatial_index,
    bounds
):
    """
    Query an R-tree.
    """

    return list(
        spatial_index.intersection(
            tuple(
                float(x)
                for x in bounds
            )
        )
    )


# ==========================================================
# EARTHPY — DATA PATH
# ==========================================================

def earthpy_data_path():
    """
    Return EarthPy's example-data directory.
    """

    import earthpy

    return str(
        earthpy.io.HOME
    )


# ==========================================================
# EARTHPY — EPSG
# ==========================================================

def earthpy_epsg(
    epsg
):
    """
    Construct an EPSG projection string.
    """

    return f"EPSG:{int(epsg)}"


# ==========================================================
# MAPCLASSIFY — CLASSIFY VALUES
# ==========================================================

def mapclassify_values(
    values,
    scheme="NaturalBreaks",
    k=5
):
    """
    Classify numerical values for mapping.
    """

    import mapclassify

    classifier = getattr(
        mapclassify,
        str(scheme)
    )

    model = classifier(
        values,
        k=int(k)
    )

    return {
        "yb":
            model.yb,

        "bins":
            model.bins,

        "counts":
            model.counts,
    }


# ==========================================================
# LIBPYSAL — QUEEN WEIGHTS
# ==========================================================

def libpysal_queen_weights(
    dataframe
):
    """
    Create Queen contiguity spatial weights.
    """

    from libpysal.weights import Queen

    return Queen.from_dataframe(
        dataframe
    )


# ==========================================================
# LIBPYSAL — ROOK WEIGHTS
# ==========================================================

def libpysal_rook_weights(
    dataframe
):
    """
    Create Rook contiguity spatial weights.
    """

    from libpysal.weights import Rook

    return Rook.from_dataframe(
        dataframe
    )


# ==========================================================
# ESDA — MORAN'S I
# ==========================================================

def esda_moran(
    values,
    weights
):
    """
    Calculate Moran's I spatial autocorrelation.
    """

    from esda.moran import Moran

    model = Moran(
        values,
        weights
    )

    return {
        "I":
            float(model.I),

        "expected":
            float(model.EI),

        "variance":
            float(model.VI_norm),

        "z_score":
            float(model.z_norm),

        "p_value":
            float(model.p_norm),
    }


# ==========================================================
# ESDA — LOCAL MORAN
# ==========================================================

def esda_local_moran(
    values,
    weights
):
    """
    Calculate Local Moran statistics.
    """

    from esda.moran import Moran_Local

    model = Moran_Local(
        values,
        weights
    )

    return {
        "Is":
            model.Is,

        "q":
            model.q,

        "p_sim":
            model.p_sim,

        "z_sim":
            model.z_sim,
    }


# ==========================================================
# SPREG — OLS
# ==========================================================

def spreg_ols(
    y,
    x,
    name_y="y",
    name_x=None
):
    """
    Run a spatial-regression OLS model.
    """

    from spreg import OLS

    if name_x is None:
        name_x = [
            f"x{i + 1}"
            for i in range(
                len(x[0])
            )
        ]

    model = OLS(
        y,
        x,
        name_y=str(name_y),
        name_x=name_x
    )

    return model


# ==========================================================
# SPOPT — LOCATION ALLOCATION
# ==========================================================

def spopt_status():
    """
    Return whether the spopt package can be imported.
    """

    module = _get_spopt()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# SPAGHETTI — NETWORK OBJECT
# ==========================================================

def spaghetti_status():
    """
    Return Spaghetti availability.
    """

    module = _get_spaghetti()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# OSMNX — STREET NETWORK
# ==========================================================

def osmnx_street_network(
    place,
    network_type="drive"
):
    """
    Download a street network from OpenStreetMap.

    Internet access is required.
    """

    import osmnx as ox

    return ox.graph_from_place(
        str(place),
        network_type=str(network_type)
    )


# ==========================================================
# OSMNX — POINT NETWORK
# ==========================================================

def osmnx_point_network(
    latitude,
    longitude,
    distance=1000,
    network_type="drive"
):
    """
    Download a street network around a coordinate.
    """

    import osmnx as ox

    return ox.graph_from_point(
        (
            float(latitude),
            float(longitude)
        ),
        dist=float(distance),
        network_type=str(network_type)
    )


# ==========================================================
# OSMNX — NETWORK SUMMARY
# ==========================================================

def osmnx_network_summary(
    graph
):
    """
    Return basic street-network information.
    """

    import networkx as nx

    return {
        "nodes":
            graph.number_of_nodes(),

        "edges":
            graph.number_of_edges(),

        "connected_components":
            nx.number_weakly_connected_components(
                graph
            )
            if nx.is_directed(graph)
            else nx.number_connected_components(
                graph
            ),
    }


# ==========================================================
# OSMNX — NETWORK TO GEODATAFRAMES
# ==========================================================

def osmnx_to_geodataframes(
    graph
):
    """
    Convert an OSMnx graph into node and edge GeoDataFrames.
    """

    import osmnx as ox

    return ox.graph_to_gdfs(
        graph
    )


# ==========================================================
# PYDECK — POINT LAYER
# ==========================================================

def pydeck_points(
    dataframe,
    latitude="latitude",
    longitude="longitude",
    radius=100
):
    """
    Create a PyDeck point layer.
    """

    import pydeck as pdk

    return pdk.Layer(
        "ScatterplotLayer",
        data=dataframe,
        get_position=[
            f"{{{longitude}}}",
            f"{{{latitude}}}"
        ],
        get_radius=float(radius)
    )


# ==========================================================
# XYZ SERVICES — PROVIDER LIST
# ==========================================================

def xyzservices_providers():
    """
    Return available XYZ tile providers.
    """

    import xyzservices.providers as providers

    return providers


# ==========================================================
# PYREGION — READ REGION FILE
# ==========================================================

def pyregion_read(
    filename
):
    """
    Read a DS9 region file.
    """

    import pyregion

    return pyregion.open(
        str(filename)
    )


# ==========================================================
# FLOPY — PACKAGE STATUS
# ==========================================================

def flopy_status():
    """
    Return FloPy information.
    """

    module = _get_flopy()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# FLOPY — MODEL SUMMARY
# ==========================================================

def flopy_model_summary(
    model
):
    """
    Summarize a FloPy model.
    """

    result = {}

    for attribute in (
        "name",
        "model_ws",
        "exe_name",
        "version",
    ):

        if hasattr(
            model,
            attribute
        ):

            result[attribute] = getattr(
                model,
                attribute
            )

    return result


# ==========================================================
# STRIPLOG — LOG STATUS
# ==========================================================

def striplog_status():
    """
    Return Striplog availability.
    """

    module = _get_striplog()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# WELLY — WELL LOG STATUS
# ==========================================================

def welly_status():
    """
    Return Welly availability.
    """

    module = _get_welly()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# WELLPATHPY — WELL PATH
# ==========================================================

def wellpathpy_status():
    """
    Return Wellpathpy availability.
    """

    module = _get_wellpathpy()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# TOPOLOGICPY — STATUS
# ==========================================================

def topologicpy_status():
    """
    Return TopologicPy availability.
    """

    module = _get_topologicpy()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# GEMPY — GEOLOGICAL MODEL STATUS
# ==========================================================

def gempy_status():
    """
    Return GemPy availability.
    """

    module = _get_gempy()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# GDAL — VERSION / STATUS
# ==========================================================

def gdal_status():
    """
    Return GDAL information.
    """

    module = _get_gdal()

    if module is None:

        return {
            "available": False
        }

    try:

        from osgeo import gdal

        version = gdal.VersionInfo(
            "--version"
        )

    except Exception:

        version = "unknown"

    return {
        "available": True,
        "version": str(version)
    }


# ==========================================================
# GDAL — OPEN DATASET
# ==========================================================

def gdal_open(
    filename,
    mode=0
):
    """
    Open a GDAL raster/vector dataset.

    mode:
        0 = read-only
        1 = update
    """

    from osgeo import gdal

    return gdal.Open(
        str(filename),
        int(mode)
    )


# ==========================================================
# GDAL — RASTER INFORMATION
# ==========================================================

def gdal_raster_info(
    filename
):
    """
    Return basic GDAL raster metadata.
    """

    from osgeo import gdal

    dataset = gdal.Open(
        str(filename)
    )

    if dataset is None:

        raise ValueError(
            f"Could not open GDAL dataset: {filename}"
        )

    return {
        "width":
            dataset.RasterXSize,

        "height":
            dataset.RasterYSize,

        "bands":
            dataset.RasterCount,

        "projection":
            dataset.GetProjection(),

        "driver":
            dataset.GetDriver().ShortName,
    }


# ==========================================================
# MOVINGPANDAS — TRAJECTORY STATUS
# ==========================================================

def movingpandas_status():
    """
    Return MovingPandas availability.
    """

    module = _get_movingpandas()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# MOMEPY — MORPHOLOGY STATUS
# ==========================================================

def momepy_status():
    """
    Return momepy availability.
    """

    module = _get_momepy()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# TOBLER — STATUS
# ==========================================================

def tobler_status():
    """
    Return Tobler availability.
    """

    module = _get_tobler()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# PYSAL — PACKAGE STATUS
# ==========================================================

def pysal_status():
    """
    Return PySAL availability and version.
    """

    module = _get_pysal()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# GIS PACKAGE STATUS
# ==========================================================

def gis_part8_status():
    """
    Check all GIS/geoscience packages.
    """

    packages = [
        "affine",
        "earthpy",
        "esda",
        "flopy",
        "GDAL",
        "gempy",
        "gempy_engine",
        "geographiclib",
        "geopandas",
        "geopy",
        "giddy",
        "libpysal",
        "mapclassify",
        "momepy",
        "movingpandas",
        "osmnx",
        "pydeck",
        "pyogrio",
        "pyproj",
        "pysal",
        "pyregion",
        "rasterio",
        "rasterstats",
        "rtree",
        "shapely",
        "spaghetti",
        "spglm",
        "spint",
        "splot",
        "spml",
        "spopt",
        "spreg",
        "striplog",
        "tobler",
        "topologicpy",
        "wellpathpy",
        "welly",
        "xyzservices",
    ]

    results = {}

    print()
    print("=" * 78)
    print(
        "DAVE — GIS / GEOSPATIAL / GEOSCIENCE STATUS"
    )
    print("=" * 78)
    print()

    for package_name in packages:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<20} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<20} unavailable"
            )

    print()

    return results


# ==========================================================
# GIS SELF TEST
# ==========================================================

def gis_part8_selftest(
    verbose=True
):
    """
    Test core GIS functionality.
    """

    tests = []


    # ------------------------------------------------------
    # SHAPELY
    # ------------------------------------------------------

    try:

        p1 = geo_point(
            0,
            0
        )

        p2 = geo_point(
            3,
            4
        )

        distance = geo_distance(
            p1,
            p2
        )

        tests.append(
            (
                "shapely",
                abs(distance - 5.0) < 1e-10
            )
        )

    except Exception as exc:

        tests.append(
            (
                "shapely",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PYPROJ
    # ------------------------------------------------------

    try:

        x, y = geo_transform(
            0,
            0,
            "EPSG:4326",
            "EPSG:3857"
        )

        tests.append(
            (
                "pyproj",
                abs(x) < 1e-6
                and abs(y) < 1e-6
            )
        )

    except Exception as exc:

        tests.append(
            (
                "pyproj",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # GEOGRAPHICLIB
    # ------------------------------------------------------

    try:

        result = geographiclib_distance(
            0,
            0,
            0,
            1
        )

        tests.append(
            (
                "geographiclib",
                result["s12"] > 100000
            )
        )

    except Exception as exc:

        tests.append(
            (
                "geographiclib",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # AFFINE
    # ------------------------------------------------------

    try:

        x, y = affine_transform(
            2,
            3,
            a=2,
            e=2
        )

        tests.append(
            (
                "affine",
                x == 4
                and y == 6
            )
        )

    except Exception as exc:

        tests.append(
            (
                "affine",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # GEOPANDAS
    # ------------------------------------------------------

    try:

        import geopandas as gpd

        dataframe = gpd.GeoDataFrame(
            {
                "name": [
                    "A",
                    "B"
                ]
            },
            geometry=[
                geo_point(0, 0),
                geo_point(1, 1)
            ],
            crs="EPSG:4326"
        )

        tests.append(
            (
                "geopandas",
                len(dataframe) == 2
            )
        )

    except Exception as exc:

        tests.append(
            (
                "geopandas",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # RTREE
    # ------------------------------------------------------

    try:

        idx = rtree_create(
            [
                (0, 0, 1, 1),
                (10, 10, 11, 11)
            ]
        )

        result = rtree_query(
            idx,
            (0, 0, 2, 2)
        )

        tests.append(
            (
                "rtree",
                0 in result
            )
        )

    except Exception as exc:

        tests.append(
            (
                "rtree",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # MAPCLASSIFY
    # ------------------------------------------------------

    try:

        result = mapclassify_values(
            [
                1,
                2,
                3,
                4,
                5
            ],
            scheme="Quantiles",
            k=2
        )

        tests.append(
            (
                "mapclassify",
                len(result["bins"]) == 2
            )
        )

    except Exception as exc:

        tests.append(
            (
                "mapclassify",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # LIBPYSAL
    # ------------------------------------------------------

    try:

        import geopandas as gpd

        polygons = gpd.GeoDataFrame(
            geometry=[
                geo_polygon(
                    [
                        (0, 0),
                        (1, 0),
                        (1, 1),
                        (0, 1)
                    ]
                ),
                geo_polygon(
                    [
                        (1, 0),
                        (2, 0),
                        (2, 1),
                        (1, 1)
                    ]
                )
            ]
        )

        weights = libpysal_queen_weights(
            polygons
        )

        tests.append(
            (
                "libpysal",
                weights.n == 2
            )
        )

    except Exception as exc:

        tests.append(
            (
                "libpysal",
                False,
                str(exc)
            )
        )


    # ======================================================
    # RESULTS
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 78)
        print(
            "DAVE — GIS / GEOSPATIAL PART 8 SELF TEST"
        )
        print("=" * 78)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 78)
        print(
            f"Passed: {passed}"
        )
        print(
            f"Failed: {failed}"
        )
        print(
            f"Total:  {len(tests)}"
        )
        print("-" * 78)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# GIS HELP
# ==========================================================

def gis_part8_help():

    print("""
==============================================================================
DAVE — GIS / GEOSPATIAL / GEOSCIENCE PART 8
==============================================================================

SHAPELY
-------

    geo_point(x, y)

    geo_line(coordinates)

    geo_polygon(coordinates)

    geo_buffer(geometry, distance)

    geo_area(geometry)

    geo_length(geometry)

    geo_distance(geometry_a, geometry_b)

    geo_intersection(geometry_a, geometry_b)

    geo_union(geometry_a, geometry_b)

    geo_contains(container, geometry)

    geo_from_wkt(text)

    geo_from_geojson(geometry)

    geo_to_geojson(geometry)


GEOPANDAS
---------

    geopandas_create(...)

    geopandas_read(filename)

    geopandas_write(dataframe, filename)

    geopandas_reproject(dataframe, crs)

    geopandas_spatial_join(
        left,
        right
    )

    geopandas_total_area(dataframe)

    geopandas_total_length(dataframe)


PYPROJ
------

    geo_transform(
        x,
        y,
        from_crs,
        to_crs
    )

    geo_crs_info(crs)

    geo_geodesic_distance(
        longitude1,
        latitude1,
        longitude2,
        latitude2
    )


GEOGRAPHICLIB
-------------

    geographiclib_distance(
        latitude1,
        longitude1,
        latitude2,
        longitude2
    )

    geographiclib_destination(
        latitude,
        longitude,
        azimuth,
        distance
    )


GEOPY
-----

    geopy_geocoder(address)

    geopy_reverse(
        latitude,
        longitude
    )


AFFINE
------

    affine_transform(
        x,
        y,
        a, b, c,
        d, e, f
    )


RASTERIO
--------

    raster_open(filename)

    raster_summary(filename)

    raster_read_band(
        filename,
        band
    )

    raster_statistics(
        filename,
        band
    )


RASTERSTATS
-----------

    raster_zonal_statistics(
        vectors,
        raster
    )


PYOGRIO
-------

    pyogrio_read(filename)

    pyogrio_write(
        dataframe,
        filename
    )


RTREE
-----

    rtree_create(bounds_list)

    rtree_query(
        spatial_index,
        bounds
    )


EARTHPY
-------

    earthpy_data_path()

    earthpy_epsg(epsg)


MAPCLASSIFY
-----------

    mapclassify_values(
        values,
        scheme,
        k
    )


LIBPYSAL
--------

    libpysal_queen_weights(dataframe)

    libpysal_rook_weights(dataframe)


ESDA
----

    esda_moran(
        values,
        weights
    )

    esda_local_moran(
        values,
        weights
    )


SPREG
-----

    spreg_ols(
        y,
        x
    )


OSMNX
-----

    osmnx_street_network(
        place,
        network_type
    )

    osmnx_point_network(
        latitude,
        longitude,
        distance
    )

    osmnx_network_summary(graph)

    osmnx_to_geodataframes(graph)


PYDECK
------

    pydeck_points(
        dataframe,
        latitude,
        longitude,
        radius
    )


XYZSERVICES
-----------

    xyzservices_providers()


PYREGION
--------

    pyregion_read(filename)


FLOPY
-----

    flopy_status()

    flopy_model_summary(model)


GEMPY
-----

    gempy_status()


WELLY / WELL LOGGING
--------------------

    welly_status()

    striplog_status()

    wellpathpy_status()


TOPOLOGICPY
-----------

    topologicpy_status()


SPATIAL / NETWORK PACKAGES
--------------------------

    spaghetti_status()

    spopt_status()

    movingpandas_status()

    momepy_status()

    tobler_status()

    pysal_status()


GDAL
----

    gdal_status()

    gdal_open(filename)

    gdal_raster_info(filename)


TESTING
-------

    gis_part8_status()

    gis_part8_selftest()

==============================================================================
""")

# ==========================================================
# DAVE
# STATISTICS / OPTIMIZATION / ECONOMETRICS / DEMOGRAPHY
# PART 9
# ==========================================================
#
# Packages covered:
#
#   cpsat-logutils
#   demes
#   PuLP
#   statsmodels
#
# Also provides cross-package utilities for:
#
#   statistical summaries
#   regression
#   time-series analysis
#   optimization
#   linear programming
#   demographic models
#   probability distributions
#
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_statsmodels():
    return load_scientific_package("statsmodels")


def _get_pulp():
    return load_scientific_package("PuLP")


def _get_demes():
    return load_scientific_package("demes")


def _get_cpsat_logutils():
    return load_scientific_package("cpsat-logutils")


# ==========================================================
# STATSMODELS — DESCRIPTIVE STATISTICS
# ==========================================================

def stats_describe(
    data
):
    """
    Generate descriptive statistics using Statsmodels/Pandas.
    """

    import pandas as pd

    if isinstance(
        data,
        pd.Series
    ):

        return data.describe()

    dataframe = pd.DataFrame(
        data
    )

    return dataframe.describe()


# ==========================================================
# STATSMODELS — OLS REGRESSION
# ==========================================================

def stats_ols(
    y,
    x,
    add_constant=True
):
    """
    Ordinary least-squares regression.

    y:
        dependent variable

    x:
        independent variable(s)
    """

    import statsmodels.api as sm

    if add_constant:

        x = sm.add_constant(
            x
        )

    model = sm.OLS(
        y,
        x
    )

    return model.fit()


# ==========================================================
# STATSMODELS — OLS SUMMARY
# ==========================================================

def stats_ols_summary(
    model
):
    """
    Return a compact OLS regression summary.
    """

    return {
        "parameters":
            model.params,

        "standard_errors":
            model.bse,

        "t_values":
            model.tvalues,

        "p_values":
            model.pvalues,

        "r_squared":
            float(model.rsquared),

        "adjusted_r_squared":
            float(model.rsquared_adj),

        "aic":
            float(model.aic),

        "bic":
            float(model.bic),

        "f_statistic":
            float(model.fvalue)
            if model.fvalue is not None
            else None,

        "observations":
            int(model.nobs),
    }


# ==========================================================
# STATSMODELS — LOGISTIC REGRESSION
# ==========================================================

def stats_logistic(
    y,
    x,
    add_constant=True
):
    """
    Logistic regression.
    """

    import statsmodels.api as sm

    if add_constant:

        x = sm.add_constant(
            x
        )

    model = sm.Logit(
        y,
        x
    )

    return model.fit(
        disp=False
    )


# ==========================================================
# STATSMODELS — POISSON REGRESSION
# ==========================================================

def stats_poisson(
    y,
    x,
    add_constant=True
):
    """
    Poisson generalized linear model.
    """

    import statsmodels.api as sm

    if add_constant:

        x = sm.add_constant(
            x
        )

    model = sm.GLM(
        y,
        x,
        family=sm.families.Poisson()
    )

    return model.fit()


# ==========================================================
# STATSMODELS — BINOMIAL GLM
# ==========================================================

def stats_binomial_glm(
    y,
    x,
    add_constant=True
):
    """
    Binomial generalized linear model.
    """

    import statsmodels.api as sm

    if add_constant:

        x = sm.add_constant(
            x
        )

    model = sm.GLM(
        y,
        x,
        family=sm.families.Binomial()
    )

    return model.fit()


# ==========================================================
# STATSMODELS — GAMMA GLM
# ==========================================================

def stats_gamma_glm(
    y,
    x,
    add_constant=True
):
    """
    Gamma generalized linear model.
    """

    import statsmodels.api as sm

    if add_constant:

        x = sm.add_constant(
            x
        )

    model = sm.GLM(
        y,
        x,
        family=sm.families.Gamma()
    )

    return model.fit()


# ==========================================================
# STATSMODELS — ANOVA
# ==========================================================

def stats_anova(
    formula,
    data
):
    """
    Perform an ANOVA analysis from a formula.
    """

    import statsmodels.api as sm
    import statsmodels.formula.api as smf

    model = smf.ols(
        str(formula),
        data=data
    ).fit()

    return sm.stats.anova_lm(
        model
    )


# ==========================================================
# STATSMODELS — CORRELATION
# ==========================================================

def stats_correlation(
    x,
    y
):
    """
    Calculate Pearson correlation using Statsmodels.
    """

    import numpy as np

    x = np.asarray(
        x,
        dtype=float
    )

    y = np.asarray(
        y,
        dtype=float
    )

    correlation = np.corrcoef(
        x,
        y
    )[0, 1]

    return float(
        correlation
    )


# ==========================================================
# STATSMODELS — ACF
# ==========================================================

def stats_acf(
    data,
    nlags=20
):
    """
    Calculate the autocorrelation function.
    """

    from statsmodels.tsa.stattools import acf

    return acf(
        data,
        nlags=int(nlags)
    )


# ==========================================================
# STATSMODELS — PACF
# ==========================================================

def stats_pacf(
    data,
    nlags=20
):
    """
    Calculate the partial autocorrelation function.
    """

    from statsmodels.tsa.stattools import pacf

    return pacf(
        data,
        nlags=int(nlags)
    )


# ==========================================================
# STATSMODELS — ARIMA
# ==========================================================

def stats_arima(
    data,
    order=(1, 0, 0)
):
    """
    Fit an ARIMA time-series model.

    order:
        (p, d, q)
    """

    from statsmodels.tsa.arima.model import ARIMA

    model = ARIMA(
        data,
        order=tuple(order)
    )

    return model.fit()


# ==========================================================
# STATSMODELS — ARIMA FORECAST
# ==========================================================

def stats_arima_forecast(
    model,
    steps=10
):
    """
    Forecast future values from an ARIMA model.
    """

    return model.forecast(
        steps=int(steps)
    )


# ==========================================================
# STATSMODELS — SARIMAX
# ==========================================================

def stats_sarimax(
    data,
    order=(1, 0, 0),
    seasonal_order=(0, 0, 0, 0),
    exog=None
):
    """
    Fit a SARIMAX model.
    """

    from statsmodels.tsa.statespace.sarimax import SARIMAX

    model = SARIMAX(
        data,
        order=tuple(order),
        seasonal_order=tuple(
            seasonal_order
        ),
        exog=exog
    )

    return model.fit(
        disp=False
    )


# ==========================================================
# STATSMODELS — SARIMAX FORECAST
# ==========================================================

def stats_sarimax_forecast(
    model,
    steps=10
):
    """
    Forecast from a SARIMAX model.
    """

    return model.forecast(
        steps=int(steps)
    )


# ==========================================================
# STATSMODELS — ADF STATIONARITY TEST
# ==========================================================

def stats_adf_test(
    data
):
    """
    Augmented Dickey-Fuller stationarity test.
    """

    from statsmodels.tsa.stattools import adfuller

    result = adfuller(
        data
    )

    return {
        "test_statistic":
            float(result[0]),

        "p_value":
            float(result[1]),

        "lags":
            int(result[2]),

        "observations":
            int(result[3]),

        "critical_values":
            result[4],
    }


# ==========================================================
# STATSMODELS — KPSS TEST
# ==========================================================

def stats_kpss_test(
    data,
    regression="c"
):
    """
    KPSS stationarity test.
    """

    from statsmodels.tsa.stattools import kpss

    result = kpss(
        data,
        regression=str(regression),
        nlags="auto"
    )

    return {
        "test_statistic":
            float(result[0]),

        "p_value":
            float(result[1]),

        "lags":
            int(result[2]),

        "critical_values":
            result[3],
    }


# ==========================================================
# STATSMODELS — DURBIN-WATSON
# ==========================================================

def stats_durbin_watson(
    residuals
):
    """
    Calculate the Durbin-Watson statistic.
    """

    from statsmodels.stats.stattools import durbin_watson

    return float(
        durbin_watson(
            residuals
        )
    )


# ==========================================================
# STATSMODELS — VIF
# ==========================================================

def stats_vif(
    x
):
    """
    Calculate variance inflation factors.
    """

    import pandas as pd
    from statsmodels.stats.outliers_influence import variance_inflation_factor

    dataframe = pd.DataFrame(
        x
    )

    results = []

    for i in range(
        dataframe.shape[1]
    ):

        results.append(
            variance_inflation_factor(
                dataframe.values,
                i
            )
        )

    return results


# ==========================================================
# STATSMODELS — DISTRIBUTION NORMALITY
# ==========================================================

def stats_normality_test(
    data
):
    """
    Perform a Jarque-Bera normality test.
    """

    from statsmodels.stats.stattools import jarque_bera

    result = jarque_bera(
        data
    )

    return {
        "statistic":
            float(result[0]),

        "p_value":
            float(result[1]),

        "skewness":
            float(result[2]),

        "kurtosis":
            float(result[3]),
    }


# ==========================================================
# PULP — CREATE LINEAR PROGRAM
# ==========================================================

def pulp_create_problem(
    name="DaveOptimization",
    sense="min"
):
    """
    Create a PuLP linear optimization problem.

    sense:
        "min" or "max"
    """

    import pulp

    if str(sense).lower() == "max":

        problem_sense = pulp.LpMaximize

    else:

        problem_sense = pulp.LpMinimize

    return pulp.LpProblem(
        str(name),
        problem_sense
    )


# ==========================================================
# PULP — VARIABLE
# ==========================================================

def pulp_variable(
    name,
    low_bound=None,
    up_bound=None,
    category="Continuous"
):
    """
    Create a PuLP optimization variable.
    """

    import pulp

    categories = {
        "continuous":
            pulp.LpContinuous,

        "integer":
            pulp.LpInteger,

        "binary":
            pulp.LpBinary,
    }

    selected_category = categories.get(
        str(category).lower(),
        pulp.LpContinuous
    )

    return pulp.LpVariable(
        str(name),
        lowBound=low_bound,
        upBound=up_bound,
        cat=selected_category
    )


# ==========================================================
# PULP — SOLVE
# ==========================================================

def pulp_solve(
    problem,
    solver=None
):
    """
    Solve a PuLP optimization problem.
    """

    if solver is None:

        result = problem.solve()

    else:

        result = problem.solve(
            solver
        )

    return {
        "status":
            problem.status,

        "status_name":
            str(
                problem.status
            ),

        "objective":
            problem.objective.value(),

        "result":
            result,
    }


# ==========================================================
# PULP — VARIABLES
# ==========================================================

def pulp_variable_values(
    problem
):
    """
    Return solved variable values.
    """

    return {
        variable.name:
            variable.value()

        for variable
        in problem.variables()
    }


# ==========================================================
# PULP — OBJECTIVE VALUE
# ==========================================================

def pulp_objective_value(
    problem
):
    """
    Return the objective value.
    """

    return problem.objective.value()


# ==========================================================
# PULP — CONSTRAINT COUNT
# ==========================================================

def pulp_constraint_summary(
    problem
):
    """
    Summarize optimization constraints.
    """

    return {
        "name":
            problem.name,

        "variables":
            len(problem.variables()),

        "constraints":
            len(problem.constraints),

        "objective":
            problem.objective.value()
            if problem.objective is not None
            else None,
    }


# ==========================================================
# PULP — KNAPSACK EXAMPLE
# ==========================================================

def pulp_knapsack(
    values,
    weights,
    capacity
):
    """
    Solve a binary knapsack optimization problem.
    """

    import pulp

    if len(values) != len(weights):

        raise ValueError(
            "values and weights must have the same length"
        )

    problem = pulp.LpProblem(
        "DaveKnapsack",
        pulp.LpMaximize
    )

    choices = [
        pulp.LpVariable(
            f"x{i}",
            cat=pulp.LpBinary
        )
        for i in range(
            len(values)
        )
    ]

    problem += pulp.lpSum(
        values[i] * choices[i]
        for i in range(
            len(values)
        )
    )

    problem += pulp.lpSum(
        weights[i] * choices[i]
        for i in range(
            len(weights)
        )
    ) <= float(capacity)

    problem.solve()

    selected = [
        i
        for i, variable
        in enumerate(choices)
        if variable.value() == 1
    ]

    return {
        "selected_items":
            selected,

        "objective":
            float(
                pulp.value(
                    problem.objective
                )
            ),

        "total_weight":
            sum(
                weights[i]
                for i in selected
            ),

        "status":
            pulp.LpStatus[
                problem.status
            ],
    }


# ==========================================================
# DEMES — LOAD DEMOGRAPHIC GRAPH
# ==========================================================

def demes_load(
    filename
):
    """
    Load a Demes demographic model from YAML.
    """

    import demes

    return demes.load(
        str(filename)
    )


# ==========================================================
# DEMES — LOAD FROM STRING
# ==========================================================

def demes_load_string(
    yaml_text
):
    """
    Load a Demes model from YAML text.
    """

    import demes

    return demes.loads(
        str(yaml_text)
    )


# ==========================================================
# DEMES — DUMP MODEL
# ==========================================================

def demes_dump(
    graph
):
    """
    Convert a Demes graph to YAML.
    """

    import demes

    return demes.dump(
        graph
    )


# ==========================================================
# DEMES — MODEL SUMMARY
# ==========================================================

def demes_summary(
    graph
):
    """
    Summarize a demographic model.
    """

    result = {
        "demes":
            [],
        "migrations":
            [],
        "pulses":
            [],
    }

    for deme in graph.demes:

        result["demes"].append(
            {
                "name":
                    deme.name,

                "description":
                    getattr(
                        deme,
                        "description",
                        None
                    ),

                "start_time":
                    deme.start_time,

                "end_time":
                    deme.end_time,

                "ancestors":
                    list(
                        deme.ancestors
                    ),

                "epochs":
                    len(
                        deme.epochs
                    ),
            }
        )

    for migration in graph.migrations:

        result["migrations"].append(
            {
                "source":
                    list(
                        migration.source
                    ),

                "dest":
                    list(
                        migration.dest
                    ),

                "rate":
                    migration.rate,

                "start_time":
                    migration.start_time,

                "end_time":
                    migration.end_time,
            }
        )

    for pulse in graph.pulses:

        result["pulses"].append(
            {
                "sources":
                    list(
                        pulse.sources
                    ),

                "dest":
                    pulse.dest,

                "proportion":
                    pulse.proportion,

                "time":
                    pulse.time,
            }
        )

    return result


# ==========================================================
# DEMES — VALIDATE MODEL
# ==========================================================

def demes_validate(
    graph
):
    """
    Validate a Demes graph.
    """

    import demes

    demes.Demes(
        graph
    )

    return True


# ==========================================================
# DEMES — GRAPH TO DICTIONARY
# ==========================================================

def demes_graph_info(
    graph
):
    """
    Return useful demographic graph information.
    """

    return {
        "name":
            getattr(
                graph,
                "description",
                None
            ),

        "num_demes":
            len(graph.demes),

        "num_migrations":
            len(graph.migrations),

        "num_pulses":
            len(graph.pulses),

        "generation_time":
            getattr(
                graph,
                "generation_time",
                None
            ),
    }


# ==========================================================
# CPSAT-LOGUTILS — STATUS
# ==========================================================

def cpsat_logutils_status():
    """
    Check availability of cpsat-logutils.

    This package is primarily a logging/helper package,
    rather than a general-purpose numerical solver.
    """

    module = _get_cpsat_logutils()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# GENERAL STATISTICS — MEAN / MEDIAN / STD
# ==========================================================

def statistical_summary(
    values
):
    """
    Calculate a compact statistical summary.
    """

    import numpy as np

    array = np.asarray(
        values,
        dtype=float
    )

    if array.size == 0:

        raise ValueError(
            "No data supplied."
        )

    return {
        "count":
            int(array.size),

        "mean":
            float(np.mean(array)),

        "median":
            float(np.median(array)),

        "standard_deviation":
            float(np.std(array)),

        "sample_standard_deviation":
            float(np.std(
                array,
                ddof=1
            ))
            if array.size > 1
            else None,

        "variance":
            float(np.var(array)),

        "minimum":
            float(np.min(array)),

        "maximum":
            float(np.max(array)),

        "range":
            float(
                np.max(array)
                -
                np.min(array)
            ),

        "q1":
            float(
                np.percentile(
                    array,
                    25
                )
            ),

        "q3":
            float(
                np.percentile(
                    array,
                    75
                )
            ),
    }


# ==========================================================
# GENERAL STATISTICS — Z-SCORES
# ==========================================================

def statistical_zscores(
    values
):
    """
    Calculate z-scores.
    """

    import numpy as np

    array = np.asarray(
        values,
        dtype=float
    )

    mean = np.mean(
        array
    )

    std = np.std(
        array
    )

    if std == 0:

        return np.zeros_like(
            array
        )

    return (
        array - mean
    ) / std


# ==========================================================
# GENERAL STATISTICS — COVARIANCE
# ==========================================================

def statistical_covariance(
    x,
    y
):
    """
    Calculate sample covariance.
    """

    import numpy as np

    return float(
        np.cov(
            x,
            y
        )[0, 1]
    )


# ==========================================================
# GENERAL STATISTICS — PEARSON
# ==========================================================

def statistical_pearson(
    x,
    y
):
    """
    Calculate Pearson correlation coefficient.
    """

    import scipy.stats as stats

    result = stats.pearsonr(
        x,
        y
    )

    return {
        "correlation":
            float(result.statistic),

        "p_value":
            float(result.pvalue),
    }


# ==========================================================
# GENERAL STATISTICS — SPEARMAN
# ==========================================================

def statistical_spearman(
    x,
    y
):
    """
    Calculate Spearman rank correlation.
    """

    import scipy.stats as stats

    result = stats.spearmanr(
        x,
        y
    )

    return {
        "correlation":
            float(result.statistic),

        "p_value":
            float(result.pvalue),
    }


# ==========================================================
# GENERAL STATISTICS — T TEST
# ==========================================================

def statistical_ttest(
    x,
    y=None
):
    """
    Perform a one-sample or two-sample t-test.

    If y is None:
        one-sample test against zero.
    """

    import scipy.stats as stats

    if y is None:

        result = stats.ttest_1samp(
            x,
            0
        )

    else:

        result = stats.ttest_ind(
            x,
            y
        )

    return {
        "t_statistic":
            float(result.statistic),

        "p_value":
            float(result.pvalue),
    }


# ==========================================================
# GENERAL STATISTICS — CHI-SQUARE
# ==========================================================

def statistical_chisquare(
    observed,
    expected=None
):
    """
    Perform a chi-square test.
    """

    import scipy.stats as stats

    result = stats.chisquare(
        observed,
        f_exp=expected
    )

    return {
        "statistic":
            float(result.statistic),

        "p_value":
            float(result.pvalue),
    }


# ==========================================================
# GENERAL STATISTICS — LINEAR REGRESSION
# ==========================================================

def statistical_linear_regression(
    x,
    y
):
    """
    Simple linear regression.
    """

    import scipy.stats as stats

    result = stats.linregress(
        x,
        y
    )

    return {
        "slope":
            float(result.slope),

        "intercept":
            float(result.intercept),

        "r_value":
            float(result.rvalue),

        "r_squared":
            float(result.rvalue ** 2),

        "p_value":
            float(result.pvalue),

        "standard_error":
            float(result.stderr),
    }


# ==========================================================
# GENERAL OPTIMIZATION — INTEGER SEARCH
# ==========================================================

def integer_grid_search(
    objective,
    bounds
):
    """
    Exhaustive integer search.

    bounds example:
        [(0, 10), (0, 20)]

    This is useful for small discrete optimization
    problems where a full MILP solver is unnecessary.
    """

    import itertools

    ranges = [
        range(
            int(low),
            int(high) + 1
        )
        for low, high
        in bounds
    ]

    best_point = None
    best_value = None

    for point in itertools.product(
        *ranges
    ):

        value = objective(
            *point
        )

        if (
            best_value is None
            or value < best_value
        ):

            best_value = value
            best_point = point

    return {
        "point":
            best_point,

        "value":
            best_value,
    }


# ==========================================================
# GENERAL OPTIMIZATION — MAXIMIZE INTEGER FUNCTION
# ==========================================================

def integer_grid_maximize(
    objective,
    bounds
):
    """
    Exhaustive integer maximization.
    """

    import itertools

    ranges = [
        range(
            int(low),
            int(high) + 1
        )
        for low, high
        in bounds
    ]

    best_point = None
    best_value = None

    for point in itertools.product(
        *ranges
    ):

        value = objective(
            *point
        )

        if (
            best_value is None
            or value > best_value
        ):

            best_value = value
            best_point = point

    return {
        "point":
            best_point,

        "value":
            best_value,
    }


# ==========================================================
# PART 9 STATUS
# ==========================================================

def statistics_part9_status():
    """
    Check statistics/optimization packages.
    """

    packages = [
        "statsmodels",
        "PuLP",
        "demes",
        "cpsat-logutils",
    ]

    results = {}

    print()
    print("=" * 78)
    print(
        "DAVE — STATISTICS / OPTIMIZATION PART 9 STATUS"
    )
    print("=" * 78)
    print()

    for package_name in packages:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<20} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<20} unavailable"
            )

    print()

    return results


# ==========================================================
# PART 9 SELF TEST
# ==========================================================

def statistics_part9_selftest(
    verbose=True
):
    """
    Test statistics, optimization,
    and demographic functionality.
    """

    tests = []


    # ------------------------------------------------------
    # STATISTICAL SUMMARY
    # ------------------------------------------------------

    try:

        result = statistical_summary(
            [1, 2, 3, 4, 5]
        )

        tests.append(
            (
                "statistical summary",
                result["mean"] == 3.0
            )
        )

    except Exception as exc:

        tests.append(
            (
                "statistical summary",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PEARSON
    # ------------------------------------------------------

    try:

        result = statistical_pearson(
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10]
        )

        tests.append(
            (
                "Pearson correlation",
                abs(
                    result["correlation"]
                    - 1.0
                ) < 1e-10
            )
        )

    except Exception as exc:

        tests.append(
            (
                "Pearson correlation",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # LINEAR REGRESSION
    # ------------------------------------------------------

    try:

        result = statistical_linear_regression(
            [1, 2, 3, 4],
            [2, 4, 6, 8]
        )

        tests.append(
            (
                "linear regression",
                abs(
                    result["slope"]
                    - 2.0
                ) < 1e-10
            )
        )

    except Exception as exc:

        tests.append(
            (
                "linear regression",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # STATSMODELS
    # ------------------------------------------------------

    try:

        import numpy as np

        x = np.arange(
            1,
            11
        )

        y = 2 * x + 1

        model = stats_ols(
            y,
            x
        )

        tests.append(
            (
                "statsmodels OLS",
                model.rsquared > 0.99
            )
        )

    except Exception as exc:

        tests.append(
            (
                "statsmodels OLS",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PULP
    # ------------------------------------------------------

    try:

        result = pulp_knapsack(
            values=[
                10,
                20,
                30
            ],
            weights=[
                1,
                2,
                3
            ],
            capacity=3
        )

        tests.append(
            (
                "PuLP",
                result["status"]
                == "Optimal"
            )
        )

    except Exception as exc:

        tests.append(
            (
                "PuLP",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # DEMES
    # ------------------------------------------------------

    try:

        yaml_text = """
description: Dave test model
time_units: generations

demes:

- name: A
  epochs:
  - start_size: 1000
    end_time: 0
"""

        graph = demes_load_string(
            yaml_text
        )

        tests.append(
            (
                "demes",
                len(graph.demes) == 1
            )
        )

    except Exception as exc:

        tests.append(
            (
                "demes",
                False,
                str(exc)
            )
        )


    # ======================================================
    # RESULTS
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 78)
        print(
            "DAVE — STATISTICS / OPTIMIZATION PART 9 SELF TEST"
        )
        print("=" * 78)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 78)

        print(
            f"Passed: {passed}"
        )

        print(
            f"Failed: {failed}"
        )

        print(
            f"Total:  {len(tests)}"
        )

        print("-" * 78)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# PART 9 HELP
# ==========================================================

def statistics_part9_help():

    print("""
==============================================================================
DAVE — STATISTICS / OPTIMIZATION / ECONOMETRICS
PART 9
==============================================================================

GENERAL STATISTICS
------------------

    statistical_summary(values)

    statistical_zscores(values)

    statistical_covariance(
        x,
        y
    )

    statistical_pearson(
        x,
        y
    )

    statistical_spearman(
        x,
        y
    )

    statistical_ttest(
        x,
        y
    )

    statistical_chisquare(
        observed,
        expected
    )

    statistical_linear_regression(
        x,
        y
    )


STATSMODELS — REGRESSION
------------------------

    stats_ols(
        y,
        x
    )

    stats_ols_summary(
        model
    )

    stats_logistic(
        y,
        x
    )

    stats_poisson(
        y,
        x
    )

    stats_binomial_glm(
        y,
        x
    )

    stats_gamma_glm(
        y,
        x
    )

    stats_anova(
        formula,
        data
    )


STATSMODELS — TIME SERIES
-------------------------

    stats_acf(
        data,
        nlags
    )

    stats_pacf(
        data,
        nlags
    )

    stats_arima(
        data,
        order
    )

    stats_arima_forecast(
        model,
        steps
    )

    stats_sarimax(
        data,
        order,
        seasonal_order
    )

    stats_sarimax_forecast(
        model,
        steps
    )

    stats_adf_test(data)

    stats_kpss_test(data)


STATSMODELS — DIAGNOSTICS
-------------------------

    stats_durbin_watson(
        residuals
    )

    stats_vif(x)

    stats_normality_test(data)


PULP — OPTIMIZATION
-------------------

    pulp_create_problem(
        name,
        sense
    )

    pulp_variable(
        name,
        low_bound,
        up_bound,
        category
    )

    pulp_solve(
        problem
    )

    pulp_variable_values(
        problem
    )

    pulp_objective_value(
        problem
    )

    pulp_constraint_summary(
        problem
    )

    pulp_knapsack(
        values,
        weights,
        capacity
    )


DEMES — POPULATION DEMOGRAPHY
----------------------------

    demes_load(filename)

    demes_load_string(yaml_text)

    demes_dump(graph)

    demes_summary(graph)

    demes_validate(graph)

    demes_graph_info(graph)


OPTIMIZATION UTILITIES
----------------------

    integer_grid_search(
        objective,
        bounds
    )

    integer_grid_maximize(
        objective,
        bounds
    )


PACKAGE STATUS
--------------

    statistics_part9_status()

    statistics_part9_selftest()

==============================================================================
""")

# ==========================================================
# DAVE
# VISUALIZATION / IMAGING / SCIENTIFIC DATA
# PART 10
# ==========================================================
#
# Packages covered:
#
#   altair
#   cmap
#   cmasher
#   cmyt
#   colorspacious
#   contourpy
#   dask-image
#   dipy
#   folium
#   GridDataFormats
#   h5py
#   hdmf
#   matplotlib
#   mpltern
#   mrcfile
#   nibabel
#   numcodecs
#   numpy
#   PIMS
#   Pint
#   plotly
#   pyarrow
#   PyAVM
#   PySmeQcd
#   PyWavelets
#   scikit-image
#   slicerator
#   tifffile
#   trx-python
#   xarray
#   yt
#   zarr
#
# NumPy / Matplotlib / Pint are extended here rather than
# reimplemented from scratch.
#
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_plotly():
    return load_scientific_package("plotly")


def _get_altair():
    return load_scientific_package("altair")


def _get_skimage():
    return load_scientific_package("scikit-image")


def _get_pywt():
    return load_scientific_package("PyWavelets")


def _get_xarray():
    return load_scientific_package("xarray")


def _get_h5py():
    return load_scientific_package("h5py")


def _get_zarr():
    return load_scientific_package("zarr")


def _get_pyarrow():
    return load_scientific_package("pyarrow")


def _get_nibabel():
    return load_scientific_package("nibabel")


def _get_dipy():
    return load_scientific_package("dipy")


def _get_mrcfile():
    return load_scientific_package("mrcfile")


def _get_tifffile():
    return load_scientific_package("tifffile")


def _get_folium():
    return load_scientific_package("folium")


def _get_contourpy():
    return load_scientific_package("contourpy")


def _get_mpltern():
    return load_scientific_package("mpltern")


def _get_yt():
    return load_scientific_package("yt")


def _get_colorspacious():
    return load_scientific_package("colorspacious")


def _get_cmasher():
    return load_scientific_package("cmasher")


def _get_cmyt():
    return load_scientific_package("cmyt")


def _get_cmap():
    return load_scientific_package("cmap")


def _get_dask_image():
    return load_scientific_package("dask-image")


def _get_numcodecs():
    return load_scientific_package("numcodecs")


def _get_hdmf():
    return load_scientific_package("hdmf")


def _get_griddataformats():
    return load_scientific_package("GridDataFormats")


def _get_pims():
    return load_scientific_package("PIMS")


def _get_slicerator():
    return load_scientific_package("slicerator")


def _get_pyavm():
    return load_scientific_package("PyAVM")


def _get_trx():
    return load_scientific_package("trx-python")


# ==========================================================
# PLOTLY — BASIC FIGURE
# ==========================================================

def plotly_line(
    x,
    y,
    title="Dave Plot"
):
    """
    Create an interactive Plotly line graph.
    """

    import plotly.graph_objects as go

    figure = go.Figure()

    figure.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            name="data"
        )
    )

    figure.update_layout(
        title=str(title)
    )

    return figure


# ==========================================================
# PLOTLY — SCATTER
# ==========================================================

def plotly_scatter(
    x,
    y,
    title="Dave Scatter Plot"
):
    """
    Create an interactive scatter plot.
    """

    import plotly.express as px

    return px.scatter(
        x=x,
        y=y,
        title=str(title)
    )


# ==========================================================
# PLOTLY — 3D SCATTER
# ==========================================================

def plotly_scatter3d(
    x,
    y,
    z,
    title="Dave 3D Scatter"
):
    """
    Create an interactive 3D scatter plot.
    """

    import plotly.express as px

    return px.scatter_3d(
        x=x,
        y=y,
        z=z,
        title=str(title)
    )


# ==========================================================
# PLOTLY — SURFACE
# ==========================================================

def plotly_surface(
    z,
    title="Dave Surface"
):
    """
    Create an interactive 3D surface plot.
    """

    import plotly.graph_objects as go

    figure = go.Figure(
        data=[
            go.Surface(
                z=z
            )
        ]
    )

    figure.update_layout(
        title=str(title)
    )

    return figure


# ==========================================================
# PLOTLY — HEATMAP
# ==========================================================

def plotly_heatmap(
    matrix,
    title="Dave Heatmap"
):
    """
    Create an interactive heatmap.
    """

    import plotly.express as px

    return px.imshow(
        matrix,
        title=str(title)
    )


# ==========================================================
# PLOTLY — HISTOGRAM
# ==========================================================

def plotly_histogram(
    values,
    title="Dave Histogram"
):
    """
    Create an interactive histogram.
    """

    import plotly.express as px

    return px.histogram(
        x=values,
        title=str(title)
    )


# ==========================================================
# ALTAIR — LINE CHART
# ==========================================================

def altair_line(
    data,
    x,
    y,
    title="Dave Altair Plot"
):
    """
    Create an Altair line chart from a DataFrame.
    """

    import altair as alt

    chart = alt.Chart(
        data
    ).mark_line().encode(
        x=x,
        y=y
    ).properties(
        title=str(title)
    )

    return chart


# ==========================================================
# ALTAIR — SCATTER
# ==========================================================

def altair_scatter(
    data,
    x,
    y,
    title="Dave Altair Scatter"
):
    """
    Create an Altair scatter plot.
    """

    import altair as alt

    return (
        alt.Chart(data)
        .mark_point()
        .encode(
            x=x,
            y=y
        )
        .properties(
            title=str(title)
        )
    )


# ==========================================================
# SCIKIT-IMAGE — IMAGE INFORMATION
# ==========================================================

def image_info(
    image
):
    """
    Return basic information about an image array.
    """

    import numpy as np

    array = np.asarray(
        image
    )

    return {
        "shape":
            tuple(array.shape),

        "dtype":
            str(array.dtype),

        "dimensions":
            int(array.ndim),

        "minimum":
            float(np.min(array)),

        "maximum":
            float(np.max(array)),

        "mean":
            float(np.mean(array)),

        "standard_deviation":
            float(np.std(array)),
    }


# ==========================================================
# SCIKIT-IMAGE — RESIZE
# ==========================================================

def image_resize(
    image,
    shape,
    preserve_range=True,
    anti_aliasing=True
):
    """
    Resize an image.
    """

    from skimage.transform import resize

    return resize(
        image,
        output_shape=tuple(shape),
        preserve_range=preserve_range,
        anti_aliasing=anti_aliasing
    )


# ==========================================================
# SCIKIT-IMAGE — ROTATE
# ==========================================================

def image_rotate(
    image,
    angle,
    resize=False
):
    """
    Rotate an image.
    """

    from skimage.transform import rotate

    return rotate(
        image,
        angle=float(angle),
        resize=bool(resize)
    )


# ==========================================================
# SCIKIT-IMAGE — GAUSSIAN BLUR
# ==========================================================

def image_gaussian(
    image,
    sigma=1
):
    """
    Apply Gaussian filtering.
    """

    from skimage.filters import gaussian

    return gaussian(
        image,
        sigma=float(sigma)
    )


# ==========================================================
# SCIKIT-IMAGE — SOBEL EDGE DETECTION
# ==========================================================

def image_sobel(
    image
):
    """
    Detect edges using the Sobel operator.
    """

    from skimage.filters import sobel

    return sobel(
        image
    )


# ==========================================================
# SCIKIT-IMAGE — CANNY EDGE DETECTION
# ==========================================================

def image_canny(
    image,
    sigma=1
):
    """
    Canny edge detection.
    """

    from skimage.feature import canny

    return canny(
        image,
        sigma=float(sigma)
    )


# ==========================================================
# SCIKIT-IMAGE — OTSU THRESHOLD
# ==========================================================

def image_otsu_threshold(
    image
):
    """
    Calculate an Otsu threshold.
    """

    from skimage.filters import threshold_otsu

    return threshold_otsu(
        image
    )


# ==========================================================
# SCIKIT-IMAGE — THRESHOLD IMAGE
# ==========================================================

def image_threshold(
    image,
    threshold=None
):
    """
    Convert an image into a binary mask.

    If threshold is None, Otsu's method is used.
    """

    import numpy as np

    if threshold is None:

        threshold = image_otsu_threshold(
            image
        )

    return np.asarray(
        image
    ) > threshold


# ==========================================================
# SCIKIT-IMAGE — LABEL COMPONENTS
# ==========================================================

def image_label(
    image
):
    """
    Label connected regions.
    """

    from skimage.measure import label

    return label(
        image
    )


# ==========================================================
# SCIKIT-IMAGE — REGION PROPERTIES
# ==========================================================

def image_regionprops(
    labeled_image
):
    """
    Calculate properties of labeled image regions.
    """

    from skimage.measure import regionprops

    regions = regionprops(
        labeled_image
    )

    result = []

    for region in regions:

        result.append(
            {
                "label":
                    int(region.label),

                "area":
                    int(region.area),

                "centroid":
                    tuple(
                        float(x)
                        for x in region.centroid
                    ),

                "bbox":
                    tuple(
                        int(x)
                        for x in region.bbox
                    ),
            }
        )

    return result


# ==========================================================
# SCIKIT-IMAGE — MORPHOLOGY
# ==========================================================

def image_binary_opening(
    image
):
    """
    Morphological binary opening.
    """

    from skimage.morphology import opening

    return opening(
        image
    )


# ==========================================================
# SCIKIT-IMAGE — MORPHOLOGY CLOSING
# ==========================================================

def image_binary_closing(
    image
):
    """
    Morphological binary closing.
    """

    from skimage.morphology import closing

    return closing(
        image
    )


# ==========================================================
# PYWAVELETS — DISCRETE WAVELET TRANSFORM
# ==========================================================

def wavelet_decompose(
    data,
    wavelet="db1",
    level=None
):
    """
    Perform a discrete wavelet decomposition.
    """

    import pywt

    return pywt.wavedec(
        data,
        wavelet=str(wavelet),
        level=level
    )


# ==========================================================
# PYWAVELETS — WAVELET RECONSTRUCTION
# ==========================================================

def wavelet_reconstruct(
    coefficients,
    wavelet="db1"
):
    """
    Reconstruct a signal from wavelet coefficients.
    """

    import pywt

    return pywt.waverec(
        coefficients,
        wavelet=str(wavelet)
    )


# ==========================================================
# PYWAVELETS — WAVELET INFORMATION
# ==========================================================

def wavelet_info(
    wavelet="db1"
):
    """
    Return information about a wavelet.
    """

    import pywt

    wavelet_object = pywt.Wavelet(
        str(wavelet)
    )

    return {
        "name":
            wavelet_object.name,

        "family":
            wavelet_object.family_name,

        "short_family":
            wavelet_object.short_family_name,

        "orthogonal":
            wavelet_object.orthogonal,

        "biorthogonal":
            wavelet_object.biorthogonal,

        "symmetry":
            wavelet_object.symmetry,

        "number_of_coefficients":
            wavelet_object.dec_len,
    }


# ==========================================================
# XARRAY — DATA ARRAY
# ==========================================================

def xarray_dataarray(
    data,
    dims=None,
    coords=None,
    name=None
):
    """
    Create an xarray DataArray.
    """

    import xarray as xr

    return xr.DataArray(
        data=data,
        dims=dims,
        coords=coords,
        name=name
    )


# ==========================================================
# XARRAY — DATASET
# ==========================================================

def xarray_dataset(
    data_vars=None,
    coords=None
):
    """
    Create an xarray Dataset.
    """

    import xarray as xr

    return xr.Dataset(
        data_vars=data_vars,
        coords=coords
    )


# ==========================================================
# XARRAY — SUMMARY
# ==========================================================

def xarray_summary(
    data
):
    """
    Return useful information about an xarray object.
    """

    return {
        "type":
            type(data).__name__,

        "dimensions":
            dict(data.sizes),

        "coordinates":
            list(data.coords),

        "variables":
            list(
                data.data_vars
            )
            if hasattr(
                data,
                "data_vars"
            )
            else None,

        "name":
            getattr(
                data,
                "name",
                None
            ),
    }


# ==========================================================
# XARRAY — INTERPOLATE
# ==========================================================

def xarray_interpolate(
    data,
    coordinates
):
    """
    Interpolate an xarray DataArray.
    """

    return data.interp(
        coordinates
    )


# ==========================================================
# XARRAY — SAVE NETCDF
# ==========================================================

def xarray_save_netcdf(
    data,
    filename
):
    """
    Save an xarray object to NetCDF.
    """

    data.to_netcdf(
        str(filename)
    )

    return str(
        filename
    )


# ==========================================================
# XARRAY — OPEN NETCDF
# ==========================================================

def xarray_open_netcdf(
    filename
):
    """
    Open a NetCDF dataset.
    """

    import xarray as xr

    return xr.open_dataset(
        str(filename)
    )


# ==========================================================
# H5PY — CREATE HDF5 FILE
# ==========================================================

def hdf5_create(
    filename
):
    """
    Create an HDF5 file.
    """

    import h5py

    file = h5py.File(
        str(filename),
        "w"
    )

    return file


# ==========================================================
# H5PY — WRITE DATASET
# ==========================================================

def hdf5_write(
    filename,
    dataset_name,
    data
):
    """
    Write a dataset into an HDF5 file.
    """

    import h5py

    with h5py.File(
        str(filename),
        "a"
    ) as file:

        if str(dataset_name) in file:

            del file[
                str(dataset_name)
            ]

        file.create_dataset(
            str(dataset_name),
            data=data
        )

    return str(
        filename
    )


# ==========================================================
# H5PY — READ DATASET
# ==========================================================

def hdf5_read(
    filename,
    dataset_name
):
    """
    Read a dataset from an HDF5 file.
    """

    import h5py

    with h5py.File(
        str(filename),
        "r"
    ) as file:

        return file[
            str(dataset_name)
        ][()]


# ==========================================================
# H5PY — LIST CONTENTS
# ==========================================================

def hdf5_contents(
    filename
):
    """
    List the top-level contents of an HDF5 file.
    """

    import h5py

    with h5py.File(
        str(filename),
        "r"
    ) as file:

        return list(
            file.keys()
        )


# ==========================================================
# ZARR — CREATE ARRAY
# ==========================================================

def zarr_create_array(
    store,
    data=None,
    shape=None,
    dtype=None
):
    """
    Create a Zarr array.

    store can be a path or supported Zarr store.
    """

    import zarr

    if data is not None:

        return zarr.open(
            store=str(store),
            mode="w",
            data=data
        )

    return zarr.open(
        store=str(store),
        mode="w",
        shape=tuple(shape),
        dtype=dtype
    )


# ==========================================================
# ZARR — OPEN
# ==========================================================

def zarr_open(
    store,
    mode="r"
):
    """
    Open a Zarr store.
    """

    import zarr

    return zarr.open(
        store=str(store),
        mode=str(mode)
    )


# ==========================================================
# ZARR — INFORMATION
# ==========================================================

def zarr_info(
    array
):
    """
    Return information about a Zarr array.
    """

    return {
        "shape":
            tuple(array.shape),

        "dtype":
            str(array.dtype),

        "chunks":
            getattr(
                array,
                "chunks",
                None
            ),

        "size":
            int(array.size),
    }


# ==========================================================
# PYARROW — ARRAY
# ==========================================================

def pyarrow_array(
    data
):
    """
    Create a PyArrow array.
    """

    import pyarrow as pa

    return pa.array(
        data
    )


# ==========================================================
# PYARROW — TABLE
# ==========================================================

def pyarrow_table(
    data
):
    """
    Create a PyArrow table.
    """

    import pyarrow as pa

    return pa.table(
        data
    )


# ==========================================================
# PYARROW — PARQUET WRITE
# ==========================================================

def pyarrow_write_parquet(
    table,
    filename
):
    """
    Write a PyArrow table to Parquet.
    """

    import pyarrow.parquet as pq

    pq.write_table(
        table,
        str(filename)
    )

    return str(
        filename
    )


# ==========================================================
# PYARROW — PARQUET READ
# ==========================================================

def pyarrow_read_parquet(
    filename
):
    """
    Read a Parquet file.
    """

    import pyarrow.parquet as pq

    return pq.read_table(
        str(filename)
    )


# ==========================================================
# NIBABEL — LOAD MEDICAL/NEUROIMAGING FILE
# ==========================================================

def nibabel_load(
    filename
):
    """
    Load a NIfTI or another supported neuroimaging file.
    """

    import nibabel as nib

    return nib.load(
        str(filename)
    )


# ==========================================================
# NIBABEL — IMAGE INFORMATION
# ==========================================================

def nibabel_info(
    image
):
    """
    Return information about a nibabel image.
    """

    return {
        "shape":
            tuple(
                image.shape
            ),

        "dtype":
            str(
                image.get_data_dtype()
            ),

        "affine":
            image.affine.tolist(),

        "header":
            str(
                image.header
            ),
    }


# ==========================================================
# NIBABEL — GET DATA
# ==========================================================

def nibabel_get_data(
    image
):
    """
    Obtain image data as an array.
    """

    return image.get_fdata()


# ==========================================================
# NIBABEL — SAVE
# ==========================================================

def nibabel_save(
    image,
    filename
):
    """
    Save a nibabel image.
    """

    import nibabel as nib

    nib.save(
        image,
        str(filename)
    )

    return str(
        filename
    )


# ==========================================================
# MRCFILE — OPEN
# ==========================================================

def mrc_open(
    filename,
    mode="r"
):
    """
    Open an MRC electron-microscopy/cryo-EM file.
    """

    import mrcfile

    return mrcfile.open(
        str(filename),
        mode=str(mode)
    )


# ==========================================================
# MRCFILE — READ DATA
# ==========================================================

def mrc_read(
    filename
):
    """
    Read MRC data into memory.
    """

    import mrcfile

    with mrcfile.open(
        str(filename),
        permissive=True
    ) as file:

        return file.data.copy()


# ==========================================================
# TIFF — READ
# ==========================================================

def tiff_read(
    filename
):
    """
    Read TIFF image data.
    """

    import tifffile

    return tifffile.imread(
        str(filename)
    )


# ==========================================================
# TIFF — WRITE
# ==========================================================

def tiff_write(
    filename,
    data
):
    """
    Write TIFF image data.
    """

    import tifffile

    tifffile.imwrite(
        str(filename),
        data
    )

    return str(
        filename
    )


# ==========================================================
# TIFF — INFORMATION
# ==========================================================

def tiff_info(
    filename
):
    """
    Inspect TIFF metadata.
    """

    import tifffile

    with tifffile.TiffFile(
        str(filename)
    ) as file:

        return {
            "pages":
                len(file.pages),

            "shape":
                file.series[0].shape
                if file.series
                else None,

            "dtype":
                str(
                    file.series[0].dtype
                )
                if file.series
                else None,
        }


# ==========================================================
# FOLIUM — MAP
# ==========================================================

def folium_map(
    latitude=0,
    longitude=0,
    zoom_start=2
):
    """
    Create an interactive web map.
    """

    import folium

    return folium.Map(
        location=[
            float(latitude),
            float(longitude)
        ],
        zoom_start=int(
            zoom_start
        )
    )


# ==========================================================
# FOLIUM — MARKER
# ==========================================================

def folium_marker(
    map_object,
    latitude,
    longitude,
    popup=None
):
    """
    Add a marker to a Folium map.
    """

    import folium

    marker = folium.Marker(
        location=[
            float(latitude),
            float(longitude)
        ],
        popup=popup
    )

    marker.add_to(
        map_object
    )

    return map_object


# ==========================================================
# CONTOURPY — CONTOUR LINES
# ==========================================================

def contour_lines(
    x,
    y,
    z,
    levels=10
):
    """
    Generate contour lines using contourpy.
    """

    import contourpy

    contour_generator = (
        contourpy.contour_generator(
            x=x,
            y=y,
            z=z
        )
    )

    return {
        "generator":
            contour_generator,

        "levels":
            contour_generator.lines(
                levels
            )
    }


# ==========================================================
# COLORSPACIOUS — COLOR CONVERSION
# ==========================================================

def color_convert(
    color,
    from_space,
    to_space
):
    """
    Convert between color spaces using colorspacious.
    """

    from colorspacious import cspace_convert

    return cspace_convert(
        color,
        str(from_space),
        str(to_space)
    )


# ==========================================================
# CMASHER — COLORMAP
# ==========================================================

def cmasher_colormap(
    name="viridis"
):
    """
    Obtain a CMasher colormap.
    """

    import cmasher as cmr

    if hasattr(
        cmr,
        str(name)
    ):

        return getattr(
            cmr,
            str(name)
        )

    return cmr.get_sub_cmap(
        "viridis",
        0,
        1
    )


# ==========================================================
# MPLTERN — TERNARY AXES
# ==========================================================

def ternary_figure():
    """
    Create a Matplotlib ternary-composition figure.

    Useful for:
        alloys
        chemistry
        phase diagrams
        mixtures
    """

    import matplotlib.pyplot as plt
    import mpltern

    figure = plt.figure()

    axes = figure.add_subplot(
        111,
        projection="ternary"
    )

    return figure, axes


# ==========================================================
# YT — DATASET LOAD
# ==========================================================

def yt_load(
    filename
):
    """
    Load a simulation dataset using yt.
    """

    import yt

    return yt.load(
        str(filename)
    )


# ==========================================================
# YT — DATASET SUMMARY
# ==========================================================

def yt_summary(
    dataset
):
    """
    Return basic information about a yt dataset.
    """

    return {
        "dataset_type":
            type(dataset).__name__,

        "domain_dimensions":
            getattr(
                dataset,
                "domain_dimensions",
                None
            ),

        "domain_left_edge":
            getattr(
                dataset,
                "domain_left_edge",
                None
            ),

        "domain_right_edge":
            getattr(
                dataset,
                "domain_right_edge",
                None
            ),

        "current_time":
            getattr(
                dataset,
                "current_time",
                None
            ),

        "geometry":
            getattr(
                dataset,
                "geometry",
                None
            ),
    }


# ==========================================================
# DASK-IMAGE — GAUSSIAN FILTER
# ==========================================================

def dask_image_gaussian(
    image,
    sigma=1
):
    """
    Apply a Gaussian filter to a Dask image.
    """

    from dask_image.ndfilters import gaussian_filter

    return gaussian_filter(
        image,
        sigma=float(sigma)
    )


# ==========================================================
# DASK-IMAGE — SOBEL
# ==========================================================

def dask_image_sobel(
    image
):
    """
    Apply a Sobel filter using Dask-image.
    """

    from dask_image.ndfilters import sobel

    return sobel(
        image
    )


# ==========================================================
# NUMCODECS — COMPRESS DATA
# ==========================================================

def numcodecs_compress(
    data,
    codec="zlib"
):
    """
    Compress bytes using Numcodecs.
    """

    import numcodecs

    codec_name = str(
        codec
    ).lower()

    if codec_name == "zlib":

        compressor = numcodecs.Zlib(
            level=6
        )

    elif codec_name == "lz4":

        compressor = numcodecs.LZ4()

    elif codec_name == "zstd":

        compressor = numcodecs.Zstd()

    else:

        raise ValueError(
            "Supported codecs: zlib, lz4, zstd"
        )

    return compressor.encode(
        data
    )


# ==========================================================
# NUMCODECS — DECOMPRESS DATA
# ==========================================================

def numcodecs_decompress(
    data,
    codec="zlib"
):
    """
    Decompress Numcodecs data.
    """

    import numcodecs

    codec_name = str(
        codec
    ).lower()

    if codec_name == "zlib":

        compressor = numcodecs.Zlib(
            level=6
        )

    elif codec_name == "lz4":

        compressor = numcodecs.LZ4()

    elif codec_name == "zstd":

        compressor = numcodecs.Zstd()

    else:

        raise ValueError(
            "Supported codecs: zlib, lz4, zstd"
        )

    return compressor.decode(
        data
    )


# ==========================================================
# PIMS — IMAGE SEQUENCE
# ==========================================================

def pims_open(
    filename
):
    """
    Open an image sequence using PIMS.
    """

    import pims

    return pims.open(
        str(filename)
    )


# ==========================================================
# PIMS — LENGTH
# ==========================================================

def pims_length(
    sequence
):
    """
    Return the number of frames in a PIMS sequence.
    """

    return len(
        sequence
    )


# ==========================================================
# SLICERATOR — SEQUENCE INDEXING
# ==========================================================

def slicerator_slice(
    sequence,
    start=None,
    stop=None,
    step=None
):
    """
    Create a sliced sequence.
    """

    from slicerator import Slicerator

    if isinstance(
        sequence,
        Slicerator
    ):

        return sequence[
            slice(
                start,
                stop,
                step
            )
        ]

    return sequence[
        slice(
            start,
            stop,
            step
        )
    ]


# ==========================================================
# GRIDDATAFORMATS — AVAILABLE
# ==========================================================

def griddataformats_status():
    """
    Check GridDataFormats availability.
    """

    module = _get_griddataformats()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# HDMF — AVAILABLE
# ==========================================================

def hdmf_status():
    """
    Check HDMF availability.
    """

    module = _get_hdmf()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# PYAVM — AVAILABLE
# ==========================================================

def pyavm_status():
    """
    Check PyAVM availability.

    PyAVM is primarily concerned with astronomical
    visualization metadata rather than general plotting.
    """

    module = _get_pyavm()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# PYSMEQCD — AVAILABLE
# ==========================================================

def pysmeqcd_status():
    """
    Check PySmeQcd availability.

    This is intentionally a status wrapper because its
    public API is specialized and should not be guessed.
    """

    module = load_scientific_package(
        "PySmeQcd"
    )

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# TRX-PYTHON — AVAILABLE
# ==========================================================

def trx_python_status():
    """
    Check trx-python availability.
    """

    module = _get_trx()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# PART 10 STATUS
# ==========================================================

def visualization_part10_status():
    """
    Check visualization/data packages.
    """

    packages = [
        "plotly",
        "altair",
        "scikit-image",
        "PyWavelets",
        "xarray",
        "h5py",
        "zarr",
        "pyarrow",
        "nibabel",
        "dipy",
        "mrcfile",
        "tifffile",
        "folium",
        "contourpy",
        "mpltern",
        "yt",
        "colorspacious",
        "cmasher",
        "cmyt",
        "cmap",
        "dask-image",
        "numcodecs",
        "hdmf",
        "GridDataFormats",
        "PIMS",
        "slicerator",
        "PyAVM",
        "trx-python",
        "PySmeQcd",
    ]

    results = {}

    print()
    print("=" * 78)
    print(
        "DAVE — VISUALIZATION / DATA PART 10 STATUS"
    )
    print("=" * 78)
    print()

    for package_name in packages:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<22} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<22} unavailable"
            )

    print()

    return results


# ==========================================================
# PART 10 SELF TEST
# ==========================================================

def visualization_part10_selftest(
    verbose=True
):
    """
    Test the major Part 10 functionality.
    """

    tests = []


    # ------------------------------------------------------
    # IMAGE INFORMATION
    # ------------------------------------------------------

    try:

        import numpy as np

        image = np.arange(
            100,
            dtype=float
        ).reshape(
            10,
            10
        )

        result = image_info(
            image
        )

        tests.append(
            (
                "image information",
                result["shape"]
                == (10, 10)
            )
        )

    except Exception as exc:

        tests.append(
            (
                "image information",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # WAVELET
    # ------------------------------------------------------

    try:

        signal = np.arange(
            16,
            dtype=float
        )

        coefficients = wavelet_decompose(
            signal,
            "db1"
        )

        reconstructed = wavelet_reconstruct(
            coefficients,
            "db1"
        )

        tests.append(
            (
                "PyWavelets",
                np.allclose(
                    signal,
                    reconstructed
                )
            )
        )

    except Exception as exc:

        tests.append(
            (
                "PyWavelets",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # XARRAY
    # ------------------------------------------------------

    try:

        array = xarray_dataarray(
            [[1, 2], [3, 4]],
            dims=["x", "y"]
        )

        tests.append(
            (
                "xarray",
                array.shape
                == (2, 2)
            )
        )

    except Exception as exc:

        tests.append(
            (
                "xarray",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # HDF5
    # ------------------------------------------------------

    try:

        import tempfile
        import os

        with tempfile.NamedTemporaryFile(
            suffix=".h5",
            delete=False
        ) as temp:

            filename = temp.name

        try:

            hdf5_write(
                filename,
                "test",
                [1, 2, 3]
            )

            data = hdf5_read(
                filename,
                "test"
            )

            tests.append(
                (
                    "h5py",
                    len(data) == 3
                )
            )

        finally:

            if os.path.exists(
                filename
            ):

                os.remove(
                    filename
                )

    except Exception as exc:

        tests.append(
            (
                "h5py",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # TIFF
    # ------------------------------------------------------

    try:

        import tempfile
        import os

        with tempfile.NamedTemporaryFile(
            suffix=".tif",
            delete=False
        ) as temp:

            filename = temp.name

        try:

            tiff_write(
                filename,
                image.astype(
                    np.uint8
                )
            )

            loaded = tiff_read(
                filename
            )

            tests.append(
                (
                    "tifffile",
                    loaded.shape
                    == image.shape
                )
            )

        finally:

            if os.path.exists(
                filename
            ):

                os.remove(
                    filename
                )

    except Exception as exc:

        tests.append(
            (
                "tifffile",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PYARROW
    # ------------------------------------------------------

    try:

        table = pyarrow_table(
            {
                "x": [1, 2, 3],
                "y": [4, 5, 6]
            }
        )

        tests.append(
            (
                "PyArrow",
                table.num_rows == 3
            )
        )

    except Exception as exc:

        tests.append(
            (
                "PyArrow",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # COLORSPACIOUS
    # ------------------------------------------------------

    try:

        converted = color_convert(
            [1, 0, 0],
            "sRGB1",
            "CIELab"
        )

        tests.append(
            (
                "colorspacious",
                len(converted) == 3
            )
        )

    except Exception as exc:

        tests.append(
            (
                "colorspacious",
                False,
                str(exc)
            )
        )


    # ======================================================
    # RESULTS
    # ======================================================

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 78)
        print(
            "DAVE — VISUALIZATION / DATA PART 10 SELF TEST"
        )
        print("=" * 78)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 78)
        print(
            f"Passed: {passed}"
        )
        print(
            f"Failed: {failed}"
        )
        print(
            f"Total:  {len(tests)}"
        )
        print("-" * 78)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# PART 10 HELP
# ==========================================================

def visualization_part10_help():

    print("""
==============================================================================
DAVE — VISUALIZATION / IMAGING / SCIENTIFIC DATA
PART 10
==============================================================================


PLOTLY
------

    plotly_line(x, y)

    plotly_scatter(x, y)

    plotly_scatter3d(x, y, z)

    plotly_surface(z)

    plotly_heatmap(matrix)

    plotly_histogram(values)


ALTAIR
------

    altair_line(
        data,
        x,
        y
    )

    altair_scatter(
        data,
        x,
        y
    )


SCIKIT-IMAGE
------------

    image_info(image)

    image_resize(
        image,
        shape
    )

    image_rotate(
        image,
        angle
    )

    image_gaussian(
        image,
        sigma
    )

    image_sobel(image)

    image_canny(
        image,
        sigma
    )

    image_otsu_threshold(image)

    image_threshold(
        image,
        threshold
    )

    image_label(image)

    image_regionprops(
        labeled_image
    )

    image_binary_opening(image)

    image_binary_closing(image)


PYWAVELETS
----------

    wavelet_decompose(
        data,
        wavelet
    )

    wavelet_reconstruct(
        coefficients,
        wavelet
    )

    wavelet_info(wavelet)


XARRAY
------

    xarray_dataarray(
        data,
        dims,
        coords,
        name
    )

    xarray_dataset(
        data_vars,
        coords
    )

    xarray_summary(data)

    xarray_interpolate(
        data,
        coordinates
    )

    xarray_save_netcdf(
        data,
        filename
    )

    xarray_open_netcdf(
        filename
    )


HDF5
----

    hdf5_create(filename)

    hdf5_write(
        filename,
        dataset_name,
        data
    )

    hdf5_read(
        filename,
        dataset_name
    )

    hdf5_contents(filename)


ZARR
----

    zarr_create_array(
        store,
        data
    )

    zarr_open(
        store,
        mode
    )

    zarr_info(array)


PYARROW
--------

    pyarrow_array(data)

    pyarrow_table(data)

    pyarrow_write_parquet(
        table,
        filename
    )

    pyarrow_read_parquet(
        filename
    )


NIBABEL
--------

    nibabel_load(filename)

    nibabel_info(image)

    nibabel_get_data(image)

    nibabel_save(
        image,
        filename
    )


MRC / CRYO-EM
-------------

    mrc_open(
        filename,
        mode
    )

    mrc_read(filename)


TIFF
----

    tiff_read(filename)

    tiff_write(
        filename,
        data
    )

    tiff_info(filename)


FOLIUM
------

    folium_map(
        latitude,
        longitude,
        zoom_start
    )

    folium_marker(
        map_object,
        latitude,
        longitude,
        popup
    )


CONTOURPY
---------

    contour_lines(
        x,
        y,
        z,
        levels
    )


COLOR SCIENCE
-------------

    color_convert(
        color,
        from_space,
        to_space
    )

    cmasher_colormap(name)


TERNARY PLOTS
-------------

    ternary_figure()

Useful for:

    alloys
    metallurgy
    chemistry
    phase diagrams
    mixture composition


YT
--

    yt_load(filename)

    yt_summary(dataset)


DASK-IMAGE
----------

    dask_image_gaussian(
        image,
        sigma
    )

    dask_image_sobel(image)


NUMCODECS
---------

    numcodecs_compress(
        data,
        codec
    )

    numcodecs_decompress(
        data,
        codec
    )


PIMS
----

    pims_open(filename)

    pims_length(sequence)


SLICERATOR
----------

    slicerator_slice(
        sequence,
        start,
        stop,
        step
    )


PACKAGE STATUS
--------------

    visualization_part10_status()

    visualization_part10_selftest()

==============================================================================
""")

# ==========================================================
# DAVE
# GIS / GEOSPATIAL / GEOSCIENCE / EARTH SCIENCE
# PART 11
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_geopandas():
    return load_scientific_package("geopandas")


def _get_shapely():
    return load_scientific_package("shapely")


def _get_pyproj():
    return load_scientific_package("pyproj")


def _get_geopy():
    return load_scientific_package("geopy")


def _get_rasterio():
    return load_scientific_package("rasterio")


def _get_rasterstats():
    return load_scientific_package("rasterstats")


def _get_fiona():
    return load_scientific_package("fiona")


def _get_pyogrio():
    return load_scientific_package("pyogrio")


def _get_rtree():
    return load_scientific_package("rtree")


def _get_osmnx():
    return load_scientific_package("osmnx")


def _get_networkx():
    return load_scientific_package("networkx")


def _get_folium():
    return load_scientific_package("folium")


def _get_affine():
    return load_scientific_package("affine")


def _get_geographiclib():
    return load_scientific_package("geographiclib")


def _get_libpysal():
    return load_scientific_package("libpysal")


def _get_esda():
    return load_scientific_package("esda")


def _get_giddy():
    return load_scientific_package("giddy")


def _get_mapclassify():
    return load_scientific_package("mapclassify")


def _get_momepy():
    return load_scientific_package("momepy")


def _get_movingpandas():
    return load_scientific_package("movingpandas")


def _get_spaghetti():
    return load_scientific_package("spaghetti")


def _get_spglm():
    return load_scientific_package("spglm")


def _get_spint():
    return load_scientific_package("spint")


def _get_splot():
    return load_scientific_package("splot")


def _get_spml():
    return load_scientific_package("spml")


def _get_spopt():
    return load_scientific_package("spopt")


def _get_tobler():
    return load_scientific_package("tobler")


def _get_xyzservices():
    return load_scientific_package("xyzservices")


def _get_striplog():
    return load_scientific_package("striplog")


def _get_welly():
    return load_scientific_package("welly")


def _get_wellpathpy():
    return load_scientific_package("wellpathpy")


def _get_pyregion():
    return load_scientific_package("pyregion")


def _get_earthpy():
    return load_scientific_package("earthpy")


def _get_flopy():
    return load_scientific_package("flopy")


def _get_gempy():
    return load_scientific_package("gempy")


def _get_gempy_engine():
    return load_scientific_package("gempy_engine")


def _get_pydeck():
    return load_scientific_package("pydeck")


def _get_topologicpy():
    return load_scientific_package("topologicpy")


# ==========================================================
# GEOPY — DISTANCE
# ==========================================================

def geo_distance(
    latitude1,
    longitude1,
    latitude2,
    longitude2
):
    """
    Calculate geodesic distance between two coordinates.

    Returns distance in meters.
    """

    from geopy.distance import geodesic

    distance = geodesic(
        (
            float(latitude1),
            float(longitude1)
        ),
        (
            float(latitude2),
            float(longitude2)
        )
    )

    return distance.meters


# ==========================================================
# GEOPY — KILOMETERS
# ==========================================================

def geo_distance_km(
    latitude1,
    longitude1,
    latitude2,
    longitude2
):
    """
    Calculate geodesic distance in kilometers.
    """

    return geo_distance(
        latitude1,
        longitude1,
        latitude2,
        longitude2
    ) / 1000.0


# ==========================================================
# GEOPY — MILES
# ==========================================================

def geo_distance_miles(
    latitude1,
    longitude1,
    latitude2,
    longitude2
):
    """
    Calculate geodesic distance in miles.
    """

    meters = geo_distance(
        latitude1,
        longitude1,
        latitude2,
        longitude2
    )

    return meters / 1609.344


# ==========================================================
# GEOGRAPHICLIB — PRECISE GEODESIC
# ==========================================================

def geographiclib_inverse(
    latitude1,
    longitude1,
    latitude2,
    longitude2
):
    """
    High-precision geodesic inverse calculation.

    Returns distance and azimuth information.
    """

    from geographiclib.geodesic import Geodesic

    result = Geodesic.WGS84.Inverse(
        float(latitude1),
        float(longitude1),
        float(latitude2),
        float(longitude2)
    )

    return result


# ==========================================================
# GEOGRAPHICLIB — DIRECT
# ==========================================================

def geographiclib_direct(
    latitude,
    longitude,
    azimuth,
    distance
):
    """
    Calculate a destination coordinate from:

        starting coordinate
        azimuth
        distance in meters
    """

    from geographiclib.geodesic import Geodesic

    return Geodesic.WGS84.Direct(
        float(latitude),
        float(longitude),
        float(azimuth),
        float(distance)
    )


# ==========================================================
# PYPROJ — COORDINATE TRANSFORMATION
# ==========================================================

def coordinate_transform(
    x,
    y,
    source_crs,
    target_crs
):
    """
    Transform coordinates between coordinate reference systems.

    Examples:

        EPSG:4326
        EPSG:3857
    """

    from pyproj import Transformer

    transformer = Transformer.from_crs(
        source_crs,
        target_crs,
        always_xy=True
    )

    return transformer.transform(
        float(x),
        float(y)
    )


# ==========================================================
# PYPROJ — TRANSFORM MANY COORDINATES
# ==========================================================

def coordinate_transform_many(
    x,
    y,
    source_crs,
    target_crs
):
    """
    Transform arrays/lists of coordinates.
    """

    from pyproj import Transformer

    transformer = Transformer.from_crs(
        source_crs,
        target_crs,
        always_xy=True
    )

    return transformer.transform(
        x,
        y
    )


# ==========================================================
# PYPROJ — CRS INFORMATION
# ==========================================================

def crs_information(
    crs
):
    """
    Return information about a coordinate reference system.
    """

    from pyproj import CRS

    coordinate_reference_system = CRS.from_user_input(
        crs
    )

    return {
        "name":
            coordinate_reference_system.name,

        "authority":
            coordinate_reference_system.to_authority(),

        "is_geographic":
            coordinate_reference_system.is_geographic,

        "is_projected":
            coordinate_reference_system.is_projected,

        "axis_info":
            [
                str(axis)
                for axis
                in coordinate_reference_system.axis_info
            ],

        "datum":
            str(
                coordinate_reference_system.datum
            ),
    }


# ==========================================================
# SHAPELY — POINT
# ==========================================================

def geometry_point(
    x,
    y
):
    """
    Create a Shapely point.
    """

    from shapely.geometry import Point

    return Point(
        float(x),
        float(y)
    )


# ==========================================================
# SHAPELY — LINE
# ==========================================================

def geometry_line(
    coordinates
):
    """
    Create a Shapely LineString.
    """

    from shapely.geometry import LineString

    return LineString(
        coordinates
    )


# ==========================================================
# SHAPELY — POLYGON
# ==========================================================

def geometry_polygon(
    coordinates
):
    """
    Create a Shapely polygon.
    """

    from shapely.geometry import Polygon

    return Polygon(
        coordinates
    )


# ==========================================================
# SHAPELY — AREA
# ==========================================================

def geometry_area(
    geometry
):
    """
    Return geometry area.
    """

    return float(
        geometry.area
    )


# ==========================================================
# SHAPELY — LENGTH
# ==========================================================

def geometry_length(
    geometry
):
    """
    Return geometry length.
    """

    return float(
        geometry.length
    )


# ==========================================================
# SHAPELY — BUFFER
# ==========================================================

def geometry_buffer(
    geometry,
    distance
):
    """
    Create a buffer around a geometry.
    """

    return geometry.buffer(
        float(distance)
    )


# ==========================================================
# SHAPELY — INTERSECTION
# ==========================================================

def geometry_intersection(
    geometry1,
    geometry2
):
    """
    Calculate geometric intersection.
    """

    return geometry1.intersection(
        geometry2
    )


# ==========================================================
# SHAPELY — UNION
# ==========================================================

def geometry_union(
    geometry1,
    geometry2
):
    """
    Calculate geometric union.
    """

    return geometry1.union(
        geometry2
    )


# ==========================================================
# SHAPELY — DISTANCE
# ==========================================================

def geometry_distance(
    geometry1,
    geometry2
):
    """
    Calculate planar geometry distance.
    """

    return float(
        geometry1.distance(
            geometry2
        )
    )


# ==========================================================
# SHAPELY — WKT
# ==========================================================

def geometry_to_wkt(
    geometry
):
    """
    Convert geometry to WKT.
    """

    return geometry.wkt


# ==========================================================
# SHAPELY — WKB
# ==========================================================

def geometry_to_wkb(
    geometry
):
    """
    Convert geometry to WKB.
    """

    return bytes(
        geometry.wkb
    )


# ==========================================================
# GEOPANDAS — GEODATAFRAME
# ==========================================================

def geopandas_dataframe(
    data=None,
    geometry=None,
    crs=None
):
    """
    Create a GeoDataFrame.
    """

    import geopandas as gpd

    return gpd.GeoDataFrame(
        data=data,
        geometry=geometry,
        crs=crs
    )


# ==========================================================
# GEOPANDAS — READ FILE
# ==========================================================

def geopandas_read(
    filename
):
    """
    Read a geospatial vector file.
    """

    import geopandas as gpd

    return gpd.read_file(
        str(filename)
    )


# ==========================================================
# GEOPANDAS — WRITE FILE
# ==========================================================

def geopandas_write(
    dataframe,
    filename,
    driver=None
):
    """
    Write a GeoDataFrame to a geospatial file.
    """

    kwargs = {}

    if driver is not None:

        kwargs["driver"] = driver

    dataframe.to_file(
        str(filename),
        **kwargs
    )

    return str(
        filename
    )


# ==========================================================
# GEOPANDAS — REPROJECT
# ==========================================================

def geopandas_reproject(
    dataframe,
    crs
):
    """
    Reproject a GeoDataFrame.
    """

    return dataframe.to_crs(
        crs
    )


# ==========================================================
# GEOPANDAS — TOTAL BOUNDS
# ==========================================================

def geopandas_bounds(
    dataframe
):
    """
    Return total spatial bounds.
    """

    bounds = dataframe.total_bounds

    return {
        "min_x":
            float(bounds[0]),

        "min_y":
            float(bounds[1]),

        "max_x":
            float(bounds[2]),

        "max_y":
            float(bounds[3]),
    }


# ==========================================================
# GEOPANDAS — SPATIAL JOIN
# ==========================================================

def geopandas_spatial_join(
    left,
    right,
    predicate="intersects"
):
    """
    Perform a spatial join.
    """

    import geopandas as gpd

    return gpd.sjoin(
        left,
        right,
        predicate=str(predicate)
    )


# ==========================================================
# RASTERIO — OPEN
# ==========================================================

def raster_open(
    filename,
    mode="r"
):
    """
    Open a raster dataset.
    """

    import rasterio

    return rasterio.open(
        str(filename),
        mode=str(mode)
    )


# ==========================================================
# RASTERIO — INFORMATION
# ==========================================================

def raster_info(
    filename
):
    """
    Return raster metadata.
    """

    import rasterio

    with rasterio.open(
        str(filename)
    ) as dataset:

        return {
            "width":
                dataset.width,

            "height":
                dataset.height,

            "count":
                dataset.count,

            "dtype":
                str(dataset.dtypes),

            "crs":
                str(dataset.crs),

            "transform":
                str(dataset.transform),

            "bounds":
                tuple(dataset.bounds),
        }


# ==========================================================
# RASTERIO — READ BAND
# ==========================================================

def raster_read_band(
    filename,
    band=1
):
    """
    Read a raster band.
    """

    import rasterio

    with rasterio.open(
        str(filename)
    ) as dataset:

        return dataset.read(
            int(band)
        )


# ==========================================================
# RASTERIO — WRITE
# ==========================================================

def raster_write(
    filename,
    data,
    transform,
    crs,
    dtype=None
):
    """
    Write a single-band raster.
    """

    import rasterio

    import numpy as np

    array = np.asarray(
        data
    )

    if array.ndim != 2:

        raise ValueError(
            "raster_write currently expects a 2D array."
        )

    if dtype is None:

        dtype = array.dtype

    with rasterio.open(
        str(filename),
        "w",
        driver="GTiff",
        height=array.shape[0],
        width=array.shape[1],
        count=1,
        dtype=dtype,
        crs=crs,
        transform=transform
    ) as dataset:

        dataset.write(
            array,
            1
        )

    return str(
        filename
    )


# ==========================================================
# RASTERSTATS — ZONAL STATISTICS
# ==========================================================

def raster_zonal_stats(
    zones,
    raster,
    stats=None
):
    """
    Calculate raster statistics inside vector zones.
    """

    from rasterstats import zonal_stats

    if stats is None:

        stats = [
            "min",
            "max",
            "mean",
            "median",
            "std"
        ]

    return zonal_stats(
        zones,
        raster,
        stats=stats
    )


# ==========================================================
# AFFINE — TRANSFORM
# ==========================================================

def affine_transform(
    x,
    y,
    transform
):
    """
    Apply an affine transform to a coordinate.
    """

    return transform * (
        float(x),
        float(y)
    )


# ==========================================================
# OSMNX — GEOCODING
# ==========================================================

def osmnx_geocode(
    address
):
    """
    Geocode an address through OSMnx.
    """

    import osmnx as ox

    return ox.geocode(
        str(address)
    )


# ==========================================================
# OSMNX — STREET GRAPH
# ==========================================================

def osmnx_street_graph(
    latitude,
    longitude,
    distance=1000,
    network_type="drive"
):
    """
    Download a street network around a coordinate.

    Requires internet access and OpenStreetMap access.
    """

    import osmnx as ox

    return ox.graph_from_point(
        (
            float(latitude),
            float(longitude)
        ),
        dist=float(distance),
        network_type=str(network_type)
    )


# ==========================================================
# OSMNX — GRAPH SUMMARY
# ==========================================================

def osmnx_graph_summary(
    graph
):
    """
    Summarize an OSMnx graph.
    """

    return {
        "nodes":
            int(graph.number_of_nodes()),

        "edges":
            int(graph.number_of_edges()),

        "directed":
            bool(graph.is_directed()),

        "multigraph":
            bool(graph.is_multigraph()),
    }


# ==========================================================
# OSMNX — GRAPH TO GEODATAFRAMES
# ==========================================================

def osmnx_graph_to_gdfs(
    graph
):
    """
    Convert an OSMnx graph to node and edge GeoDataFrames.
    """

    import osmnx as ox

    nodes, edges = ox.graph_to_gdfs(
        graph
    )

    return {
        "nodes": nodes,
        "edges": edges
    }


# ==========================================================
# LIBPYSAL — WEIGHTS
# ==========================================================

def spatial_weights_knn(
    coordinates,
    k=4
):
    """
    Create K-nearest-neighbor spatial weights.
    """

    from libpysal.weights import KNN

    return KNN.from_array(
        coordinates,
        k=int(k)
    )


# ==========================================================
# LIBPYSAL — DISTANCE WEIGHTS
# ==========================================================

def spatial_weights_distance(
    coordinates,
    threshold
):
    """
    Create distance-band spatial weights.
    """

    from libpysal.weights import DistanceBand

    return DistanceBand(
        coordinates,
        threshold=float(threshold)
    )


# ==========================================================
# ESDA — MORAN'S I
# ==========================================================

def spatial_morans_i(
    values,
    weights
):
    """
    Calculate global Moran's I.
    """

    from esda.moran import Moran

    result = Moran(
        values,
        weights
    )

    return {
        "I":
            float(result.I),

        "expected_I":
            float(result.EI),

        "variance":
            float(result.VI_norm),

        "z_score":
            float(result.z_norm),

        "p_value":
            float(result.p_norm),
    }


# ==========================================================
# ESDA — LOCAL MORAN'S I
# ==========================================================

def spatial_local_moran(
    values,
    weights
):
    """
    Calculate Local Moran statistics.
    """

    from esda.moran import Moran_Local

    result = Moran_Local(
        values,
        weights
    )

    return {
        "I":
            result.Is,

        "p_values":
            result.p_sim,

        "z_scores":
            result.z_sim,
    }


# ==========================================================
# MAPCLASSIFY — QUANTILES
# ==========================================================

def classify_quantiles(
    values,
    k=5
):
    """
    Classify values using quantiles.
    """

    import mapclassify

    classifier = mapclassify.Quantiles(
        values,
        k=int(k)
    )

    return {
        "bins":
            classifier.bins,

        "labels":
            classifier.yb,
    }


# ==========================================================
# MAPCLASSIFY — NATURAL BREAKS
# ==========================================================

def classify_natural_breaks(
    values,
    k=5
):
    """
    Classify values using Fisher-Jenks natural breaks.
    """

    import mapclassify

    classifier = mapclassify.NaturalBreaks(
        values,
        k=int(k)
    )

    return {
        "bins":
            classifier.bins,

        "labels":
            classifier.yb,
    }


# ==========================================================
# MOVINGPANDAS — TRAJECTORY
# ==========================================================

def trajectory_summary(
    trajectory
):
    """
    Return basic information about a MovingPandas trajectory.
    """

    return {
        "type":
            type(trajectory).__name__,

        "start":
            str(
                trajectory.get_start_time()
            )
            if hasattr(
                trajectory,
                "get_start_time"
            )
            else None,

        "end":
            str(
                trajectory.get_end_time()
            )
            if hasattr(
                trajectory,
                "get_end_time"
            )
            else None,
    }


# ==========================================================
# WELL PATH — IMPORT
# ==========================================================

def wellpath_import(
    filename
):
    """
    Load a well-path survey using wellpathpy.
    """

    import wellpathpy as wp

    return wp.read_csv(
        str(filename)
    )


# ==========================================================
# WELL PATH — SURVEY
# ==========================================================

def wellpath_survey(
    md,
    inc,
    azi
):
    """
    Create a well-path survey from:

        measured depth
        inclination
        azimuth
    """

    import wellpathpy as wp

    return wp.survey(
        md,
        inc,
        azi
    )


# ==========================================================
# WELLY — WELL
# ==========================================================

def welly_read(
    filename
):
    """
    Read a well-log file using Welly.
    """

    import welly

    return welly.Well.from_las(
        str(filename)
    )


# ==========================================================
# STRIPLOG — AVAILABLE
# ==========================================================

def striplog_status():
    """
    Check Striplog availability.
    """

    module = _get_striplog()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# FLOPY — MODEL LOAD
# ==========================================================

def flopy_model_load(
    model_name,
    model_ws="."
):
    """
    Load a MODFLOW model with FloPy.
    """

    import flopy

    return flopy.modflow.Modflow.load(
        str(model_name),
        model_ws=str(model_ws)
    )


# ==========================================================
# FLOPY — MODEL SUMMARY
# ==========================================================

def flopy_model_summary(
    model
):
    """
    Summarize a FloPy model.
    """

    return {
        "name":
            getattr(
                model,
                "name",
                None
            ),

        "version":
            getattr(
                model,
                "version",
                None
            ),

        "model_ws":
            str(
                getattr(
                    model,
                    "model_ws",
                    ""
                )
            ),

        "packages":
            [
                type(package).__name__
                for package
                in getattr(
                    model,
                    "packagelist",
                    []
                )
            ],
    }


# ==========================================================
# GEMPY — STATUS
# ==========================================================

def gempy_status():
    """
    Check GemPy availability.
    """

    module = _get_gempy()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# GEMPY ENGINE — STATUS
# ==========================================================

def gempy_engine_status():
    """
    Check GemPy Engine availability.
    """

    module = _get_gempy_engine()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# PYREGION — REGION FILE
# ==========================================================

def pyregion_read(
    filename
):
    """
    Read a DS9 region file.
    """

    import pyregion

    return pyregion.open(
        str(filename)
    )


# ==========================================================
# EARTHPY — STATUS
# ==========================================================

def earthpy_status():
    """
    Check EarthPy availability.
    """

    module = _get_earthpy()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# PYDECK — STATUS
# ==========================================================

def pydeck_status():
    """
    Check PyDeck availability.
    """

    module = _get_pydeck()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# TOPOLOGICPY — STATUS
# ==========================================================

def topologicpy_status():
    """
    Check TopologicPy availability.
    """

    module = _get_topologicpy()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None,
    }


# ==========================================================
# XYZ SERVICES — PROVIDERS
# ==========================================================

def xyzservices_providers():
    """
    List available XYZ tile providers.
    """

    import xyzservices.providers

    return xyzservices.providers.flatten()


# ==========================================================
# PART 11 STATUS
# ==========================================================

def gis_part11_status():

    packages = [
        "geopandas",
        "shapely",
        "pyproj",
        "geopy",
        "rasterio",
        "rasterstats",
        "pyogrio",
        "rtree",
        "osmnx",
        "folium",
        "affine",
        "geographiclib",
        "libpysal",
        "esda",
        "giddy",
        "mapclassify",
        "momepy",
        "movingpandas",
        "spaghetti",
        "spglm",
        "spint",
        "splot",
        "spml",
        "spopt",
        "tobler",
        "xyzservices",
        "striplog",
        "welly",
        "wellpathpy",
        "pyregion",
        "earthpy",
        "flopy",
        "gempy",
        "gempy_engine",
        "pydeck",
        "topologicpy",
    ]

    results = {}

    print()
    print("=" * 78)
    print(
        "DAVE — GIS / GEOSCIENCE PART 11 STATUS"
    )
    print("=" * 78)
    print()

    for package_name in packages:

        try:

            module = load_scientific_package(
                package_name
            )

            version = getattr(
                module,
                "__version__",
                "unknown"
            )

            results[package_name] = {
                "available": True,
                "version": str(version)
            }

            print(
                f"[OK] {package_name:<22} {version}"
            )

        except Exception as exc:

            results[package_name] = {
                "available": False,
                "error": str(exc)
            }

            print(
                f"[--] {package_name:<22} unavailable"
            )

    print()

    return results


# ==========================================================
# PART 11 SELF TEST
# ==========================================================

def gis_part11_selftest(
    verbose=True
):

    tests = []


    # ------------------------------------------------------
    # GEODESIC DISTANCE
    # ------------------------------------------------------

    try:

        distance = geo_distance_km(
            40.7128,
            -74.0060,
            40.7138,
            -74.0060
        )

        tests.append(
            (
                "geopy distance",
                distance > 0
            )
        )

    except Exception as exc:

        tests.append(
            (
                "geopy distance",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # GEOGRAPHICLIB
    # ------------------------------------------------------

    try:

        result = geographiclib_inverse(
            40.7128,
            -74.0060,
            40.7138,
            -74.0060
        )

        tests.append(
            (
                "geographiclib",
                "s12" in result
            )
        )

    except Exception as exc:

        tests.append(
            (
                "geographiclib",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # SHAPELY
    # ------------------------------------------------------

    try:

        point = geometry_point(
            0,
            0
        )

        buffer = geometry_buffer(
            point,
            10
        )

        tests.append(
            (
                "shapely",
                buffer.area > 0
            )
        )

    except Exception as exc:

        tests.append(
            (
                "shapely",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # PYPROJ
    # ------------------------------------------------------

    try:

        x, y = coordinate_transform(
            -74.0060,
            40.7128,
            "EPSG:4326",
            "EPSG:3857"
        )

        tests.append(
            (
                "pyproj",
                abs(x) > 1
                and abs(y) > 1
            )
        )

    except Exception as exc:

        tests.append(
            (
                "pyproj",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # GEOPANDAS
    # ------------------------------------------------------

    try:

        import geopandas as gpd

        dataframe = geopandas_dataframe(
            {
                "name": ["A", "B"]
            },
            geometry=[
                geometry_point(0, 0),
                geometry_point(1, 1)
            ],
            crs="EPSG:4326"
        )

        tests.append(
            (
                "geopandas",
                len(dataframe) == 2
            )
        )

    except Exception as exc:

        tests.append(
            (
                "geopandas",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # MAP CLASSIFICATION
    # ------------------------------------------------------

    try:

        classification = classify_quantiles(
            [1, 2, 3, 4, 5, 6],
            k=3
        )

        tests.append(
            (
                "mapclassify",
                len(classification["bins"]) == 3
            )
        )

    except Exception as exc:

        tests.append(
            (
                "mapclassify",
                False,
                str(exc)
            )
        )


    # ------------------------------------------------------
    # RESULTS
    # ------------------------------------------------------

    passed = 0
    failed = 0

    if verbose:

        print()
        print("=" * 78)
        print(
            "DAVE — GIS / GEOSCIENCE PART 11 SELF TEST"
        )
        print("=" * 78)
        print()

    for test in tests:

        name = test[0]
        result = test[1]

        if result:

            passed += 1

            if verbose:

                print(
                    f"[PASS] {name}"
                )

        else:

            failed += 1

            if verbose:

                print(
                    f"[FAIL] {name}"
                )

                if len(test) > 2:

                    print(
                        f"       {test[2]}"
                    )

    if verbose:

        print()
        print("-" * 78)
        print(
            f"Passed: {passed}"
        )
        print(
            f"Failed: {failed}"
        )
        print(
            f"Total:  {len(tests)}"
        )
        print("-" * 78)
        print()

    return {
        "passed": passed,
        "failed": failed,
        "total": len(tests)
    }


# ==========================================================
# PART 11 HELP
# ==========================================================

def gis_part11_help():

    print("""
==============================================================================
DAVE — GIS / GEOSPATIAL / GEOSCIENCE
PART 11
==============================================================================


GEODESY
-------

    geo_distance(
        latitude1,
        longitude1,
        latitude2,
        longitude2
    )

    geo_distance_km(...)

    geo_distance_miles(...)

    geographiclib_inverse(...)

    geographiclib_direct(...)


COORDINATE SYSTEMS
------------------

    coordinate_transform(
        x,
        y,
        source_crs,
        target_crs
    )

    coordinate_transform_many(
        x,
        y,
        source_crs,
        target_crs
    )

    crs_information(crs)


SHAPELY GEOMETRY
----------------

    geometry_point(x, y)

    geometry_line(coordinates)

    geometry_polygon(coordinates)

    geometry_area(geometry)

    geometry_length(geometry)

    geometry_buffer(
        geometry,
        distance
    )

    geometry_intersection(
        geometry1,
        geometry2
    )

    geometry_union(
        geometry1,
        geometry2
    )

    geometry_distance(
        geometry1,
        geometry2
    )

    geometry_to_wkt(geometry)

    geometry_to_wkb(geometry)


GEOPANDAS
---------

    geopandas_dataframe(...)

    geopandas_read(filename)

    geopandas_write(
        dataframe,
        filename
    )

    geopandas_reproject(
        dataframe,
        crs
    )

    geopandas_bounds(dataframe)

    geopandas_spatial_join(
        left,
        right,
        predicate
    )


RASTER DATA
-----------

    raster_open(
        filename,
        mode
    )

    raster_info(filename)

    raster_read_band(
        filename,
        band
    )

    raster_write(
        filename,
        data,
        transform,
        crs
    )

    raster_zonal_stats(
        zones,
        raster,
        stats
    )


OPENSTREETMAP / OSMNX
---------------------

    osmnx_geocode(address)

    osmnx_street_graph(
        latitude,
        longitude,
        distance,
        network_type
    )

    osmnx_graph_summary(graph)

    osmnx_graph_to_gdfs(graph)


SPATIAL STATISTICS
------------------

    spatial_weights_knn(
        coordinates,
        k
    )

    spatial_weights_distance(
        coordinates,
        threshold
    )

    spatial_morans_i(
        values,
        weights
    )

    spatial_local_moran(
        values,
        weights
    )


MAP CLASSIFICATION
------------------

    classify_quantiles(
        values,
        k
    )

    classify_natural_breaks(
        values,
        k
    )


WELL / BOREHOLE DATA
--------------------

    wellpath_import(filename)

    wellpath_survey(
        md,
        inc,
        azi
    )

    welly_read(filename)

    striplog_status()


GROUNDWATER / HYDROLOGY
-----------------------

    flopy_model_load(
        model_name,
        model_ws
    )

    flopy_model_summary(model)


GEOLOGICAL MODELING
-------------------

    gempy_status()

    gempy_engine_status()


ASTRONOMICAL REGIONS
--------------------

    pyregion_read(filename)


EARTH SCIENCE
-------------

    earthpy_status()


WEB MAPS
--------

    pydeck_status()

    xyzservices_providers()


TOPOLOGICAL MODELING
--------------------

    topologicpy_status()


STATUS / TESTING
----------------

    gis_part11_status()

    gis_part11_selftest()


==============================================================================
""")

# ==========================================================
# DAVE
# ADVANCED SIMULATION / MOLECULAR DYNAMICS /
# COMPUTATIONAL PHYSICS / CROSS-PACKAGE INTEGRATION
# PART 12 — FINAL PACKAGE INTEGRATION
# ==========================================================


# ==========================================================
# PACKAGE LOADERS
# ==========================================================

def _get_openmm():
    return load_scientific_package("OpenMM")


def _get_mdanalysis():
    return load_scientific_package("MDAnalysis")


def _get_mdtraj():
    return load_scientific_package("mdtraj")


def _get_mdapy():
    return load_scientific_package("mdapy")


def _get_freud():
    return load_scientific_package("freud")


def _get_mmtf():
    return load_scientific_package("mmtf-python")


def _get_brian2():
    return load_scientific_package("Brian2")


def _get_nengo():
    return load_scientific_package("nengo")


def _get_elephant():
    return load_scientific_package("elephant")


def _get_neo():
    return load_scientific_package("neo")


def _get_pynapple():
    return load_scientific_package("pynapple")


def _get_pynwb():
    return load_scientific_package("pynwb")


def _get_quantities():
    return load_scientific_package("quantities")


def _get_pymatgen():
    return load_scientific_package("pymatgen")


def _get_spglib():
    return load_scientific_package("spglib")


def _get_pyrolite():
    return load_scientific_package("pyrolite")


def _get_rdkit():
    return load_scientific_package("rdkit")


def _get_chemparse():
    return load_scientific_package("chemparse")


def _get_chempy():
    return load_scientific_package("chempy")


def _get_pubchempy():
    return load_scientific_package("pubchempy")


def _get_radioactivedecay():
    return load_scientific_package("radioactivedecay")


def _get_plasmapy():
    return load_scientific_package("plasmapy")


def _get_ase():
    return load_scientific_package("ase")


def _get_spglib():
    return load_scientific_package("spglib")


# ==========================================================
# OPENMM — BASIC SYSTEM STATUS
# ==========================================================

def openmm_status():
    """
    Check OpenMM availability and version.
    """

    module = _get_openmm()

    if module is None:

        return {
            "available": False,
            "version": None
        }

    return {
        "available": True,
        "version": str(
            getattr(
                module,
                "__version__",
                "unknown"
            )
        )
    }


# ==========================================================
# OPENMM — PLATFORM INFORMATION
# ==========================================================

def openmm_platforms():
    """
    Return the OpenMM computation platforms available
    on the current machine.
    """

    import openmm

    platforms = []

    for index in range(
        openmm.Platform.getNumPlatforms()
    ):

        platform = (
            openmm.Platform.getPlatform(
                index
            )
        )

        platforms.append(
            {
                "name":
                    platform.getName(),

                "speed":
                    platform.getSpeed()
            }
        )

    return platforms


# ==========================================================
# OPENMM — SIMPLE SYSTEM
# ==========================================================

def openmm_simple_system(
    particle_mass=1.0,
    particles=1
):
    """
    Create a simple OpenMM system containing particles.

    This is useful for testing OpenMM itself before
    constructing a complete molecular model.
    """

    import openmm

    system = openmm.System()

    for _ in range(
        int(particles)
    ):

        system.addParticle(
            float(particle_mass)
        )

    return system


# ==========================================================
# MDANALYSIS — LOAD TRAJECTORY
# ==========================================================

def mdanalysis_load(
    topology,
    trajectory=None
):
    """
    Load a molecular dynamics system with MDAnalysis.
    """

    import MDAnalysis as mda

    if trajectory is None:

        return mda.Universe(
            str(topology)
        )

    return mda.Universe(
        str(topology),
        str(trajectory)
    )


# ==========================================================
# MDANALYSIS — ATOM COUNT
# ==========================================================

def mdanalysis_atom_count(
    universe
):
    """
    Return the number of atoms.
    """

    return int(
        universe.atoms.n_atoms
    )


# ==========================================================
# MDANALYSIS — RESIDUE COUNT
# ==========================================================

def mdanalysis_residue_count(
    universe
):
    """
    Return the number of residues.
    """

    return int(
        universe.residues.n_residues
    )


# ==========================================================
# MDANALYSIS — CENTER OF MASS
# ==========================================================

def mdanalysis_center_of_mass(
    universe
):
    """
    Calculate the molecular center of mass.
    """

    return universe.atoms.center_of_mass()


# ==========================================================
# MDANALYSIS — RADIUS OF GYRATION
# ==========================================================

def mdanalysis_radius_of_gyration(
    universe
):
    """
    Calculate radius of gyration.
    """

    return float(
        universe.atoms.radius_of_gyration()
    )


# ==========================================================
# MDTRAJ — LOAD
# ==========================================================

def mdtraj_load(
    filename,
    top=None
):
    """
    Load an MD trajectory using MDTraj.
    """

    import mdtraj as md

    if top is None:

        return md.load(
            str(filename)
        )

    return md.load(
        str(filename),
        top=str(top)
    )


# ==========================================================
# MDTRAJ — DISTANCE
# ==========================================================

def mdtraj_distance(
    trajectory,
    atom_pairs
):
    """
    Calculate distances between atom pairs.
    """

    import mdtraj as md

    return md.compute_distances(
        trajectory,
        atom_pairs
    )


# ==========================================================
# MDTRAJ — RMSD
# ==========================================================

def mdtraj_rmsd(
    trajectory,
    reference=None
):
    """
    Calculate RMSD relative to a reference frame.
    """

    if reference is None:

        reference = trajectory

    return trajectory.rmsd(
        reference
    )


# ==========================================================
# FREUD — PARTICLE SYSTEM
# ==========================================================

def freud_box(
    box_size
):
    """
    Create a periodic cubic box.
    """

    import freud

    return freud.box.Box.cube(
        float(box_size)
    )


# ==========================================================
# FREUD — RADIAL DISTRIBUTION FUNCTION
# ==========================================================

def freud_rdf(
    box,
    positions,
    bins=50,
    r_max=None
):
    """
    Calculate a radial distribution function.
    """

    import freud

    if r_max is None:

        r_max = float(
            min(box.Lx, box.Ly, box.Lz)
        ) / 2.0

    rdf = freud.density.RDF(
        bins=int(bins),
        r_max=float(r_max)
    )

    rdf.compute(
        (box, positions),
        reset=True
    )

    return {
        "r":
            rdf.bin_centers,

        "g_r":
            rdf.rdf
    }


# ==========================================================
# MDAPY — STATUS
# ==========================================================

def mdapy_status():
    """
    Check mdapy availability.
    """

    module = _get_mdapy()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None
    }


# ==========================================================
# MMTF — STATUS
# ==========================================================

def mmtf_status():
    """
    Show MMTF support status.
    """

    try:
        module = load_scientific_package(
            "mmtf_python"
        )

        version = getattr(
            module,
            "__version__",
            "unknown"
        )

        print(
            f"[OK] mmtf-python {version}"
        )

        return {
            "available": True,
            "version": str(version)
        }

    except Exception as exc:

        print(
            f"[--] mmtf-python unavailable: {exc}"
        )

        return {
            "available": False,
            "error": str(exc)
        }

# ==========================================================
# BRIAN2 — NEURON
# ==========================================================

def brian2_neuron(
    equation,
    threshold,
    reset,
    duration=10
):
    """
    Run a basic Brian2 neuron simulation.

    duration is in milliseconds.
    """

    from brian2 import (
        NeuronGroup,
        StateMonitor,
        ms,
        run
    )

    neurons = NeuronGroup(
        1,
        model=str(equation),
        threshold=str(threshold),
        reset=str(reset),
        method="euler"
    )

    monitor = StateMonitor(
        neurons,
        True,
        record=True
    )

    run(
        float(duration) * ms
    )

    return {
        "neuron":
            neurons,

        "monitor":
            monitor
    }


# ==========================================================
# BRIAN2 — STATUS
# ==========================================================

def brian2_status():
    """
    Check Brian2 availability.
    """

    module = _get_brian2()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None
    }


# ==========================================================
# NENGO — STATUS
# ==========================================================

def nengo_status():
    """
    Check Nengo availability.
    """

    module = _get_nengo()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None
    }


# ==========================================================
# NEO — STATUS
# ==========================================================

def neo_status():
    """
    Check Neo availability.
    """

    module = _get_neo()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None
    }


# ==========================================================
# ELEPHANT — STATUS
# ==========================================================

def elephant_status():
    """
    Check Elephant availability.
    """

    module = _get_elephant()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None
    }


# ==========================================================
# PYNAPPLE — STATUS
# ==========================================================

def pynapple_status():
    """
    Check Pynapple availability.
    """

    module = _get_pynapple()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None
    }


# ==========================================================
# PYNWB — STATUS
# ==========================================================

def pynwb_status():
    """
    Check PyNWB availability.
    """

    module = _get_pynwb()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None
    }


# ==========================================================
# PYMATGEN — STRUCTURE FROM FORMULA
# ==========================================================

def pymatgen_composition(
    formula
):
    """
    Parse a chemical composition using pymatgen.
    """

    from pymatgen.core import Composition

    composition = Composition(
        str(formula)
    )

    return {
        "formula":
            composition.formula,

        "reduced_formula":
            composition.reduced_formula,

        "weight":
            float(
                composition.weight
            ),

        "elements":
            [
                str(element)
                for element
                in composition.elements
            ]
    }


# ==========================================================
# PYMATGEN — LATTICE
# ==========================================================

def pymatgen_lattice(
    a,
    b=None,
    c=None,
    alpha=90,
    beta=90,
    gamma=90
):
    """
    Create a crystal lattice.
    """

    from pymatgen.core import Lattice

    if b is None:

        b = a

    if c is None:

        c = a

    return Lattice.from_parameters(
        float(a),
        float(b),
        float(c),
        float(alpha),
        float(beta),
        float(gamma)
    )

# ==========================================================
# SPGLIB — SPACE GROUP
# ==========================================================

def spglib_spacegroup(
    lattice,
    positions=None,
    numbers=None,
    symprec=1e-5
):
    """
    Determine the international space-group symbol
    for a crystal structure.

    Supports:

        spglib_spacegroup(
            lattice,
            positions,
            numbers
        )

    and:

        spglib_spacegroup(
            (lattice, positions, numbers)
        )
    """

    return _spglib_spacegroup_validated(
        lattice,
        positions,
        numbers,
        symprec=symprec
    )

# ==========================================================
# PYROLITE — STATUS
# ==========================================================

def pyrolite_status():
    """
    Check pyrolite availability.
    """

    module = _get_pyrolite()

    return {
        "available":
            module is not None,

        "version":
            getattr(
                module,
                "__version__",
                "unknown"
            )
            if module is not None
            else None
    }


# ==========================================================
# RDKIT — SMILES MOLECULE
# ==========================================================

def rdkit_molecule(
    smiles
):
    """
    Create an RDKit molecule from SMILES.
    """

    from rdkit import Chem

    molecule = Chem.MolFromSmiles(
        str(smiles)
    )

    if molecule is None:

        raise ValueError(
            "Invalid SMILES string."
        )

    return molecule


# ==========================================================
# RDKIT — MOLECULAR FORMULA
# ==========================================================

def rdkit_formula(
    smiles
):
    """
    Determine a molecular formula from SMILES.
    """

    from rdkit import Chem
    from rdkit.Chem import rdMolDescriptors

    molecule = Chem.MolFromSmiles(
        str(smiles)
    )

    if molecule is None:

        raise ValueError(
            "Invalid SMILES string."
        )

    return rdMolDescriptors.CalcMolFormula(
        molecule
    )


# ==========================================================
# RDKIT — MOLECULAR WEIGHT
# ==========================================================

def rdkit_molecular_weight(
    smiles
):
    """
    Calculate molecular weight from SMILES.
    """

    from rdkit import Chem
    from rdkit.Chem import Descriptors

    molecule = Chem.MolFromSmiles(
        str(smiles)
    )

    if molecule is None:

        raise ValueError(
            "Invalid SMILES string."
        )

    return float(
        Descriptors.MolWt(
            molecule
        )
    )


# ==========================================================
# RDKIT — CANONICAL SMILES
# ==========================================================

def rdkit_canonical_smiles(
    smiles
):
    """
    Convert SMILES to canonical SMILES.
    """

    from rdkit import Chem

    molecule = Chem.MolFromSmiles(
        str(smiles)
    )

    if molecule is None:

        raise ValueError(
            "Invalid SMILES string."
        )

    return Chem.MolToSmiles(
        molecule,
        canonical=True
    )


# ==========================================================
# CHEMPARSE — FORMULA
# ==========================================================

def chemparse_formula(
    formula
):
    """
    Parse a chemical formula into element counts.
    """

    import chemparse

    return chemparse.parse_formula(
        str(formula)
    )


# ==========================================================
# CHEMPY — MOLECULAR WEIGHT
# ==========================================================

def chempy_molecular_weight(
    formula
):
    """
    Calculate molecular mass using ChemPy.
    """

    from chempy import Substance

    substance = Substance.from_formula(
        str(formula)
    )

    return float(
        substance.mass
    )


# ==========================================================
# PUBCHEMPY — COMPOUND SEARCH
# ==========================================================

def pubchem_search(
    query,
    namespace="name"
):
    """
    Search PubChem.

    Requires internet access.
    """

    import pubchempy as pcp

    compounds = pcp.get_compounds(
        str(query),
        str(namespace)
    )

    results = []

    for compound in compounds:

        results.append(
            {
                "cid":
                    getattr(
                        compound,
                        "cid",
                        None
                    ),

                "molecular_formula":
                    getattr(
                        compound,
                        "molecular_formula",
                        None
                    ),

                "molecular_weight":
                    getattr(
                        compound,
                        "molecular_weight",
                        None
                    ),

                "iupac_name":
                    getattr(
                        compound,
                        "iupac_name",
                        None
                    )
            }
        )

    return results


# ==========================================================
# RADIOACTIVE DECAY — NUCLIDE
# ==========================================================

def radioactive_nuclide(
    nuclide
):
    """
    Create a radioactive-decay nuclide object.
    """

    import radioactivedecay as rd

    return rd.Nuclide(
        str(nuclide)
    )

# ==========================================================
# RADIOACTIVE DECAY — DECAY DATA
# ==========================================================

def radioactive_half_life(
    nuclide
):
    """
    Return the half-life of a radionuclide.

    Example:

        radioactive_half_life("U-238")
    """

    isotope = radioactive_nuclide(
        nuclide
    )

    return isotope.half_life()

# ==========================================================
# PLASMAPY — PARTICLE
# ==========================================================

def plasma_particle(
    symbol
):
    """
    Return a PlasmaPy Particle object.

    Examples:

        plasma_particle("e-")
        plasma_particle("p+")
        plasma_particle("alpha")
        plasma_particle("He-4")
    """

    from plasmapy.particles import Particle

    return Particle(
        str(symbol)
    )

# ==========================================================
# ASE — ATOMS
# ==========================================================

def ase_atoms(
    symbols,
    positions=None
):
    """
    Create an ASE Atoms object.
    """

    from ase import Atoms

    kwargs = {}

    if positions is not None:

        kwargs["positions"] = positions

    return Atoms(
        symbols=symbols,
        **kwargs
    )


# ==========================================================
# ASE — DISTANCE
# ==========================================================

def ase_distance(
    atoms,
    atom1,
    atom2
):
    """
    Calculate distance between two atoms.
    """

    return float(
        atoms.get_distance(
            int(atom1),
            int(atom2)
        )
    )


# ==========================================================
# ASE — CELL
# ==========================================================

def ase_cell(
    atoms
):
    """
    Return the unit-cell information.
    """

    return atoms.cell.array


# ==========================================================
# CROSS-PACKAGE — CHEMICAL FORMULA REPORT
# ==========================================================

def cross_package_formula_report(
    formula
):
    """
    Use several installed chemistry packages to create
    a combined formula report.

    This function attempts multiple packages independently.
    """

    report = {
        "formula": str(formula)
    }


    # ------------------------------------------------------
    # CHEMPARSE
    # ------------------------------------------------------

    try:

        report["chemparse"] = (
            chemparse_formula(
                formula
            )
        )

    except Exception as exc:

        report["chemparse_error"] = str(
            exc
        )


    # ------------------------------------------------------
    # PYMATGEN
    # ------------------------------------------------------

    try:

        report["pymatgen"] = (
            pymatgen_composition(
                formula
            )
        )

    except Exception as exc:

        report["pymatgen_error"] = str(
            exc
        )


    # ------------------------------------------------------
    # CHEMPY
    # ------------------------------------------------------

    try:

        report["chempy_mass"] = (
            chempy_molecular_weight(
                formula
            )
        )

    except Exception as exc:

        report["chempy_error"] = str(
            exc
        )


    # ------------------------------------------------------
    # MENDELEEV
    # ------------------------------------------------------

    try:

        if "mendeleev" in globals():

            report["mendeleev"] = (
                "available"
            )

        else:

            report["mendeleev"] = (
                "registry-based integration available"
            )

    except Exception:

        pass


    return report


# ==========================================================
# CROSS-PACKAGE — MOLECULE REPORT
# ==========================================================

def cross_package_molecule_report(
    smiles
):
    """
    Combine RDKit and PubChem information.

    PubChem lookup is optional and requires Internet access.
    """

    report = {
        "smiles":
            str(smiles)
    }


    # ------------------------------------------------------
    # RDKIT
    # ------------------------------------------------------

    try:

        report["canonical_smiles"] = (
            rdkit_canonical_smiles(
                smiles
            )
        )

        report["formula"] = (
            rdkit_formula(
                smiles
            )
        )

        report["molecular_weight"] = (
            rdkit_molecular_weight(
                smiles
            )
        )

    except Exception as exc:

        report["rdkit_error"] = str(
            exc
        )


    # ------------------------------------------------------
    # PUBCHEM
    # ------------------------------------------------------

    try:

        report["pubchem"] = (
            pubchem_search(
                smiles,
                namespace="smiles"
            )
        )

    except Exception as exc:

        report["pubchem_error"] = str(
            exc
        )


    return report


# ==========================================================
# CROSS-PACKAGE — CRYSTAL REPORT
# ==========================================================

def cross_package_crystal_report(
    formula
):
    """
    Create a basic materials/crystal report.

    Uses pymatgen and the existing chemistry infrastructure.
    """

    report = {
        "formula":
            str(formula)
    }

    try:

        composition = pymatgen_composition(
            formula
        )

        report["composition"] = composition

    except Exception as exc:

        report["composition_error"] = str(
            exc
        )

    try:

        report["chemparse"] = (
            chemparse_formula(
                formula
            )
        )

    except Exception as exc:

        report["chemparse_error"] = str(
            exc
        )

    return report


# ==========================================================
# CROSS-PACKAGE — COORDINATE REPORT
# ==========================================================

def cross_package_coordinate_report(
    latitude,
    longitude
):
    """
    Create a combined geospatial coordinate report.
    """

    report = {
        "latitude":
            float(latitude),

        "longitude":
            float(longitude)
    }


    try:

        report["web_mercator"] = (
            coordinate_transform(
                longitude,
                latitude,
                "EPSG:4326",
                "EPSG:3857"
            )
        )

    except Exception as exc:

        report["projection_error"] = str(
            exc
        )


    try:

        report["wgs84"] = (
            crs_information(
                "EPSG:4326"
            )
        )

    except Exception as exc:

        report["crs_error"] = str(
            exc
        )


    return report


# ==========================================================
# CROSS-PACKAGE — SCIENTIFIC PACKAGE STATUS
# ==========================================================

def all_scientific_package_status():
    """
    Produce one combined status report for the entire
    scientific-package system.
    """

    try:

        return scientific_package_status()

    except Exception:

        results = {}

        for name in SCIENTIFIC_PACKAGES:

            try:

                module = load_scientific_package(
                    name
                )

                results[name] = {
                    "available": module is not None,

                    "version":
                        getattr(
                            module,
                            "__version__",
                            "unknown"
                        )
                        if module is not None
                        else None
                }

            except Exception as exc:

                results[name] = {
                    "available": False,
                    "error": str(exc)
                }

        return results


# ==========================================================
# CROSS-PACKAGE — PACKAGE CATEGORY REPORT
# ==========================================================

def scientific_package_report():
    """
    Print a categorized scientific-package report.
    """

    print()
    print("=" * 78)
    print(
        "DAVE — COMPLETE SCIENTIFIC PACKAGE REPORT"
    )
    print("=" * 78)
    print()

    try:

        categories = (
            scientific_package_categories()
        )

    except Exception:

        categories = sorted(
            set(
                package_category(
                    name
                )
                for name
                in SCIENTIFIC_PACKAGES
            )
        )

    for category in categories:

        print()
        print(
            f"[{str(category).upper()}]"
        )
        print(
            "-" * 78
        )

        try:

            names = packages(
                category=category
            )

        except Exception:

            names = [
                name
                for name
                in SCIENTIFIC_PACKAGES
                if package_category(name)
                == category
            ]

        for name in names:

            try:

                available = (
                    scientific_package_available(
                        name
                    )
                )

            except Exception:

                available = False

            status = (
                "INSTALLED"
                if available
                else "UNAVAILABLE"
            )

            print(
                f"{name:<30} {status}"
            )

    print()


# ==========================================================
# COMPLETE PACKAGE SELF TEST
# ==========================================================

def final_scientific_selftest(
    verbose=True
):
    """
    Run the major package-integration self tests.

    Individual optional packages are allowed to be missing.
    """

    results = {}


    # ------------------------------------------------------
    # PART 10
    # ------------------------------------------------------

    try:

        results["part10"] = (
            visualization_part10_selftest(
                verbose=verbose
            )
        )

    except Exception as exc:

        results["part10"] = {
            "error": str(exc)
        }


    # ------------------------------------------------------
    # PART 11
    # ------------------------------------------------------

    try:

        results["part11"] = (
            gis_part11_selftest(
                verbose=verbose
            )
        )

    except Exception as exc:

        results["part11"] = {
            "error": str(exc)
        }


    # ------------------------------------------------------
    # OPENMM
    # ------------------------------------------------------

    try:

        status = openmm_status()

        results["openmm"] = status

        if verbose:

            print(
                "[OK] OpenMM status checked"
            )

    except Exception as exc:

        results["openmm"] = {
            "error": str(exc)
        }


    # ------------------------------------------------------
    # MOLECULAR DYNAMICS
    # ------------------------------------------------------

    for name, function in [
        (
            "MDAnalysis",
            _get_mdanalysis
        ),
        (
            "MDTraj",
            _get_mdtraj
        ),
        (
            "freud",
            _get_freud
        ),
        (
            "mdapy",
            _get_mdapy
        ),
    ]:

        try:

            module = function()

            results[name] = {
                "available":
                    module is not None,

                "version":
                    getattr(
                        module,
                        "__version__",
                        "unknown"
                    )
                    if module is not None
                    else None
            }

            if verbose:

                print(
                    f"[OK] {name} status checked"
                )

        except Exception as exc:

            results[name] = {
                "error": str(exc)
            }


    # ------------------------------------------------------
    # MATERIALS
    # ------------------------------------------------------

    try:

        results["pymatgen"] = {
            "available":
                _get_pymatgen() is not None
        }

    except Exception as exc:

        results["pymatgen"] = {
            "error": str(exc)
        }


    # ------------------------------------------------------
    # CHEMISTRY
    # ------------------------------------------------------

    for name, function in [
        (
            "RDKit",
            _get_rdkit
        ),
        (
            "chemparse",
            _get_chemparse
        ),
        (
            "ChemPy",
            _get_chempy
        ),
        (
            "PubChemPy",
            _get_pubchempy
        ),
        (
            "radioactivedecay",
            _get_radioactivedecay
        ),
    ]:

        try:

            module = function()

            results[name] = {
                "available":
                    module is not None
            }

        except Exception as exc:

            results[name] = {
                "error": str(exc)
            }


    if verbose:

        print()
        print("=" * 78)
        print(
            "FINAL SCIENTIFIC PACKAGE SELF TEST COMPLETE"
        )
        print("=" * 78)
        print()

    return results


# ==========================================================
# FINAL HELP
# ==========================================================

def final_scientific_help():

    print("""
==============================================================================
DAVE
FINAL SCIENTIFIC PACKAGE INTEGRATION
==============================================================================


MOLECULAR DYNAMICS
------------------

    openmm_status()

    openmm_platforms()

    openmm_simple_system(
        particle_mass,
        particles
    )

    mdanalysis_load(
        topology,
        trajectory
    )

    mdanalysis_atom_count(
        universe
    )

    mdanalysis_residue_count(
        universe
    )

    mdanalysis_center_of_mass(
        universe
    )

    mdanalysis_radius_of_gyration(
        universe
    )

    mdtraj_load(
        filename,
        top
    )

    mdtraj_distance(
        trajectory,
        atom_pairs
    )

    mdtraj_rmsd(
        trajectory,
        reference
    )

    freud_box(
        box_size
    )

    freud_rdf(
        box,
        positions,
        bins,
        r_max
    )


NEUROSCIENCE / COMPUTATIONAL NEURAL SYSTEMS
-------------------------------------------

    brian2_neuron(...)

    brian2_status()

    nengo_status()

    neo_status()

    elephant_status()

    pynapple_status()

    pynwb_status()


MATERIALS / CRYSTALS
--------------------

    pymatgen_composition(
        formula
    )

    pymatgen_lattice(
        a,
        b,
        c,
        alpha,
        beta,
        gamma
    )

    spglib_spacegroup(
        cell,
        symprec
    )

    pyrolite_status()


CHEMICAL STRUCTURES
-------------------

    rdkit_molecule(
        smiles
    )

    rdkit_formula(
        smiles
    )

    rdkit_molecular_weight(
        smiles
    )

    rdkit_canonical_smiles(
        smiles
    )

    chemparse_formula(
        formula
    )

    chempy_molecular_weight(
        formula
    )

    pubchem_search(
        query,
        namespace
    )


RADIOACTIVITY
-------------

    radioactive_nuclide(
        nuclide
    )

    radioactive_half_life(
        nuclide
    )

    radioactive_decay_data(
        nuclide
    )


PLASMA PHYSICS
--------------

    plasma_particle_info(
        particle
    )


ATOMISTIC SIMULATION
--------------------

    ase_atoms(
        symbols,
        positions
    )

    ase_distance(
        atoms,
        atom1,
        atom2
    )

    ase_cell(
        atoms
    )


CROSS-PACKAGE FEATURES
----------------------

    cross_package_formula_report(
        formula
    )

    cross_package_molecule_report(
        smiles
    )

    cross_package_crystal_report(
        formula
    )

    cross_package_coordinate_report(
        latitude,
        longitude
    )


PACKAGE MANAGEMENT
------------------

    all_scientific_package_status()

    scientific_package_report()

    final_scientific_selftest()


==============================================================================
""")

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


def _package_status(package_name):
    """Return availability and version for a registered optional package."""
    try:
        module = load_scientific_package(package_name)
        return {
            "available": True,
            "version": str(getattr(module, "__version__", "unknown")),
        }
    except Exception as exc:
        return {"available": False, "version": None, "error": str(exc)}


def diffrax_status(): return _package_status("diffrax")
def dynamiqs_status(): return _package_status("dynamiqs")
def equinox_status(): return _package_status("equinox")
def lineax_status(): return _package_status("lineax")
def optimistix_status(): return _package_status("optimistix")
def opt_einsum_status(): return _package_status("opt_einsum")
def emcee_status(): return _package_status("emcee")
def formulaic_status(): return _package_status("formulaic")
def gudhi_status(): return _package_status("gudhi")
def mdanalysis_status(): return _package_status("MDAnalysis")
def mdtraj_status(): return _package_status("mdtraj")
def matplotlib_status(): return _package_status("matplotlib")
def plotly_status(): return _package_status("plotly")
def altair_status(): return _package_status("altair")
def xarray_status(): return _package_status("xarray")
def zarr_status(): return _package_status("zarr")
def h5py_status(): return _package_status("h5py")
def nibabel_status(): return _package_status("nibabel")
def pywavelets_status(): return _package_status("PyWavelets")
def skimage_status(): return _package_status("scikit_image")
def tifffile_status(): return _package_status("tifffile")
def dipy_status(): return _package_status("dipy")
def folium_status(): return _package_status("folium")
def yt_status(): return _package_status("yt")

# ==========================================================
# ADDITIONAL SCIENCE CALCULATORS
# ==========================================================

def _science_finite_values(**values):
    converted = {}
    for name, value in values.items():
        try:
            number = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{name} must be a finite number.") from exc
        if not math.isfinite(number):
            raise ValueError(f"{name} must be a finite number.")
        converted[name] = number
    return converted


def epidemiology_2x2(exposed_cases, exposed_non_cases, unexposed_cases, unexposed_non_cases):
    """Return risks, risk ratio, odds ratio, and risk difference from a 2x2 table."""
    v = _science_finite_values(exposed_cases=exposed_cases, exposed_non_cases=exposed_non_cases,
                               unexposed_cases=unexposed_cases, unexposed_non_cases=unexposed_non_cases)
    if any(x < 0 for x in v.values()):
        raise ValueError("2x2 table counts must be non-negative.")
    ec, en, uc, un = v.values()
    et, ut = ec + en, uc + un
    er = ec / et if et else None
    ur = uc / ut if ut else None
    undefined = []
    if et == 0:
        undefined.append("exposed_risk: no exposed participants")
    if ut == 0:
        undefined.append("unexposed_risk: no unexposed participants")
    if er is None or ur is None or ur == 0:
        undefined.append("risk_ratio: requires both risks and a non-zero unexposed risk")
    if en == 0 or uc == 0:
        undefined.append("odds_ratio: denominator is zero")
    return {"exposed_risk": er, "unexposed_risk": ur,
            "risk_ratio": er / ur if er is not None and ur else None,
            "odds_ratio": ec * un / (en * uc) if en and uc else None,
            "risk_difference": er - ur if er is not None and ur is not None else None,
            "undefined_measures": undefined}


def weight_based_dose(dose_mg_per_kg, weight_kg):
    """Calculate total dose in mg from mg/kg and body weight in kg."""
    dose, weight = _science_finite_values(dose_mg_per_kg=dose_mg_per_kg,
                                           weight_kg=weight_kg).values()
    if dose < 0 or weight <= 0:
        raise ValueError("Dose must be non-negative and weight positive.")
    return dose * weight


def convert_mass_concentration(value, from_unit, to_unit):
    """Convert common mass concentrations among mg/L, g/L, mg/dL, and ug/mL."""
    value = float(value)
    if not math.isfinite(value) or value < 0:
        raise ValueError("Concentration must be finite and non-negative.")
    factors = {"mg/l": 1.0, "g/l": 1000.0, "mg/dl": 10.0, "ug/ml": 1.0}
    source, target = str(from_unit).strip().lower(), str(to_unit).strip().lower()
    if source not in factors or target not in factors:
        raise ValueError("Supported units: mg/L, g/L, mg/dL, and ug/mL.")
    return value * factors[source] / factors[target]


def glucose_mg_dl_to_mmol_l(value_mg_dl):
    """Convert glucose from mg/dL to mmol/L using molar mass 180.156 g/mol."""
    value = float(value_mg_dl)
    if not math.isfinite(value) or value < 0:
        raise ValueError("Glucose must be finite and non-negative.")
    return value / 18.0156


def glucose_mmol_l_to_mg_dl(value_mmol_l):
    """Convert glucose from mmol/L to mg/dL using molar mass 180.156 g/mol."""
    value = float(value_mmol_l)
    if not math.isfinite(value) or value < 0:
        raise ValueError("Glucose must be finite and non-negative.")
    return value * 18.0156


def cholesterol_mg_dl_to_mmol_l(value_mg_dl):
    """Convert cholesterol from mg/dL to mmol/L using molar mass 386.65 g/mol."""
    value = float(value_mg_dl)
    if not math.isfinite(value) or value < 0:
        raise ValueError("Cholesterol must be finite and non-negative.")
    return value / 38.665


def creatinine_mg_dl_to_umol_l(value_mg_dl):
    """Convert creatinine from mg/dL to umol/L using factor 88.4."""
    value = float(value_mg_dl)
    if not math.isfinite(value) or value < 0:
        raise ValueError("Creatinine must be finite and non-negative.")
    return value * 88.4


def heat_conduction_rate(conductivity_w_m_k, area_m2, temperature_difference_k, thickness_m):
    """Calculate steady one-dimensional conduction heat rate in watts."""
    k, area, delta_t, thickness = _science_finite_values(
        conductivity_w_m_k=conductivity_w_m_k, area_m2=area_m2,
        temperature_difference_k=temperature_difference_k, thickness_m=thickness_m).values()
    if min(k, area, thickness) <= 0:
        raise ValueError("Conductivity, area, and thickness must be positive.")
    return k * area * delta_t / thickness


def heat_convection_rate(heat_transfer_coefficient_w_m2_k, area_m2, surface_temp_k, fluid_temp_k):
    """Calculate convective heat transfer in watts using Newton's cooling law."""
    h, area, surface, fluid = _science_finite_values(
        heat_transfer_coefficient_w_m2_k=heat_transfer_coefficient_w_m2_k,
        area_m2=area_m2, surface_temp_k=surface_temp_k, fluid_temp_k=fluid_temp_k).values()
    if h < 0 or area < 0 or surface < 0 or fluid < 0:
        raise ValueError("h, area, and absolute temperatures must be non-negative.")
    return h * area * (surface - fluid)


def heat_radiation_rate(emissivity, area_m2, surface_temp_k, surroundings_temp_k):
    """Calculate net radiative heat transfer in watts (Stefan-Boltzmann law)."""
    e, area, surface, surrounding = _science_finite_values(
        emissivity=emissivity, area_m2=area_m2, surface_temp_k=surface_temp_k,
        surroundings_temp_k=surroundings_temp_k).values()
    if not 0 <= e <= 1 or area < 0 or surface < 0 or surrounding < 0:
        raise ValueError("Emissivity must be in [0,1]; area and temperatures non-negative.")
    return e * 5.670374419e-8 * area * (surface**4 - surrounding**4)


def carnot_efficiency(hot_temperature_k, cold_temperature_k):
    """Calculate ideal Carnot efficiency as a fraction from absolute temperatures."""
    hot, cold = _science_finite_values(hot_temperature_k=hot_temperature_k,
                                       cold_temperature_k=cold_temperature_k).values()
    if cold < 0 or hot <= 0 or hot < cold:
        raise ValueError("Require hot temperature >= cold temperature >= 0 K and hot > 0 K.")
    return 1 - cold / hot


def volumetric_thermal_expansion(initial_volume_m3, expansion_coefficient_per_k,
                                 temperature_change_k):
    """Calculate volume change using the linearized volumetric expansion model."""
    volume, coefficient, delta = _science_finite_values(
        initial_volume_m3=initial_volume_m3,
        expansion_coefficient_per_k=expansion_coefficient_per_k,
        temperature_change_k=temperature_change_k).values()
    if volume < 0 or coefficient < 0:
        raise ValueError("Initial volume and expansion coefficient must be non-negative.")
    return volume * coefficient * delta


def ohms_law(voltage_v=None, current_a=None, resistance_ohm=None):
    """Given two electrical values, return voltage (V), current (A), resistance (ohm), and power (W)."""
    supplied = {"voltage_v": voltage_v, "current_a": current_a,
                "resistance_ohm": resistance_ohm}
    if sum(value is not None for value in supplied.values()) != 2:
        raise ValueError("Provide exactly two of voltage_v, current_a, and resistance_ohm.")
    values = {k: float(v) for k, v in supplied.items() if v is not None}
    if any(not math.isfinite(v) for v in values.values()):
        raise ValueError("Electrical values must be finite.")
    if any(v < 0 for v in values.values()):
        raise ValueError("Electrical values must be non-negative.")
    if voltage_v is None:
        current, resistance = values["current_a"], values["resistance_ohm"]
        voltage = current * resistance
    elif current_a is None:
        voltage, resistance = values["voltage_v"], values["resistance_ohm"]
        if resistance == 0:
            raise ValueError("Cannot calculate current from zero resistance.")
        current = voltage / resistance
    else:
        voltage, current = values["voltage_v"], values["current_a"]
        if current == 0:
            raise ValueError("Cannot calculate resistance from zero current.")
        resistance = voltage / current
    return {"voltage_v": voltage, "current_a": current,
            "resistance_ohm": resistance, "power_w": voltage * current}


def rc_time_constant(resistance_ohm, capacitance_f):
    """Calculate RC circuit time constant in seconds."""
    resistance, capacitance = _science_finite_values(
        resistance_ohm=resistance_ohm, capacitance_f=capacitance_f).values()
    if resistance < 0 or capacitance < 0:
        raise ValueError("Resistance and capacitance must be non-negative.")
    return resistance * capacitance


def equivalent_resistance(resistances_ohm, connection="series"):
    """Calculate equivalent resistance for ideal series or parallel resistors."""
    values = [float(x) for x in resistances_ohm]
    if not values or any(not math.isfinite(x) or x <= 0 for x in values):
        raise ValueError("Provide positive finite resistor values.")
    mode = str(connection).strip().lower()
    if mode == "series":
        return sum(values)
    if mode == "parallel":
        return 1 / sum(1 / x for x in values)
    raise ValueError("connection must be 'series' or 'parallel'.")


def number_needed_to_treat(control_event_rate, treatment_event_rate):
    """Return NNT when treatment reduces the event rate."""
    control, treatment = _science_finite_values(control_event_rate=control_event_rate,
                                                  treatment_event_rate=treatment_event_rate).values()
    if not (0 <= control <= 1 and 0 <= treatment <= 1):
        raise ValueError("Event rates must be between 0 and 1.")
    reduction = control - treatment
    if reduction <= 0:
        raise ValueError("NNT requires a lower event rate with treatment.")
    return math.ceil(1 / reduction)


def drug_concentration_after_dose(initial_concentration, half_life_hours, elapsed_hours):
    """Estimate first-order concentration decay using a stated half-life."""
    initial, half_life, elapsed = _science_finite_values(
        initial_concentration=initial_concentration, half_life_hours=half_life_hours,
        elapsed_hours=elapsed_hours).values()
    if initial < 0 or half_life <= 0 or elapsed < 0:
        raise ValueError("Concentration/time must be non-negative and half-life positive.")
    return initial * 0.5 ** (elapsed / half_life)


def mean_arterial_pressure(systolic_mmhg, diastolic_mmhg):
    """Estimate mean arterial pressure as DBP + (SBP-DBP)/3, in mmHg."""
    systolic, diastolic = _science_finite_values(
        systolic_mmhg=systolic_mmhg, diastolic_mmhg=diastolic_mmhg).values()
    if diastolic < 0 or systolic < diastolic:
        raise ValueError("Require systolic pressure >= non-negative diastolic pressure.")
    return diastolic + (systolic - diastolic) / 3


def _validated_counts(counts):
    values = [float(x) for x in counts]
    if not values or any(not math.isfinite(x) or x < 0 for x in values):
        raise ValueError("counts must be a non-empty sequence of finite non-negative values.")
    return values


def shannon_diversity(counts, base=math.e):
    """Calculate Shannon diversity from non-negative taxon counts."""
    values, base = _validated_counts(counts), float(base)
    if not math.isfinite(base) or base <= 0 or base == 1:
        raise ValueError("base must be positive and not equal to 1.")
    total = sum(values)
    return 0.0 if total == 0 else -sum((x / total) * math.log(x / total, base) for x in values if x)


def simpson_diversity(counts):
    """Calculate Simpson diversity (1 - sum of squared relative abundances)."""
    values = _validated_counts(counts)
    total = sum(values)
    return 0.0 if total == 0 else 1 - sum((x / total) ** 2 for x in values)


def pielou_evenness(counts):
    """Calculate Pielou's evenness; returns zero for fewer than two taxa."""
    values = _validated_counts(counts)
    richness = sum(x > 0 for x in values)
    return 0.0 if richness <= 1 else shannon_diversity(values) / math.log(richness)


def logistic_population(initial_population, growth_rate, carrying_capacity, time):
    """Calculate population at time t under the logistic growth model."""
    n0, rate, capacity, elapsed = _science_finite_values(
        initial_population=initial_population, growth_rate=growth_rate,
        carrying_capacity=carrying_capacity, time=time).values()
    if n0 <= 0 or capacity <= 0 or n0 > capacity:
        raise ValueError("Population and carrying capacity must be positive; initial population <= capacity.")
    return capacity / (1 + ((capacity - n0) / n0) * math.exp(-rate * elapsed))


def reynolds_number(density_kg_m3, velocity_m_s, characteristic_length_m, dynamic_viscosity_pa_s):
    """Calculate dimensionless Reynolds number using SI inputs."""
    density, velocity, length, viscosity = _science_finite_values(
        density_kg_m3=density_kg_m3, velocity_m_s=velocity_m_s,
        characteristic_length_m=characteristic_length_m,
        dynamic_viscosity_pa_s=dynamic_viscosity_pa_s).values()
    if density <= 0 or length < 0 or viscosity <= 0:
        raise ValueError("Density/viscosity must be positive and length non-negative.")
    return density * abs(velocity) * length / viscosity


def control_natural_frequency(mass_kg, stiffness_n_m):
    """Calculate undamped natural angular frequency in rad/s."""
    mass, stiffness = _science_finite_values(mass_kg=mass_kg, stiffness_n_m=stiffness_n_m).values()
    if mass <= 0 or stiffness <= 0:
        raise ValueError("Mass and stiffness must be positive.")
    return math.sqrt(stiffness / mass)


def control_damping_ratio(mass_kg, damping_n_s_m, stiffness_n_m):
    """Calculate dimensionless damping ratio for a second-order system."""
    mass, damping, stiffness = _science_finite_values(
        mass_kg=mass_kg, damping_n_s_m=damping_n_s_m, stiffness_n_m=stiffness_n_m).values()
    if mass <= 0 or stiffness <= 0 or damping < 0:
        raise ValueError("Mass/stiffness must be positive and damping non-negative.")
    return damping / (2 * math.sqrt(mass * stiffness))


def cantilever_tip_deflection(point_load_n, length_m, youngs_modulus_pa, second_moment_m4):
    """Calculate end deflection for an end-loaded uniform cantilever (SI)."""
    load, length, modulus, inertia = _science_finite_values(
        point_load_n=point_load_n, length_m=length_m, youngs_modulus_pa=youngs_modulus_pa,
        second_moment_m4=second_moment_m4).values()
    if length < 0 or modulus <= 0 or inertia <= 0:
        raise ValueError("Length must be non-negative; modulus and inertia positive.")
    return load * length ** 3 / (3 * modulus * inertia)


def beam_bending_stress(moment_nm, second_moment_m4, distance_m):
    """Calculate elastic beam bending stress in pascals from SI inputs."""
    moment, inertia, distance = _science_finite_values(
        moment_nm=moment_nm, second_moment_m4=second_moment_m4,
        distance_m=distance_m).values()
    if inertia <= 0 or distance < 0:
        raise ValueError("Second moment must be positive and distance non-negative.")
    return abs(moment) * distance / inertia


def gsw_seawater_properties(practical_salinity, temperature_c, pressure_dbar=0, longitude=0, latitude=0):
    """Return TEOS-10 salinity, temperature, density, and sound speed using optional gsw."""
    gsw = load_scientific_package("gsw")
    sp, temp, pressure, lon, lat = _science_finite_values(
        practical_salinity=practical_salinity, temperature_c=temperature_c,
        pressure_dbar=pressure_dbar, longitude=longitude, latitude=latitude).values()
    if sp < 0 or pressure < 0 or not -90 <= lat <= 90:
        raise ValueError("Salinity/pressure must be non-negative and latitude in [-90, 90].")
    sa = gsw.SA_from_SP(sp, pressure, lon, lat)
    ct = gsw.CT_from_t(sa, temp, pressure)
    return {"absolute_salinity_g_kg": float(sa), "conservative_temperature_c": float(ct),
            "density_kg_m3": float(gsw.rho(sa, ct, pressure)),
            "sound_speed_m_s": float(gsw.sound_speed(sa, ct, pressure))}


def gsw_status():
    """Report whether the optional seawater package is available."""
    return _package_status("gsw")


def sklearn_train_test_split(features, targets, test_size=0.2, random_state=42, stratify=False):
    """Split data with scikit-learn; returns X_train, X_test, y_train, y_test."""
    load_scientific_package("scikit_learn")
    from sklearn.model_selection import train_test_split
    features, targets = _validate_sklearn_data(features, targets)
    _validate_test_size(test_size, len(targets))
    return train_test_split(
        features, targets, test_size=test_size, random_state=random_state,
        stratify=targets if stratify else None)


def sklearn_classification_report(y_true, y_pred):
    """Return scikit-learn classification metrics as a dictionary."""
    load_scientific_package("scikit_learn")
    from sklearn.metrics import classification_report
    if len(y_true) == 0 or len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same non-zero length.")
    return classification_report(y_true, y_pred, output_dict=True, zero_division=0)


def sklearn_linear_regression(features, targets, test_size=0.2, random_state=42):
    """Fit a linear regression model and return the model, predictions, RMSE, and R²."""
    load_scientific_package("scikit_learn")
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score
    from sklearn.model_selection import train_test_split
    features, targets = _validate_sklearn_data(features, targets)
    _validate_test_size(test_size, len(targets))
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=test_size, random_state=random_state)
    model = LinearRegression().fit(x_train, y_train)
    predictions = model.predict(x_test)
    mse = mean_squared_error(y_test, predictions)
    return {"model": model, "predictions": predictions, "rmse": math.sqrt(float(mse)),
            "r2": float(r2_score(y_test, predictions))}


def scikit_learn_status():
    """Report whether optional scikit-learn is available."""
    return _package_status("scikit_learn")


def _validate_sklearn_data(features, targets):
    """Use sklearn's own array checks to enforce aligned finite numeric data."""
    from sklearn.utils.validation import check_X_y
    try:
        x, y = check_X_y(features, targets, dtype="numeric")
    except Exception as exc:
        raise ValueError(f"features/targets must be aligned finite numeric data: {exc}") from exc
    return x, y


def _validate_test_size(test_size, sample_count):
    if isinstance(test_size, bool) or not isinstance(test_size, (int, float)):
        raise ValueError("test_size must be a fraction in (0, 1) or an integer sample count.")
    if isinstance(test_size, float):
        if not math.isfinite(test_size) or not 0 < test_size < 1:
            raise ValueError("Fractional test_size must be in (0, 1).")
        test_count = math.ceil(test_size * sample_count)
    else:
        test_count = test_size
    if test_count < 1 or test_count >= sample_count:
        raise ValueError("test_size must leave at least one training and one test sample.")


def sklearn_logistic_classification(features, targets, test_size=0.2, random_state=42):
    """Fit logistic classification and return model, predictions, accuracy and report."""
    load_scientific_package("scikit_learn")
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    features, targets = _validate_sklearn_data(features, targets)
    _validate_test_size(test_size, len(targets))
    if len(set(targets.tolist())) < 2:
        raise ValueError("Logistic classification requires at least two target classes.")
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=test_size, random_state=random_state, stratify=targets)
    model = LogisticRegression(max_iter=1000).fit(x_train, y_train)
    predictions = model.predict(x_test)
    return {"model": model, "predictions": predictions,
            "accuracy": float(accuracy_score(y_test, predictions)),
            "report": sklearn_classification_report(y_test, predictions)}


def _gsw_selftest_probe():
    """Check that optional GSW calls return physically plausible seawater values."""
    result = gsw_seawater_properties(35, 15, 0, -40, 30)
    assert 30 < result["absolute_salinity_g_kg"] < 40
    assert 1000 < result["density_kg_m3"] < 1100
    assert 1000 < result["sound_speed_m_s"] < 2000
    return result


def _sklearn_selftest_probe():
    """Exercise optional classification, splitting, and regression end to end."""
    features = [[float(i)] for i in range(20)]
    labels = [0 if i < 10 else 1 for i in range(20)]
    x_train, x_test, y_train, y_test = sklearn_train_test_split(
        features, labels, test_size=0.25, random_state=7, stratify=True)
    assert len(x_train) == 15 and len(x_test) == len(y_test) == 5
    report = sklearn_classification_report([0, 1], [0, 1])
    assert report["accuracy"] == 1.0
    classifier = sklearn_logistic_classification(features, labels, test_size=0.25, random_state=7)
    assert 0 <= classifier["accuracy"] <= 1
    regression = sklearn_linear_regression(features, [3 * i + 2 for i in range(20)],
                                           test_size=0.25, random_state=7)
    assert regression["rmse"] < 1e-8 and regression["r2"] > 0.999
    return {"split": len(x_test), "classification_accuracy": classifier["accuracy"],
            "regression_r2": regression["r2"]}


# ==========================================================
# ADDITIONAL APPLIED SCIENCE CALCULATORS
# ==========================================================

def michaelis_menten_velocity(vmax, substrate_concentration, km):
    """Calculate enzyme velocity Vmax*[S]/(Km+[S]) in the input velocity units."""
    vmax, substrate, km = _science_finite_values(
        vmax=vmax, substrate_concentration=substrate_concentration, km=km).values()
    if vmax < 0 or substrate < 0 or km <= 0:
        raise ValueError("Vmax and substrate must be non-negative; Km must be positive.")
    return vmax * substrate / (km + substrate)


def henderson_hasselbalch(pka, base_concentration, acid_concentration):
    """Calculate buffer pH from pKa and conjugate base/acid concentrations."""
    pka, base, acid = _science_finite_values(
        pka=pka, base_concentration=base_concentration,
        acid_concentration=acid_concentration).values()
    if base <= 0 or acid <= 0:
        raise ValueError("Base and acid concentrations must be positive.")
    return pka + math.log10(base / acid)


def beer_lambert_absorbance(molar_absorptivity_l_mol_cm, concentration_mol_l,
                            path_length_cm):
    """Calculate absorbance A = epsilon*c*l using L mol⁻¹ cm⁻¹, mol/L, and cm."""
    epsilon, concentration, length = _science_finite_values(
        molar_absorptivity_l_mol_cm=molar_absorptivity_l_mol_cm,
        concentration_mol_l=concentration_mol_l, path_length_cm=path_length_cm).values()
    if min(epsilon, concentration, length) < 0:
        raise ValueError("Absorptivity, concentration, and path length must be non-negative.")
    return epsilon * concentration * length


def osmotic_pressure_kpa(molarity_mol_l, temperature_k, vanthoff_factor=1):
    """Estimate ideal osmotic pressure in kPa (molarity mol/L, temperature K)."""
    molarity, temperature, factor = _science_finite_values(
        molarity_mol_l=molarity_mol_l, temperature_k=temperature_k,
        vanthoff_factor=vanthoff_factor).values()
    if molarity < 0 or temperature <= 0 or factor <= 0:
        raise ValueError("Molarity must be non-negative; temperature and factor positive.")
    return factor * molarity * 8.31446261815324 * temperature


def magnus_relative_humidity(temperature_c, dewpoint_c):
    """Estimate relative humidity (%) with the Magnus saturation-vapor-pressure formula."""
    temperature, dewpoint = _science_finite_values(
        temperature_c=temperature_c, dewpoint_c=dewpoint_c).values()
    if temperature <= -243.5 or dewpoint <= -243.5:
        raise ValueError("Magnus equation temperatures must be above -243.5 C.")
    es_t = math.exp(17.67 * temperature / (temperature + 243.5))
    es_d = math.exp(17.67 * dewpoint / (dewpoint + 243.5))
    return 100 * es_d / es_t


def magnus_dewpoint_c(temperature_c, relative_humidity_percent):
    """Estimate dew point in Celsius with the Magnus formula and RH in (0, 100]."""
    temperature, rh = _science_finite_values(
        temperature_c=temperature_c,
        relative_humidity_percent=relative_humidity_percent).values()
    if temperature <= -243.5 or not 0 < rh <= 100:
        raise ValueError("Temperature must exceed -243.5 C and RH be in (0, 100].")
    gamma = math.log(rh / 100) + 17.67 * temperature / (243.5 + temperature)
    return 243.5 * gamma / (17.67 - gamma)


def isa_pressure_altitude_pa(altitude_m):
    """Estimate standard-atmosphere pressure in Pa from altitude in the troposphere."""
    altitude, = _science_finite_values(altitude_m=altitude_m).values()
    if not -500 <= altitude <= 11000:
        raise ValueError("This troposphere approximation supports altitudes from -500 to 11000 m.")
    return 101325 * (1 - 2.25577e-5 * altitude) ** 5.25588


def hydrostatic_pressure_kpa(fluid_density_kg_m3, depth_m, gravity_m_s2=9.80665):
    """Calculate gauge hydrostatic pressure in kPa from density, depth, and gravity."""
    density, depth, gravity = _science_finite_values(
        fluid_density_kg_m3=fluid_density_kg_m3, depth_m=depth_m,
        gravity_m_s2=gravity_m_s2).values()
    if density <= 0 or depth < 0 or gravity <= 0:
        raise ValueError("Density/gravity must be positive and depth non-negative.")
    return density * gravity * depth / 1000


def geothermal_temperature_c(surface_temperature_c, geothermal_gradient_c_per_km,
                             depth_m):
    """Estimate subsurface temperature using a constant geothermal gradient."""
    surface, gradient, depth = _science_finite_values(
        surface_temperature_c=surface_temperature_c,
        geothermal_gradient_c_per_km=geothermal_gradient_c_per_km,
        depth_m=depth_m).values()
    if depth < 0:
        raise ValueError("Depth must be non-negative.")
    return surface + gradient * depth / 1000


def signal_rms(samples):
    """Calculate root-mean-square amplitude of a non-empty finite sample sequence."""
    values = [float(x) for x in samples]
    if not values or any(not math.isfinite(x) for x in values):
        raise ValueError("samples must be a non-empty sequence of finite values.")
    return math.sqrt(sum(x * x for x in values) / len(values))


def signal_peak_to_peak(samples):
    """Return the peak-to-peak range of a non-empty finite sample sequence."""
    values = [float(x) for x in samples]
    if not values or any(not math.isfinite(x) for x in values):
        raise ValueError("samples must be a non-empty sequence of finite values.")
    return max(values) - min(values)


def signal_snr_db(signal_samples, noise_samples):
    """Calculate signal-to-noise ratio in dB from signal and noise sample sequences."""
    signal = signal_rms([float(x) for x in signal_samples])
    noise = signal_rms([float(x) for x in noise_samples])
    if signal <= 0 or noise <= 0:
        raise ValueError("Signal and noise RMS must both be positive.")
    return 20 * math.log10(signal / noise)


def zero_crossing_rate(samples):
    """Return the fraction of adjacent sample pairs that cross or touch zero."""
    values = [float(x) for x in samples]
    if len(values) < 2 or any(not math.isfinite(x) for x in values):
        raise ValueError("Provide at least two finite samples.")
    crossings = sum((left >= 0) != (right >= 0)
                    for left, right in zip(values, values[1:]))
    return crossings / (len(values) - 1)


def sample_rate_hz(sample_count, duration_s):
    """Calculate sample rate in Hz from sample count and elapsed seconds."""
    count, duration = _science_finite_values(
        sample_count=sample_count, duration_s=duration_s).values()
    if count <= 0 or duration <= 0 or not count.is_integer():
        raise ValueError("Sample count must be a positive integer and duration positive.")
    return count / duration


def sound_intensity_level_db(intensity_w_m2, reference_w_m2=1e-12):
    """Calculate sound intensity level in dB relative to a positive reference intensity."""
    intensity, reference = _science_finite_values(
        intensity_w_m2=intensity_w_m2, reference_w_m2=reference_w_m2).values()
    if intensity <= 0 or reference <= 0:
        raise ValueError("Intensity and reference intensity must be positive.")
    return 10 * math.log10(intensity / reference)


def sound_intensity_from_db(level_db, reference_w_m2=1e-12):
    """Convert dB intensity level and reference intensity to W/m²."""
    level, reference = _science_finite_values(
        level_db=level_db, reference_w_m2=reference_w_m2).values()
    if reference <= 0:
        raise ValueError("Reference intensity must be positive.")
    return reference * 10 ** (level / 10)


def capacitor_energy_j(capacitance_f, voltage_v):
    """Calculate stored capacitor energy in joules (C in farads, V in volts)."""
    capacitance, voltage = _science_finite_values(
        capacitance_f=capacitance_f, voltage_v=voltage_v).values()
    if capacitance < 0:
        raise ValueError("Capacitance must be non-negative.")
    return 0.5 * capacitance * voltage ** 2


def inductor_energy_j(inductance_h, current_a):
    """Calculate stored inductor energy in joules (L in henries, I in amperes)."""
    inductance, current = _science_finite_values(
        inductance_h=inductance_h, current_a=current_a).values()
    if inductance < 0:
        raise ValueError("Inductance must be non-negative.")
    return 0.5 * inductance * current ** 2


def capacitive_reactance_ohm(frequency_hz, capacitance_f):
    """Calculate capacitive reactance magnitude in ohms."""
    frequency, capacitance = _science_finite_values(
        frequency_hz=frequency_hz, capacitance_f=capacitance_f).values()
    if frequency <= 0 or capacitance <= 0:
        raise ValueError("Frequency and capacitance must be positive.")
    return 1 / (2 * math.pi * frequency * capacitance)


def inductive_reactance_ohm(frequency_hz, inductance_h):
    """Calculate inductive reactance magnitude in ohms."""
    frequency, inductance = _science_finite_values(
        frequency_hz=frequency_hz, inductance_h=inductance_h).values()
    if frequency <= 0 or inductance <= 0:
        raise ValueError("Frequency and inductance must be positive.")
    return 2 * math.pi * frequency * inductance


def thermal_diffusivity_m2_s(conductivity_w_m_k, density_kg_m3,
                             specific_heat_j_kg_k):
    """Calculate thermal diffusivity alpha = k/(rho*cp) in m²/s."""
    conductivity, density, specific_heat = _science_finite_values(
        conductivity_w_m_k=conductivity_w_m_k, density_kg_m3=density_kg_m3,
        specific_heat_j_kg_k=specific_heat_j_kg_k).values()
    if conductivity <= 0 or density <= 0 or specific_heat <= 0:
        raise ValueError("Conductivity, density, and specific heat must be positive.")
    return conductivity / (density * specific_heat)


def cohens_d(group_a, group_b):
    """Calculate pooled-standard-deviation Cohen's d for two numeric samples."""
    a, b = [float(x) for x in group_a], [float(x) for x in group_b]
    if min(len(a), len(b)) < 2 or any(not math.isfinite(x) for x in a + b):
        raise ValueError("Each group needs at least two finite observations.")
    va = sum((x - sum(a) / len(a)) ** 2 for x in a) / (len(a) - 1)
    vb = sum((x - sum(b) / len(b)) ** 2 for x in b) / (len(b) - 1)
    pooled = math.sqrt(((len(a) - 1) * va + (len(b) - 1) * vb) /
                       (len(a) + len(b) - 2))
    if pooled == 0:
        raise ValueError("Cohen's d is undefined when pooled standard deviation is zero.")
    return (sum(a) / len(a) - sum(b) / len(b)) / pooled


def standard_error_of_mean(samples):
    """Calculate sample standard error of the mean for at least two observations."""
    values = [float(x) for x in samples]
    if len(values) < 2 or any(not math.isfinite(x) for x in values):
        raise ValueError("Provide at least two finite observations.")
    mean = sum(values) / len(values)
    sd = math.sqrt(sum((x - mean) ** 2 for x in values) / (len(values) - 1))
    return sd / math.sqrt(len(values))



def acoustic_sound_pressure_level_db(rms_pressure_pa, reference_pressure_pa=20e-6):
    """Calculate sound pressure level in dB re a positive reference pressure."""
    pressure, reference = _science_finite_values(
        rms_pressure_pa=rms_pressure_pa,
        reference_pressure_pa=reference_pressure_pa).values()
    if pressure <= 0 or reference <= 0:
        raise ValueError("RMS and reference pressures must be positive.")
    return 20 * math.log10(pressure / reference)


def acoustic_pressure_from_spl_pa(level_db, reference_pressure_pa=20e-6):
    """Convert sound pressure level in dB to RMS pressure in pascals."""
    level, reference = _science_finite_values(
        level_db=level_db, reference_pressure_pa=reference_pressure_pa).values()
    if reference <= 0:
        raise ValueError("Reference pressure must be positive.")
    return reference * 10 ** (level / 20)


def doppler_frequency_hz(source_frequency_hz, sound_speed_m_s,
                         source_toward_observer_m_s=0,
                         observer_toward_source_m_s=0):
    """Classical Doppler frequency; positive velocities mean motion toward the other."""
    frequency, speed, source_v, observer_v = _science_finite_values(
        source_frequency_hz=source_frequency_hz, sound_speed_m_s=sound_speed_m_s,
        source_toward_observer_m_s=source_toward_observer_m_s,
        observer_toward_source_m_s=observer_toward_source_m_s).values()
    if frequency <= 0 or speed <= 0 or speed <= source_v or speed + observer_v <= 0:
        raise ValueError("Frequency and sound speed must be positive and velocities physical.")
    return frequency * (speed + observer_v) / (speed - source_v)


def microbial_population(initial_count, growth_rate_per_h, elapsed_h):
    """Project population by continuous exponential growth (rate per hour)."""
    initial, rate, elapsed = _science_finite_values(
        initial_count=initial_count, growth_rate_per_h=growth_rate_per_h,
        elapsed_h=elapsed_h).values()
    if initial < 0 or elapsed < 0:
        raise ValueError("Initial count and elapsed time must be non-negative.")
    return initial * math.exp(rate * elapsed)


def microbial_doubling_time_h(growth_rate_per_h):
    """Calculate population doubling time from continuous growth rate per hour."""
    rate = _science_finite_values(growth_rate_per_h=growth_rate_per_h)["growth_rate_per_h"]
    if rate <= 0:
        raise ValueError("Growth rate must be positive.")
    return math.log(2) / rate


def microbial_log_reduction(start_count, end_count):
    """Calculate log10 reduction from starting to ending viable counts."""
    start, end = _science_finite_values(
        start_count=start_count, end_count=end_count).values()
    if start <= 0 or end <= 0 or end > start:
        raise ValueError("Counts must be positive and ending count cannot exceed starting count.")
    return math.log10(start / end)


def pharmacokinetic_loading_dose_mg(target_concentration_mg_l,
                                    volume_distribution_l, bioavailability=1.0):
    """Estimate one-compartment loading amount from target concentration and Vd."""
    target, volume, bio = _science_finite_values(
        target_concentration_mg_l=target_concentration_mg_l,
        volume_distribution_l=volume_distribution_l,
        bioavailability=bioavailability).values()
    if target < 0 or volume <= 0 or not 0 < bio <= 1:
        raise ValueError("Target must be non-negative, volume positive, and bioavailability in (0, 1].")
    return target * volume / bio


def pharmacokinetic_maintenance_rate_mg_h(clearance_l_h,
                                           target_concentration_mg_l,
                                           bioavailability=1.0):
    """Estimate maintenance input rate for target concentration (mg/hour)."""
    clearance, target, bio = _science_finite_values(
        clearance_l_h=clearance_l_h, target_concentration_mg_l=target_concentration_mg_l,
        bioavailability=bioavailability).values()
    if clearance < 0 or target < 0 or not 0 < bio <= 1:
        raise ValueError("Clearance and target must be non-negative; bioavailability in (0, 1].")
    return clearance * target / bio


def pharmacokinetic_half_life_h(volume_distribution_l, clearance_l_h):
    """Calculate one-compartment elimination half-life from Vd and clearance."""
    volume, clearance = _science_finite_values(
        volume_distribution_l=volume_distribution_l, clearance_l_h=clearance_l_h).values()
    if volume <= 0 or clearance <= 0:
        raise ValueError("Volume of distribution and clearance must be positive.")
    return math.log(2) * volume / clearance


def seawater_density_kg_m3(temperature_c, salinity_psu):
    """Approximate seawater density at 1 atm using UNESCO 1983 EOS-80."""
    t, s = _science_finite_values(
        temperature_c=temperature_c, salinity_psu=salinity_psu).values()
    if not 0 <= t <= 40 or not 0 <= s <= 42:
        raise ValueError("EOS-80 approximation requires temperature 0–40 °C and salinity 0–42 PSU.")
    rho_w = (999.842594 + 6.793952e-2*t - 9.095290e-3*t**2
             + 1.001685e-4*t**3 - 1.120083e-6*t**4 + 6.536332e-9*t**5)
    a = (0.824493 - 4.0899e-3*t + 7.6438e-5*t**2
         - 8.2467e-7*t**3 + 5.3875e-9*t**4)
    b = -5.72466e-3 + 1.0227e-4*t - 1.6546e-6*t**2
    return rho_w + a*s + b*s**1.5 + 4.8314e-4*s**2


def ocean_depth_from_gauge_pressure_m(pressure_kpa, density_kg_m3=1025,
                                      gravity_m_s2=9.80665):
    """Estimate depth from gauge pressure with constant density and gravity."""
    pressure, density, gravity = _science_finite_values(
        pressure_kpa=pressure_kpa, density_kg_m3=density_kg_m3,
        gravity_m_s2=gravity_m_s2).values()
    if pressure < 0 or density <= 0 or gravity <= 0:
        raise ValueError("Gauge pressure must be non-negative; density and gravity positive.")
    return pressure * 1000 / (density * gravity)

# ==========================================================
# ADDITIONAL SCIENCE AREAS AND WIKIPEDIA SEARCH
# ==========================================================

def hargreaves_samani_et0_mm_day(tmax_c, tmin_c, tmean_c, ra_mj_m2_day):
    """Estimate reference evapotranspiration (mm/day) by Hargreaves-Samani."""
    tmax, tmin, tmean, ra = _science_finite_values(
        tmax_c=tmax_c, tmin_c=tmin_c, tmean_c=tmean_c,
        ra_mj_m2_day=ra_mj_m2_day).values()
    if tmax < tmin or ra < 0:
        raise ValueError("Require Tmax >= Tmin and non-negative extraterrestrial radiation.")
    return max(0.0, 0.0023 * (tmean + 17.8) * math.sqrt(tmax - tmin) * ra)


def soil_porosity_fraction(bulk_density_kg_m3, particle_density_kg_m3=2650):
    """Estimate soil porosity as 1 - bulk density / particle density."""
    bulk, particle = _science_finite_values(
        bulk_density_kg_m3=bulk_density_kg_m3,
        particle_density_kg_m3=particle_density_kg_m3).values()
    if bulk < 0 or particle <= 0 or bulk > particle:
        raise ValueError("Require 0 <= bulk density <= positive particle density.")
    return 1 - bulk / particle


def soil_water_content_fraction(water_volume_m3, soil_volume_m3):
    """Calculate volumetric soil-water content as water volume / soil volume."""
    water, soil = _science_finite_values(
        water_volume_m3=water_volume_m3, soil_volume_m3=soil_volume_m3).values()
    if water < 0 or soil <= 0 or water > soil:
        raise ValueError("Require 0 <= water volume <= positive soil volume.")
    return water / soil


def food_moisture_percent(wet_sample_mass_g, dry_matter_mass_g, basis="wet"):
    """Calculate food moisture percentage on wet or dry basis."""
    wet, dry = _science_finite_values(
        wet_sample_mass_g=wet_sample_mass_g,
        dry_matter_mass_g=dry_matter_mass_g).values()
    if wet <= 0 or dry < 0 or dry > wet:
        raise ValueError("Require wet mass > 0 and 0 <= dry matter <= wet mass.")
    water = wet - dry
    basis = str(basis).strip().lower()
    if basis == "wet":
        return 100 * water / wet
    if basis == "dry":
        if dry == 0:
            raise ValueError("Dry-basis moisture is undefined when dry matter is zero.")
        return 100 * water / dry
    raise ValueError("basis must be 'wet' or 'dry'.")


def water_activity_from_equilibrium_rh(relative_humidity_percent):
    """Estimate water activity as equilibrium relative humidity / 100."""
    rh, = _science_finite_values(
        relative_humidity_percent=relative_humidity_percent).values()
    if not 0 <= rh <= 100:
        raise ValueError("Relative humidity must be between 0 and 100 percent.")
    return rh / 100


def diagnostic_test_metrics(true_positive, false_positive, true_negative, false_negative):
    """Return sensitivity, specificity, PPV, NPV, accuracy, and undefined-measure notes."""
    values = _science_finite_values(true_positive=true_positive,
        false_positive=false_positive, true_negative=true_negative,
        false_negative=false_negative)
    if any(v < 0 for v in values.values()):
        raise ValueError("Confusion-matrix counts must be non-negative.")
    tp, fp, tn, fn = values.values()
    def ratio(numerator, denominator):
        return numerator / denominator if denominator else None
    undefined = []
    formulas = {
        "sensitivity": (tp, tp + fn), "specificity": (tn, tn + fp),
        "positive_predictive_value": (tp, tp + fp),
        "negative_predictive_value": (tn, tn + fn),
        "accuracy": (tp + tn, tp + fp + tn + fn),
    }
    result = {}
    for name, (num, den) in formulas.items():
        result[name] = ratio(num, den)
        if den == 0:
            undefined.append(f"{name}: denominator is zero")
    result["undefined_measures"] = undefined
    return result


def co2_from_oxidized_carbon_kg(carbon_mass_kg, oxidation_fraction=1.0):
    """Estimate direct CO2 mass from oxidized elemental carbon mass (44/12 ratio)."""
    carbon, oxidation = _science_finite_values(
        carbon_mass_kg=carbon_mass_kg,
        oxidation_fraction=oxidation_fraction).values()
    if carbon < 0 or not 0 <= oxidation <= 1:
        raise ValueError("Carbon mass must be non-negative and oxidation fraction in [0,1].")
    return carbon * oxidation * (44 / 12)


def seismic_energy_j(moment_magnitude):
    """Estimate earthquake radiated energy in joules from magnitude (empirical relation)."""
    magnitude, = _science_finite_values(moment_magnitude=moment_magnitude).values()
    return 10 ** (1.5 * magnitude + 4.8)


def photon_energy_j(wavelength_m):
    """Calculate photon energy in joules from vacuum wavelength in meters."""
    wavelength, = _science_finite_values(wavelength_m=wavelength_m).values()
    if wavelength <= 0:
        raise ValueError("Wavelength must be positive.")
    return 6.62607015e-34 * 299792458 / wavelength


def snell_refracted_angle_deg(n_incident, n_transmitted, incident_angle_deg):
    """Calculate refracted angle from Snell's law; raises on total internal reflection."""
    n1, n2, angle = _science_finite_values(
        n_incident=n_incident, n_transmitted=n_transmitted,
        incident_angle_deg=incident_angle_deg).values()
    if n1 <= 0 or n2 <= 0 or not 0 <= angle < 90:
        raise ValueError("Indices must be positive and incidence angle in [0, 90) degrees.")
    sine_out = n1 * math.sin(math.radians(angle)) / n2
    if sine_out > 1:
        raise ValueError("Total internal reflection: no real refracted angle.")
    return math.degrees(math.asin(sine_out))


def thin_lens_image_distance_m(focal_length_m, object_distance_m):
    """Calculate signed image distance for a thin lens using the Cartesian lens equation."""
    focal, obj = _science_finite_values(
        focal_length_m=focal_length_m,
        object_distance_m=object_distance_m).values()
    if focal == 0 or obj == 0:
        raise ValueError("Focal length and object distance must be non-zero.")
    denominator = 1 / focal - 1 / obj
    if denominator == 0:
        raise ValueError("Image is at infinity for this focal/object-distance combination.")
    return 1 / denominator


def stress_from_force_pa(force_n, area_m2):
    """Calculate normal stress in pascals from force in N and area in m²."""
    force, area = _science_finite_values(force_n=force_n, area_m2=area_m2).values()
    if area <= 0:
        raise ValueError("Area must be positive.")
    return force / area


def engineering_strain(initial_length_m, final_length_m):
    """Calculate engineering strain (final - initial) / initial."""
    initial, final = _science_finite_values(
        initial_length_m=initial_length_m,
        final_length_m=final_length_m).values()
    if initial <= 0 or final < 0:
        raise ValueError("Initial length must be positive and final length non-negative.")
    return (final - initial) / initial


def factor_of_safety(strength_pa, working_stress_pa):
    """Calculate factor of safety as material strength / absolute working stress."""
    strength, stress = _science_finite_values(
        strength_pa=strength_pa, working_stress_pa=working_stress_pa).values()
    if strength <= 0 or stress == 0:
        raise ValueError("Strength must be positive and working stress non-zero.")
    return strength / abs(stress)


def sensible_heat_j(mass_kg, specific_heat_j_kg_k, temperature_change_k):
    """Calculate sensible heat Q = m cp delta-T in joules."""
    mass, heat_capacity, delta = _science_finite_values(
        mass_kg=mass_kg, specific_heat_j_kg_k=specific_heat_j_kg_k,
        temperature_change_k=temperature_change_k).values()
    if mass < 0 or heat_capacity < 0:
        raise ValueError("Mass and specific heat must be non-negative.")
    return mass * heat_capacity * delta


def latent_heat_j(mass_kg, latent_heat_j_kg):
    """Calculate phase-change heat in joules from mass and specific latent heat."""
    mass, latent = _science_finite_values(
        mass_kg=mass_kg, latent_heat_j_kg=latent_heat_j_kg).values()
    if mass < 0 or latent < 0:
        raise ValueError("Mass and latent heat must be non-negative.")
    return mass * latent


def nernst_potential_v(standard_potential_v, temperature_k, electrons_transferred,
                       reaction_quotient):
    """Calculate Nernst potential in volts (dimensionless reaction quotient)."""
    e0, temperature, electrons, quotient = _science_finite_values(
        standard_potential_v=standard_potential_v, temperature_k=temperature_k,
        electrons_transferred=electrons_transferred,
        reaction_quotient=reaction_quotient).values()
    if temperature <= 0 or electrons <= 0 or quotient <= 0:
        raise ValueError("Temperature, electron count, and reaction quotient must be positive.")
    return e0 - (8.31446261815324 * temperature / (electrons * 96485.33212)) * math.log(quotient)


def solution_dilution_molarity(stock_molarity, stock_volume_l, final_volume_l):
    """Calculate diluted concentration in mol/L using C1*V1=C2*V2."""
    stock, aliquot, final = _science_finite_values(
        stock_molarity=stock_molarity, stock_volume_l=stock_volume_l,
        final_volume_l=final_volume_l).values()
    if stock < 0 or aliquot < 0 or final <= 0 or aliquot > final:
        raise ValueError("Require non-negative stock and aliquot, positive final volume, and aliquot <= final volume.")
    return stock * aliquot / final


def percent_yield(actual_yield, theoretical_yield):
    """Calculate percent chemical yield from consistent actual/theoretical units."""
    actual, theoretical = _science_finite_values(
        actual_yield=actual_yield,
        theoretical_yield=theoretical_yield).values()
    if actual < 0 or theoretical <= 0:
        raise ValueError("Actual yield must be non-negative and theoretical yield positive.")
    return 100 * actual / theoretical


def gini_coefficient(values):
    """Calculate the Gini coefficient for a non-negative numeric sample."""
    data = sorted(float(x) for x in values)
    if not data or any(not math.isfinite(x) or x < 0 for x in data):
        raise ValueError("Provide a non-empty sequence of finite non-negative values.")
    total = sum(data)
    if total == 0:
        return 0.0
    n = len(data)
    return (2 * sum((i + 1) * x for i, x in enumerate(data)) / (n * total)
            - (n + 1) / n)


def population_exponential_projection(initial_population, growth_rate_per_time,
                                      elapsed_time):
    """Project population under continuous exponential growth/decline."""
    initial, rate, elapsed = _science_finite_values(
        initial_population=initial_population,
        growth_rate_per_time=growth_rate_per_time,
        elapsed_time=elapsed_time).values()
    if initial < 0 or elapsed < 0:
        raise ValueError("Initial population and elapsed time must be non-negative.")
    return initial * math.exp(rate * elapsed)


def wikipedia_status():
    """Report whether the requests-backed MediaWiki API client is available."""
    try:
        import requests
    except ImportError:
        return {"available": False, "version": None,
                "error": "Install requests with python -m pip install requests",
                "network_checked": False}
    return {"available": True, "version": requests.__version__,
            "network_checked": False}


def _wikipedia_call(language, operation):
    """Call an operation with a language-bound MediaWiki API requester."""
    import os
    import re
    import threading

    try:
        import requests
    except ImportError as exc:
        raise RuntimeError(
            "Wikipedia features require requests. Install it with "
            "python -m pip install requests."
        ) from exc

    language_aliases = {
        "english": "en", "spanish": "es", "japanese": "ja",
        "mandarin": "zh", "chinese": "zh", "french": "fr",
        "中文": "zh", "日本語": "ja", "español": "es", "français": "fr",
    }
    selected = str(language or globals().get("language", "en")).strip().lower()
    selected = language_aliases.get(selected, selected)
    if not re.fullmatch(r"[a-z][a-z0-9-]{1,11}", selected):
        raise ValueError("language must be a valid Wikipedia language code.")

    user_agent = os.environ.get("DAVE_WIKIPEDIA_USER_AGENT", "").strip()
    if not user_agent:
        user_agent = "DaveScientificCalculator/1.0 (https://github.com/rachburgess/Dave)"
    session = requests.Session()
    session.headers.update({"User-Agent": user_agent})

    def request(params):
        query = dict(params)
        query.update({"format": "json", "formatversion": "2", "utf8": "1"})
        endpoint = f"https://{selected}.wikipedia.org/w/api.php"
        try:
            response = session.get(endpoint, params=query, timeout=(5, 25))
            response.raise_for_status()
            payload = response.json()
        except requests.exceptions.RequestException as exc:
            raise RuntimeError(f"MediaWiki API request failed: {exc}") from exc
        except ValueError as exc:
            raise RuntimeError("MediaWiki returned a malformed JSON response.") from exc
        if not isinstance(payload, dict):
            raise RuntimeError("MediaWiki returned an unexpected JSON response.")
        if "error" in payload:
            error = payload["error"]
            raise RuntimeError(
                f"MediaWiki API error {error.get('code', '')}: "
                f"{error.get('info', error)}"
            )
        return payload

    lock = getattr(_wikipedia_call, "_dave_request_lock", None)
    if lock is None:
        lock = threading.RLock()
        _wikipedia_call._dave_request_lock = lock
    try:
        with lock:
            return operation(request)
    finally:
        session.close()

def _wikipedia_page_from_response(data):
    """Return the first page in a query response or a clear missing-page result."""
    pages = data.get("query", {}).get("pages", [])
    if not pages or "missing" in pages[0]:
        return {"error": "page_not_found", "message": "Wikipedia page was not found."}
    return pages[0]


def wikipedia_search(query, results=5, language=None):
    """Search Wikipedia and return matching article titles (requires requests and internet access)."""
    query = str(query).strip()
    if not query:
        raise ValueError("query must not be empty.")
    if isinstance(results, bool) or not isinstance(results, int) or not 1 <= results <= 20:
        raise ValueError("results must be an integer from 1 to 20.")
    def search(request):
        data = request({"action": "query", "list": "search", "srsearch": query,
                        "srlimit": results})
        return [item["title"] for item in data.get("query", {}).get("search", [])]
    return _wikipedia_call(language, search)


def wikipedia_summary(query, sentences=3, language=None):
    """Fetch a short Wikipedia article summary (requires requests and internet access)."""
    query = str(query).strip()
    if not query:
        raise ValueError("query must not be empty.")
    if isinstance(sentences, bool) or not isinstance(sentences, int) or not 1 <= sentences <= 10:
        raise ValueError("sentences must be an integer from 1 to 10.")
    def summary(request):
        data = request({"action": "query", "prop": "extracts", "titles": query,
                        "redirects": "1", "exintro": "1", "explaintext": "1",
                        "exsentences": sentences})
        page = _wikipedia_page_from_response(data)
        return page if "error" in page else page.get("extract", "")
    return _wikipedia_call(language, summary)


def wikipedia_page_info(title, language=None, include_content=False):
    """Return Wikipedia page title, URL, id and summary; optionally include full text."""
    title = str(title).strip()
    if not title:
        raise ValueError("title must not be empty.")
    if not isinstance(include_content, bool):
        raise ValueError("include_content must be True or False.")
    def fetch(request):
        params = {"action": "query", "prop": "info|extracts", "titles": title,
                  "redirects": "1", "inprop": "url", "explaintext": "1"}
        if include_content:
            params["exsectionformat"] = "wiki"
        else:
            params.update({"exintro": "1", "exsentences": "3"})
        page = _wikipedia_page_from_response(request(params))
        if "error" in page:
            return page
        result = {"title": page.get("title", title), "url": page.get("fullurl", ""),
                  "pageid": page.get("pageid"), "summary": page.get("extract", "")}
        if include_content:
            result["content"] = page.get("extract", "")
        return result
    return _wikipedia_call(language, fetch)


def wikipedia_article(title, language=None):
    """Fetch and return the complete text of a Wikipedia article."""
    title = str(title).strip()
    if not title:
        raise ValueError("title must not be empty.")
    def fetch(request):
        data = request({"action": "query", "prop": "extracts", "titles": title,
                        "redirects": "1", "explaintext": "1",
                        "exsectionformat": "wiki"})
        page = _wikipedia_page_from_response(data)
        return page if "error" in page else page.get("extract", "")
    return _wikipedia_call(language, fetch)


def _format_wikipedia_article(title, content, width=72):
    """Clean Wikipedia's mixed markup and wrap it as readable terminal text."""
    import re
    import textwrap
    width = max(36, int(width))
    title = str(title).strip() or "Wikipedia Article"
    text = str(content or "")
    # Page extracts may repeat their title and split display equations across
    # lines. Join each complete TeX display block before formatting the prose.
    source_lines = text.replace("\r\n", "\n").replace("\r", "\n").splitlines()
    folded_lines = []
    index = 0
    while index < len(source_lines):
        line = source_lines[index]
        if "{\\displaystyle" not in line:
            folded_lines.append(line)
            index += 1
            continue
        block = [line.strip()]
        depth = line.count("{") - line.count("}")
        index += 1
        while depth > 0 and index < len(source_lines):
            part = source_lines[index].strip()
            if part:
                block.append(part)
            depth += part.count("{") - part.count("}")
            index += 1
        # Wikipedia's text extract may contain a visual, line-broken rendering
        # of an equation immediately before the actual TeX source. Drop that
        # fragment when it is a run of short symbol-only lines; the TeX block
        # below is the recoverable equation and avoids displaying it twice.
        fragment_count = 0
        remove_from = len(folded_lines)
        cursor = len(folded_lines) - 1
        while cursor >= 0 and len(folded_lines) - cursor <= 28:
            previous = folded_lines[cursor].strip()
            if not previous:
                cursor -= 1
                continue
            if len(previous) <= 24 and not re.search(r"[A-Za-z]{4,}", previous):
                fragment_count += 1
                remove_from = cursor
                cursor -= 1
                continue
            break
        if fragment_count >= 3:
            del folded_lines[remove_from:]
        folded_lines.append(" ".join(block))
    text = "\n".join(folded_lines)
    text = re.sub(r"<ref\b[^>]*>.*?</ref\s*>", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("\u200b", "").replace("\u2060", "")
    text = text.replace("\u00a0", " ").replace("\u202f", " ")
    text = re.sub(r"\[\[([^]|]+)\|([^]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^]]+)\]\]", r"\1", text)
    text = re.sub(r"'{2,3}(.+?)'{2,3}", r"\1", text)
    def latex_to_plain(source):
        """Convert the common LaTeX commands used in Wikipedia equations."""
        greek = {"alpha": "α", "beta": "β", "gamma": "γ", "Gamma": "Γ",
                 "delta": "δ", "Delta": "Δ", "epsilon": "ε", "theta": "θ",
                 "lambda": "λ", "mu": "μ", "nu": "ν", "pi": "π",
                 "rho": "ρ", "sigma": "σ", "Sigma": "Σ", "tau": "τ",
                 "phi": "φ", "omega": "ω", "hbar": "ħ"}
        symbols = {"times": "×", "cdot": "·", "pm": "±", "le": "≤",
                   "ge": "≥", "neq": "≠", "approx": "≈", "infty": "∞",
                   "partial": "∂", "sim": "∼", "to": "→", "rightarrow": "→"}

        def group(index):
            while index < len(source) and source[index].isspace():
                index += 1
            if index >= len(source) or source[index] != "{":
                return (source[index:index + 1], index + 1) if index < len(source) else ("", index)
            value, end = sequence(index + 1, stop=True)
            return value, end

        def sequence(index=0, stop=False):
            pieces = []
            while index < len(source):
                char = source[index]
                if char == "}" and stop:
                    return "".join(pieces), index + 1
                if char == "\\":
                    index += 1
                    if index >= len(source):
                        break
                    if source[index].isalpha():
                        end = index + 1
                        while end < len(source) and source[end].isalpha():
                            end += 1
                        command = source[index:end]
                        index = end
                    else:
                        command = source[index]
                        index += 1
                    if command in {"frac", "dfrac", "tfrac"}:
                        numerator, index = group(index)
                        denominator, index = group(index)
                        pieces.append(f"({numerator.strip()})/({denominator.strip()})")
                    elif command in {"sqrt"}:
                        radicand, index = group(index)
                        pieces.append(f"√({radicand.strip()})")
                    elif command in {"mathrm", "mathbf", "mathit", "text", "operatorname"}:
                        value, index = group(index)
                        pieces.append(value)
                    elif command in {"left", "right", "displaystyle", ",", "!", ";", "quad", "qquad"}:
                        if command in {"quad", "qquad"}:
                            pieces.append(" ")
                    elif command in greek:
                        pieces.append(greek[command])
                    elif command in symbols:
                        pieces.append(symbols[command])
                    elif command in {"ln", "log", "sin", "cos", "tan", "exp"}:
                        pieces.append(command)
                    else:
                        pieces.append(command)
                    continue
                if char in "^_":
                    operator = char
                    value, index = group(index + 1)
                    value = value.strip()
                    pieces.append(operator + (value if len(value) == 1 else f"({value})"))
                    continue
                if char == "{":
                    value, index = group(index)
                    pieces.append(value)
                    continue
                if char == "}":
                    index += 1
                    continue
                if char == "~":
                    pieces.append(" ")
                else:
                    pieces.append(char)
                index += 1
            return "".join(pieces), index

        plain, _ = sequence()
        plain = re.sub(r"(?<=\d)(?=[A-Za-zα-ωΓΔ∂π])", " ", plain)
        plain = re.sub(r"(?<=[A-Za-zα-ωΓΔ∂π])(?=[A-Za-zα-ωΓΔ∂π])", " ", plain)
        plain = re.sub(r"\s*/\s*", " / ", plain)
        plain = re.sub(r"\s+", " ", plain)
        return plain.strip()

    # Convert full, balanced display-math wrappers. A regex cannot safely find
    # their end because equations contain nested braces (fractions/subscripts).
    marker = r"{\displaystyle"
    converted = []
    cursor = 0
    while True:
        start = text.find(marker, cursor)
        if start < 0:
            converted.append(text[cursor:])
            break
        converted.append(text[cursor:start])
        depth = 0
        end = start
        while end < len(text):
            if text[end] == "{":
                depth += 1
            elif text[end] == "}":
                depth -= 1
                if depth == 0:
                    end += 1
                    break
            end += 1
        body_start = start + len(marker)
        body_end = end - 1 if depth == 0 else end
        converted.append(latex_to_plain(text[body_start:body_end]))
        cursor = end
    text = "".join(converted)
    text = re.sub(r"(?<=\d)\*(?=\d)", "×", text)
    output = [title, "═" * min(len(title), width), ""]
    paragraph = []

    def flush_paragraph():
        if paragraph:
            joined = " ".join(part.strip() for part in paragraph if part.strip())
            if joined:
                output.extend(textwrap.wrap(joined, width=width, break_long_words=False,
                                            break_on_hyphens=False))
                output.append("")
            paragraph.clear()

    raw_lines = text.splitlines()
    separator = re.compile(r"^[─━─━═=\-_*~]{3,}$")
    if raw_lines and re.sub(r"^#{1,6}\s*", "", raw_lines[0].strip()).casefold() == title.casefold():
        raw_lines.pop(0)
        if raw_lines and separator.fullmatch(raw_lines[0].strip()):
            raw_lines.pop(0)
    for index, raw_line in enumerate(raw_lines):
        line = raw_line.strip()
        # Some article sources use a plain heading followed by a Unicode
        # underline instead of MediaWiki's == Heading == notation.
        if (line and index + 1 < len(raw_lines)
                and separator.fullmatch(raw_lines[index + 1].strip())):
            flush_paragraph()
            output.extend((line, "─" * min(len(line), width), ""))
            continue
        if separator.fullmatch(line):
            continue
        heading = re.fullmatch(r"={2,6}\s*(.*?)\s*={2,6}", line)
        if heading:
            flush_paragraph()
            label = heading.group(1).strip()
            if label:
                output.extend((label, "─" * min(len(label), width), ""))
            continue
        if not line:
            flush_paragraph()
            continue
        bullet = re.match(r"^([*#]+)\s*(.+)$", line)
        if bullet:
            flush_paragraph()
            depth, item = bullet.groups()
            prefix = ("• " if depth[0] == "*" else "1. ") + item.strip()
            wrapped = textwrap.wrap(prefix, width=width, subsequent_indent="  ")
            output.extend(wrapped or [prefix])
            output.append("")
            continue
        paragraph.append(line)
    flush_paragraph()
    return "\n".join(output).rstrip()


def _wikipedia_article_format_selftest():
    """Check that article sections, paragraphs, and lists are formatted."""
    sample = """Lead sentence.

== Mechanism ==

A long explanatory paragraph with enough words to wrap cleanly across a narrow test width.

* First item
* Second item"""
    rendered = _format_wikipedia_article("Muon", sample, width=40)
    noisy = _format_wikipedia_article("Muon", """A sentence split\nacross source lines.\n\nHistory of discovery\n────────────────────\n\nEquation: {\\displaystyle \\frac{a}{b}}\n""", width=40)
    lines = rendered.splitlines()
    if not rendered.startswith("Muon\n══") or "Mechanism\n" not in rendered:
        raise AssertionError("Article title or section headings were not formatted.")
    if "== Mechanism ==" in rendered or "• First item" not in rendered:
        raise AssertionError("Wiki heading or list markup was not converted.")
    if any(len(line) > 40 for line in lines):
        raise AssertionError("Article paragraphs were not wrapped to the requested width.")
    if "A sentence split across source lines." not in noisy or "(a) / (b)" not in noisy:
        raise AssertionError("Wrapped prose or display math was not cleaned up.")
    if "History of discovery\n────────────────────" not in noisy:
        raise AssertionError("Underline style section heading was not formatted.")
    duplicate_title = _format_wikipedia_article("Muon", "Muon\n====\n\nLead sentence.")
    if duplicate_title.count("Muon") != 1:
        raise AssertionError("The source article title was printed more than once.")
    nested_math = _format_wikipedia_article("Muon", "{\\displaystyle \\frac{a+b}{c}}")
    if "(a+b) / (c)" not in nested_math:
        raise AssertionError("Nested display math was not converted cleanly.")
    decay_rate = _format_wikipedia_article(
        "Muon",
        "{\\displaystyle \\Gamma = \\frac{G_{\\text{F}}^{2}m_{\\mu}^{5}}"
        "{192\\pi^{3}} I(\\frac{m_{\\text{e}}^{2}}{m_{\\mu}^{2}})}",
    )
    expected_rate = "Γ = (G_F^2 m_μ^5) / (192 π^3) I((m_e^2) / (m_μ^2))"
    if expected_rate not in decay_rate or "\\frac" in decay_rate or "displaystyle" in decay_rate:
        raise AssertionError("Muon decay-rate equation was not rendered as readable math.")
    duplicate_math = _format_wikipedia_article(
        "Muon", "3.4 ∗\n\n10\n\n− 5\n\n{\\displaystyle 3.4*10^{-5}}"
    )
    if duplicate_math.count("3.4×10^(-5)") != 1 or "3.4 ∗" in duplicate_math:
        raise AssertionError("Split duplicate math fragments were not removed.")
    return "article headings, wrapped prose, math, and lists formatted"


def _execute_wikipedia_command(expression):
    """Execute a literal-only Wikipedia function call and format its result."""
    import ast
    node = ast.parse(expression, mode="eval").body
    allowed = {"wikipedia_search", "wikipedia_summary", "wikipedia_page_info", "wikipedia_article"}
    if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name) or node.func.id not in allowed:
        raise ValueError("Use wikipedia_search(...), wikipedia_summary(...), wikipedia_page_info(...), or wikipedia_article(...).")
    try:
        args = [ast.literal_eval(arg) for arg in node.args]
        kwargs = {kw.arg: ast.literal_eval(kw.value) for kw in node.keywords if kw.arg is not None}
    except (ValueError, TypeError) as exc:
        raise ValueError("Wikipedia command arguments must be literal strings, numbers, or booleans.") from exc
    result = globals()[node.func.id](*args, **kwargs)
    if isinstance(result, dict) and result.get("error") == "page_not_found":
        return f"Wikipedia page not found: {result.get('message', '')}".rstrip()
    if node.func.id == "wikipedia_article":
        article_title = args[0] if args else kwargs.get("title", "Wikipedia Article")
        return _format_wikipedia_article(article_title, result)
    if isinstance(result, list):
        return "\n".join(f"{index}. {title}" for index, title in enumerate(result, 1)) or "No articles found."
    if isinstance(result, dict):
        if result.get("error") == "disambiguation":
            options = "\n".join(f"  - {title}" for title in result.get("options", []))
            return f"Ambiguous page: {result.get('query', '')}\n{options}"
        return "\n".join(f"{key}: {value}" for key, value in result.items())
    return str(result)


def _wikipedia_command_selftest():
    """Check the calculator command path without making network requests."""
    name = "wikipedia_search"
    original = globals()[name]
    original_article = globals()["wikipedia_article"]
    globals()[name] = lambda query, results=5, language=None: ["Artificial photosynthesis", "Photosynthesis"]
    try:
        output = _execute_wikipedia_command('wikipedia_search("photosynthesis", results=2)')
        if "1. Artificial photosynthesis" not in output or "2. Photosynthesis" not in output:
            raise AssertionError("Wikipedia search result formatting failed.")
        globals()["wikipedia_article"] = lambda title, language=None: "Lead sentence.\n\n== Mechanism ==\n\nSecond paragraph."
        article = _execute_wikipedia_command('wikipedia_article("Muon")')
        if not article.startswith("Muon\n══") or "Mechanism\n" not in article or "Second paragraph." not in article:
            raise AssertionError("Wikipedia full-article command did not format complete article text.")
        try:
            _execute_wikipedia_command('wikipedia_search(__import__("os"))')
        except ValueError:
            pass
        else:
            raise AssertionError("Non-literal Wikipedia arguments should be rejected.")
        return "Wikipedia command dispatch and result formatting passed"
    finally:
        globals()[name] = original
        globals()["wikipedia_article"] = original_article


def _wikipedia_exact_title_selftest():
    """Check MediaWiki API request shapes without making network requests."""
    requests = []
    def fake_request(params):
        requests.append(dict(params))
        page = {"title": "Muon", "pageid": 123,
                "fullurl": "https://en.wikipedia.org/wiki/Muon",
                "extract": "Muon summary" if "exintro" in params else
                           "Muon article paragraph one.\n\nMuon article paragraph two."}
        return {"query": {"pages": [page]}}
    original = globals()["_wikipedia_call"]
    globals()["_wikipedia_call"] = lambda language, operation: operation(fake_request)
    try:
        if wikipedia_summary("Muon") != "Muon summary":
            raise AssertionError("MediaWiki summary extract was not returned.")
        if requests[-1].get("exintro") != "1" or requests[-1].get("exsentences") != 3:
            raise AssertionError("Summary request did not ask for the requested intro sentences.")
        info = wikipedia_page_info("Muon")
        if info.get("title") != "Muon" or info.get("pageid") != 123:
            raise AssertionError("Page information was not mapped from the API response.")
        full_text = wikipedia_article("Muon")
        if "paragraph two" not in full_text or "exintro" in requests[-1]:
            raise AssertionError("Full-article lookup did not request the complete extract.")
        return "MediaWiki summary, page-info, and full-article requests passed"
    finally:
        globals()["_wikipedia_call"] = original


def _wikipedia_status_selftest():
    """Check that requests is installed and reported by the Wikipedia client."""
    status = wikipedia_status()
    if not status.get("available") or not status.get("version"):
        raise AssertionError(status.get("error", "requests client is unavailable"))
    import requests
    if status["version"] != requests.__version__:
        raise AssertionError("Wikipedia client reported the wrong requests version.")
    return f"requests {status['version']} available; no network request made"


def _wikipedia_input_selftest():
    """Check validation without making any external request."""
    checks = ((lambda: wikipedia_search("", results=1), "empty query"),
              (lambda: wikipedia_search("science", results=21), "too many results"),
              (lambda: wikipedia_summary("science", sentences=0), "invalid sentence count"),
              (lambda: wikipedia_page_info(" "), "empty page title"))
    for operation, label in checks:
        try:
            operation()
        except ValueError:
            continue
        raise AssertionError(f"Wikipedia validation did not reject {label}.")
    return "input validation passed; network not contacted"


def selftest():
    """
    Dave master self-test.

    This version is deliberately defensive:
    - Never directly references an undefined Dave function.
    - Uses globals() to find functions that actually exist.
    - Reports PASS or FAIL for every requested check.
    - Does not use multiline eval() tests.
    - Does not execute quit/exit/help commands.
    - Tests the functions actually present in Dave.
    """

    import math
    import traceback

    passed = 0
    failed = 0

    results = []

    print()
    print("=" * 78)
    print("DAVE — COMPLETE MASTER SELF-TEST")
    print("=" * 78)
    print()

    # ==========================================================
    # SAFE TEST RUNNER
    # ==========================================================

    def test(name, function, *args, **kwargs):
        nonlocal passed, failed

        try:
            result = function(*args, **kwargs)

            passed += 1
            results.append(
                ("PASS", name, result)
            )

            print(f"[PASS] {name}")

            return result

        except Exception as exc:

            failed += 1
            results.append(
                ("FAIL", name, exc)
            )

            print(
                f"[FAIL] {name}: "
                f"{type(exc).__name__}: {exc}"
            )

            return None

    def test_value(name, function, expected, tolerance=1e-6):
        """Check a scalar function result against a known value."""
        def check():
            result = float(function())
            if not math.isclose(
                result,
                float(expected),
                rel_tol=tolerance,
                abs_tol=tolerance
            ):
                raise AssertionError(
                    f"expected {expected}, got {result}"
                )
            return result

        return test(name, check)

    # ==========================================================
    # TEST A FUNCTION ONLY IF IT REALLY EXISTS
    # ==========================================================

    def test_function(name, function_name, *args, **kwargs):
        function = globals().get(function_name)
        if not callable(function):
            def missing_function():
                raise NameError(f"{function_name} is not defined")
            return test(name, missing_function)
        return test(name, function, *args, **kwargs)

    def test_optional_package(name, package_name, function):
        availability = _package_status(package_name)
        if not availability.get("available"):
            def unavailable_package():
                raise ImportError(f"optional package {package_name} is unavailable")
            return test(name, unavailable_package)
        return test(name, function)

    # ==========================================================
    # BASIC PYTHON / MATH
    # ==========================================================

    test(
        "2 + 2",
        lambda: 2 + 2
    )

    test(
        "sqrt(81)",
        lambda: math.sqrt(81)
    )

    test(
        "factorial(5)",
        lambda: math.factorial(5)
    )

    test(
        "log(10)",
        lambda: math.log10(10)
    )

    test(
        "ln(E)",
        lambda: math.log(math.e)
    )

    test(
        "exp(2)",
        lambda: math.exp(2)
    )

    test(
        "absolute value",
        lambda: abs(-5)
    )

    test(
        "round",
        lambda: round(3.14159, 2)
    )

    test(
        "floor",
        lambda: math.floor(3.9)
    )

    test(
        "ceil",
        lambda: math.ceil(3.1)
    )

    test(
        "sin",
        lambda: math.sin(math.pi / 2)
    )

    test(
        "cos",
        lambda: math.cos(math.pi)
    )

    test(
        "tan",
        lambda: math.tan(math.pi / 4)
    )

    # ==========================================================
    # SYMPY — USE sp DIRECTLY
    #
    # This avoids assuming that functions such as simplify()
    # exist as standalone Python globals.
    # ==========================================================

    test(
        "SymPy simplify",
        lambda: sp.simplify(x + x)
    )

    test(
        "SymPy expand",
        lambda: sp.expand((x + 1) ** 2)
    )

    test(
        "SymPy factor",
        lambda: sp.factor(x ** 2 - 9)
    )

    test(
        "SymPy solve",
        lambda: sp.solve(x ** 2 - 9, x)
    )

    test(
        "SymPy roots",
        lambda: sp.roots(x ** 2 - 9, x)
    )

    test(
        "SymPy derivative",
        lambda: sp.diff(x ** 3, x)
    )

    test(
        "SymPy integral",
        lambda: sp.integrate(x ** 2, x)
    )

    test(
        "SymPy limit",
        lambda: sp.limit(
            sp.sin(x) / x,
            x,
            0
        )
    )

    test(
        "SymPy series",
        lambda: sp.series(
            sp.sin(x),
            x,
            0,
            6
        )
    )

    test(
        "SymPy matrix trace",
        lambda: sp.Matrix(
            [[1, 2], [3, 4]]
        ).trace()
    )

    test(
        "SymPy matrix norm",
        lambda: sp.Matrix(
            [[1, 2], [3, 4]]
        ).norm()
    )

    test(
        "SymPy matrix RREF",
        lambda: sp.Matrix(
            [[1, 2], [2, 4]]
        ).rref()[0]
    )

    # ==========================================================
    # DAVE'S ACTUAL CORE FUNCTIONS
    # ==========================================================

    test_function(
        "matrix_trace",
        "matrix_trace",
        [[1, 2], [3, 4]]
    )

    test_function(
        "HEALPix coordinates",
        "healpix_coordinates",
        10,
        16
    )

    test_function(
        "HEALPix neighbors",
        "healpix_neighbors",
        10,
        16
    )

    test_function(
        "astronomical observation report",
        "astronomical_observation_report",
        10,
        20,
        51.4769,
        -0.0005
    )

    test_function(
        "matrix_norm",
        "matrix_norm",
        [[1, 2], [3, 4]]
    )

    test_function(
        "matrix_rref",
        "matrix_rref",
        [[1, 2], [2, 4]]
    )

    test_function(
        "matrix_columnspace",
        "matrix_columnspace",
        [[1, 2], [3, 4]]
    )

    test_function(
        "matrix_rowspace",
        "matrix_rowspace",
        [[1, 2], [3, 4]]
    )

    test_function(
        "characteristic_polynomial",
        "characteristic_polynomial",
        [[1, 2], [3, 4]]
    )

    # ==========================================================
    # STATISTICS
    #
    # These are functions that actually exist in dave4.py.
    # ==========================================================

    data = [1, 2, 3, 4, 5]

    test_function(
        "quartiles",
        "quartiles",
        data
    )

    test_function(
        "IQR",
        "iqr",
        data
    )

    test_function(
        "covariance",
        "covariance",
        [1, 2, 3],
        [2, 4, 6]
    )

    test_function(
        "correlation",
        "correlation",
        [1, 2, 3],
        [2, 4, 6]
    )

    test_function(
        "z_scores",
        "z_scores",
        data
    )

    test_function(
        "moving_average",
        "moving_average",
        data,
        3
    )

    test_function(
        "skewness",
        "skewness",
        data
    )

    test_function(
        "kurtosis",
        "kurtosis",
        data
    )

    test_function(
        "geometric_mean",
        "geometric_mean",
        data
    )

    test_function(
        "harmonic_mean",
        "harmonic_mean",
        data
    )

    test_function(
        "correlation_strength",
        "correlation_strength",
        0.8
    )

    test_function(
        "percentile",
        "percentile",
        data,
        50
    )

    # ==========================================================
    # EQUATION SOLVERS
    # ==========================================================

    test_function(
        "solvefor",
        "solvefor",
        "x**2 + y - 5",
        "y"
    )

    test_function(
        "solve_equation",
        "solve_equation",
        "x**2=9"
    )

    test_function(
        "nsolve_equation",
        "nsolve_equation",
        "x**2-2",
        1
    )

    test_function(
        "dsolve_equation",
        "dsolve_equation",
        "Derivative(y(x),x)-y(x)",
        "y"
    )

    test_function(
        "series_expansion",
        "series_expansion",
        "sin(x)",
        0,
        6
    )

    test_function(
        "astronomical distance",
        "astronomical_distance",
        1,
        "AU"
    )

    test_function(
        "is_equivalent",
        "is_equivalent",
        "x**2-1",
        "(x-1)*(x+1)"
    )

    # ==========================================================
    # PHYSICS
    # ==========================================================

    test_function(
        "velocity",
        "velocity",
        100,
        10
    )

    test_function(
        "ideal_gas_moles",
        "ideal_gas_moles",
        101325,
        1,
        273.15
    )

    test_function(
        "relativistic_ke",
        "relativistic_ke",
        1,
        1000
    )

    test_function(
        "momentum_vector",
        "momentum_vector",
        2,
        [1, 2, 3]
    )

    test_function(
        "distance",
        "distance",
        [0, 0, 0],
        [1, 1, 1]
    )

    test_function(
        "triangle_perimeter",
        "triangle_perimeter",
        3,
        4,
        5
    )

    test_function(
        "arc_length",
        "arc_length",
        5,
        math.pi
    )

    test_function(
        "factor_list",
        "factor_list",
        60
    )

    test_function(
        "totient",
        "totient",
        10
    )

    test_function(
        "largest_prime_factor",
        "largest_prime_factor",
        60
    )

    test_function(
        "validate_expr",
        "validate_expr",
        "x**2 + 1"
    )

    # ==========================================================
    # BASIC SCIENTIFIC FUNCTIONS
    # ==========================================================

    test_function(
        "simple interest",
        "simple_interest",
        1000,
        0.05,
        2
    )

    test_function(
        "compound interest",
        "compound_interest",
        1000,
        0.05,
        2
    )

    test_function(
        "probability",
        "probability",
        5,
        10
    )

    test_function(
        "binomial probability",
        "binomial_probability",
        10,
        5,
        0.5
    )

    test_function(
        "permutations",
        "permutations",
        5,
        2
    )

    test_function(
        "combinations",
        "combinations",
        5,
        2
    )

    test_function(
        "quadratic solver",
        "solve_quadratic",
        1,
        0,
        -4
    )

    test_function(
        "fibonacci",
        "fibonacci",
        10
    )

    test_function(
        "is_prime",
        "is_prime",
        97
    )

    test_function(
        "primes_up_to",
        "primes_up_to",
        20
    )

    test_function(
        "polar_complex",
        "polar_complex",
        1,
        0
    )

    # ==========================================================
    # CHEMISTRY / ELEMENTS
    #
    # Only test functions if they really exist.
    # ==========================================================

    test_function(
        "atomic mass",
        "atomic_mass",
        "Fe"
    )

    test_function(
        "element density",
        "density_element",
        "Fe"
    )

    test_function(
        "melting point",
        "melting_point",
        "Fe"
    )

    test_function(
        "boiling point",
        "boiling_point",
        "Fe"
    )

    test_function(
        "electron configuration",
        "electron_configuration",
        "Fe"
    )

    test_function(
        "electronegativity",
        "electronegativity",
        "Fe"
    )

    test_function(
        "atomic radius",
        "atomic_radius",
        "Fe"
    )

    test_function(
        "covalent radius",
        "covalent_radius",
        "Fe"
    )

    test_function(
        "oxidation states",
        "oxidation_states",
        "Fe"
    )

    test_function(
        "thermal conductivity",
        "thermal_conductivity",
        "Cu"
    )

    test_function(
        "specific heat",
        "specific_heat",
        "Cu"
    )

    test_function(
        "element information",
        "element_info",
        "Fe"
    )

    test_function(
        "find element",
        "find_element",
        "iron"
    )

    # ==========================================================
    # CHEMISTRY PACKAGE INTEGRATIONS
    # ==========================================================

    test_function(
        "chemparse H2O",
        "chemparse_formula",
        "H2O"
    )

    test_function(
        "ChemPy H2O",
        "chempy_molecular_weight",
        "H2O"
    )

    test_function(
        "RDKit molecule",
        "rdkit_molecule",
        "CCO"
    )

    test_function(
        "RDKit formula",
        "rdkit_formula",
        "CCO"
    )

    test_function(
        "RDKit molecular weight",
        "rdkit_molecular_weight",
        "CCO"
    )

    test_function(
        "RDKit canonical SMILES",
        "rdkit_canonical_smiles",
        "CCO"
    )

    test_function(
        "radioactive nuclide",
        "radioactive_nuclide",
        "U-238"
    )

    test_function(
        "radioactive half-life",
        "radioactive_half_life",
        "U-238"
    )

    test_function(
        "radioactive decay data",
        "radioactive_decay_data",
        "U-238"
    )

    test_function(
        "plasma particle",
        "plasma_particle_info",
        "e-"
    )

    # ==========================================================
    # ASTRONOMY
    # ==========================================================

    test_function(
        "astronomy constants",
        "astro_constants"
    )

    test_function(
        "astronomical time",
        "astro_time",
        "2026-01-01T00:00:00"
    )

    test_function(
        "SkyCoord",
        "skycoord",
        10.6847,
        41.2687
    )

    test_function(
        "galactic coordinates",
        "galactic_coordinates",
        10.6847,
        41.2687
    )

    test_function(
        "HEALPix pixel",
        "healpix_pixel",
        0,
        0,
        nside=16
    )

    test_function(
        "HEALPix pixel area",
        "healpix_pixel_area",
        16
    )

    test_function(
        "ERFA version",
        "erfa_version"
    )

    test_function(
        "astronomy package status",
        "astronomy_package_status"
    )

    # Dedicated astronomy test
    test_function(
        "astronomy self-test",
        "astronomy_selftest",
        False
    )

    # ==========================================================
    # GIS / GEOSPATIAL
    #
    # geo_distance() in the actual file accepts four coordinates,
    # not Shapely point objects.
    # ==========================================================

    test_function(
        "geographic distance",
        "geo_distance",
        40.7128,
        -74.0060,
        51.5074,
        -0.1278
    )

    test_function(
        "geo distance km",
        "geo_distance_km",
        40.7128,
        -74.0060,
        51.5074,
        -0.1278
    )

    test_function(
        "geo distance miles",
        "geo_distance_miles",
        40.7128,
        -74.0060,
        51.5074,
        -0.1278
    )

    test_function(
        "geographiclib distance",
        "geographiclib_distance",
        40.7128,
        -74.0060,
        51.5074,
        -0.1278
    )

    test_function(
        "geographiclib destination",
        "geographiclib_destination",
        40.7128,
        -74.0060,
        90,
        1000
    )

    # ==========================================================
    # ATOMISTIC / MATERIALS
    # ==========================================================

    test_function(
        "ASE atoms",
        "ase_atoms",
        ["H", "H"],
        [
            [0, 0, 0],
            [0, 0, 0.74]
        ]
    )

    test_function(
        "pymatgen composition",
        "pymatgen_composition",
        "Fe2O3"
    )

    test_function(
        "pymatgen lattice",
        "pymatgen_lattice",
        3,
        3,
        3,
        90,
        90,
        90
    )

    test_function(
        "spglib space group",
        "spglib_spacegroup",
        (
            [
                [3.0, 0.0, 0.0],
                [0.0, 3.0, 0.0],
                [0.0, 0.0, 3.0],
            ],
            [
                [0.0, 0.0, 0.0],
            ],
            [
                14,
            ],
        )
    )

    test_function(
        "pyrolite status",
        "pyrolite_status"
    )

    # ==========================================================
    # ADVANCED PHYSICS
    # ==========================================================

    test_function(
        "QuTiP |0>",
        "qutip_qubit_zero"
    )

    test_function(
        "QuTiP |1>",
        "qutip_qubit_one"
    )

    test_function(
        "QuTiP basis",
        "qutip_basis",
        2,
        0
    )

    test_function(
        "QuTiP Pauli X",
        "qutip_pauli",
        "x"
    )

    test_function(
        "QuTiP Pauli Y",
        "qutip_pauli",
        "y"
    )

    test_function(
        "QuTiP Pauli Z",
        "qutip_pauli",
        "z"
    )

    test_function(
        "QMSolve status",
        "qmsolve_status"
    )

    test_function(
        "Quantecon Markov chain",
        "quantecon_markov_chain",
        [
            [0.9, 0.1],
            [0.2, 0.8]
        ]
    )

    test_function(
        "Quantecon stationary distribution",
        "quantecon_stationary_distribution",
        [
            [0.9, 0.1],
            [0.2, 0.8]
        ]
    )

    test_function(
        "Plasma particle",
        "plasma_particle",
        "e-"
    )

    test_function(
        "Plasma particle mass",
        "plasma_particle_mass",
        "e-"
    )

    test_function(
        "Plasma particle charge",
        "plasma_particle_charge",
        "e-"
    )

    test_function(
        "Plasma Debye length",
        "plasma_debye_length",
        10000,
        1e19
    )

    test_function(
        "Plasma thermal speed",
        "plasma_thermal_speed",
        10000,
        "e-"
    )

    test_function(
        "MetPy potential temperature",
        "metpy_potential_temperature",
        1000,
        300
    )

    test_function(
        "MetPy dewpoint",
        "metpy_dewpoint",
        20,
        50
    )

    test_function(
        "MetPy heat index",
        "metpy_heat_index",
        30,
        60
    )

    test_function(
        "MetPy wind components",
        "metpy_wind_components",
        10,
        90
    )

    test_value(
        "MetPy relative humidity",
        lambda: metpy_relative_humidity(25, 12),
        44.29983646993876,
        1e-5
    )

    test_value(
        "MetPy wind chill",
        lambda: metpy_wind_chill(0, 10),
        -7.052924578603699,
        1e-5
    )

    test_value(
        "BMI calculation",
        lambda: bmi(70, 1.75),
        70 / (1.75 ** 2)
    )

    test_value(
        "Mifflin-St Jeor estimate",
        lambda: mifflin_st_jeor(70, 175, 30, "male"),
        1648.75
    )

    test_value(
        "cardiac output calculation",
        lambda: cardiac_output(70, 70),
        4.9
    )

    test_value(
        "minute ventilation calculation",
        lambda: minute_ventilation(500, 12),
        6.0
    )

    test_value("epidemiology risk ratio", lambda: epidemiology_2x2(10, 90, 5, 95)["risk_ratio"], 2.0)
    test_value("number needed to treat", lambda: number_needed_to_treat(0.2, 0.1), 10)
    test_value("first-order drug decay", lambda: drug_concentration_after_dose(100, 5, 10), 25)
    test_value("mean arterial pressure", lambda: mean_arterial_pressure(120, 80), 93.33333333333333)
    test_value("Shannon diversity", lambda: shannon_diversity([1, 1]), math.log(2))
    test_value("Simpson diversity", lambda: simpson_diversity([1, 1]), 0.5)
    test_value("Pielou evenness", lambda: pielou_evenness([1, 1]), 1.0)
    test_value("logistic population at initial time", lambda: logistic_population(10, 0.1, 100, 0), 10)
    test_value("Reynolds number", lambda: reynolds_number(1000, 1, 0.1, 0.001), 100000)
    test_value("control natural frequency", lambda: control_natural_frequency(1, 4), 2)
    test_value("control damping ratio", lambda: control_damping_ratio(1, 2, 1), 1)
    test_value("cantilever tip deflection", lambda: cantilever_tip_deflection(100, 2, 200e9, 1e-6), 0.0013333333333333333)
    test_value("beam bending stress", lambda: beam_bending_stress(100, 1e-6, 0.01), 1e6)
    test_function("GSW oceanography status", "gsw_status")
    test_function("scikit-learn status", "scikit_learn_status")
    test_value("weight-based dose", lambda: weight_based_dose(5, 20), 100)
    test_value("mass concentration units", lambda: convert_mass_concentration(1, "g/L", "mg/dL"), 100)
    test_value("glucose unit conversion", lambda: glucose_mg_dl_to_mmol_l(90), 90 / 18.0156)
    test_value("cholesterol unit conversion", lambda: cholesterol_mg_dl_to_mmol_l(193.325), 5)
    test_value("creatinine unit conversion", lambda: creatinine_mg_dl_to_umol_l(1), 88.4)
    test_value("conduction heat rate", lambda: heat_conduction_rate(2, 3, 10, 0.5), 120)
    test_value("convection heat rate", lambda: heat_convection_rate(10, 2, 310, 300), 200)
    test_value("radiative heat rate", lambda: heat_radiation_rate(1, 1, 400, 300), 5.670374419e-8 * (400**4 - 300**4))
    test_value("ideal gas pressure", lambda: ideal_gas_pressure(1, 300, 0.02494338785445972), 100000)
    test_value("Carnot efficiency", lambda: carnot_efficiency(600, 300), 0.5)
    test_value("thermal expansion", lambda: volumetric_thermal_expansion(1, 1e-3, 10), 0.01)
    test_value("Ohm's law", lambda: ohms_law(voltage_v=12, resistance_ohm=6)["current_a"], 2)
    test_value("RC time constant", lambda: rc_time_constant(1000, 1e-6), 0.001)
    test_value("parallel resistance", lambda: equivalent_resistance([10, 10], "parallel"), 5)
    test_optional_package("scikit-learn integrations", "scikit_learn", _sklearn_selftest_probe)

    test_value("Michaelis-Menten velocity", lambda: michaelis_menten_velocity(10, 2, 2), 5)
    test_value("Henderson-Hasselbalch pH", lambda: henderson_hasselbalch(7.4, 1, 1), 7.4)
    test_value("Beer-Lambert absorbance", lambda: beer_lambert_absorbance(1000, 0.001, 1), 1)
    test_value("ideal osmotic pressure", lambda: osmotic_pressure_kpa(0.1, 300), 249.4338785445972)
    test_value("Magnus humidity", lambda: magnus_relative_humidity(20, 10), 52.5, tolerance=0.02)
    test_value("Magnus dew point", lambda: magnus_dewpoint_c(20, magnus_relative_humidity(20, 10)), 10)
    test_value("standard atmosphere pressure", lambda: isa_pressure_altitude_pa(0), 101325)
    test_value("hydrostatic pressure", lambda: hydrostatic_pressure_kpa(1000, 10), 98.0665)
    test_value("geothermal temperature", lambda: geothermal_temperature_c(15, 25, 2000), 65)
    test_value("signal RMS", lambda: signal_rms([-1, 1]), 1)
    test_value("signal peak-to-peak", lambda: signal_peak_to_peak([-2, 3]), 5)
    test_value("signal SNR", lambda: signal_snr_db([1, 1], [0.1, -0.1]), 20)
    test_value("zero crossing rate", lambda: zero_crossing_rate([-1, 1, -1]), 1)
    test_value("sample rate", lambda: sample_rate_hz(10, 2), 5)
    test_value("sound intensity level", lambda: sound_intensity_level_db(1e-6), 60)
    test_value("sound intensity conversion", lambda: sound_intensity_from_db(60), 1e-6)
    test_value("capacitor stored energy", lambda: capacitor_energy_j(0.01, 10), 0.5)
    test_value("inductor stored energy", lambda: inductor_energy_j(0.5, 2), 1)
    test_value("capacitive reactance", lambda: capacitive_reactance_ohm(50, 100e-6), 1 / (2 * math.pi * 50 * 100e-6))
    test_value("inductive reactance", lambda: inductive_reactance_ohm(50, 0.1), 2 * math.pi * 50 * 0.1)
    test_value("thermal diffusivity", lambda: thermal_diffusivity_m2_s(0.6, 1000, 4000), 1.5e-7)
    test_value("Cohen's d", lambda: cohens_d([2, 4], [1, 3]), 1 / math.sqrt(2))
    test_value("standard error", lambda: standard_error_of_mean([1, 2, 3, 4]), math.sqrt(5 / 3) / 2)
    test_value("acoustic SPL", lambda: acoustic_sound_pressure_level_db(0.02), 60)
    test_value("pressure from SPL", lambda: acoustic_pressure_from_spl_pa(60), 0.02)
    test_value("Doppler frequency", lambda: doppler_frequency_hz(1000, 340, 10), 1000 * 340 / 330)
    test_value("microbial exponential growth", lambda: microbial_population(100, math.log(2), 3), 800)
    test_value("microbial doubling time", lambda: microbial_doubling_time_h(math.log(2)), 1)
    test_value("microbial log reduction", lambda: microbial_log_reduction(1e6, 1e3), 3)
    test_value("PK loading amount", lambda: pharmacokinetic_loading_dose_mg(2, 10, 0.5), 40)
    test_value("PK maintenance rate", lambda: pharmacokinetic_maintenance_rate_mg_h(5, 2, 0.5), 20)
    test_value("PK elimination half-life", lambda: pharmacokinetic_half_life_h(10, 2), math.log(2) * 5)
    test_value("seawater density", lambda: seawater_density_kg_m3(15, 35), 1025.972753865)
    test_value("depth from gauge pressure", lambda: ocean_depth_from_gauge_pressure_m(100, 1000, 10), 10)

    test_value("Hargreaves-Samani ET0", lambda: hargreaves_samani_et0_mm_day(25, 15, 20, 20), 5.498568395500778)
    test_value("soil porosity", lambda: soil_porosity_fraction(1325, 2650), 0.5)
    test_value("soil water fraction", lambda: soil_water_content_fraction(0.2, 0.5), 0.4)
    test_value("food wet-basis moisture", lambda: food_moisture_percent(100, 80), 20)
    test_value("food dry-basis moisture", lambda: food_moisture_percent(100, 80, "dry"), 25)
    test_value("water activity", lambda: water_activity_from_equilibrium_rh(65), 0.65)
    test_value("diagnostic sensitivity", lambda: diagnostic_test_metrics(80, 10, 90, 20)["sensitivity"], 0.8)
    test_value("CO2 from oxidized carbon", lambda: co2_from_oxidized_carbon_kg(12), 44)
    test_value("seismic energy estimate", lambda: seismic_energy_j(0), 10 ** 4.8)
    test_value("photon energy", lambda: photon_energy_j(500e-9), 6.62607015e-34 * 299792458 / 500e-9)
    test_value("Snell refraction", lambda: snell_refracted_angle_deg(1, 1.5, 30), 19.47122063449069)
    test_value("thin lens image distance", lambda: thin_lens_image_distance_m(0.1, 0.3), 0.15)
    test_value("normal stress", lambda: stress_from_force_pa(100, 0.001), 100000)
    test_value("engineering strain", lambda: engineering_strain(1, 1.1), 0.1)
    test_value("factor of safety", lambda: factor_of_safety(200e6, 50e6), 4)
    test_value("sensible heat", lambda: sensible_heat_j(2, 4200, 10), 84000)
    test_value("latent heat", lambda: latent_heat_j(2, 334000), 668000)
    test_value("Nernst equilibrium potential", lambda: nernst_potential_v(0.75, 298.15, 2, 1), 0.75)
    test_value("solution dilution", lambda: solution_dilution_molarity(1, 0.01, 0.1), 0.1)
    test_value("chemical percent yield", lambda: percent_yield(8, 10), 80)
    test_value("Gini coefficient", lambda: gini_coefficient([0, 0, 1, 1]), 0.5)
    test_value("exponential population projection", lambda: population_exponential_projection(100, 0.1, math.log(2) / 0.1), 200)
    test("MediaWiki requests client status", _wikipedia_status_selftest)
    test("Wikipedia input validation (no network)", _wikipedia_input_selftest)
    test("Wikipedia command dispatch (no network)", _wikipedia_command_selftest)
    test("Wikipedia exact-title lookup (no network)", _wikipedia_exact_title_selftest)
    test("Wikipedia article formatting (no network)", _wikipedia_article_format_selftest)
    test("Expression command evaluation (expected values)", _expression_command_selftest)
    test("Dave language selection (five languages)", _language_selftest)

    # ==========================================================
    # ADVANCED NUMERICAL PACKAGE STATUS
    # ==========================================================

    test_function(
        "Diffrax status",
        "diffrax_status"
    )

    test_function(
        "Dynamiqs status",
        "dynamiqs_status"
    )

    test_function(
        "Equinox status",
        "equinox_status"
    )

    test_function(
        "Lineax status",
        "lineax_status"
    )

    test_function(
        "Optimistix status",
        "optimistix_status"
    )

    test_function(
        "opt_einsum status",
        "opt_einsum_status"
    )

    test_function(
        "emcee status",
        "emcee_status"
    )

    test_function(
        "formulaic status",
        "formulaic_status"
    )

    test_function(
        "GUDHI status",
        "gudhi_status"
    )

    test_function(
        "topoly status",
        "topoly_status"
    )

    # ==========================================================
    # BIOLOGY / BIOINFORMATICS
    # ==========================================================

    test_function(
        "Biopython sequence",
        "biopython_sequence",
        "ATGC"
    )

    test_function(
        "Biopython reverse complement",
        "biopython_reverse_complement",
        "ATGC"
    )

    test_function(
        "Biopython translation",
        "biopython_translate",
        "ATGGCC"
    )

    test_function(
        "Biotite DNA",
        "biotite_dna",
        "ATGC"
    )

    test_function(
        "Biotite reverse complement",
        "biotite_reverse_complement",
        "ATGC"
    )

    test_function(
        "DendroPy tree",
        "dendropy_tree",
        "(A,B,(C,D));"
    )

    test_function(
        "msprime ancestry",
        "msprime_ancestry",
        10,
        1
    )

    test_function(
        "msprime mutations",
        "msprime_mutations",
        10,
        1
    )

    test_function(
        "scikit-bio DNA",
        "skbio_dna",
        "ATGC"
    )

    test_function(
        "scikit-bio RNA",
        "skbio_rna",
        "AUGC"
    )

    test_function(
        "scikit-bio protein",
        "skbio_protein",
        "MKWVTF"
    )

    # ==========================================================
    # MOLECULAR DYNAMICS
    # ==========================================================

    test_function(
        "OpenMM status",
        "openmm_status"
    )

    test_function(
        "MDAnalysis status",
        "mdanalysis_status"
    )

    test_function(
        "MDTraj status",
        "mdtraj_status"
    )

    test_function(
        "mdapy status",
        "mdapy_status"
    )

    test_function(
        "MMTF status",
        "mmtf_status"
    )

    test_function(
        "Brian2 status",
        "brian2_status"
    )

    test_function(
        "Nengo status",
        "nengo_status"
    )

    test_function(
        "Neo status",
        "neo_status"
    )

    test_function(
        "Elephant status",
        "elephant_status"
    )

    test_function(
        "Pynapple status",
        "pynapple_status"
    )

    test_function(
        "PyNWB status",
        "pynwb_status"
    )

    # ==========================================================
    # VISUALIZATION / DATA
    # ==========================================================

    test_function(
        "matplotlib status",
        "matplotlib_status"
    )

    test_function(
        "Plotly status",
        "plotly_status"
    )

    test_function(
        "Altair status",
        "altair_status"
    )

    test_function(
        "xarray status",
        "xarray_status"
    )

    test_function(
        "Zarr status",
        "zarr_status"
    )

    test_function(
        "h5py status",
        "h5py_status"
    )

    test_function(
        "Nibabel status",
        "nibabel_status"
    )

    test_function(
        "PyWavelets status",
        "pywavelets_status"
    )

    test_function(
        "scikit-image status",
        "skimage_status"
    )

    test_function(
        "Tifffile status",
        "tifffile_status"
    )

    test_function(
        "DIPY status",
        "dipy_status"
    )

    test_function(
        "Folium status",
        "folium_status"
    )

    test_function(
        "yt status",
        "yt_status"
    )

    # ==========================================================
    # PACKAGE MANAGEMENT
    # ==========================================================

    test_function(
        "all scientific package status",
        "all_scientific_package_status"
    )

    test_function(
        "scientific package report",
        "scientific_package_report"
    )

    # ==========================================================
    # FINAL DEDICATED SELF-TEST
    # ==========================================================

    test_function(
        "final scientific self-test",
        "final_scientific_selftest"
    )

    # ==========================================================
    # FINAL SUMMARY
    # ==========================================================

    total = passed + failed

    print()
    print("=" * 78)
    print("DAVE — SELF-TEST SUMMARY")
    print("=" * 78)
    print()
    print(f"Passed : {passed}")
    print(f"Failed : {failed}")
    print(f"Total  : {total}")
    print()

    if failed == 0:
        print("SELF-TEST FINISHED WITH NO FAILURES.")
    else:
        print(
            f"SELF-TEST FINISHED WITH {failed} FAILURE(S)."
        )

    print("=" * 78)
    print()

    return {
        "passed": passed,
        "failed": failed,
        "total": total,
        "results": results,
    }

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

def translate(text, target=None):

    target = target or language
    target = {"zh": "zh-CN", "jp": "ja", "mandarin": "zh-CN"}.get(
        str(target).strip().lower(), target)

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
    """Calculate ideal-gas pressure in pascals from mol, kelvin, and m³."""
    n, temperature, volume = _science_finite_values(
        moles=n, temperature_k=T, volume_m3=V).values()
    if n < 0 or temperature <= 0 or volume <= 0:
        raise ValueError("Moles must be non-negative; temperature and volume positive.")
    return n * 8.31446261815324 * temperature / volume

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

def polar_complex(
    magnitude,
    angle
):
    """
    Convert polar-form complex coordinates to
    a rectangular complex number.

    The angle follows Dave's global angle_mode:

        angle_mode = "rad"
            angle is interpreted as radians

        angle_mode = "deg"
            angle is interpreted as degrees

    Example:

        polar_complex(2, 90)

    when angle_mode == "deg" gives approximately:

        2j
    """

    import math

    # Safely obtain Dave's current angle mode.
    mode = globals().get(
        "angle_mode",
        "rad"
    )

    magnitude = float(
        magnitude
    )

    angle = float(
        angle
    )

    if str(mode).lower() == "deg":
        angle = math.radians(
            angle
        )

    real = magnitude * math.cos(
        angle
    )

    imaginary = magnitude * math.sin(
        angle
    )

    # Remove tiny floating-point artifacts.
    if abs(real) < 1e-12:
        real = 0.0

    if abs(imaginary) < 1e-12:
        imaginary = 0.0

    return complex(
        real,
        imaginary
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

def _show_help_full_english():

    help_text = """

=========================================================
DAVE — COMPLETE EXPANDED HELP LIST
=========================================================

LANGUAGE SETTINGS
-----------------
Select one of the five interface languages with:
    lang en       English
    lang es       Spanish
    lang ja       Japanese
    lang zh       Mandarin Chinese
    lang fr       French
You can also use: english(), spanish(), japanese(), mandarin(), french().
Wikipedia searches use the selected language by default. Mathematical expression
and scientific function names remain English.

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

[bold cyan]SCIENTIFIC PACKAGE FEATURES[/bold cyan]

Dave now includes a large collection of optional
scientific, engineering, chemistry, biology, astronomy,
geospatial, simulation, statistics, and visualization tools.

Packages are loaded only when needed.

────────────────────────────────────────────────────────────
[bold yellow]ASTRONOMY & SPACE[/bold yellow]
────────────────────────────────────────────────────────────

astro_constants(...)
    Show astronomical constants.

astro_convert(value, from_unit, to_unit)
    Convert astronomical quantities and units.

astro_time(value, format="isot", scale="utc")
    Convert or inspect astronomical time.

astro_time_report(value)
    Generate a detailed astronomical time report.

julian_date(value)
    Calculate the Julian Date.

modified_julian_date(value)
    Calculate the Modified Julian Date.

skycoord(...)
    Create an astronomical sky coordinate.

astro_coordinate(...)
    Create and inspect celestial coordinates.

ra_dec(...)
    Create right-ascension/declination coordinates.

angular_separation(...)
    Calculate angular separation between two coordinates.

position_angle(...)
    Calculate the position angle between coordinates.

transform_coordinates(...)
    Transform coordinates between astronomical frames.

galactic_coordinates(...)
    Convert coordinates to Galactic coordinates.

galactic_to_icrs(...)
    Convert Galactic coordinates to ICRS.

earth_location(...)
    Create an Earth location.

observatory(...)
    Work with astronomical observatory locations.

altaz(...)
    Convert celestial coordinates to Alt/Az.

astronomical_distance(...)
    Convert astronomical distances.

astronomical_observation_report(...)
    Generate an observation report.

healpix_pixel(...)
    Calculate a HEALPix pixel.

healpix_coordinates(...)
    Convert HEALPix pixels to coordinates.

healpix_neighbors(...)
    Find neighboring HEALPix pixels.

healpix_pixel_area(...)
    Calculate HEALPix pixel area.

erfa_version()
    Show the installed ERFA version.

astronomy_package_status()
    Show astronomy package availability.

astronomy_selftest()
    Test astronomy functionality.


────────────────────────────────────────────────────────────
[bold yellow]ADVANCED NUMERICAL & PHYSICS[/bold yellow]
────────────────────────────────────────────────────────────

scipy_root(...)
    Find numerical roots.

scipy_minimize(...)
    Perform numerical minimization.

scipy_curve_fit(...)
    Fit functions to experimental data.

scipy_interpolate(...)
    Perform numerical interpolation.

scipy_spline(...)
    Create spline interpolations.

scipy_integrate(...)
    Perform numerical integration.

scipy_ode(...)
    Solve ordinary differential equations.

scipy_linear_solve(...)
    Solve linear systems.

scipy_eigenvalues(...)
    Calculate eigenvalues and eigenvectors.

scipy_fft(...)
    Perform Fourier transforms.

scipy_describe(...)
    Generate statistical descriptions.

scipy_normal_pdf(...)
    Evaluate a normal probability density function.

scipy_special(...)
    Access special mathematical functions.

mpmath_precision(...)
    Set arbitrary numerical precision.

mpmath_pi(...)
    Calculate high-precision pi.

mpmath_exp(...)
    High-precision exponential.

mpmath_log(...)
    High-precision logarithm.

mpmath_findroot(...)
    Find high-precision roots.

mpmath_integrate(...)
    High-precision numerical integration.

uncertainty(...)
    Create values with uncertainty.

uncertainty_operations(...)
    Perform calculations while propagating uncertainty.

unyt_convert(...)
    Convert physical quantities using unyt.

quantities_convert(...)
    Convert physical quantities using quantities.

lmfit_fit(...)
    Perform nonlinear fitting with lmfit.

lmfit_report(...)
    Display detailed fit information.

qutip_basis(...)
    Create quantum basis states.

qutip_qubit(...)
    Create quantum states.

qutip_pauli(...)
    Generate Pauli operators.

qutip_expectation(...)
    Calculate quantum expectation values.

qutip_density(...)
    Create density matrices.

qutip_tensor(...)
    Create tensor-product quantum systems.

qutip_schrodinger(...)
    Solve the Schrödinger equation.

qutip_master(...)
    Solve master equations.

qmsolve_status()
    Show qmsolve availability.

quantecon_markov(...)
    Work with Markov chains.

quantecon_stationary(...)
    Calculate stationary distributions.

quantecon_lq(...)
    Solve linear-quadratic problems.

plasmapy_particle(...)
    Analyze plasma particles.

plasmapy_debye(...)
    Calculate Debye length.

plasmapy_frequency(...)
    Calculate plasma frequencies.

plasmapy_gyrofrequency(...)
    Calculate gyrofrequencies.

plasmapy_thermal_speed(...)
    Calculate thermal particle speeds.

metpy_potential_temperature(...)
    Calculate potential temperature.

metpy_dewpoint(...)
    Calculate dew point.

metpy_heat_index(...)
    Calculate heat index.

metpy_wind_components(...)
    Calculate wind components.

metpy_relative_humidity(temperature_c, dewpoint_c)
    Calculate relative humidity in percent.

metpy_wind_chill(temperature_c, wind_speed_m_s)
    Calculate wind chill in degrees Celsius.

PHYSIOLOGY — GENERAL CALCULATORS

bmi(weight_kg, height_m)
    Calculate BMI in kg/m^2 (a screening measure, not a diagnosis).

mifflin_st_jeor(weight_kg, height_cm, age_years, sex)
    Estimate resting energy expenditure in kcal/day.

cardiac_output(heart_rate_bpm, stroke_volume_ml)
    Calculate cardiac output in L/min.

minute_ventilation(tidal_volume_ml, respiratory_rate_bpm)
    Calculate minute ventilation in L/min.

CLINICAL / EPIDEMIOLOGY

epidemiology_2x2(exposed_cases, exposed_non_cases, unexposed_cases, unexposed_non_cases)
    Calculate risks, risk ratio, odds ratio, and risk difference.
number_needed_to_treat(control_event_rate, treatment_event_rate)
    Calculate NNT when treatment reduces the event rate.
drug_concentration_after_dose(initial_concentration, half_life_hours, elapsed_hours)
mean_arterial_pressure(systolic_mmhg, diastolic_mmhg)
    Estimate first-order concentration decay and mean arterial pressure.

ECOLOGY / POPULATION

shannon_diversity(counts, base=math.e)
simpson_diversity(counts)
pielou_evenness(counts)
logistic_population(initial_population, growth_rate, carrying_capacity, time)
    Calculate diversity indices and logistic population growth.

OCEANOGRAPHY / MACHINE LEARNING (OPTIONAL PACKAGES)

gsw_seawater_properties(practical_salinity, temperature_c, pressure_dbar=0, longitude=0, latitude=0)
sklearn_train_test_split(features, targets, ...)
sklearn_classification_report(y_true, y_pred)
sklearn_linear_regression(features, targets, ...)
    These helpers require optional gsw or scikit-learn installations.

ENGINEERING (SI UNITS)

reynolds_number(density_kg_m3, velocity_m_s, characteristic_length_m, dynamic_viscosity_pa_s)
control_natural_frequency(mass_kg, stiffness_n_m)
control_damping_ratio(mass_kg, damping_n_s_m, stiffness_n_m)
cantilever_tip_deflection(point_load_n, length_m, youngs_modulus_pa, second_moment_m4)
beam_bending_stress(moment_nm, second_moment_m4, distance_m)
    Calculate fluid flow, vibration, and beam quantities.

CLINICAL UNITS / LAB CONVERSIONS

weight_based_dose(dose_mg_per_kg, weight_kg)
convert_mass_concentration(value, from_unit, to_unit)
    Convert among mg/L, g/L, mg/dL, and ug/mL.
glucose_mg_dl_to_mmol_l(value_mg_dl)
glucose_mmol_l_to_mg_dl(value_mmol_l)
cholesterol_mg_dl_to_mmol_l(value_mg_dl)
creatinine_mg_dl_to_umol_l(value_mg_dl)
    Convert common lab units; results depend on analyte-specific molar mass.

HEAT TRANSFER / THERMODYNAMICS

heat_conduction_rate(conductivity_w_m_k, area_m2, temperature_difference_k, thickness_m)
heat_convection_rate(heat_transfer_coefficient_w_m2_k, area_m2, surface_temp_k, fluid_temp_k)
heat_radiation_rate(emissivity, area_m2, surface_temp_k, surroundings_temp_k)
carnot_efficiency(hot_temperature_k, cold_temperature_k)
volumetric_thermal_expansion(initial_volume_m3, expansion_coefficient_per_k, temperature_change_k)
    Use SI units and absolute temperatures in kelvin.

ELECTRICAL CIRCUITS

ohms_law(voltage_v=None, current_a=None, resistance_ohm=None)
rc_time_constant(resistance_ohm, capacitance_f)
equivalent_resistance(resistances_ohm, connection="series")
    Solve basic ideal Ohm's law, RC, and resistor network calculations.




────────────────────────────────────────────────────────────

BIOCHEMISTRY

michaelis_menten_velocity(vmax, substrate_concentration, km)
henderson_hasselbalch(pka, base_concentration, acid_concentration)
beer_lambert_absorbance(molar_absorptivity_l_mol_cm, concentration_mol_l, path_length_cm)
osmotic_pressure_kpa(molarity_mol_l, temperature_k, vanthoff_factor=1)
    Enzyme kinetics, buffer pH, absorbance, and ideal osmotic pressure.

ENVIRONMENT / HYDROLOGY / GEOLOGY

magnus_relative_humidity(temperature_c, dewpoint_c)
magnus_dewpoint_c(temperature_c, relative_humidity_percent)
isa_pressure_altitude_pa(altitude_m)
hydrostatic_pressure_kpa(fluid_density_kg_m3, depth_m, gravity_m_s2=9.80665)
geothermal_temperature_c(surface_temperature_c, geothermal_gradient_c_per_km, depth_m)
    Atmospheric, hydrostatic, and geothermal estimates with stated units.

SIGNAL PROCESSING / ACOUSTICS

signal_rms(samples)
signal_peak_to_peak(samples)
signal_snr_db(signal_samples, noise_samples)
zero_crossing_rate(samples)
sample_rate_hz(sample_count, duration_s)
sound_intensity_level_db(intensity_w_m2, reference_w_m2=1e-12)
sound_intensity_from_db(level_db, reference_w_m2=1e-12)
    Calculate signal summaries, sampling rate, and acoustic intensity levels.

CIRCUITS / MATERIALS / STATISTICS

capacitor_energy_j(capacitance_f, voltage_v)
inductor_energy_j(inductance_h, current_a)
capacitive_reactance_ohm(frequency_hz, capacitance_f)
inductive_reactance_ohm(frequency_hz, inductance_h)
thermal_diffusivity_m2_s(conductivity_w_m_k, density_kg_m3, specific_heat_j_kg_k)
cohens_d(group_a, group_b)
standard_error_of_mean(samples)
    SI units are used for electrical and material calculations.


AGRICULTURE / FOOD / ENVIRONMENT

hargreaves_samani_et0_mm_day(tmax_c, tmin_c, tmean_c, ra_mj_m2_day)
soil_porosity_fraction(bulk_density_kg_m3, particle_density_kg_m3=2650)
soil_water_content_fraction(water_volume_m3, soil_volume_m3)
food_moisture_percent(wet_sample_mass_g, dry_matter_mass_g, basis="wet")
water_activity_from_equilibrium_rh(relative_humidity_percent)
co2_from_oxidized_carbon_kg(carbon_mass_kg, oxidation_fraction=1.0)

MEDICINE / STATISTICS / POPULATION

diagnostic_test_metrics(true_positive, false_positive, true_negative, false_negative)
gini_coefficient(values)
population_exponential_projection(initial_population, growth_rate_per_time, elapsed_time)
    Undefined diagnostic ratios are returned as None with an explanation.

GEOLOGY / OPTICS / MECHANICS / ELECTROCHEMISTRY

seismic_energy_j(moment_magnitude)
photon_energy_j(wavelength_m)
snell_refracted_angle_deg(n_incident, n_transmitted, incident_angle_deg)
thin_lens_image_distance_m(focal_length_m, object_distance_m)
stress_from_force_pa(force_n, area_m2)
engineering_strain(initial_length_m, final_length_m)
factor_of_safety(strength_pa, working_stress_pa)
sensible_heat_j(mass_kg, specific_heat_j_kg_k, temperature_change_k)
latent_heat_j(mass_kg, latent_heat_j_kg)
nernst_potential_v(standard_potential_v, temperature_k, electrons_transferred, reaction_quotient)
solution_dilution_molarity(stock_molarity, stock_volume_l, final_volume_l)
percent_yield(actual_yield, theoretical_yield)


MICROBIOLOGY / PHARMACOKINETICS

microbial_population(initial_count, growth_rate_per_h, elapsed_h)
microbial_doubling_time_h(growth_rate_per_h)
microbial_log_reduction(start_count, end_count)
pharmacokinetic_loading_dose_mg(target_concentration_mg_l, volume_distribution_l, bioavailability=1.0)
pharmacokinetic_maintenance_rate_mg_h(clearance_l_h, target_concentration_mg_l, bioavailability=1.0)
pharmacokinetic_half_life_h(volume_distribution_l, clearance_l_h)
    Exponential population models and one-compartment PK estimates, with explicit units.

OCEANOGRAPHY / ACOUSTICS

seawater_density_kg_m3(temperature_c, salinity_psu)
ocean_depth_from_gauge_pressure_m(pressure_kpa, density_kg_m3=1025, gravity_m_s2=9.80665)
acoustic_sound_pressure_level_db(rms_pressure_pa, reference_pressure_pa=20e-6)
acoustic_pressure_from_spl_pa(level_db, reference_pressure_pa=20e-6)
doppler_frequency_hz(source_frequency_hz, sound_speed_m_s, source_toward_observer_m_s=0, observer_toward_source_m_s=0)
    EOS-80 density is the atmospheric-pressure approximation; depth uses constant density/gravity.
    Doppler velocities are positive when moving toward the other object.

WIKIPEDIA SEARCH (MEDIAWIKI API + NETWORK)

wikipedia_status()
    Report that the built-in MediaWiki API client is available.
wikipedia_search(query, results=5, language="en")
wikipedia_summary(query, sentences=3, language="en")
wikipedia_page_info(title, language="en", include_content=False)
wikipedia_article(title, language=None)
    Search titles, fetch summaries, page details, or full article text.
    Full articles are formatted with wrapped paragraphs, section headings, and lists.
    Uses the requests package and requires internet access. Install requests with python -m pip install requests.
    Calls use the public MediaWiki API; internet access is required.

[bold yellow]ADVANCED JAX / DIFFERENTIABLE COMPUTING[/bold yellow]
────────────────────────────────────────────────────────────

diffrax_ode(...)
    Solve advanced differential equations.

diffrax_solution(...)
    Inspect a Diffrax solution.

diffrax_grid(...)
    Evaluate a solution on a grid.

advanced_ode_report(...)
    Generate an advanced ODE report.

dynamiqs_basis(...)
    Create quantum basis states.

dynamiqs_fock(...)
    Create Fock states.

dynamiqs_annihilation(...)
    Create annihilation operators.

dynamiqs_creation(...)
    Create creation operators.

dynamiqs_number(...)
    Create number operators.

dynamiqs_density(...)
    Create density matrices.

equinox_array(...)
    Create Equinox-compatible arrays.

equinox_mlp(...)
    Create a simple neural network.

equinox_gradient(...)
    Calculate gradients.

equinox_jit(...)
    Run JIT-compiled calculations.

lineax_solve(...)
    Solve linear systems with Lineax.

lineax_least_squares(...)
    Perform least-squares calculations.

optimistix_root(...)
    Find roots using Optimistix.

optimistix_minimize(...)
    Perform optimization using Optimistix.

optimized_einsum(...)
    Perform optimized Einstein summation.

optimized_einsum_path(...)
    Inspect an optimized contraction path.

emcee_sample(...)
    Run MCMC sampling.

emcee_chain(...)
    Inspect MCMC chains.

emcee_log_probability(...)
    Evaluate MCMC log probabilities.

emcee_autocorrelation(...)
    Analyze MCMC autocorrelation.

formulaic_model(...)
    Create statistical model matrices.

formulaic_design_matrix(...)
    Generate design matrices.

gudhi_simplex_tree(...)
    Create a simplicial complex.

gudhi_summary(...)
    Summarize a topological structure.

gudhi_betti_numbers(...)
    Calculate Betti numbers.

gudhi_persistence(...)
    Calculate persistent homology.

gudhi_intervals(...)
    Inspect persistence intervals.

topoly_status()
    Show topological analysis package status.


────────────────────────────────────────────────────────────
[bold yellow]STATISTICS & OPTIMIZATION[/bold yellow]
────────────────────────────────────────────────────────────

statistical_summary(...)
    Generate statistical summaries.

z_scores(...)
    Calculate z-scores.

covariance_matrix(...)
    Calculate covariance matrices.

pearson_correlation(...)
    Calculate Pearson correlation.

spearman_correlation(...)
    Calculate Spearman correlation.

t_test(...)
    Perform t-tests.

chi_square_test(...)
    Perform chi-square tests.

linear_regression(...)
    Perform linear regression.

integer_grid_search(...)
    Search integer parameter combinations.

maximize_function(...)
    Maximize a numerical function.

statsmodels_describe(...)
    Generate Statsmodels descriptive statistics.

statsmodels_ols(...)
    Perform ordinary least-squares regression.

statsmodels_summary(...)
    Generate a complete regression summary.

statsmodels_logistic(...)
    Perform logistic regression.

statsmodels_poisson(...)
    Perform Poisson regression.

statsmodels_glm(...)
    Create generalized linear models.

statsmodels_anova(...)
    Perform ANOVA.

statsmodels_correlation(...)
    Calculate statistical correlations.

statsmodels_acf(...)
    Calculate autocorrelation.

statsmodels_pacf(...)
    Calculate partial autocorrelation.

statsmodels_arima(...)
    Perform ARIMA modeling.

statsmodels_forecast(...)
    Generate time-series forecasts.

statsmodels_sarimax(...)
    Perform SARIMAX modeling.

statsmodels_adf(...)
    Perform Augmented Dickey-Fuller tests.

statsmodels_kpss(...)
    Perform KPSS tests.

durbin_watson(...)
    Calculate the Durbin-Watson statistic.

variance_inflation(...)
    Calculate variance inflation factors.

normality_test(...)
    Test data for normality.

pulp_create(...)
    Create an optimization problem.

pulp_variable(...)
    Create an optimization variable.

pulp_solve(...)
    Solve a linear optimization problem.

pulp_values(...)
    Display optimization variable values.

pulp_objective(...)
    Display the optimization objective.

pulp_constraints(...)
    Display optimization constraints.

pulp_knapsack(...)
    Solve a knapsack optimization problem.

demes_load(...)
    Load a demographic model.

demes_load_string(...)
    Load a demographic model from text.

demes_summary(...)
    Summarize a demographic model.

demes_validate(...)
    Validate a demographic model.

demes_graph_info(...)
    Inspect demographic graph information.

cpsat_logutils_status()
    Show CP-SAT logging utility status.


────────────────────────────────────────────────────────────
[bold yellow]BIOLOGY & BIOINFORMATICS[/bold yellow]
────────────────────────────────────────────────────────────

anndata_create(...)
    Create an AnnData object.

anndata_summary(...)
    Summarize an AnnData dataset.

anndata_concat(...)
    Combine AnnData datasets.

biom_create(...)
    Create a BIOM table.

biom_summary(...)
    Summarize a BIOM table.

biopython_sequence(...)
    Create and inspect biological sequences.

biopython_reverse_complement(...)
    Calculate a DNA reverse complement.

biopython_translate(...)
    Translate DNA/RNA sequences.

biopython_gc(...)
    Calculate GC content.

biopython_alignment(...)
    Perform sequence alignment.

bioregistry_normalize(...)
    Normalize biological identifiers.

biotite_sequence(...)
    Create biological sequences with Biotite.

dendropy_tree(...)
    Load or create phylogenetic trees.

dendropy_summary(...)
    Summarize a phylogenetic tree.

dendropy_mrca(...)
    Find the most recent common ancestor.

msprime_ancestry(...)
    Simulate ancestry.

msprime_mutations(...)
    Simulate mutations.

pybedtools_sort(...)
    Sort genomic intervals.

pybedtools_intersect(...)
    Intersect genomic intervals.

pysam_fasta(...)
    Read FASTA files.

pysam_vcf(...)
    Read VCF files.

pysam_bam(...)
    Read BAM files.

scanpy_normalize(...)
    Normalize single-cell data.

scanpy_log(...)
    Log-transform single-cell data.

scanpy_pca(...)
    Perform PCA on single-cell data.

skbio_dna(...)
    Work with DNA sequences.

skbio_rna(...)
    Work with RNA sequences.

skbio_protein(...)
    Work with protein sequences.

tskit_summary(...)
    Summarize a tree sequence.


────────────────────────────────────────────────────────────
[bold yellow]CHEMISTRY & MATERIALS[/bold yellow]
────────────────────────────────────────────────────────────

pymatgen_composition(formula)
    Analyze a chemical composition.

pymatgen_lattice(...)
    Create a crystal lattice.

spglib_spacegroup(...)
    Determine crystal symmetry and space group.

rdkit_molecule(smiles)
    Create an RDKit molecule.

rdkit_formula(smiles)
    Calculate molecular formula from SMILES.

rdkit_molecular_weight(smiles)
    Calculate molecular weight from SMILES.

rdkit_canonical_smiles(smiles)
    Generate canonical SMILES.

chemparse_formula(formula)
    Parse a chemical formula.

chempy_molecular_weight(formula)
    Calculate molecular weight with Chempy.

pubchem_search(query, namespace="name")
    Search PubChem.

radioactive_nuclide(nuclide)
    Analyze a radioactive nuclide.

radioactive_half_life(nuclide)
    Calculate/display radioactive half-life.

radioactive_decay_data(nuclide)
    Display radioactive decay information.

plasma_particle_info(particle)
    Display particle information from PlasmaPy.

ase_atoms(symbols, positions=None)
    Create an ASE atomic structure.

ase_distance(atoms, atom1, atom2)
    Calculate atomic distances.

ase_cell(atoms)
    Inspect an ASE unit cell.

cross_package_formula_report(formula)
    Compare chemical formula information from
    multiple chemistry packages.

cross_package_molecule_report(smiles)
    Combine molecular information from multiple packages.

cross_package_crystal_report(formula)
    Generate a combined crystal/material report.


────────────────────────────────────────────────────────────
[bold yellow]MOLECULAR DYNAMICS & SIMULATION[/bold yellow]
────────────────────────────────────────────────────────────

openmm_status()
    Show OpenMM availability.

openmm_platforms()
    Show available OpenMM computation platforms.

openmm_simple_system(...)
    Create a simple OpenMM molecular system.

mdanalysis_load(topology, trajectory=None)
    Load molecular dynamics data.

mdanalysis_atom_count(...)
    Count atoms in a molecular system.

mdanalysis_residue_count(...)
    Count residues.

mdanalysis_center_of_mass(...)
    Calculate center of mass.

mdanalysis_radius_of_gyration(...)
    Calculate radius of gyration.

mdtraj_load(filename, top=None)
    Load an MDTraj trajectory.

mdtraj_distance(...)
    Calculate distances between atoms.

mdtraj_rmsd(...)
    Calculate RMSD.

freud_box(box_size)
    Create a freud simulation box.

freud_rdf(...)
    Calculate a radial distribution function.

brian2_neuron(...)
    Create and simulate a simple Brian2 neuron.

mdapy_status()
    Show mdapy availability.

mmtf_status()
    Show MMTF support status.

brian2_status()
    Show Brian2 availability.

nengo_status()
    Show Nengo availability.

neo_status()
    Show Neo availability.

elephant_status()
    Show Elephant availability.

pynapple_status()
    Show Pynapple availability.

pynwb_status()
    Show NWB support status.


────────────────────────────────────────────────────────────
[bold yellow]GEOSPATIAL / GIS / GEOSCIENCE[/bold yellow]
────────────────────────────────────────────────────────────

geo_distance(...)
    Calculate geographic distance.

geo_distance_km(...)
    Calculate geographic distance in kilometers.

geo_distance_miles(...)
    Calculate geographic distance in miles.

geographiclib_inverse(...)
    Solve the geographic inverse problem.

geographiclib_direct(...)
    Solve the geographic direct problem.

coordinate_transform(...)
    Transform coordinates between CRS systems.

coordinate_transform_many(...)
    Transform multiple coordinates.

crs_information(...)
    Display CRS information.

geometry_point(...)
    Create a geometric point.

geometry_line(...)
    Create a geometric line.

geometry_polygon(...)
    Create a polygon.

geometry_area(...)
    Calculate geometry area.

geometry_length(...)
    Calculate geometry length.

geometry_buffer(...)
    Create a geometry buffer.

geometry_intersection(...)
    Find geometry intersections.

geometry_union(...)
    Combine geometries.

geometry_distance(...)
    Calculate geometry distance.

geometry_to_wkt(...)
    Convert geometry to WKT.

geometry_to_wkb(...)
    Convert geometry to WKB.

geopandas_dataframe(...)
    Create a GeoDataFrame.

geopandas_read(...)
    Read geospatial data.

geopandas_write(...)
    Write geospatial data.

geopandas_reproject(...)
    Reproject geospatial data.

geopandas_bounds(...)
    Find geographic bounds.

geopandas_spatial_join(...)
    Perform a spatial join.

raster_open(...)
    Open a raster dataset.

raster_info(...)
    Display raster information.

raster_read_band(...)
    Read a raster band.

raster_write(...)
    Write raster data.

raster_zonal_stats(...)
    Calculate zonal statistics.

osmnx_geocode(...)
    Geocode a location using OpenStreetMap.

osmnx_street_graph(...)
    Download/create a street network.

osmnx_graph_summary(...)
    Summarize a street graph.

osmnx_graph_to_gdfs(...)
    Convert a network to GeoDataFrames.

spatial_weights_knn(...)
    Create K-nearest-neighbor spatial weights.

spatial_weights_distance(...)
    Create distance-based spatial weights.

spatial_morans_i(...)
    Calculate Moran's I.

spatial_local_moran(...)
    Calculate Local Moran statistics.

classify_quantiles(...)
    Classify geographic data by quantiles.

classify_natural_breaks(...)
    Perform natural-breaks classification.

trajectory_summary(...)
    Summarize a well trajectory.

wellpath_import(...)
    Import well-path data.

wellpath_survey(...)
    Analyze well surveys.

welly_read(...)
    Read well-log data.

striplog_status()
    Show Striplog availability.

flopy_model_load(...)
    Load a groundwater model.

flopy_model_summary(...)
    Summarize a groundwater model.

gempy_status()
    Show GemPy availability.

gempy_engine_status()
    Show GemPy engine availability.

pyregion_read(...)
    Read astronomical/geospatial regions.

earthpy_status()
    Show EarthPy availability.

pydeck_status()
    Show PyDeck availability.

topologicpy_status()
    Show TopologicPy availability.

xyzservices_providers()
    List available map tile providers.

cross_package_coordinate_report(...)
    Generate a combined coordinate/CRS report.


────────────────────────────────────────────────────────────
[bold yellow]VISUALIZATION & SCIENTIFIC DATA[/bold yellow]
────────────────────────────────────────────────────────────

The visualization/data integration adds support for:

• Matplotlib
• Plotly
• Altair
• NumPy
• Xarray
• Dask Image
• scikit-image
• PyWavelets
• tifffile
• nibabel
• h5py
• HDMF
• Zarr
• PyArrow
• mrcfile
• PIMS
• Slicerator
• yt
• mpltern
• cmap
• cmasher
• cmyt
• colorspacious
• contourpy
• folium
• GridDataFormats
• PyAVM
• PySmeQcd
• trx-python

These packages provide tools for:

• Scientific plotting
• Interactive visualization
• Image processing
• Medical imaging
• Multidimensional arrays
• Wavelet analysis
• HDF5 data
• Zarr data
• TIFF images
• MRC microscopy data
• Neuroimaging
• Scientific file formats
• Interactive maps
• Large scientific datasets
• 3D scientific visualization


────────────────────────────────────────────────────────────
[bold yellow]PACKAGE MANAGEMENT & DIAGNOSTICS[/bold yellow]
────────────────────────────────────────────────────────────

packages()
    List scientific packages known to Dave.

packages(category)
    List packages in a category.

packages(installed_only=True)
    Show only installed/available packages.

scientific_package_available(name)
    Check whether a package is available.

scientific_package_status()
    Display package installation/status information.

scientific_package_categories()
    Display scientific package categories.

package_category(name)
    Show a package's category.

scientific_package_report()
    Display a complete scientific package report.

all_scientific_package_status()
    Display the status of all supported packages.

astronomy_package_status()
    Check astronomy packages.

gis_part11_status()
    Check GIS/geoscience packages.

mdapy_status()
    Check molecular-dynamics packages.

topoly_status()
    Check topology packages.

openmm_status()
    Check OpenMM.

qmsolve_status()
    Check qmsolve.

final_scientific_selftest()
    Run the complete scientific package self-test.

astronomy_selftest()
    Run astronomy tests.

gis_part11_selftest()
    Run GIS/geoscience tests.

visualization_part10_selftest()
    Run visualization/data tests.


────────────────────────────────────────────────────────────
[bold yellow]CROSS-PACKAGE REPORTS[/bold yellow]
────────────────────────────────────────────────────────────

cross_package_formula_report(formula)
    Compare the same chemical formula across several
    chemistry/materials packages.

cross_package_molecule_report(smiles)
    Combine RDKit and PubChem molecular information.

cross_package_crystal_report(formula)
    Combine composition and materials information.

cross_package_coordinate_report(latitude, longitude)
    Combine geodesy and CRS information.

scientific_package_report()
    Show the overall scientific computing environment.


────────────────────────────────────────────────────────────
[bold green]TIP[/bold green]

Many scientific packages are optional. Dave will attempt to
load them only when their functionality is requested.

If a package is unavailable, Dave should report that package
as unavailable rather than preventing the rest of the
calculator from working.

Use:

    scientific_package_status()

or:

    final_scientific_selftest()

to check the scientific environment.

Use:

    scientific_package_report()

for a complete overview of the installed scientific ecosystem.

=========================================================
END OF HELP
=========================================================
"""

    help_text = help_text.replace(
        "Select one of the five interface languages with:", tr("language_help"))
    console.print(
        Panel.fit(
            help_text,
            title=tr("help"),
            border_style="cyan"
        )
    )
 

LOCALIZED_HELP_PAGES = {'en': 'DAVE — SCIENTIFIC CALCULATOR HELP\n'
       'LANGUAGE: Set with lang en, lang es, lang ja, lang zh, or lang fr. Function '
       'names are entered as shown in the command directory.\n'
       'USAGE: Enter an expression such as 2 + 2 or sqrt(81). Use help for this guide, '
       'selftest to check functions, history to view prior expressions, and quit to '
       'exit.\n'
       'SCIENCES: Mathematics, algebra, calculus, statistics, probability, astronomy, '
       'physics, chemistry, biology, physiology, medicine, pharmacokinetics, '
       'meteorology, climate, ecology, geology, geography, oceanography, engineering, '
       'materials, neuroscience, quantum science, signal processing, and visualization.\n'
       'WIKIPEDIA: wikipedia_search("topic"), wikipedia_summary("topic"), '
       'wikipedia_article("title"). Uses the MediaWiki API through requests.\n'
       'Install requests with python -m pip install requests; internet access is required.\n'
       'AVAILABLE FUNCTION COMMANDS:',
 'es': 'DAVE — AYUDA DE LA CALCULADORA CIENTÍFICA\n'
       'IDIOMA: Configúralo con lang en, lang es, lang ja, lang zh o lang fr. Introduce '
       'los nombres de función tal como aparecen en el directorio de comandos.\n'
       'USO: Escribe una expresión como 2 + 2 o sqrt(81). Usa help para esta guía, '
       'selftest para comprobar funciones, history para ver el historial y quit para '
       'salir.\n'
       'CIENCIAS: Matemáticas, álgebra, cálculo, estadística, probabilidad, astronomía, '
       'física, química, biología, fisiología, medicina, farmacocinética, meteorología, '
       'clima, ecología, geología, geografía, oceanografía, ingeniería, materiales, '
       'neurociencia, ciencia cuántica, procesamiento de señales y visualización.\n'
       'WIKIPEDIA: wikipedia_search("tema"), wikipedia_summary("tema"), '
       'wikipedia_article("título"). Requiere requests (python -m pip install requests) y conexión a internet.\n'
       'COMANDOS DE FUNCIONES DISPONIBLES:',
 'fr': 'DAVE — AIDE DE LA CALCULATRICE SCIENTIFIQUE\n'
       'LANGUE : Choisissez avec lang en, lang es, lang ja, lang zh ou lang fr. '
       'Saisissez les fonctions selon les noms du répertoire des commandes.\n'
       'UTILISATION : Saisissez une expression comme 2 + 2 ou sqrt(81). Tapez help pour '
       'ce guide, selftest pour tester les fonctions, history pour afficher l’historique '
       'et quit pour quitter.\n'
       'SCIENCES : Mathématiques, algèbre, calcul, statistiques, probabilités, '
       'astronomie, physique, chimie, biologie, physiologie, médecine, '
       'pharmacocinétique, météorologie, climat, écologie, géologie, géographie, '
       'océanographie, ingénierie, matériaux, neurosciences, science quantique, '
       'traitement du signal et visualisation.\n'
       'WIKIPÉDIA : wikipedia_search("sujet"), wikipedia_summary("sujet"), '
       'wikipedia_article("titre"). Nécessite requests (python -m pip install requests) et une connexion Internet.\n'
       'RÉPERTOIRE DES COMMANDES DE FONCTIONS DISPONIBLES :',
 'ja': 'DAVE — 科学計算機ヘルプ\n'
       '言語: lang en、lang es、lang ja、lang zh、lang frで設定します。関数名はコマンド一覧の表記どおりに入力します。\n'
       '使い方: 2 + 2 や sqrt(81) '
       'のような式を入力します。helpでこの案内、selftestで関数テスト、historyで履歴を表示し、quitで終了します。\n'
       '科学分野: '
       '数学、代数、微積分、統計、確率、天文学、物理学、化学、生物学、生理学、医学、薬物動態、気象、気候、生態学、地質学、地理学、海洋学、工学、材料科学、神経科学、量子科学、信号処理、可視化。\n'
       'Wikipedia: '
       'wikipedia_search("トピック")、wikipedia_summary("トピック")、wikipedia_article("記事名")。requestsパッケージとネット接続が必要です。\n'
       '利用可能な関数コマンド:',
 'zh': 'DAVE — 科学计算器帮助\n'
       '语言：使用 lang en、lang es、lang ja、lang zh 或 lang fr 设置。函数名称请按命令目录中的写法输入。\n'
       '使用：输入 2 + 2 或 sqrt(81) 等算式。输入 help 查看本指南，selftest 检查函数，history 查看历史，quit 退出。\n'
       '科学领域：数学、代数、微积分、统计、概率、天文学、物理、化学、生物、生理学、医学、药代动力学、气象、气候、生态、地质、地理、海洋学、工程、材料、神经科学、量子科学、信号处理和可视化。\n'
       '维基百科：wikipedia_search("主题")、wikipedia_summary("主题")、wikipedia_article("标题")。需要 requests 软件包（python -m pip install requests）和互联网连接。\n'
       '可用函数命令目录：'}
ABOUT_TEXTS = {'en': 'Dave is a scientific calculator with mathematical, statistical, and scientific '
       'tools. Set the interface language with lang en, lang es, lang ja, lang zh, or '
       'lang fr. Function names remain unchanged so they can be entered as calculator '
       'commands.',
 'es': 'Dave es una calculadora científica con herramientas matemáticas, estadísticas y '
       'científicas. Configura el idioma con lang en, lang es, lang ja, lang zh o lang '
       'fr. Los nombres de las funciones no cambian y se introducen como comandos de la '
       'calculadora.',
 'fr': 'Dave est une calculatrice scientifique dotée d’outils mathématiques, '
       'statistiques et scientifiques. Choisissez la langue avec lang en, lang es, lang '
       'ja, lang zh ou lang fr. Les noms des fonctions restent inchangés pour être '
       'saisis comme commandes.',
 'ja': 'Daveは数学、統計、科学のツールを備えた科学計算機です。lang en、lang es、lang ja、lang zh、lang '
       'frで表示言語を設定します。関数名は計算コマンドとして入力できるよう変更しません。',
 'zh': 'Dave 是一款提供数学、统计和科学工具的科学计算器。使用 lang en、lang es、lang ja、lang zh 或 lang fr '
       '设置界面语言。函数名称保持不变，以便作为计算器命令输入。'}
ABOUT_TITLES = {'en': 'About Dave',
 'es': 'Acerca de Dave',
 'fr': 'À propos de Dave',
 'ja': 'Daveについて',
 'zh': '关于 Dave'}

def show_help():
    """Display complete English reference or localized help and command directory."""
    if language == "en":
        return _show_help_full_english()
    names = sorted(name for name, value in variables.items() if callable(value))
    text = LOCALIZED_HELP_PAGES[language] + "\n" + ", ".join(names)
    console.print(Panel.fit(text, title=tr("help"), border_style="cyan"))


def show_about():
    """Display Dave information in the currently selected language."""
    console.print(Panel.fit(ABOUT_TEXTS[language], title=ABOUT_TITLES[language], border_style="yellow"))


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

def mandarin():
    return set_language("zh")

def chinese():
    return set_language("zh")

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

def tr(key, **format_values):
    """Return a short interface label in the selected Dave language."""
    text = languages.get(language, languages["en"]).get(key, languages["en"].get(key, key))
    return text.format(**format_values) if format_values else text


def set_language(lang):
    """Select English, Spanish, Japanese, Mandarin Chinese, or French."""
    global language
    code = str(lang).strip().lower().replace("_", "-")
    aliases = {
        "english": "en", "spanish": "es", "japanese": "ja", "jp": "ja",
        "mandarin": "zh", "chinese": "zh", "中文": "zh", "zh-cn": "zh",
        "zh-hans": "zh", "french": "fr",
    }
    code = aliases.get(code, code)
    if code not in languages:
        return tr("unsupported_language")
    language = code
    return tr("language_set", name=language_names[code])


def _language_selftest():
    """Exercise each supported language and restore the current selection."""
    global language
    original = language
    try:
        required_keys = set(languages["en"])
        for code, table in languages.items():
            if required_keys - set(table) or any(not table.get(key) for key in required_keys):
                raise AssertionError(f"Incomplete interface translations for {code}.")
        aliases = {"English": "en", "Spanish": "es", "Japanese": "ja",
                   "Mandarin": "zh", "French": "fr"}
        for name, code in aliases.items():
            set_language(name)
            if language != code or not tr("welcome") or not tr("prompt"):
                raise AssertionError(f"Language selection failed for {name}.")
        wrappers = {"en": english, "es": spanish, "ja": japanese,
                    "zh": mandarin, "fr": french}
        expected_help = {"en": "Help", "es": "Ayuda", "ja": "ヘルプ",
                         "zh": "帮助", "fr": "Aide"}
        for code, wrapper in wrappers.items():
            wrapper()
            if language != code or tr("help") != expected_help[code]:
                raise AssertionError(f"Language wrapper or translation failed for {code}.")
        command_names = set(variables)
        for code in ("en", "es", "ja", "zh", "fr"):
            set_language(code)
            if set(variables) != command_names:
                raise AssertionError(f"Calculator command set changed in language {code}.")
            _expression_command_selftest()
            result = float(_evaluate_expression_command("sqrt(81)"))
            if result != 9.0:
                raise AssertionError(f"Calculator expression failed in language {code}.")
            if code not in LOCALIZED_HELP_PAGES or code not in ABOUT_TEXTS:
                raise AssertionError(f"Missing localized help or About text for {code}.")
        set_language("zh-CN")
        if language != "zh":
            raise AssertionError("zh-CN must select Mandarin Chinese.")
        return "five interface languages and aliases passed"
    finally:
        language = original


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
language_names = {"en": "English", "es": "Español", "ja": "日本語",
                  "zh": "中文 (Mandarin)", "fr": "Français"}
languages = {
    "en": {"welcome": "Welcome", "about": "Dave scientific calculator", "goodbye": "Goodbye",
           "help": "Help", "answer": "Answer", "error": "Error", "prompt": "Enter an equation or type help:",
           "enter_equation": "Enter equation here:", "unknown_command": "Unknown command",
           "language_set": "Language set to {name}.", "unsupported_language": "Unsupported language. Use en, es, ja, zh, or fr.",
           "no_history": "No history yet."},
    "es": {"welcome": "Bienvenido", "about": "Calculadora científica Dave", "goodbye": "Adiós",
           "help": "Ayuda", "answer": "Respuesta", "error": "Error", "prompt": "Escribe una ecuación o ayuda:",
           "enter_equation": "Ingrese una ecuación:", "unknown_command": "Comando desconocido",
           "language_set": "Idioma cambiado a {name}.", "unsupported_language": "Idioma no compatible. Usa en, es, ja, zh o fr.",
           "no_history": "Aún no hay historial."},
    "ja": {"welcome": "ようこそ", "about": "Dave 科学計算機", "goodbye": "さようなら",
           "help": "ヘルプ", "answer": "答え", "error": "エラー", "prompt": "式を入力するか、help と入力してください:",
           "enter_equation": "式を入力してください:", "unknown_command": "不明なコマンド",
           "language_set": "言語を{name}に設定しました。", "unsupported_language": "未対応の言語です。en、es、ja、zh、frを指定してください。",
           "no_history": "履歴はありません。"},
    "zh": {"welcome": "欢迎", "about": "Dave 科学计算器", "goodbye": "再见",
           "help": "帮助", "answer": "答案", "error": "错误", "prompt": "请输入算式或输入 help：",
           "enter_equation": "请输入算式：", "unknown_command": "未知命令",
           "language_set": "语言已设为{name}。", "unsupported_language": "不支持此语言。请使用 en、es、ja、zh 或 fr。",
           "no_history": "暂无历史记录。"},
    "fr": {"welcome": "Bienvenue", "about": "Calculatrice scientifique Dave", "goodbye": "Au revoir",
           "help": "Aide", "answer": "Réponse", "error": "Erreur", "prompt": "Saisissez une équation ou help :",
           "enter_equation": "Saisissez une équation :", "unknown_command": "Commande inconnue",
           "language_set": "Langue définie sur {name}.", "unsupported_language": "Langue non prise en charge. Utilisez en, es, ja, zh ou fr.",
           "no_history": "Aucun historique pour le moment."},
}
for _code, _translations in {'en': {'goodbye': 'Goodbye, and thank you for using Dave!', 'about_text': 'You are running Dave Version 1.0.8.', 'degree_enabled': 'Degree mode enabled', 'radian_enabled': 'Radian mode enabled', 'angle_degrees': 'Angle mode set to degrees.', 'angle_radians': 'Angle mode set to radians.', 'usage_abs': 'Usage: absolute value of <expression> (for example, absolute value of -5).', 'usage_abs_empty': 'Usage: absolute value of <expression>.', 'graph_error': 'Graph error', 'graph3d_error': '3D graph error', 'wikipedia_error': 'Wikipedia error', 'assignment_error': 'Assignment error', 'symbol_overwrite': 'Cannot overwrite symbolic variables x, y, or z', 'language_help': 'Choose the interface language with lang en, lang es, lang ja, lang zh, or lang fr. Command and scientific function names remain unchanged.'}, 'es': {'goodbye': '¡Adiós y gracias por usar Dave!', 'about_text': 'Estás usando Dave versión 1.0.8.', 'degree_enabled': 'Modo de grados activado', 'radian_enabled': 'Modo de radianes activado', 'angle_degrees': 'Modo angular establecido en grados.', 'angle_radians': 'Modo angular establecido en radianes.', 'usage_abs': 'Uso: absolute value of <expresión> (por ejemplo, absolute value of -5).', 'usage_abs_empty': 'Uso: absolute value of <expresión>.', 'graph_error': 'Error de gráfica', 'graph3d_error': 'Error de gráfica 3D', 'wikipedia_error': 'Error de Wikipedia', 'assignment_error': 'Error de asignación', 'symbol_overwrite': 'No se pueden sobrescribir las variables simbólicas x, y o z', 'language_help': 'Elige el idioma de la interfaz con lang en, lang es, lang ja, lang zh o lang fr. Los nombres de comandos y funciones científicas no cambian.'}, 'ja': {'goodbye': 'Daveをご利用いただき、ありがとうございました。', 'about_text': 'Dave バージョン1.0.8を実行中です。', 'degree_enabled': '度数法を有効にしました', 'radian_enabled': 'ラジアン法を有効にしました', 'angle_degrees': '角度モードを度数法に設定しました。', 'angle_radians': '角度モードをラジアン法に設定しました。', 'usage_abs': '使い方: absolute value of <式>（例: absolute value of -5）。', 'usage_abs_empty': '使い方: absolute value of <式>。', 'graph_error': 'グラフエラー', 'graph3d_error': '3Dグラフエラー', 'wikipedia_error': 'Wikipediaエラー', 'assignment_error': '代入エラー', 'symbol_overwrite': '記号変数 x、y、z は上書きできません', 'language_help': 'lang en、lang es、lang ja、lang zh、lang fr で表示言語を選択します。コマンド名と科学関数名は変更されません。'}, 'zh': {'goodbye': '再见，感谢使用 Dave！', 'about_text': '当前运行的是 Dave 1.0.8 版。', 'degree_enabled': '已启用角度制', 'radian_enabled': '已启用弧度制', 'angle_degrees': '角度模式已设为角度制。', 'angle_radians': '角度模式已设为弧度制。', 'usage_abs': '用法：absolute value of <表达式>（例如 absolute value of -5）。', 'usage_abs_empty': '用法：absolute value of <表达式>。', 'graph_error': '绘图错误', 'graph3d_error': '三维绘图错误', 'wikipedia_error': '维基百科错误', 'assignment_error': '赋值错误', 'symbol_overwrite': '不能覆盖符号变量 x、y 或 z', 'language_help': '使用 lang en、lang es、lang ja、lang zh 或 lang fr 选择界面语言。命令名和科学函数名保持不变。'}, 'fr': {'goodbye': 'Au revoir et merci d’utiliser Dave !', 'about_text': 'Dave version 1.0.8 est en cours d’exécution.', 'degree_enabled': 'Mode degrés activé', 'radian_enabled': 'Mode radians activé', 'angle_degrees': 'Mode angulaire réglé en degrés.', 'angle_radians': 'Mode angulaire réglé en radians.', 'usage_abs': 'Utilisation : absolute value of <expression> (par exemple, absolute value of -5).', 'usage_abs_empty': 'Utilisation : absolute value of <expression>.', 'graph_error': 'Erreur de graphique', 'graph3d_error': 'Erreur de graphique 3D', 'wikipedia_error': 'Erreur Wikipédia', 'assignment_error': 'Erreur d’affectation', 'symbol_overwrite': 'Impossible de remplacer les variables symboliques x, y ou z', 'language_help': 'Choisissez la langue de l’interface avec lang en, lang es, lang ja, lang zh ou lang fr. Les noms des commandes et fonctions scientifiques restent inchangés.'}}.items():
    languages[_code].update(_translations)

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
    "english": english, "spanish": spanish, "japanese": japanese,
    "mandarin": mandarin, "french": french,
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

    # ================= METEOROLOGY =================

    "metpy_relative_humidity": metpy_relative_humidity,
    "metpy_wind_chill": metpy_wind_chill,

    # ================= PHYSIOLOGY =================

    "bmi": bmi,
    "mifflin_st_jeor": mifflin_st_jeor,
    "cardiac_output": cardiac_output,
    "minute_ventilation": minute_ventilation,
    "epidemiology_2x2": epidemiology_2x2,
    "number_needed_to_treat": number_needed_to_treat,
    "drug_concentration_after_dose": drug_concentration_after_dose,
    "mean_arterial_pressure": mean_arterial_pressure,
    "shannon_diversity": shannon_diversity,
    "simpson_diversity": simpson_diversity,
    "pielou_evenness": pielou_evenness,
    "logistic_population": logistic_population,
    "reynolds_number": reynolds_number,
    "control_natural_frequency": control_natural_frequency,
    "control_damping_ratio": control_damping_ratio,
    "cantilever_tip_deflection": cantilever_tip_deflection,
    "beam_bending_stress": beam_bending_stress,
    "weight_based_dose": weight_based_dose,
    "convert_mass_concentration": convert_mass_concentration,
    "glucose_mg_dl_to_mmol_l": glucose_mg_dl_to_mmol_l,
    "glucose_mmol_l_to_mg_dl": glucose_mmol_l_to_mg_dl,
    "cholesterol_mg_dl_to_mmol_l": cholesterol_mg_dl_to_mmol_l,
    "creatinine_mg_dl_to_umol_l": creatinine_mg_dl_to_umol_l,
    "heat_conduction_rate": heat_conduction_rate,
    "heat_convection_rate": heat_convection_rate,
    "heat_radiation_rate": heat_radiation_rate,
    "carnot_efficiency": carnot_efficiency,
    "volumetric_thermal_expansion": volumetric_thermal_expansion,
    "ohms_law": ohms_law,
    "rc_time_constant": rc_time_constant,
    "equivalent_resistance": equivalent_resistance,
    "sklearn_logistic_classification": sklearn_logistic_classification,
    "hargreaves_samani_et0_mm_day": hargreaves_samani_et0_mm_day,
    "soil_porosity_fraction": soil_porosity_fraction,
    "soil_water_content_fraction": soil_water_content_fraction,
    "food_moisture_percent": food_moisture_percent,
    "water_activity_from_equilibrium_rh": water_activity_from_equilibrium_rh,
    "diagnostic_test_metrics": diagnostic_test_metrics,
    "co2_from_oxidized_carbon_kg": co2_from_oxidized_carbon_kg,
    "seismic_energy_j": seismic_energy_j,
    "photon_energy_j": photon_energy_j,
    "snell_refracted_angle_deg": snell_refracted_angle_deg,
    "thin_lens_image_distance_m": thin_lens_image_distance_m,
    "stress_from_force_pa": stress_from_force_pa,
    "engineering_strain": engineering_strain,
    "factor_of_safety": factor_of_safety,
    "sensible_heat_j": sensible_heat_j,
    "latent_heat_j": latent_heat_j,
    "nernst_potential_v": nernst_potential_v,
    "solution_dilution_molarity": solution_dilution_molarity,
    "percent_yield": percent_yield,
    "gini_coefficient": gini_coefficient,
    "population_exponential_projection": population_exponential_projection,
    "wikipedia_status": wikipedia_status,
    "wikipedia_search": wikipedia_search,
    "wikipedia_summary": wikipedia_summary,
    "wikipedia_page_info": wikipedia_page_info,
    "wikipedia_article": wikipedia_article,
    "michaelis_menten_velocity": michaelis_menten_velocity,
    "henderson_hasselbalch": henderson_hasselbalch,
    "beer_lambert_absorbance": beer_lambert_absorbance,
    "osmotic_pressure_kpa": osmotic_pressure_kpa,
    "magnus_relative_humidity": magnus_relative_humidity,
    "magnus_dewpoint_c": magnus_dewpoint_c,
    "isa_pressure_altitude_pa": isa_pressure_altitude_pa,
    "hydrostatic_pressure_kpa": hydrostatic_pressure_kpa,
    "geothermal_temperature_c": geothermal_temperature_c,
    "signal_rms": signal_rms,
    "signal_peak_to_peak": signal_peak_to_peak,
    "signal_snr_db": signal_snr_db,
    "zero_crossing_rate": zero_crossing_rate,
    "sample_rate_hz": sample_rate_hz,
    "sound_intensity_level_db": sound_intensity_level_db,
    "sound_intensity_from_db": sound_intensity_from_db,
    "capacitor_energy_j": capacitor_energy_j,
    "inductor_energy_j": inductor_energy_j,
    "capacitive_reactance_ohm": capacitive_reactance_ohm,
    "inductive_reactance_ohm": inductive_reactance_ohm,
    "thermal_diffusivity_m2_s": thermal_diffusivity_m2_s,
    "cohens_d": cohens_d,
    "standard_error_of_mean": standard_error_of_mean,
    "acoustic_sound_pressure_level_db": acoustic_sound_pressure_level_db,
    "acoustic_pressure_from_spl_pa": acoustic_pressure_from_spl_pa,
    "doppler_frequency_hz": doppler_frequency_hz,
    "microbial_population": microbial_population,
    "microbial_doubling_time_h": microbial_doubling_time_h,
    "microbial_log_reduction": microbial_log_reduction,
    "pharmacokinetic_loading_dose_mg": pharmacokinetic_loading_dose_mg,
    "pharmacokinetic_maintenance_rate_mg_h": pharmacokinetic_maintenance_rate_mg_h,
    "pharmacokinetic_half_life_h": pharmacokinetic_half_life_h,
    "seawater_density_kg_m3": seawater_density_kg_m3,
    "ocean_depth_from_gauge_pressure_m": ocean_depth_from_gauge_pressure_m,
    "gsw_seawater_properties": gsw_seawater_properties,
    "sklearn_train_test_split": sklearn_train_test_split,
    "sklearn_classification_report": sklearn_classification_report,
    "sklearn_linear_regression": sklearn_linear_regression,

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

def _evaluate_expression_command(expression):
    """Evaluate an expression through Dave's real expression namespace."""
    expr = sp.sympify(expression, locals={**variables, **user_vars})
    expr = sp.simplify(expr)
    if expr.has(sp.zoo):
        raise ZeroDivisionError("Division by zero")
    if hasattr(expr, "evalf") and expr.is_number:
        expr = expr.evalf()
    return expr


def _expression_command_selftest():
    """Verify representative built-in and added science commands by value."""
    import math
    checks = (
        ("2 + 2", 4.0),
        ("sqrt(81)", 9.0),
        ("soil_porosity_fraction(1325, 2650)", 0.5),
        ("bmi(70, 1.75)", 70 / (1.75 ** 2)),
        ("photon_energy_j(5e-7)", 6.62607015e-34 * 299792458 / 5e-7),
        ("microbial_population(100, 0.6931471805599453, 3)", 800.0),
        ("seawater_density_kg_m3(15, 35)", 1025.972753865),
        ("pharmacokinetic_half_life_h(10, 2)", math.log(2) * 5),
        ("acoustic_sound_pressure_level_db(0.02)", 60.0),
    )
    for command, expected in checks:
        actual = float(_evaluate_expression_command(command))
        if not math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-30):
            raise AssertionError(f"Command {command!r}: expected {expected}, got {actual}.")
    return f"{len(checks)} calculator commands evaluated to expected results"


# =========================================================
# MAIN LOOP
# =========================================================

while True:

    problem = input("\n" + tr("prompt") + " ").strip()

    if problem == "":
        continue

    # ---------------- HELP ----------------
    if problem.lower() in ("help", "ayuda", "aide", "ヘルプ", "帮助", "ayuda", "aide"):
        show_help()
        continue

    # ---------------- ABOUT ----------------
    elif problem.lower() == "about":
        show_about()
        continue

    # ---------------- ELEMENTS ----------------
    elif problem.strip() == "elements()":
        elements()
        continue

    # ---------------- LANGUAGE ----------------
    elif problem.lower().startswith("lang "):
        parts = problem.split(maxsplit=1)
        console.print("[green]" + set_language(parts[1]) + "[/green]" if len(parts) > 1 else
                      "[red]" + tr("unsupported_language") + "[/red]")
        continue

    # ---------------- TIME ----------------
    elif problem == "time":
        console.print(datetime.datetime.now().strftime("%H:%M:%S"))
        continue

    elif problem == "date":
        console.print(datetime.datetime.now().strftime("%Y-%m-%d"))
        continue

    elif problem == "month":
        month = datetime.datetime.now().month
        month_names = {
            "en": "January February March April May June July August September October November December",
            "es": "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre",
            "fr": "janvier février mars avril mai juin juillet août septembre octobre novembre décembre",
            "ja": "1月 2月 3月 4月 5月 6月 7月 8月 9月 10月 11月 12月",
            "zh": "一月 二月 三月 四月 五月 六月 七月 八月 九月 十月 十一月 十二月",
        }
        console.print(month_names[language].split()[month - 1])
        continue

    elif problem == "year":
        console.print(datetime.datetime.now().strftime("%Y"))
        continue

    # ---------------- ANGLE MODES ----------------
    elif problem == "deg":
        angle_mode = "deg"
        console.print("[cyan]" + tr("degree_enabled") + "[/cyan]")
        continue

    elif problem == "rad":
        angle_mode = "rad"
        console.print("[cyan]" + tr("radian_enabled") + "[/cyan]")
        continue

    # ---------------- HISTORY ----------------
    elif problem == "history":

        if not history:
            console.print("[yellow]" + tr("no_history") + "[/yellow]")

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
            console.print(f"[red]{tr('graph_error')}:[/red] {e}")

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
            console.print(f"[red]{tr('graph3d_error')}:[/red] {e}")

        continue
     

    # ---------------- QUIT ----------------
    elif problem.lower() in ["quit", "exit", "q", "salir", "終了", "退出", "quitter"]:

        console.print("[green]" + tr("goodbye") + "[/green]")
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
                    "[red]" + tr("symbol_overwrite") + "[/red]"
                )

                continue

            user_vars[var_name] = value

            with open(SAVE_FILE, "wb") as f:
                pickle.dump(user_vars, f)

            console.print(
                f"[cyan]{var_name}[/cyan] = {value}"
            )

        except Exception as e:
            console.print(f"[red]{tr('assignment_error')}:[/red] {e}")

        continue

    # ---------------- NORMAL EXPRESSIONS ----------------
    else:

        # Handle text commands first
        cmd = problem.strip().lower()

        if cmd == "absolute value":
            console.print(tr("usage_abs"))
            continue

        elif cmd.startswith("absolute value of "):
            value_expression = problem.strip()[len("absolute value of "):].strip()
            if not value_expression:
                console.print(tr("usage_abs_empty"))
                continue
            problem = f"abs({value_expression})"
            cmd = problem.lower()

        elif cmd in ("selftest", "selftest()"):
            selftest()
            continue

        if cmd == "help":
            show_help()
            continue

        elif cmd == "about":
            show_about()
            continue

        elif cmd == "deg":
            angle_mode = "deg"
            console.print("[green]" + tr("angle_degrees") + "[/green]")
            continue

        elif cmd == "rad":
            angle_mode = "rad"
            console.print("[green]" + tr("angle_radians") + "[/green]")
            continue

        elif cmd in ("quit", "exit", "q"):
            break

        if cmd.startswith(("wikipedia_search(", "wikipedia_summary(", "wikipedia_page_info(", "wikipedia_article(")):
            try:
                console.print(_execute_wikipedia_command(problem), markup=False)
            except Exception as e:
                console.print(f"[red]{tr('wikipedia_error')}:[/red] {e}")
            continue

        try:

            expr = _evaluate_expression_command(problem)

            console.print(
                Panel.fit(
                    str(expr),
                    title=tr("answer"),
                    border_style="green"
                )
            )

            variables["ans"] = expr
            history.append(f"{problem} = {expr}")

        except Exception as e:
            console.print(f"[red]{tr('error')}:[/red] {e}")
