import json
import shutil
from pathlib import Path
from unittest.mock import patch

import pandas as pd
import pytest

import sas7bdat_converter.converter as converter

current_dir = Path().absolute()


def test_batch_to_csv_path_sas(tmp_path, sas_file_1, sas_file_2, sas_file_3):
    converted_file_1 = tmp_path.joinpath("file1.csv")
    converted_file_2 = tmp_path.joinpath("file2.csv")
    converted_file_3 = tmp_path.joinpath("file3.csv")

    file_dict = [
        {"sas7bdat_file": sas_file_1, "export_file": converted_file_1},
        {"sas7bdat_file": sas_file_2, "export_file": converted_file_2},
        {"sas7bdat_file": sas_file_3, "export_file": converted_file_3},
    ]

    converter.batch_to_csv(file_dict)

    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


def test_batch_to_csv_path_xpt(tmp_path, xpt_file_1, xpt_file_2):
    converted_file_1 = tmp_path.joinpath("file1.csv")
    converted_file_2 = tmp_path.joinpath("file2.csv")

    file_dict = [
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file_1},
        {"sas7bdat_file": xpt_file_2, "export_file": converted_file_2},
    ]

    converter.batch_to_csv(file_dict)

    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file():
        files_created = True

    assert files_created


def test_batch_to_csv_str_sas(tmp_path, sas_file_1, sas_file_2, sas_file_3):
    converted_file_1 = tmp_path.joinpath("file1.csv")
    converted_file_2 = tmp_path.joinpath("file2.csv")
    converted_file_3 = tmp_path.joinpath("file3.csv")

    file_dict = [
        {"sas7bdat_file": str(sas_file_1), "export_file": str(converted_file_1)},
        {"sas7bdat_file": str(sas_file_2), "export_file": str(converted_file_2)},
        {"sas7bdat_file": str(sas_file_3), "export_file": str(converted_file_3)},
    ]

    converter.batch_to_csv(file_dict)  # type: ignore

    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


def test_batch_to_csv_str_xpt(tmp_path, xpt_file_1, xpt_file_2):
    converted_file_1 = tmp_path.joinpath("file1.csv")
    converted_file_2 = tmp_path.joinpath("file2.csv")

    file_dict = [
        {"sas7bdat_file": str(xpt_file_1), "export_file": str(converted_file_1)},
        {"sas7bdat_file": str(xpt_file_2), "export_file": str(converted_file_2)},
    ]

    converter.batch_to_csv(file_dict)  # type: ignore

    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file():
        files_created = True

    assert files_created


def test_batch_to_csv_continue_sas(tmp_path, capfd, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.csv")
    converted_file = tmp_path.joinpath("file1.csv")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    converter.batch_to_csv(file_dict, continue_on_error=True, verbose=False)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" not in out


def test_batch_to_csv_continue_sas_verbose(tmp_path, capfd, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.csv")
    converted_file = tmp_path.joinpath("file1.csv")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    converter.batch_to_csv(file_dict, continue_on_error=True)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" in out


def test_batch_to_csv_continue_xpt(tmp_path, capfd, xpt_file_1):
    bad_xpt_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.csv")
    converted_file = tmp_path.joinpath("file1.csv")

    file_dict = [
        {"sas7bdat_file": bad_xpt_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    converter.batch_to_csv(file_dict, continue_on_error=True, verbose=False)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" not in out


def test_batch_to_csv_continue_xpt_verbose(tmp_path, capfd, xpt_file_1):
    bad_xpt_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.csv")
    converted_file = tmp_path.joinpath("file1.csv")

    file_dict = [
        {"sas7bdat_file": bad_xpt_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    converter.batch_to_csv(file_dict, continue_on_error=True)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" in out


def test_batch_to_csv_no_continue_sas(tmp_path, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.csv")
    converted_file = tmp_path.joinpath("file1.csv")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    with pytest.raises(Exception):  # noqa: B017
        converter.batch_to_csv(file_dict, continue_on_error=False)


def test_batch_to_csv_no_continue_xpt(tmp_path, xpt_file_1):
    bad_xpt_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.csv")
    converted_file = tmp_path.joinpath("file1.csv")

    file_dict = [
        {"sas7bdat_file": bad_xpt_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    with pytest.raises(Exception):  # noqa: B017
        converter.batch_to_csv(file_dict, continue_on_error=False, verbose=False)


file_dicts = [
    [{"bad_key": "test.sas7bdat", "export_file": "test.csv"}],
    [{"sas7bdat_file": "test.sas7bdat", "bad_key": "test.csv"}],
    [{"sas_bad_key": "test.sas7bdate", "export_bad_key": "test.csv"}],
]


@pytest.mark.parametrize("file_dict", file_dicts)
def test_batch_to_csv_invalid_key_sas(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter.batch_to_csv(file_dict)

    assert "Invalid key provided" in str(execinfo.value)


file_dicts = [
    [{"bad_key": "test.xpt", "export_file": "test.csv"}],
    [{"sas7bdat_file": "test.xpt", "bad_key": "test.csv"}],
    [{"sas_bad_key": "test.xptt", "export_bad_key": "test.csv"}],
]


@pytest.mark.parametrize("file_dict", file_dicts)
def test_batch_to_csv_invalid_key_xpt(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter.batch_to_csv(file_dict)

    assert "Invalid key provided" in str(execinfo.value)


def test_batch_to_excel_path_sas(tmp_path, sas_file_1, sas_file_2, sas_file_3):
    converted_file_1 = tmp_path.joinpath("file1.xlsx")
    converted_file_2 = tmp_path.joinpath("file2.xlsx")
    converted_file_3 = tmp_path.joinpath("file3.xlsx")

    file_dict = [
        {"sas7bdat_file": sas_file_1, "export_file": converted_file_1},
        {"sas7bdat_file": sas_file_2, "export_file": converted_file_2},
        {"sas7bdat_file": sas_file_3, "export_file": converted_file_3},
    ]

    converter.batch_to_excel(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


def test_batch_to_excel_path_xpt(tmp_path, xpt_file_1, xpt_file_2):
    converted_file_1 = tmp_path.joinpath("file1.xlsx")
    converted_file_2 = tmp_path.joinpath("file2.xlsx")

    file_dict = [
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file_1},
        {"sas7bdat_file": xpt_file_2, "export_file": converted_file_2},
    ]

    converter.batch_to_excel(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file():
        files_created = True

    assert files_created


def test_batch_to_excel_str_sas(tmp_path, sas_file_1, sas_file_2, sas_file_3):
    converted_file_1 = tmp_path.joinpath("file1.xlsx")
    converted_file_2 = tmp_path.joinpath("file2.xlsx")
    converted_file_3 = tmp_path.joinpath("file3.xlsx")

    file_dict = [
        {"sas7bdat_file": str(sas_file_1), "export_file": str(converted_file_1)},
        {"sas7bdat_file": str(sas_file_2), "export_file": str(converted_file_2)},
        {"sas7bdat_file": str(sas_file_3), "export_file": str(converted_file_3)},
    ]

    converter.batch_to_excel(file_dict)  # type: ignore
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


def test_batch_to_excel_str_xpt(tmp_path, xpt_file_1, xpt_file_2):
    converted_file_1 = tmp_path.joinpath("file1.xlsx")
    converted_file_2 = tmp_path.joinpath("file2.xlsx")

    file_dict = [
        {"sas7bdat_file": str(xpt_file_1), "export_file": str(converted_file_1)},
        {"sas7bdat_file": str(xpt_file_2), "export_file": str(converted_file_2)},
    ]

    converter.batch_to_excel(file_dict)  # type: ignore
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file():
        files_created = True

    assert files_created


def test_batch_to_excel_continue_sas(tmp_path, capfd, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.xlsx")
    converted_file = tmp_path.joinpath("file1.xlsx")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    converter.batch_to_excel(file_dict, continue_on_error=True, verbose=False)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" not in out


def test_batch_to_excel_continue_sas_verbose(tmp_path, capfd, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.xlsx")
    converted_file = tmp_path.joinpath("file1.xlsx")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    converter.batch_to_excel(file_dict, continue_on_error=True)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" in out


def test_batch_to_excel_continue_xpt(tmp_path, capfd, xpt_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.xlsx")
    converted_file = tmp_path.joinpath("file1.xlsx")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    converter.batch_to_excel(file_dict, continue_on_error=True, verbose=False)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" not in out


def test_batch_to_excel_continue_xpt_verbose(tmp_path, capfd, xpt_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.xlsx")
    converted_file = tmp_path.joinpath("file1.xlsx")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    converter.batch_to_excel(file_dict, continue_on_error=True)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" in out


def test_batch_to_excel_no_continue_sas(tmp_path, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.xlsx")
    converted_file = tmp_path.joinpath("file1.xlsx")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    with pytest.raises(FileNotFoundError):
        converter.batch_to_excel(file_dict, continue_on_error=False)


def test_batch_to_excel_no_continue_xpt(tmp_path, xpt_file_1):
    bad_xpt_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.xlsx")
    converted_file = tmp_path.joinpath("file1.xlsx")

    file_dict = [
        {"sas7bdat_file": bad_xpt_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    with pytest.raises(FileNotFoundError):
        converter.batch_to_excel(file_dict, continue_on_error=False)


file_dicts = [
    [{"bad_key": "test.sas7bdat", "export_file": "test.xlsx"}],
    [{"sas7bdat_file": "test.sas7bdat", "bad_key": "test.xlsx"}],
    [{"sas_bad_key": "test.sas7bdate", "export_bad_key": "test.xlsx"}],
]


@pytest.mark.parametrize("file_dict", file_dicts)
def test_batch_to_excel_invalid_key_sas(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter.batch_to_excel(file_dict)

    assert "Invalid key provided" in str(execinfo.value)


file_dicts = [
    [{"bad_key": "test.xpt", "export_file": "test.xlsx"}],
    [{"sas7bdat_file": "test.xpt", "bad_key": "test.xlsx"}],
    [{"sas_bad_key": "test.xptt", "export_bad_key": "test.xlsx"}],
]


@pytest.mark.parametrize("file_dict", file_dicts)
def test_batch_to_excel_invalid_key_xpt(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter.batch_to_excel(file_dict)

    assert "Invalid key provided" in str(execinfo.value)


def test_batch_to_json_path_sas(tmp_path, sas_file_1, sas_file_2, sas_file_3):
    converted_file_1 = tmp_path.joinpath("file1.json")
    converted_file_2 = tmp_path.joinpath("file2.json")
    converted_file_3 = tmp_path.joinpath("file3.json")

    file_dict = [
        {"sas7bdat_file": sas_file_1, "export_file": converted_file_1},
        {"sas7bdat_file": sas_file_2, "export_file": converted_file_2},
        {"sas7bdat_file": sas_file_3, "export_file": converted_file_3},
    ]

    converter.batch_to_json(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


def test_batch_to_json_path_xpt(tmp_path, xpt_file_1, xpt_file_2):
    converted_file_1 = tmp_path.joinpath("file1.json")
    converted_file_2 = tmp_path.joinpath("file2.json")

    file_dict = [
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file_1},
        {"sas7bdat_file": xpt_file_2, "export_file": converted_file_2},
    ]

    converter.batch_to_json(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file():
        files_created = True

    assert files_created


def test_batch_to_json_path_str_sas(tmp_path, sas_file_1, sas_file_2, sas_file_3):
    converted_file_1 = tmp_path.joinpath("file1.json")
    converted_file_2 = tmp_path.joinpath("file2.json")
    converted_file_3 = tmp_path.joinpath("file3.json")

    file_dict = [
        {"sas7bdat_file": str(sas_file_1), "export_file": str(converted_file_1)},
        {"sas7bdat_file": str(sas_file_2), "export_file": str(converted_file_2)},
        {"sas7bdat_file": str(sas_file_3), "export_file": str(converted_file_3)},
    ]

    converter.batch_to_json(file_dict)  # type: ignore
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


def test_batch_to_json_path_str_xpt(tmp_path, xpt_file_1, xpt_file_2):
    converted_file_1 = tmp_path.joinpath("file1.json")
    converted_file_2 = tmp_path.joinpath("file2.json")

    file_dict = [
        {"sas7bdat_file": str(xpt_file_1), "export_file": str(converted_file_1)},
        {"sas7bdat_file": str(xpt_file_2), "export_file": str(converted_file_2)},
    ]

    converter.batch_to_json(file_dict)  # type: ignore
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file():
        files_created = True

    assert files_created


def test_batch_to_json_continue_sas(tmp_path, capfd, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.json")
    converted_file = tmp_path.joinpath("file1.json")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    converter.batch_to_json(file_dict, continue_on_error=True, verbose=False)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" not in out


def test_batch_to_json_continue_sas_verbose(tmp_path, capfd, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.json")
    converted_file = tmp_path.joinpath("file1.json")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    converter.batch_to_json(file_dict, continue_on_error=True)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" in out


def test_batch_to_json_continue_xpt(tmp_path, capfd, xpt_file_1):
    bad_xpt_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.json")
    converted_file = tmp_path.joinpath("file1.json")

    file_dict = [
        {"sas7bdat_file": bad_xpt_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    converter.batch_to_json(file_dict, continue_on_error=True, verbose=False)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" not in out


def test_batch_to_json_continue_xpt_verbose(tmp_path, capfd, xpt_file_1):
    bad_xpt_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.json")
    converted_file = tmp_path.joinpath("file1.json")

    file_dict = [
        {"sas7bdat_file": bad_xpt_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    converter.batch_to_json(file_dict, continue_on_error=True)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" in out


def test_batch_to_json_no_continue_sas(tmp_path, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.json")
    converted_file = tmp_path.joinpath("file1.json")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    with pytest.raises(Exception):  # noqa: B017
        converter.batch_to_json(file_dict, continue_on_error=False)


def test_batch_to_json_no_continue_xpt(tmp_path, xpt_file_1):
    bad_xpt_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.json")
    converted_file = tmp_path.joinpath("file1.json")

    file_dict = [
        {"sas7bdat_file": bad_xpt_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    with pytest.raises(Exception):  # noqa: B017
        converter.batch_to_json(file_dict, continue_on_error=False)


file_dicts = [
    [{"bad_key": "test.sas7bdat", "export_file": "test.json"}],
    [{"sas7bdat_file": "test.sas7bdat", "bad_key": "test.json"}],
    [{"sas_bad_key": "test.sas7bdate", "export_bad_key": "test.json"}],
]


@pytest.mark.parametrize("file_dict", file_dicts)
def test_batch_to_json_invalid_key_sas(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter.batch_to_json(file_dict)

    assert "Invalid key provided" in str(execinfo.value)


file_dicts = [
    [{"bad_key": "test.xpt", "export_file": "test.json"}],
    [{"sas7bdat_file": "test.xpt", "bad_key": "test.json"}],
    [{"sas_bad_key": "test.xptt", "export_bad_key": "test.json"}],
]


@pytest.mark.parametrize("file_dict", file_dicts)
def test_batch_to_json_invalid_key_xpt(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter.batch_to_json(file_dict)

    assert "Invalid key provided" in str(execinfo.value)


optionals = [
    {},
    {"root_node": "root"},
    {"first_node": "item"},
    {"root_node": "root", "first_node": "item"},
]


@pytest.mark.parametrize("optional", optionals)
def test_batch_to_xml_path_sas(tmp_path, sas_file_1, sas_file_2, sas_file_3, optional):
    converted_file_1 = tmp_path.joinpath("file1.xml")
    converted_file_2 = tmp_path.joinpath("file2.xml")
    converted_file_3 = tmp_path.joinpath("file3.xml")

    if optional.get("root_node") and optional.get("first_node"):
        file_dict = [
            {
                "sas7bdat_file": sas_file_1,
                "export_file": converted_file_1,
                "root_node": optional.get("root_node"),
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": sas_file_2,
                "export_file": converted_file_2,
                "root_node": optional.get("root_node"),
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": sas_file_3,
                "export_file": converted_file_3,
                "root_node": optional.get("root_node"),
                "first_node": optional.get("first_node"),
            },
        ]
    elif optional.get("root_node"):
        file_dict = [
            {
                "sas7bdat_file": sas_file_1,
                "export_file": converted_file_1,
                "root_node": optional.get("root_node"),
            },
            {
                "sas7bdat_file": sas_file_2,
                "export_file": converted_file_2,
                "root_node": optional.get("root_node"),
            },
            {
                "sas7bdat_file": sas_file_3,
                "export_file": converted_file_3,
                "root_node": optional.get("root_node"),
            },
        ]
    elif optional.get("first_node"):
        file_dict = [
            {
                "sas7bdat_file": sas_file_1,
                "export_file": converted_file_1,
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": sas_file_2,
                "export_file": converted_file_2,
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": sas_file_3,
                "export_file": converted_file_3,
                "first_node": optional.get("first_node"),
            },
        ]
    else:
        file_dict = [
            {
                "sas7bdat_file": sas_file_1,
                "export_file": converted_file_1,
            },
            {
                "sas7bdat_file": sas_file_2,
                "export_file": converted_file_2,
            },
            {
                "sas7bdat_file": sas_file_3,
                "export_file": converted_file_3,
            },
        ]

    converter.batch_to_xml(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


@pytest.mark.parametrize("optional", optionals)
def test_batch_to_xml_path_xpt(tmp_path, xpt_file_1, xpt_file_2, optional):
    converted_file_1 = tmp_path.joinpath("file1.xml")
    converted_file_2 = tmp_path.joinpath("file2.xml")

    if optional.get("root_node") and optional.get("first_node"):
        file_dict = [
            {
                "sas7bdat_file": xpt_file_1,
                "export_file": converted_file_1,
                "root_node": optional.get("root_node"),
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": xpt_file_2,
                "export_file": converted_file_2,
                "root_node": optional.get("root_node"),
                "first_node": optional.get("first_node"),
            },
        ]
    elif optional.get("root_node"):
        file_dict = [
            {
                "sas7bdat_file": xpt_file_1,
                "export_file": converted_file_1,
                "root_node": optional.get("root_node"),
            },
            {
                "sas7bdat_file": xpt_file_2,
                "export_file": converted_file_2,
                "root_node": optional.get("root_node"),
            },
        ]
    elif optional.get("first_node"):
        file_dict = [
            {
                "sas7bdat_file": xpt_file_1,
                "export_file": converted_file_1,
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": xpt_file_2,
                "export_file": converted_file_2,
                "first_node": optional.get("first_node"),
            },
        ]
    else:
        file_dict = [
            {
                "sas7bdat_file": xpt_file_1,
                "export_file": converted_file_1,
            },
            {
                "sas7bdat_file": xpt_file_2,
                "export_file": converted_file_2,
            },
        ]

    converter.batch_to_xml(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file():
        files_created = True

    assert files_created


@pytest.mark.parametrize("optional", optionals)
def test_batch_to_xml_str_sas(tmp_path, sas_file_1, sas_file_2, sas_file_3, optional):
    converted_file_1 = tmp_path.joinpath("file1.xml")
    converted_file_2 = tmp_path.joinpath("file2.xml")
    converted_file_3 = tmp_path.joinpath("file3.xml")

    if optional.get("root_node") and optional.get("first_node"):
        file_dict = [
            {
                "sas7bdat_file": str(sas_file_1),
                "export_file": str(converted_file_1),
                "root_node": optional.get("root_node"),
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": str(sas_file_2),
                "export_file": str(converted_file_2),
                "root_node": optional.get("root_node"),
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": str(sas_file_3),
                "export_file": str(converted_file_3),
                "root_node": optional.get("root_node"),
                "first_node": optional.get("first_node"),
            },
        ]
    elif optional.get("root_node"):
        file_dict = [
            {
                "sas7bdat_file": str(sas_file_1),
                "export_file": str(converted_file_1),
                "root_node": optional.get("root_node"),
            },
            {
                "sas7bdat_file": str(sas_file_2),
                "export_file": str(converted_file_2),
                "root_node": optional.get("root_node"),
            },
            {
                "sas7bdat_file": str(sas_file_3),
                "export_file": str(converted_file_3),
                "root_node": optional.get("root_node"),
            },
        ]
    elif optional.get("first_node"):
        file_dict = [
            {
                "sas7bdat_file": str(sas_file_1),
                "export_file": str(converted_file_1),
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": str(sas_file_2),
                "export_file": str(converted_file_2),
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": str(sas_file_3),
                "export_file": str(converted_file_3),
                "first_node": optional.get("first_node"),
            },
        ]
    else:
        file_dict = [
            {
                "sas7bdat_file": str(sas_file_1),
                "export_file": str(converted_file_1),
            },
            {
                "sas7bdat_file": str(sas_file_2),
                "export_file": str(converted_file_2),
            },
            {
                "sas7bdat_file": str(sas_file_3),
                "export_file": str(converted_file_3),
            },
        ]

    converter.batch_to_xml(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


@pytest.mark.parametrize("optional", optionals)
def test_batch_to_xml_str_xpt(tmp_path, xpt_file_1, xpt_file_2, optional):
    converted_file_1 = tmp_path.joinpath("file1.xml")
    converted_file_2 = tmp_path.joinpath("file2.xml")

    if optional.get("root_node") and optional.get("first_node"):
        file_dict = [
            {
                "sas7bdat_file": str(xpt_file_1),
                "export_file": str(converted_file_1),
                "root_node": optional.get("root_node"),
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": str(xpt_file_2),
                "export_file": str(converted_file_2),
                "root_node": optional.get("root_node"),
                "first_node": optional.get("first_node"),
            },
        ]
    elif optional.get("root_node"):
        file_dict = [
            {
                "sas7bdat_file": str(xpt_file_1),
                "export_file": str(converted_file_1),
                "root_node": optional.get("root_node"),
            },
            {
                "sas7bdat_file": str(xpt_file_2),
                "export_file": str(converted_file_2),
                "root_node": optional.get("root_node"),
            },
        ]
    elif optional.get("first_node"):
        file_dict = [
            {
                "sas7bdat_file": str(xpt_file_1),
                "export_file": str(converted_file_1),
                "first_node": optional.get("first_node"),
            },
            {
                "sas7bdat_file": str(xpt_file_2),
                "export_file": str(converted_file_2),
                "first_node": optional.get("first_node"),
            },
        ]
    else:
        file_dict = [
            {
                "sas7bdat_file": str(xpt_file_1),
                "export_file": str(converted_file_1),
            },
            {
                "sas7bdat_file": str(xpt_file_2),
                "export_file": str(converted_file_2),
            },
        ]

    converter.batch_to_xml(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file():
        files_created = True

    assert files_created


def test_batch_to_xml_continue_sas(tmp_path, capfd, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.xml")
    converted_file = tmp_path.joinpath("file1.xml")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    converter.batch_to_xml(file_dict, continue_on_error=True, verbose=False)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" not in out


def test_batch_to_xml_continue_sas_verbose(tmp_path, capfd, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.xml")
    converted_file = tmp_path.joinpath("file1.xml")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    converter.batch_to_xml(file_dict, continue_on_error=True)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" in out


def test_batch_to_xml_continue_xpt(tmp_path, capfd, xpt_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.xml")
    converted_file = tmp_path.joinpath("file1.xml")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    converter.batch_to_xml(file_dict, continue_on_error=True, verbose=False)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" not in out


def test_batch_to_xml_continue_xpt_verbose(tmp_path, capfd, xpt_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.xml")
    converted_file = tmp_path.joinpath("file1.xml")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    converter.batch_to_xml(file_dict, continue_on_error=True)
    out, _ = capfd.readouterr()

    assert converted_file.is_file()
    assert "Error converting" in out


def test_batch_to_xml_no_continue_sas(tmp_path, sas_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.sas7bdat")
    bad_converted_file = tmp_path.joinpath("bad_file.xml")
    converted_file = tmp_path.joinpath("file1.xml")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": sas_file_1, "export_file": converted_file},
    ]

    with pytest.raises(Exception):  # noqa: B017
        converter.batch_to_xml(file_dict, continue_on_error=False)


def test_batch_to_xml_no_continue_xpt(tmp_path, xpt_file_1):
    bad_sas_file = tmp_path.joinpath("bad_file.xpt")
    bad_converted_file = tmp_path.joinpath("bad_file.xml")
    converted_file = tmp_path.joinpath("file1.xml")

    file_dict = [
        {"sas7bdat_file": bad_sas_file, "export_file": bad_converted_file},
        {"sas7bdat_file": xpt_file_1, "export_file": converted_file},
    ]

    with pytest.raises(Exception):  # noqa: B017
        converter.batch_to_xml(file_dict, continue_on_error=False)


file_dicts = [
    [{"bad_key": "test.sas7bdat", "export_file": "test.xml"}],
    [{"sas7bdat_file": "test.sas7bdat", "bad_key": "test.xml"}],
    [{"sas_bad_key": "test.sas7bdate", "export_bad_key": "test.xml"}],
    [
        {
            "sas7bdat_file": "test.sas7bdat",
            "export_file": "test.xml",
            "root_node": "test",
            "bad": "test",
        }
    ],
    [
        {
            "sas7bdat_file": "test.sas7bdat",
            "export_file": "test.xml",
            "bad": "test",
            "first_node": "test",
        }
    ],
]


@pytest.mark.parametrize("file_dict", file_dicts)
def test_batch_to_xml_invalid_key_sas(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter.batch_to_xml(file_dict)

    assert "Invalid key provided" in str(execinfo.value)


file_dicts = [
    [{"bad_key": "test.xpt", "export_file": "test.xml"}],
    [{"sas7bdat_file": "test.xpt", "bad_key": "test.xml"}],
    [{"sas_bad_key": "test.xptt", "export_bad_key": "test.xml"}],
    [
        {
            "sas7bdat_file": "test.xpt",
            "export_file": "test.xml",
            "root_node": "test",
            "bad": "test",
        }
    ],
    [
        {
            "sas7bdat_file": "test.xpt",
            "export_file": "test.xml",
            "bad": "test",
            "first_node": "test",
        }
    ],
]


@pytest.mark.parametrize("file_dict", file_dicts)
def test_batch_to_xml_invalid_key_xpt(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter.batch_to_xml(file_dict)

    assert "Invalid key provided" in str(execinfo.value)


def test_dir_to_csv_same_dir_path_sas(tmp_path, sas7bdat_dir):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    converter.dir_to_csv(tmp_path)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".csv"])

    assert sas_counter == convert_counter


def test_dir_to_csv_same_dir_path_xpt(tmp_path, xpt_dir):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    converter.dir_to_csv(tmp_path)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".csv"])

    assert sas_counter == convert_counter


def test_dir_to_csv_same_dir_str_sas(tmpdir, sas7bdat_dir):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    converter.dir_to_csv(tmpdir)
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".csv"])

    assert sas_counter == convert_counter


def test_dir_to_csv_same_dir_str_xpt(tmpdir, xpt_dir):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, tmpdir)

    converter.dir_to_csv(tmpdir)
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".csv"])

    assert sas_counter == convert_counter


def test_dir_to_csv_continue_sas(tmp_path, capfd, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))

    converter.dir_to_csv(tmp_path, continue_on_error=True, verbose=False)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".csv"])
    out, _ = capfd.readouterr()

    assert sas_counter == convert_counter
    assert "Error converting" not in out


def test_dir_to_csv_continue_sas_verbose(tmp_path, capfd, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))

    converter.dir_to_csv(tmp_path, continue_on_error=True)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".csv"])
    out, _ = capfd.readouterr()

    assert sas_counter == convert_counter
    assert "Error converting" in out


def test_dir_to_csv_continue_xpt(tmp_path, capfd, xpt_dir, bad_xpt_file):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for sas_file in xpt_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))

    converter.dir_to_csv(tmp_path, continue_on_error=True, verbose=False)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".csv"])
    out, _ = capfd.readouterr()

    assert sas_counter == convert_counter
    assert "Error converting" not in out


def test_dir_to_csv_continue_xpt_verbose(tmp_path, capfd, xpt_dir, bad_xpt_file):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for sas_file in xpt_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))

    converter.dir_to_csv(tmp_path, continue_on_error=True)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".csv"])
    out, _ = capfd.readouterr()

    assert sas_counter == convert_counter
    assert "Error converting" in out


def test_dir_to_csv_no_continue_sas(tmp_path, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))
    with pytest.raises(Exception):  # noqa: B017
        converter.dir_to_csv(tmp_path, continue_on_error=False)


def test_dir_to_csv_no_continue_xpt(tmp_path, xpt_dir, bad_xpt_file):
    sas_files = [str(x) for x in xpt_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))
    with pytest.raises(Exception):  # noqa: B017
        converter.dir_to_csv(tmp_path, continue_on_error=False)


def test_dir_to_csv_different_dir_path_sas(tmp_path, sas7bdat_dir):
    converter.dir_to_csv(dir_path=sas7bdat_dir, export_path=tmp_path)
    sas_counter = len([name for name in sas7bdat_dir.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".csv"])

    assert sas_counter == convert_counter


def test_dir_to_csv_different_dir_path_xpt(tmp_path, xpt_dir):
    converter.dir_to_csv(dir_path=xpt_dir, export_path=tmp_path)
    xpt_counter = len([name for name in xpt_dir.iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".csv"])

    assert xpt_counter == convert_counter


def test_dir_to_csv_different_dir_str_sas(tmpdir, sas7bdat_dir):
    converter.dir_to_csv(dir_path=str(sas7bdat_dir), export_path=tmpdir)
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".csv"])

    assert sas_counter == convert_counter


def test_dir_to_csv_different_dir_str_xpt(tmpdir, xpt_dir):
    converter.dir_to_csv(dir_path=str(xpt_dir), export_path=tmpdir)
    xpt_counter = len([name for name in Path(xpt_dir).iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".csv"])

    assert xpt_counter == convert_counter


def test_dir_to_excel_same_dir_path_sas(tmp_path, sas7bdat_dir):
    sas_files = [x for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    converter.dir_to_excel(tmp_path)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xlsx"])

    assert sas_counter == convert_counter


def test_dir_to_excel_same_dir_path_xpt(tmp_path, xpt_dir):
    xpt_files = [x for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    converter.dir_to_excel(tmp_path)
    xpt_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xlsx"])

    assert xpt_counter == convert_counter


def test_dir_to_excel_same_dir_str_sas(tmpdir, sas7bdat_dir):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    converter.dir_to_excel(tmpdir)
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xlsx"])

    assert sas_counter == convert_counter


def test_dir_to_excel_same_dir_str_xpt(tmpdir, xpt_dir):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, tmpdir)

    converter.dir_to_excel(tmpdir)
    xpt_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xlsx"])

    assert xpt_counter == convert_counter


def test_dir_to_excel_different_dir_path_sas(tmp_path, sas7bdat_dir):
    converter.dir_to_excel(dir_path=sas7bdat_dir, export_path=tmp_path)
    sas_counter = len([name for name in sas7bdat_dir.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xlsx"])

    assert sas_counter == convert_counter


def test_dir_to_excel_different_dir_path_xpt(tmp_path, xpt_dir):
    converter.dir_to_excel(dir_path=xpt_dir, export_path=tmp_path)
    xpt_counter = len([name for name in xpt_dir.iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xlsx"])

    assert xpt_counter == convert_counter


def test_dir_to_excel_different_dir_str_sas(tmpdir, sas7bdat_dir):
    converter.dir_to_excel(dir_path=str(sas7bdat_dir), export_path=tmpdir)
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xlsx"])

    assert sas_counter == convert_counter


def test_dir_to_excel_different_dir_str_xpt(tmpdir, xpt_dir):
    converter.dir_to_excel(dir_path=str(xpt_dir), export_path=tmpdir)
    xpt_counter = len([name for name in Path(xpt_dir).iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xlsx"])

    assert xpt_counter == convert_counter


def test_dir_to_excel_continue_sas(tmp_path, capfd, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))

    converter.dir_to_excel(tmp_path, continue_on_error=True, verbose=False)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xlsx"])
    out, _ = capfd.readouterr()

    assert sas_counter == convert_counter
    assert "Error converting" not in out


def test_dir_to_excel_continue_sas_verbose(tmp_path, capfd, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))

    converter.dir_to_excel(tmp_path, continue_on_error=True)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xlsx"])
    out, _ = capfd.readouterr()

    assert sas_counter == convert_counter
    assert "Error converting" in out


def test_dir_to_excel_continue_xpt(tmp_path, capfd, xpt_dir, bad_xpt_file):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))

    converter.dir_to_excel(tmp_path, continue_on_error=True, verbose=False)
    xpt_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xlsx"])
    out, _ = capfd.readouterr()

    assert xpt_counter == convert_counter
    assert "Error converting" not in out


def test_dir_to_excel_continue_xpt_verbose(tmp_path, capfd, xpt_dir, bad_xpt_file):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))

    converter.dir_to_excel(tmp_path, continue_on_error=True)
    xpt_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xlsx"])
    out, _ = capfd.readouterr()

    assert xpt_counter == convert_counter
    assert "Error converting" in out


def test_dir_to_excel_no_continue_sas(tmp_path, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))
    with pytest.raises(Exception):  # noqa: B017
        converter.dir_to_excel(tmp_path, continue_on_error=False)


def test_dir_to_excel_no_continue_xpt(tmp_path, xpt_dir, bad_xpt_file):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))
    with pytest.raises(Exception):  # noqa: B017
        converter.dir_to_excel(tmp_path, continue_on_error=False)


def test_dir_to_json_same_dir_path_sas(tmp_path, sas7bdat_dir):
    sas_files = [x for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmp_path)

    converter.dir_to_json(tmp_path)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".json"])

    assert sas_counter == convert_counter


def test_dir_to_json_same_dir_path_xpt(tmp_path, xpt_dir):
    xpt_files = [x for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, tmp_path)

    converter.dir_to_json(tmp_path)
    xpt_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".json"])

    assert xpt_counter == convert_counter


def test_dir_to_json_same_dir_str_sas(tmpdir, sas7bdat_dir):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    converter.dir_to_json(tmpdir)
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".json"])

    assert sas_counter == convert_counter


def test_dir_to_json_same_dir_str_xpt(tmpdir, xpt_dir):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, tmpdir)

    converter.dir_to_json(tmpdir)
    xpt_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".json"])

    assert xpt_counter == convert_counter


def test_dir_to_json_different_dir_path_sas(tmp_path, sas7bdat_dir):
    converter.dir_to_json(sas7bdat_dir, tmp_path)
    sas_counter = len([name for name in sas7bdat_dir.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".json"])

    assert sas_counter == convert_counter


def test_dir_to_json_different_dir_path_xpt(tmp_path, xpt_dir):
    converter.dir_to_json(xpt_dir, tmp_path)
    xpt_counter = len([name for name in xpt_dir.iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".json"])

    assert xpt_counter == convert_counter


def test_dir_to_json_different_dir_str_sas(tmpdir, sas7bdat_dir):
    converter.dir_to_json(str(sas7bdat_dir), tmpdir)
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".json"])

    assert sas_counter == convert_counter


def test_dir_to_json_different_dir_str_xpt(tmpdir, xpt_dir):
    converter.dir_to_json(str(xpt_dir), tmpdir)
    xpt_counter = len([name for name in Path(xpt_dir).iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".json"])

    assert xpt_counter == convert_counter


def test_dir_to_json_continue_sas(tmp_path, capfd, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))

    converter.dir_to_json(tmp_path, continue_on_error=True, verbose=False)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".json"])
    out, _ = capfd.readouterr()

    assert sas_counter == convert_counter
    assert "Error converting" not in out


def test_dir_to_json_continue_sas_verbose(tmp_path, capfd, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))

    converter.dir_to_json(tmp_path, continue_on_error=True)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".json"])
    out, _ = capfd.readouterr()

    assert sas_counter == convert_counter
    assert "Error converting" in out


def test_dir_to_json_continue_xpt(tmp_path, capfd, xpt_dir, bad_xpt_file):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))

    converter.dir_to_json(tmp_path, continue_on_error=True, verbose=False)
    xpt_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".json"])
    out, _ = capfd.readouterr()

    assert xpt_counter == convert_counter
    assert "Error converting" not in out


def test_dir_to_json_continue_xpt_verbose(tmp_path, capfd, xpt_dir, bad_xpt_file):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))

    converter.dir_to_json(tmp_path, continue_on_error=True)
    xpt_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".json"])
    out, _ = capfd.readouterr()

    assert xpt_counter == convert_counter
    assert "Error converting" in out


def test_dir_to_json_no_continue_sas(tmp_path, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))
    with pytest.raises(Exception):  # noqa: B017
        converter.dir_to_json(tmp_path, continue_on_error=False)


def test_dir_to_json_no_continue_xpt(tmp_path, xpt_dir, bad_xpt_file):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))
    with pytest.raises(Exception):  # noqa: B017
        converter.dir_to_json(tmp_path, continue_on_error=False)


def test_dir_to_xml_same_dir_path_sas(tmp_path, sas7bdat_dir):
    sas_files = [x for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    converter.dir_to_xml(tmp_path)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xml"])

    assert sas_counter == convert_counter


def test_dir_to_xml_same_dir_path_xpt(tmp_path, xpt_dir):
    xpt_files = [x for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    converter.dir_to_xml(tmp_path)
    xpt_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xml"])

    assert xpt_counter == convert_counter


def test_dir_to_xml_same_dir_str_sas(tmpdir, sas7bdat_dir):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    converter.dir_to_xml(tmpdir)
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xml"])

    assert sas_counter == convert_counter


def test_dir_to_xml_same_dir_str_xpt(tmpdir, xpt_dir):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, tmpdir)

    converter.dir_to_xml(tmpdir)
    xpt_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xml"])

    assert xpt_counter == convert_counter


def test_dir_to_xml_different_dir_path_sas(tmp_path, sas7bdat_dir):
    converter.dir_to_xml(sas7bdat_dir, tmp_path)
    sas_counter = len([name for name in sas7bdat_dir.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xml"])

    assert sas_counter == convert_counter


def test_dir_to_xml_different_dir_path_xpt(tmp_path, xpt_dir):
    converter.dir_to_xml(xpt_dir, tmp_path)
    xpt_counter = len([name for name in xpt_dir.iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xml"])

    assert xpt_counter == convert_counter


def test_dir_to_xml_different_dir_str_sas(tmpdir, sas7bdat_dir):
    converter.dir_to_xml(str(sas7bdat_dir), tmpdir)
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xml"])

    assert sas_counter == convert_counter


def test_dir_to_xml_different_dir_str_xpt(tmpdir, xpt_dir):
    converter.dir_to_xml(str(xpt_dir), tmpdir)
    xpt_counter = len([name for name in Path(xpt_dir).iterdir() if name.suffix == ".xpt"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xml"])

    assert xpt_counter == convert_counter


def test_dir_to_xml_continue_sas(tmp_path, capfd, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))

    converter.dir_to_xml(tmp_path, continue_on_error=True, verbose=False)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xml"])
    out, _ = capfd.readouterr()

    assert sas_counter == convert_counter
    assert "Error converting" not in out


def test_dir_to_xml_continue_sas_verbose(tmp_path, capfd, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))

    converter.dir_to_xml(tmp_path, continue_on_error=True)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xml"])
    out, _ = capfd.readouterr()

    assert sas_counter == convert_counter
    assert "Error converting" in out


def test_dir_to_xml_continue_xpt(tmp_path, capfd, xpt_dir, bad_xpt_file):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))

    converter.dir_to_xml(tmp_path, continue_on_error=True, verbose=False)
    xpt_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xml"])
    out, _ = capfd.readouterr()

    assert xpt_counter == convert_counter
    assert "Error converting" not in out


def test_dir_to_xml_continue_xpt_verbose(tmp_path, capfd, xpt_dir, bad_xpt_file):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))

    converter.dir_to_xml(tmp_path, continue_on_error=True)
    xpt_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xpt"]) - 1
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xml"])
    out, _ = capfd.readouterr()

    assert xpt_counter == convert_counter
    assert "Error converting" in out


def test_dir_to_xml_no_continue_sas(tmp_path, sas7bdat_dir, bad_sas_file):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    shutil.copy(bad_sas_file, str(tmp_path))
    with pytest.raises(Exception):  # noqa: B017
        converter.dir_to_xml(tmp_path, continue_on_error=False)


def test_dir_to_xml_no_continue_xpt(tmp_path, xpt_dir, bad_xpt_file):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, str(tmp_path))

    shutil.copy(bad_xpt_file, str(tmp_path))
    with pytest.raises(Exception):  # noqa: B017
        converter.dir_to_xml(tmp_path, continue_on_error=False)


exception_data = [
    (
        "sas7bdat conversion error - Valid extension for to_csv conversion is: .csv",
        [".csv"],
        "to_csv",
    ),
    (
        "sas7bdat conversion error - Valid extensions for to_csv conversion are: .csv, .txt",
        [".csv", ".txt"],
        "to_csv",
    ),
]


@pytest.mark.parametrize("exception", exception_data)
def test_file_extension_exception_message(exception):
    valid_message = exception[0]
    valid_extensions = exception[1]
    test_message = converter._file_extension_exception_message(exception[2], valid_extensions)

    assert valid_message == test_message


def test_invalid_key_exception_message_no_optional():
    valid_message = "Invalid key provided, expected keys are: sas7bdat_file, export_file"
    required_keys = ["sas7bdat_file", "export_file"]
    test_message = converter._invalid_key_exception_message(required_keys=required_keys)

    assert valid_message == test_message


def test_invalid_key_exception_message_optional():
    valid_message = "Invalid key provided, expected keys are: sas7bdat_file, export_file and optional keys are: root_node, first_node"  # noqa: E501
    required_keys = ["sas7bdat_file", "export_file"]
    optional_keys = ["root_node", "first_node"]
    test_message = converter._invalid_key_exception_message(
        required_keys=required_keys, optional_keys=optional_keys
    )

    assert valid_message == test_message


@pytest.mark.parametrize(
    "data",
    [
        (
            (
                ".txt",
                ".csv",
            ),
            ".xml",
        ),
        ((".sas7bdat",), ".json"),
    ],
)
def test_is_valid_extension_false(data):
    valid_extensions = data[0]
    file_extension = data[1]
    assert not converter._is_valid_extension(valid_extensions, file_extension)


@pytest.mark.parametrize(
    "data",
    [
        (
            (
                ".txt",
                ".csv",
            ),
            ".csv",
        ),
        ((".sas7bdat",), ".sas7bdat"),
    ],
)
def test_is_valid_extension_true(data):
    valid_extensions = data[0]
    file_extension = data[1]
    assert converter._is_valid_extension(valid_extensions, file_extension)


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("sas_file_1", "file1.csv"),
        ("sas_file_2", "file2.csv"),
        ("sas_file_3", "file3.csv"),
    ],
)
def test_to_csv_path_sas(tmp_path, fixture_name, expected_name, expected_dir, request):
    sas_file = Path(request.getfixturevalue(fixture_name))
    converted_file = tmp_path.joinpath(expected_name)
    expected_file = expected_dir.joinpath(expected_name)
    converter.to_csv(sas_file, converted_file)

    with open(expected_file) as f:
        expected = f.read().rstrip()

    with open(converted_file) as f:
        got = f.read().rstrip()

    assert got == expected


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("xpt_file_1", "file1.csv"),
        ("xpt_file_2", "file2.csv"),
    ],
)
def test_to_csv_path_xpt(tmp_path, fixture_name, expected_name, request, xpt_expected_dir):
    xpt_file = Path(request.getfixturevalue(fixture_name))
    converted_file = tmp_path.joinpath(expected_name)
    expected_file = xpt_expected_dir.joinpath(expected_name)
    converter.to_csv(xpt_file, converted_file)

    with open(expected_file) as f:
        expected = f.read().rstrip()

    with open(converted_file) as f:
        got = f.read().rstrip()

    assert got == expected


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("sas_file_1", "file1.csv"),
        ("sas_file_2", "file2.csv"),
        ("sas_file_3", "file3.csv"),
    ],
)
def test_to_csv_str_sas(tmpdir, fixture_name, expected_name, request, expected_dir):
    sas_file = request.getfixturevalue(fixture_name)
    converted_file = str(Path(tmpdir).joinpath(expected_name))
    expected_file = expected_dir.joinpath(expected_name)
    converter.to_csv(sas_file, converted_file)

    with open(expected_file) as f:
        expected = f.read().rstrip()

    with open(converted_file) as f:
        got = f.read().rstrip()

    assert got == expected


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("xpt_file_1", "file1.csv"),
        ("xpt_file_2", "file2.csv"),
    ],
)
def test_to_csv_str_xpt(tmpdir, fixture_name, expected_name, request, xpt_expected_dir):
    sas_file = request.getfixturevalue(fixture_name)
    converted_file = str(Path(tmpdir).joinpath(expected_name))
    expected_file = xpt_expected_dir.joinpath(expected_name)
    converter.to_csv(sas_file, converted_file)

    with open(expected_file) as f:
        expected = f.read().rstrip()

    with open(converted_file) as f:
        got = f.read().rstrip()

    assert got == expected


def test_to_csv_invalid_extension():
    with pytest.raises(AttributeError) as execinfo:
        converter.to_csv("test.sas7bdat", "test.bad")

    assert "sas7bdat conversion error - Valid extension" in str(execinfo.value)


def test_to_dataframe_sas(sas_file_1):
    d = {
        "integer_row": [
            1.0,
            2.0,
            3.0,
            4.0,
            5.0,
        ],
        "text_row": [
            "Some text",
            "Some more text",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc lobortis, risus nec euismod condimentum, lectus ligula porttitor massa, vel ornare mauris arcu vel augue. Maecenas rhoncus consectetur nisl, ac convallis enim pellentesque efficitur. Praesent tristique .  End of textlectus a dolor sodales, in porttitor felis auctor. Etiam dui mauris, commodo at venenatis eu, lacinia nec tellus. Curabitur dictum tincidunt convallis. Duis vestibulum mauris quis felis euismod bibendum. Nulla eget nunc arcu. Nam quis est urna. In eleifend ultricies ultrices. In lacinia auctor ex, sed commodo nisl fringilla sed. Fusce iaculis viverra eros, nec elementum velit aliquam non. Aenean sollicitudin consequat libero, eget mattis.",  # noqa: E501
            "Text",
            "Test",
        ],
        "float_row": [
            2.5,
            17.23,
            3.21,
            100.9,
            98.6,
        ],
        "date_row": [
            "2018-01-02",
            "2018-02-05",
            "2017-11-21",
            "2016-05-19",
            "1999-10-25",
        ],
    }

    df = pd.DataFrame(data=d)
    df["date_row"] = pd.to_datetime(df["date_row"])
    df = df[["integer_row", "text_row", "float_row", "date_row"]]
    df_file = converter.to_dataframe(sas_file_1)
    df_file["date_row"] = pd.to_datetime(df["date_row"]).dt.floor("s")
    pd.testing.assert_frame_equal(df, df_file, check_datetimelike_compat=True)


def test_to_dataframe_xpt(xpt_file_1):
    d = {
        "irow": [
            1.0,
            2.0,
        ],
        "trow": [
            "Some text",
            "Some more test",
        ],
        "frow": [
            1.50,
            17.23,
        ],
    }

    df = pd.DataFrame(data=d)
    df_file = converter.to_dataframe(xpt_file_1)
    pd.testing.assert_frame_equal(df, df_file)


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("sas_file_1", "file1.xlsx"),
        ("sas_file_2", "file2.xlsx"),
        ("sas_file_3", "file3.xlsx"),
    ],
)
def test_to_excel_path_sas(tmp_path, fixture_name, expected_name, request, expected_dir):
    sas_file = Path(request.getfixturevalue(fixture_name))
    converted_file = tmp_path.joinpath(expected_name)
    expected_file = expected_dir.joinpath(expected_name)
    converter.to_excel(sas_file, converted_file)

    df_expected = pd.read_excel(expected_file, engine="openpyxl")
    df_converted = pd.read_excel(converted_file, engine="openpyxl")

    pd.testing.assert_frame_equal(df_expected, df_converted)


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("xpt_file_1", "file1.xlsx"),
        ("xpt_file_2", "file2.xlsx"),
    ],
)
def test_to_excel_path_xpt(tmp_path, fixture_name, expected_name, request, xpt_expected_dir):
    xpt_file = Path(request.getfixturevalue(fixture_name))
    converted_file = tmp_path.joinpath(expected_name)
    expected_file = xpt_expected_dir.joinpath(expected_name)
    converter.to_excel(xpt_file, converted_file)

    df_expected = pd.read_excel(expected_file, engine="openpyxl")
    df_converted = pd.read_excel(converted_file, engine="openpyxl")

    pd.testing.assert_frame_equal(df_expected, df_converted)


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("sas_file_1", "file1.xlsx"),
        ("sas_file_2", "file2.xlsx"),
        ("sas_file_3", "file3.xlsx"),
    ],
)
def test_to_excel_str_sas(tmpdir, fixture_name, expected_name, request, expected_dir):
    sas_file = request.getfixturevalue(fixture_name)
    converted_file = str(Path(tmpdir).joinpath(expected_name))
    expected_file = expected_dir.joinpath(expected_name)
    converter.to_excel(sas_file, converted_file)

    df_expected = pd.read_excel(expected_file, engine="openpyxl")
    df_converted = pd.read_excel(converted_file, engine="openpyxl")

    pd.testing.assert_frame_equal(df_expected, df_converted)


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("xpt_file_1", "file1.xlsx"),
        ("xpt_file_2", "file2.xlsx"),
    ],
)
def test_to_excel_str_xpt(tmpdir, fixture_name, expected_name, request, xpt_expected_dir):
    xpt_file = request.getfixturevalue(fixture_name)
    converted_file = str(Path(tmpdir).joinpath(expected_name))
    expected_file = xpt_expected_dir.joinpath(expected_name)
    converter.to_excel(xpt_file, converted_file)

    df_expected = pd.read_excel(expected_file, engine="openpyxl")
    df_converted = pd.read_excel(converted_file, engine="openpyxl")

    pd.testing.assert_frame_equal(df_expected, df_converted)


def test_to_excel_missing_openpyxl(tmp_path, sas_file_1):
    with patch("pandas.DataFrame.to_excel", side_effect=ModuleNotFoundError):
        with pytest.raises(ModuleNotFoundError) as execinfo:
            converter.to_excel(sas_file_1, tmp_path / "test.xlsx")

    assert "optional dependency openpyxl is required" in str(execinfo.value)


def test_to_excel_invalid_extension():
    with pytest.raises(AttributeError) as execinfo:
        converter.to_excel("test.sas7bdat", "test.bad")

    assert "sas7bdat conversion error - Valid extension" in str(execinfo.value)


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("sas_file_1", "file1.json"),
        ("sas_file_2", "file2.json"),
        ("sas_file_3", "file3.json"),
    ],
)
def test_to_json_path_sas(tmp_path, fixture_name, expected_name, request, expected_dir):
    sas_file = Path(request.getfixturevalue(fixture_name))
    converted_file = tmp_path.joinpath(expected_name)
    expected_file = expected_dir.joinpath(expected_name)
    converter.to_json(sas_file, converted_file)

    with open(expected_file) as f:
        expected = json.load(f)

    with open(converted_file) as f:
        got = json.load(f)

    assert got == expected


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("xpt_file_1", "file1.json"),
        ("xpt_file_2", "file2.json"),
    ],
)
def test_to_json_path_xpt(tmp_path, fixture_name, expected_name, request, xpt_expected_dir):
    xpt_file = Path(request.getfixturevalue(fixture_name))
    converted_file = tmp_path.joinpath(expected_name)
    expected_file = xpt_expected_dir.joinpath(expected_name)
    converter.to_json(xpt_file, converted_file)

    with open(expected_file) as f:
        expected = json.load(f)

    with open(converted_file) as f:
        got = json.load(f)

    assert got == expected


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("sas_file_1", "file1.json"),
        ("sas_file_2", "file2.json"),
        ("sas_file_3", "file3.json"),
    ],
)
def test_to_json_str_sas(tmpdir, fixture_name, expected_name, request, expected_dir):
    sas_file = request.getfixturevalue(fixture_name)
    converted_file = str(Path(tmpdir).joinpath(expected_name))
    expected_file = expected_dir.joinpath(expected_name)
    converter.to_json(sas_file, converted_file)

    with open(expected_file) as f:
        expected = json.load(f)

    with open(converted_file) as f:
        got = json.load(f)

    assert got == expected


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("xpt_file_1", "file1.json"),
        ("xpt_file_2", "file2.json"),
    ],
)
def test_to_json_str_xpt(tmpdir, fixture_name, expected_name, request, xpt_expected_dir):
    xpt_file = request.getfixturevalue(fixture_name)
    converted_file = str(Path(tmpdir).joinpath(expected_name))
    expected_file = xpt_expected_dir.joinpath(expected_name)
    converter.to_json(xpt_file, converted_file)

    with open(expected_file) as f:
        expected = json.load(f)

    with open(converted_file) as f:
        got = json.load(f)

    assert got == expected


def test_to_json_invalid_extension():
    with pytest.raises(AttributeError) as execinfo:
        converter.to_json("test.sas7bdat", "test.bad")

    assert "sas7bdat conversion error - Valid extension" in str(execinfo.value)


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("sas_file_1", "file1.xml"),
        ("sas_file_2", "file2.xml"),
        ("sas_file_3", "file3.xml"),
    ],
)
def test_to_xml_path_sas(tmp_path, fixture_name, expected_name, expected_dir, request):
    sas_file = Path(request.getfixturevalue(fixture_name))
    converted_file = tmp_path.joinpath(expected_name)
    expected_file = expected_dir.joinpath(expected_name)
    converter.to_xml(sas_file, converted_file)

    with open(expected_file) as f:
        expected = f.read().rstrip()

    with open(converted_file) as f:
        got = f.read().rstrip()

    assert got == expected


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("xpt_file_1", "file1.xml"),
        ("xpt_file_2", "file2.xml"),
    ],
)
def test_to_xml_path_xpt(tmp_path, fixture_name, expected_name, request, xpt_expected_dir):
    xpt_file = Path(request.getfixturevalue(fixture_name))
    converted_file = tmp_path.joinpath(expected_name)
    expected_file = xpt_expected_dir.joinpath(expected_name)
    converter.to_xml(xpt_file, converted_file)

    with open(expected_file) as f:
        expected = f.read().rstrip()

    with open(converted_file) as f:
        got = f.read().rstrip()

    assert got == expected


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("sas_file_1", "file1.xml"),
        ("sas_file_2", "file2.xml"),
        ("sas_file_3", "file3.xml"),
    ],
)
def test_to_xml_str_sas(tmpdir, fixture_name, expected_name, request, expected_dir):
    sas_file = request.getfixturevalue(fixture_name)
    converted_file = str(Path(tmpdir).joinpath(expected_name))
    expected_file = expected_dir.joinpath(expected_name)
    converter.to_xml(sas_file, converted_file)

    with open(expected_file) as f:
        expected = f.read().rstrip()

    with open(converted_file) as f:
        got = f.read().rstrip()

    assert got == expected


@pytest.mark.parametrize(
    "fixture_name, expected_name",
    [
        ("xpt_file_1", "file1.xml"),
        ("xpt_file_2", "file2.xml"),
    ],
)
def test_to_xml_str_xpt(tmpdir, fixture_name, expected_name, request, xpt_expected_dir):
    xpt_file = request.getfixturevalue(fixture_name)
    converted_file = str(Path(tmpdir).joinpath(expected_name))
    expected_file = xpt_expected_dir.joinpath(expected_name)
    converter.to_xml(xpt_file, converted_file)

    with open(expected_file) as f:
        expected = f.read().rstrip()

    with open(converted_file) as f:
        got = f.read().rstrip()

    assert got == expected


def test_to_xml_invalid_extension():
    with pytest.raises(AttributeError) as execinfo:
        converter.to_xml("test.sas7bdat", "test.bad")

    assert "sas7bdat conversion error - Valid extension" in str(execinfo.value)


@pytest.mark.parametrize(
    "file_dict",
    [
        {
            "sas7bdat_fil": "test.sas7bdat",
            "export_file": "test.csv",
        },
        {
            "sas7bdat_file": "test.sas7bdat",
            "export_fil": "test.csv",
        },
        {
            "sas7bdat_file": "test.sas7bdat",
        },
        {
            "export_file": "test.csv",
        },
    ],
)
def test_raise_on_invalid_file_dict_error(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter._rise_on_invalid_file_dict(file_dict)

    assert "Invalid key" in str(execinfo.value)


@pytest.mark.parametrize(
    "path, expected", [(Path("test/path"), str(Path("test/path"))), ("test/path", "test/path")]
)
def test_format_path(path, expected):
    converted = converter._format_path(path)

    assert converted == expected
    assert isinstance(converted, str)


@pytest.mark.parametrize("file_type", ["csv", "xlsx", "json", "xml"])
def test_walk_dir_sas(tmpdir, sas7bdat_dir, file_type):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    converter._walk_dir(file_type, tmpdir)
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len(
        [name for name in Path(tmpdir).iterdir() if name.suffix == f".{file_type}"]
    )

    assert sas_counter == convert_counter


@pytest.mark.parametrize("file_type", ["csv", "xlsx", "json", "xml"])
def test_walk_dir_xpt(tmpdir, xpt_dir, file_type):
    xpt_files = [str(x) for x in xpt_dir.iterdir()]
    for xpt_file in xpt_files:
        shutil.copy(xpt_file, tmpdir)

    converter._walk_dir(file_type, tmpdir)
    xpt_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xpt"])
    convert_counter = len(
        [name for name in Path(tmpdir).iterdir() if name.suffix == f".{file_type}"]
    )

    assert xpt_counter == convert_counter
