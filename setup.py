from setuptools import setup
import os

VERSION = "0.5.0"


def write_version_py(version=VERSION, filename="colormaps/_version.py"):
    cnt = "# THIS FILE IS GENERATED FROM SETUP.PY\n" + '__version__ = "%(version)s"\n'
    with open(filename, "w") as f:
        f.write(cnt % {"version": version})


write_version_py()

setup(
    name="colormaps",
    author="Pratiman Patel",
    version=VERSION,
    author_email="pratiman_patel@hotmail.com",
    packages=[
        "colormaps",
    ],
    package_data={
        "colormaps": [
            "colormaps/ncar_ncl/*",
            "colormaps/cartocolors/*",
            "colormaps/cmocean/*",
            "colormaps/colorbrewer/*",
            "colormaps/cubehelix/*",
            "colormaps/scientific/*",
            "colormaps/tableau/*",
            "colormaps/sciviz/*",
            "colormaps/colorcet/*",
            "colormaps/cmasher/*",
            "colormaps/carbonplan/*",
        ],
    },
    data_files=[
        ("", ["LICENSE"]),
    ],
    url="https://pratiman-91.github.io/colormaps/",
    description="A collection of colormaps or color palettes for Python",
    install_requires=["matplotlib", "numpy", "packaging"],
)
