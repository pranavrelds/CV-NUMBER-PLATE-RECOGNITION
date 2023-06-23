import setuptools

VERSION = '0.0.1'
PROJECT_NAME = 'Automatic Number Palte Recognition'
AUTHOR_NAME = 'Pranav Tondgaonkar'

setuptools.setup(
    version=VERSION,
    PROJECT_NAME = PROJECT_NAME,
    author= AUTHOR_NAME,
    description= DESCRIPTION,
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where='src')
)