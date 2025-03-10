import pathlib

from setuptools import setup

import hyfetch

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="HyFetch",
    version=hyfetch.__version__,
    description="neofetch with flags <3",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hykilpikonna/HyFetch",
    author="Azalea Gui",
    author_email="me@hydev.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=['hyfetch'],
    package_data={'hyfetch': ['hyfetch/*']},
    include_package_data=True,
    install_requires=['setuptools', 'hypy_utils>=1.0.6', 'typing_extensions'],
    entry_points={
        "console_scripts": [
            "hyfetch=hyfetch.main:run",
        ]
    },
)
