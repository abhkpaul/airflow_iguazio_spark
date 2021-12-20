'''
Create an egg file of the project
'''
from setuptools import setup, find_packages

setup(name="igz_func",
      version="1.0",
      packages=find_packages(),
      install_requires=[
          'pyspark',
          'mlrun'
      ])
