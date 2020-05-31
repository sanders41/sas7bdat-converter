import pytest

from pathlib import Path


SAS7BDAT_DIR = Path().absolute().joinpath('tests/assets/sas7bdat_files')


@pytest.fixture(scope='session')
def expected_dir():
    return Path().absolute().joinpath('tests/assets/expected_files')

@pytest.fixture(scope='session')
def sas_file_1():
    return SAS7BDAT_DIR.joinpath('file1.sas7bdat')


@pytest.fixture(scope='session')
def sas_file_2():
    return SAS7BDAT_DIR.joinpath('file2.sas7bdat')


@pytest.fixture(scope='session')
def sas_file_3():
    return SAS7BDAT_DIR.joinpath('file3.sas7bdat')


@pytest.fixture(scope='session')
def sas7bdat_dir():
    return SAS7BDAT_DIR