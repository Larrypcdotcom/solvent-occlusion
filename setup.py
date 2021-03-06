# Created by Rui-Liang Lyu, April 14, 2020
#

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="solvent-occlusion",
    version="0.1.2",
    author="Rui-Liang Lyu",
    author_email="lyu.chemistry@tamu.edu",

    description="Calculating solvent occlusion of protein residues upon binding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lyu18/solvent-occlusion",

    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy>=1.17",
        "pandas>=0.24",
        "tqdm>=4.39"
    ]
)
