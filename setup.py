import os

from setuptools import setup

from setuptools.command.develop import develop
from setuptools.command.install import install

# from distutils.core import setup

setup(
    name='d3m_ibex',
    version='1.1.2',
    description='Named entity extraction',
    author='New Knowledge',
    packages=['d3m_ibex'],
    package_data={'d3m_ibex': ['exclude_words.txt']},
    include_package_data=True,
    install_requires=[
        'spacy==1.7.0',
        'flask>=1.0.2',
        'nose>=1.3.7'
    ],
)
