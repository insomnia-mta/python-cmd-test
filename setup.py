from setuptools import find_packages, setup
import os

from demo import __version__

setup(
    name         = 'Imre',
    version      = __version__,
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
