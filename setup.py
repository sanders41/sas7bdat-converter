from pathlib import Path
from setuptools import find_packages, setup

HERE = Path(__file__).parent
README = (HERE.joinpath('README.md').read_text())

setup(
    name='sas7bdat_converter',
    version='0.3.6',
    author='Paul Sanders',
    author_email='psanders1@gmail.com',
    license='Apache 2.0',
    description='Convert sas7bdat files into other formats',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/sanders41/sas7bdat_converter',
    download_url='https://github.com/sanders41/sas7bdat_converter/archive/v0.3.5.tar.gz',
    packages=['sas7bdat_converter'],
    install_requires=[
        'pandas>=0.25.3',
        'XlsxWriter>=1.2.6',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent'
    ],
    keywords=['sas', 'sas7bdat', 'converter']
)
