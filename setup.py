import os

from setuptools import setup

from setuptools.command.develop import develop
from setuptools.command.install import install

# from distutils.core import setup

setup(
    name='d3m_ibex',
    version='1.1.3',
    description='Named entity extraction',
    author='New Knowledge',
    packages=['d3m_ibex'],
    package_data={'d3m_ibex': ['exclude_words.txt']},
    include_package_data=True,
    install_requires=[
        'spacy==2.1.0',
        'flask>=1.0.2',
        'nose>=1.3.7'
    ],
    dependency_links=[
        'https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.1.0/en_core_web_md-2.1.0.tar.gz',
        'https://github.com/explosion/spacy-models/releases/download/es_core_news_md-2.1.0/es_core_news_md-2.1.0.tar.gz'
    ]
)
