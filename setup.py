from setuptools import find_packages, setup
import os

setup(
    name         = 'Imre',
    version      = '1.0',
    author       = 'Tibor Simon',
    author_email = 'tibor@tiborsimon.io',
    packages     = find_packages(),
    install_requires=[
          'termcolor'
    ],
    entry_points={
        'console_scripts': [
            'imre = demo.cli:imre'
        ]
    }
)
