from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sas7bdat_converter',
    version='0.0.1',
    author='Paul Sanders',
    author_email='psanders1@gmail.com'
    deeacription='Convert sas7bdat files into other formats',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sanders41/sas7bdat_converter',
    packages=find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI APPROVED :: APACHE SOFTWARE LICENSE',
        'Operating System :: OS Independent',
    ),
)
