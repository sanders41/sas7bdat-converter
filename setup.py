from setuptools import setup
from setuptools import find_packages

long_description = '''
Converts proprietary sas7bdat files from SAS into formats such as csv and XML useable by other programs. Currently supported conversiaions are csv, Excel (xlsx format), json, Pandas DataFrame, and XML.

Conversions can be done on a single file, a batch of files, or a whole directory.
'''

setup(
    name='sas7bdat_converter',
    version='0.2.7',
    author='Paul Sanders',
    author_email='psanders1@gmail.com',
    license='Apache 2.0',
    description='Convert sas7bdat files into other formats',
    long_description=long_description,
    url='https://github.com/sanders41/sas7bdat_converter',
    download_url='https://github.com/sanders41/sas7bdat_converter/archive/v0.2.7.tar.gz',
    install_requires=['pandas>=0.24.2',
                      'XlsxWriter>=1.1.8'],
    extras_require={
        'test': ['xlrd>=1.2.0'],
    },
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent'
    ],
)
