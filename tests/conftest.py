from pathlib import Path

import pytest

ASSETS_DIR = Path().absolute().joinpath("tests/assets")


@pytest.fixture(scope="module")
def expected_dir():
    return ASSETS_DIR / "expected_files"


@pytest.fixture(scope="module")
def sas_file_1():
    return ASSETS_DIR.joinpath("sas7bdat_files/file1.sas7bdat")


@pytest.fixture(scope="module")
def sas_file_2():
    return ASSETS_DIR.joinpath("sas7bdat_files/file2.sas7bdat")


@pytest.fixture(scope="module")
def sas_file_3():
    return ASSETS_DIR.joinpath("sas7bdat_files/file3.sas7bdat")


@pytest.fixture(scope="module")
def sas7bdat_dir():
    return ASSETS_DIR / "sas7bdat_files"


@pytest.fixture
def bad_sas_file():
    return ASSETS_DIR.joinpath("bad_sas_files/bad_sas_file.sas7bdat")


@pytest.fixture(scope="module")
def xpt_file_1():
    return ASSETS_DIR.joinpath("xpt_files/file1.xpt")


@pytest.fixture(scope="module")
def xpt_file_2():
    return ASSETS_DIR.joinpath("xpt_files/file2.xpt")


@pytest.fixture(scope="module")
def xpt_dir():
    return ASSETS_DIR / "xpt_files"


@pytest.fixture
def bad_xpt_file():
    return ASSETS_DIR.joinpath("bad_sas_files/bad_xpt_file.xpt")


@pytest.fixture(scope="module")
def xpt_expected_dir():
    return ASSETS_DIR / "expected_xpt"
