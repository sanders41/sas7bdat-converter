import filecmp
import os
import shutil
from pathlib import Path

import pandas as pd
import pytest

import sas7bdat_converter.converter as converter

current_dir = Path().absolute()


def test_batch_to_csv_path(tmp_path, sas_file_1, sas_file_2, sas_file_3):
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


def test_batch_to_csv_str(tmp_path, sas_file_1, sas_file_2, sas_file_3):
    converted_file_1 = tmp_path.joinpath("file1.csv")
    converted_file_2 = tmp_path.joinpath("file2.csv")
    converted_file_3 = tmp_path.joinpath("file3.csv")

    file_dict = [
        {"sas7bdat_file": str(sas_file_1), "export_file": str(converted_file_1)},
        {"sas7bdat_file": str(sas_file_2), "export_file": str(converted_file_2)},
        {"sas7bdat_file": str(sas_file_3), "export_file": str(converted_file_3)},
    ]

    converter.batch_to_csv(file_dict)

    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


file_dicts = [
    [{"bad_key": "test.sas7bdat", "export_file": "test.csv"}],
    [{"sas7bdat_file": "test.sas7bdat", "bad_key": "test.csv"}],
    [{"sas_bad_key": "test.sas7bdate", "export_bad_key": "test.csv"}],
]


@pytest.mark.parametrize("file_dict", file_dicts)
def test_batch_to_csv_invalid_key(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter.batch_to_csv(file_dict)

    assert "Invalid key provided" in str(execinfo.value)


def test_batch_to_excel_path(tmp_path, sas_file_1, sas_file_2, sas_file_3):
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


def test_batch_to_excel_str(tmp_path, sas_file_1, sas_file_2, sas_file_3):
    converted_file_1 = tmp_path.joinpath("file1.xlsx")
    converted_file_2 = tmp_path.joinpath("file2.xlsx")
    converted_file_3 = tmp_path.joinpath("file3.xlsx")

    file_dict = [
        {"sas7bdat_file": str(sas_file_1), "export_file": str(converted_file_1)},
        {"sas7bdat_file": str(sas_file_2), "export_file": str(converted_file_2)},
        {"sas7bdat_file": str(sas_file_3), "export_file": str(converted_file_3)},
    ]

    converter.batch_to_excel(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


file_dicts = [
    [{"bad_key": "test.sas7bdat", "export_file": "test.xlsx"}],
    [{"sas7bdat_file": "test.sas7bdat", "bad_key": "test.xlsx"}],
    [{"sas_bad_key": "test.sas7bdate", "export_bad_key": "test.xlsx"}],
]


@pytest.mark.parametrize("file_dict", file_dicts)
def test_batch_to_excel_invalid_key(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter.batch_to_excel(file_dict)

    assert "Invalid key provided" in str(execinfo.value)


def test_batch_to_json_path(tmp_path, sas_file_1, sas_file_2, sas_file_3):
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


def test_batch_to_json_path_str(tmp_path, sas_file_1, sas_file_2, sas_file_3):
    converted_file_1 = tmp_path.joinpath("file1.json")
    converted_file_2 = tmp_path.joinpath("file2.json")
    converted_file_3 = tmp_path.joinpath("file3.json")

    file_dict = [
        {"sas7bdat_file": str(sas_file_1), "export_file": str(converted_file_1)},
        {"sas7bdat_file": str(sas_file_2), "export_file": str(converted_file_2)},
        {"sas7bdat_file": str(sas_file_3), "export_file": str(converted_file_3)},
    ]

    converter.batch_to_json(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


file_dicts = [
    [{"bad_key": "test.sas7bdat", "export_file": "test.json"}],
    [{"sas7bdat_file": "test.sas7bdat", "bad_key": "test.json"}],
    [{"sas_bad_key": "test.sas7bdate", "export_bad_key": "test.json"}],
]


@pytest.mark.parametrize("file_dict", file_dicts)
def test_batch_to_json_invalid_key(file_dict):
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
def test_batch_to_xml_path(tmp_path, sas_file_1, sas_file_2, sas_file_3, optional):
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
            {"sas7bdat_file": sas_file_1, "export_file": converted_file_1,},
            {"sas7bdat_file": sas_file_2, "export_file": converted_file_2,},
            {"sas7bdat_file": sas_file_3, "export_file": converted_file_3,},
        ]

    converter.batch_to_xml(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


@pytest.mark.parametrize("optional", optionals)
def test_batch_to_xml_str(tmp_path, sas_file_1, sas_file_2, sas_file_3, optional):
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
            {"sas7bdat_file": str(sas_file_1), "export_file": str(converted_file_1),},
            {"sas7bdat_file": str(sas_file_2), "export_file": str(converted_file_2),},
            {"sas7bdat_file": str(sas_file_3), "export_file": str(converted_file_3),},
        ]

    converter.batch_to_xml(file_dict)
    files_created = False

    if converted_file_1.is_file() and converted_file_2.is_file() and converted_file_3.is_file():
        files_created = True

    assert files_created


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
def test_batch_to_xml_invalid_key(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter.batch_to_xml(file_dict)

    assert "Invalid key provided" in str(execinfo.value)


def test_dir_to_csv_same_dir_path(tmp_path, sas7bdat_dir):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    converter.dir_to_csv(tmp_path)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".csv"])

    assert sas_counter == convert_counter


def test_dir_to_csv_same_dir_str(tmpdir, sas7bdat_dir):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    converter.dir_to_csv(tmpdir)
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".csv"])

    assert sas_counter == convert_counter


def test_dir_to_csv_different_dir_path(tmp_path, sas7bdat_dir):
    converter.dir_to_csv(dir_path=sas7bdat_dir, export_path=tmp_path)
    sas_counter = len([name for name in sas7bdat_dir.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".csv"])

    assert sas_counter == convert_counter


def test_dir_to_csv_different_dir_str(tmpdir, sas7bdat_dir):
    converter.dir_to_csv(dir_path=str(sas7bdat_dir), export_path=tmpdir)
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".csv"])

    assert sas_counter == convert_counter


def test_dir_to_excel_same_dir_path(tmp_path, sas7bdat_dir):
    sas_files = [x for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    converter.dir_to_excel(tmp_path)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xlsx"])

    assert sas_counter == convert_counter


def test_dir_to_excel_same_dir_str(tmpdir, sas7bdat_dir):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    converter.dir_to_excel(tmpdir)
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xlsx"])

    assert sas_counter == convert_counter


def test_dir_to_excel_different_dir_path(tmp_path, sas7bdat_dir):
    converter.dir_to_excel(dir_path=sas7bdat_dir, export_path=tmp_path)
    sas_counter = len([name for name in sas7bdat_dir.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xlsx"])

    assert sas_counter == convert_counter


def test_dir_to_excel_different_dir_str(tmpdir, sas7bdat_dir):
    converter.dir_to_excel(dir_path=str(sas7bdat_dir), export_path=tmpdir)
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xlsx"])

    assert sas_counter == convert_counter


def test_dir_to_json_same_dir_path(tmp_path, sas7bdat_dir):
    sas_files = [x for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmp_path)

    converter.dir_to_json(tmp_path)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".json"])

    assert sas_counter == convert_counter


def test_dir_to_json_same_dir_str(tmpdir, sas7bdat_dir):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    converter.dir_to_json(tmpdir)
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".json"])

    assert sas_counter == convert_counter


def test_dir_to_json_different_dir_path(tmp_path, sas7bdat_dir):
    converter.dir_to_json(sas7bdat_dir, tmp_path)
    sas_counter = len([name for name in sas7bdat_dir.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".json"])

    assert sas_counter == convert_counter


def test_dir_to_json_different_dir_str(tmpdir, sas7bdat_dir):
    converter.dir_to_json(str(sas7bdat_dir), tmpdir)
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".json"])

    assert sas_counter == convert_counter


def test_dir_to_xml_same_dir_path(tmp_path, sas7bdat_dir):
    sas_files = [x for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, str(tmp_path))

    converter.dir_to_xml(tmp_path)
    sas_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xml"])

    assert sas_counter == convert_counter


def test_dir_to_xml_same_dir_str(tmpdir, sas7bdat_dir):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    converter.dir_to_xml(tmpdir)
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xml"])

    assert sas_counter == convert_counter


def test_dir_to_xml_different_dir_path(tmp_path, sas7bdat_dir):
    converter.dir_to_xml(sas7bdat_dir, tmp_path)
    sas_counter = len([name for name in sas7bdat_dir.iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in tmp_path.iterdir() if name.suffix == ".xml"])

    assert sas_counter == convert_counter


def test_dir_to_xml_different_dir_str(tmpdir, sas7bdat_dir):
    converter.dir_to_xml(str(sas7bdat_dir), tmpdir)
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".xml"])

    assert sas_counter == convert_counter


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
    valid_message = "Invalid key provided, expected keys are: sas7bdat_file, export_file and optional keys are: root_node, first_node"
    required_keys = ["sas7bdat_file", "export_file"]
    optional_keys = ["root_node", "first_node"]
    test_message = converter._invalid_key_exception_message(
        required_keys=required_keys, optional_keys=optional_keys
    )

    assert valid_message == test_message


@pytest.mark.parametrize("data", [((".txt", ".csv",), ".xml"), ((".sas7bdat",), ".json"),])
def test_is_valid_extension_false(data):
    valid_extensions = data[0]
    file_extension = data[1]
    assert not converter._is_valid_extension(valid_extensions, file_extension)


@pytest.mark.parametrize("data", [((".txt", ".csv",), ".csv"), ((".sas7bdat",), ".sas7bdat"),])
def test_is_valid_extension_true(data):
    valid_extensions = data[0]
    file_extension = data[1]
    assert converter._is_valid_extension(valid_extensions, file_extension)


@pytest.fixture(params=["sas_file_1", "sas_file_2", "sas_file_3"])
def test_to_csv_path(tmp_path, request, expected_dir):
    sas_file = Path(request.getfixturevalue(request.param))
    converted_file = tmp_path.joinpath("file1.csv")
    expected_file = expected_dir.joinpath("file1.csv")
    converter.to_csv(sas_file, converted_file)

    assert filecmp.cmp(converted_file, expected_file, shallow=False)


@pytest.fixture(params=["sas_file_1", "sas_file_2", "sas_file_3"])
def test_to_csv_str(tmpdir, request, expected_dir):
    sas_file = request.getfixturevalue(request.param)
    converted_file = str(Path(tmpdir).joinpath("file1.csv"))
    expected_file = expected_dir.joinpath("file1.csv")
    converter.to_csv(sas_file, converted_file)

    assert filecmp.cmp(converted_file, expected_file, shallow=False)


def test_to_csv_invalid_extension():
    with pytest.raises(AttributeError) as execinfo:
        converter.to_csv("test.sas7bdat", "test.bad")

    assert "sas7bdat conversion error - Valid extension" in str(execinfo.value)


def test_to_dataframe(sas_file_1):
    d = {
        "integer_row": [1.0, 2.0, 3.0, 4.0, 5.0,],
        "text_row": [
            "Some text",
            "Some more text",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc lobortis, risus nec euismod condimentum, lectus ligula porttitor massa, vel ornare mauris arcu vel augue. Maecenas rhoncus consectetur nisl, ac convallis enim pellentesque efficitur. Praesent tristique .  End of textlectus a dolor sodales, in porttitor felis auctor. Etiam dui mauris, commodo at venenatis eu, lacinia nec tellus. Curabitur dictum tincidunt convallis. Duis vestibulum mauris quis felis euismod bibendum. Nulla eget nunc arcu. Nam quis est urna. In eleifend ultricies ultrices. In lacinia auctor ex, sed commodo nisl fringilla sed. Fusce iaculis viverra eros, nec elementum velit aliquam non. Aenean sollicitudin consequat libero, eget mattis.",
            "Text",
            "Test",
        ],
        "float_row": [2.5, 17.23, 3.21, 100.9, 98.6,],
        "date_row": ["2018-01-02", "2018-02-05", "2017-11-21", "2016-05-19", "1999-10-25",],
    }

    df = pd.DataFrame(data=d)
    df["date_row"] = pd.to_datetime(df["date_row"])
    df = df[["integer_row", "text_row", "float_row", "date_row"]]
    df_file = converter.to_dataframe(sas_file_1)
    pd.testing.assert_frame_equal(df, df_file, check_datetimelike_compat=True)


@pytest.fixture(params=["sas_file_1", "sas_file_2", "sas_file_3"])
def test_to_excel_path(tmp_path, request, expected_dir):
    sas_file = Path(request.getfixturevalue(request.param))
    converted_file = tmp_path.joinpath("file1.xlsx")
    expected_file = expected_dir.joinpath("file1.xlsx")
    converter.to_excel(sas_file, converted_file)

    df_expected = pd.read_excel(expected_file, engine="openpyxl")
    df_converted = pd.read_excel(converted_file, engine="openpyxl")

    pd.testing.assert_frame_equal(df_expected, df_converted)


@pytest.fixture(params=["sas_file_1", "sas_file_2", "sas_file_3"])
def test_to_excel_str(tmpdir, request, expected_dir):
    sas_file = request.getfixturevalue(request.param)
    converted_file = str(Path(tmpdir).joinpath("file1.xlsx"))
    expected_file = expected_dir.joinpath("file1.xlsx")
    converter.to_excel(sas_file, converted_file)

    df_expected = pd.read_excel(expected_file, engine="openpyxl")
    df_converted = pd.read_excel(converted_file, engine="openpyxl")

    pd.testing.assert_frame_equal(df_expected, df_converted)


def test_to_excel_invalid_extension():
    with pytest.raises(AttributeError) as execinfo:
        converter.to_excel("test.sas7bdat", "test.bad")

    assert "sas7bdat conversion error - Valid extension" in str(execinfo.value)


@pytest.fixture(params=["sas_file_1", "sas_file_2", "sas_file_3"])
def test_to_json_path(tmp_path, request, expected_dir):
    sas_file = Path(request.getfixturevalue(request.param))
    converted_file = tmp_path.joinpath("file1.json")
    expected_file = expected_dir.joinpath("file1.json")
    converter.to_json(sas_file, converted_file)

    assert filecmp.cmp(converted_file, expected_file, shallow=False)


@pytest.fixture(params=["sas_file_1", "sas_file_2", "sas_file_3"])
def test_to_json_str(tmpdir, request, expected_dir):
    sas_file = request.getfixturevalue(request.param)
    converted_file = str(Path(tmpdir).joinpath("file1.json"))
    expected_file = expected_dir.joinpath("file1.json")
    converter.to_json(sas_file, converted_file)

    assert filecmp.cmp(converted_file, expected_file, shallow=False)


def test_to_json_invalid_extension():
    with pytest.raises(AttributeError) as execinfo:
        converter.to_json("test.sas7bdat", "test.bad")

    assert "sas7bdat conversion error - Valid extension" in str(execinfo.value)


@pytest.fixture(params=["sas_file_1", "sas_file_2", "sas_file_3"])
def test_to_xml_path(tmp_path, request, expected_dir):
    sas_file = Path(request.getfixturevalue(request.param))
    converted_file = tmp_path.joinpath("file1.xml")
    expected_file = expected_dir.joinpath("file1.xml")
    converter.to_xml(sas_file, converted_file)

    assert filecmp.cmp(converted_file, expected_file, shallow=False)


@pytest.fixture(params=["sas_file_1", "sas_file_2", "sas_file_3"])
def test_to_xml_str(tmpdir, request, expected_dir):
    sas_file = request.getfixturevalue(request.param)
    converted_file = str(Path(tmpdir).joinpath("file1.xml"))
    expected_file = expected_dir.joinpath("file1.xml")
    converter.to_xml(sas_file, converted_file)

    assert filecmp.cmp(converted_file, expected_file, shallow=False)


def test_to_xml_invalid_extension():
    with pytest.raises(AttributeError) as execinfo:
        converter.to_xml("test.sas7bdat", "test.bad")

    assert "sas7bdat conversion error - Valid extension" in str(execinfo.value)


def test_raise_on_invalid_file_dict_valid():
    file_dict = {
        "sas7bdat_file": "test.sas7bdat",
        "export_file": "test.csv",
    }

    result = converter._rise_on_invalid_file_dict(file_dict)

    assert not result


@pytest.mark.parametrize(
    "file_dict",
    [
        {"sas7bdat_fil": "test.sas7bdat", "export_file": "test.csv",},
        {"sas7bdat_file": "test.sas7bdat", "export_fil": "test.csv",},
        {"sas7bdat_file": "test.sas7bdat",},
        {"export_file": "test.csv",},
    ],
)
def test_raise_on_invalid_file_dict_error(file_dict):
    with pytest.raises(KeyError) as execinfo:
        converter._rise_on_invalid_file_dict(file_dict)

    assert "Invalid key" in str(execinfo.value)


@pytest.mark.parametrize("path", [Path("test/path"), "test/path"])
def test_format_path(path):
    converted = converter._format_path(path)
    assert converted == "test/path"
    assert isinstance(converted, str)


@pytest.mark.parametrize("file_type", ["csv", "xlsx", "json", "xml"])
def test_walk_dir(tmpdir, sas7bdat_dir, file_type):
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    converter._walk_dir(file_type, tmpdir)
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == ".sas7bdat"])
    convert_counter = len(
        [name for name in Path(tmpdir).iterdir() if name.suffix == f".{file_type}"]
    )

    assert sas_counter == convert_counter
