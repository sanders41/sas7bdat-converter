import filecmp
import os
import pandas as pd
import pytest
import shutil
import xlrd
from pathlib import Path
from glob import glob
from sas7bdat_converter.converter import SASConverter


current_dir = Path().absolute()
expected_dir = current_dir.joinpath(Path('tests/data/expected_files'))
sas7bdat_dir = current_dir.joinpath(Path('tests/data/sas7bdat_files'))
sas_file1 = sas7bdat_dir / 'file1.sas7bdat'
sas_file2 = sas7bdat_dir / 'file2.sas7bdat'
sas_file3 = sas7bdat_dir / 'file3.sas7bdat'


def test_batch_to_csv(tmpdir):
    sas_converter = SASConverter()
    converted_file1 = Path(tmpdir) / 'file1.csv'
    converted_file2 = Path(tmpdir) / 'file2.csv'
    converted_file3 = Path(tmpdir) / 'file3.csv'

    file_dict = [
        {'sas7bdat_file': sas_file1, 'export_file': converted_file1},
        {'sas7bdat_file': sas_file2, 'export_file': converted_file2},
        {'sas7bdat_file': sas_file3, 'export_file': converted_file3},
    ]

    sas_converter.batch_to_csv(file_dict)

    files_created = False

    if ((Path(tmpdir) / converted_file1).is_file() and
            (Path(tmpdir) / converted_file2).is_file() and
            (Path(tmpdir) / converted_file3).is_file()):
        files_created = True

    assert files_created


def test_batch_to_excel(tmpdir):
    sas_converter = SASConverter()
    converted_file1 = Path(tmpdir) / 'file1.xlsx'
    converted_file2 = Path(tmpdir) / 'file2.xlsx'
    converted_file3 = Path(tmpdir) / 'file3.xlsx'

    file_dict = [
        {'sas7bdat_file': sas_file1, 'export_file': converted_file1},
        {'sas7bdat_file': sas_file2, 'export_file': converted_file2},
        {'sas7bdat_file': sas_file3, 'export_file': converted_file3},
    ]

    sas_converter.batch_to_excel(file_dict)
    files_created = False

    if ((Path(tmpdir) / converted_file1).is_file() and
            (Path(tmpdir) / converted_file2).is_file() and
            (Path(tmpdir) / converted_file3).is_file()):
        files_created = True

    assert(files_created)


def test_batch_to_json(tmpdir):
    sas_converter = SASConverter()
    converted_file1 = Path(tmpdir) / 'file1.json'
    converted_file2 = Path(tmpdir) / 'file2.json'
    converted_file3 = Path(tmpdir) / 'file3.json'

    file_dict = [
        {'sas7bdat_file': sas_file1, 'export_file': converted_file1},
        {'sas7bdat_file': sas_file2, 'export_file': converted_file2},
        {'sas7bdat_file': sas_file3, 'export_file': converted_file3},
    ]

    sas_converter.batch_to_json(file_dict)
    files_created = False

    if ((Path(tmpdir) / converted_file1).is_file() and
            (Path(tmpdir) / converted_file2).is_file() and
            (Path(tmpdir) / converted_file3).is_file()):
        files_created = True

    assert(files_created)


def test_batch_to_xml(tmpdir):
    sas_converter = SASConverter()
    converted_file1 = Path(tmpdir) / 'file1.xml'
    converted_file2 = Path(tmpdir) / 'file2.xml'
    converted_file3 = Path(tmpdir) / 'file3.xml'

    file_dict = [
        {'sas7bdat_file': sas_file1, 'export_file': converted_file1},
        {'sas7bdat_file': sas_file2, 'export_file': converted_file2},
        {'sas7bdat_file': sas_file3, 'export_file': converted_file3},
    ]

    sas_converter.batch_to_xml(file_dict)
    files_created = False

    if ((Path(tmpdir) / converted_file1).is_file() and
            (Path(tmpdir) / converted_file2).is_file() and
            (Path(tmpdir) / converted_file3).is_file()):
        files_created = True

    assert(files_created)


def test_dir_to_csv_same_dir(tmpdir):
    sas_converter = SASConverter()
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    sas_converter.dir_to_csv(str(tmpdir))
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'sas7bdat'])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'csv'])

    assert sas_counter == convert_counter


def test_dir_to_csv_different_dir(tmpdir):
    sas_converter = SASConverter()
    sas_converter.dir_to_csv(str(sas7bdat_dir), str(tmpdir))
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == 'sas7bdat'])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'csv'])

    assert sas_counter == convert_counter


def test_dir_to_excel_same_dir(tmpdir):
    sas_converter = SASConverter()
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    sas_converter.dir_to_excel(str(tmpdir))
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'sas7bdat'])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'xlsx'])

    assert sas_counter == convert_counter


def test_dir_to_excel_different_dir(tmpdir):
    sas_converter = SASConverter()
    sas_converter.dir_to_excel(str(sas7bdat_dir), str(tmpdir))
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == 'sas7bdat'])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'xlsx'])

    assert sas_counter == convert_counter


def test_dir_to_json_same_dir(tmpdir):
    sas_converter = SASConverter()
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    sas_converter.dir_to_json(str(tmpdir))
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'sas7bdat'])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'json'])

    assert sas_counter == convert_counter


def test_dir_to_json_different_dir(tmpdir):
    sas_converter = SASConverter()
    sas_converter.dir_to_json(str(sas7bdat_dir), str(tmpdir))
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == 'sas7bdat'])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'json'])

    assert sas_counter == convert_counter


def test_dir_to_xml_same_dir(tmpdir):
    sas_converter = SASConverter()
    sas_files = [str(x) for x in sas7bdat_dir.iterdir()]
    for sas_file in sas_files:
        shutil.copy(sas_file, tmpdir)

    sas_converter.dir_to_xml(str(tmpdir))
    sas_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'sas7bdat'])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'xml'])

    assert sas_counter == convert_counter


def test_dir_to_excel_different_dir(tmpdir):
    sas_converter = SASConverter()
    sas_converter.dir_to_xml(str(sas7bdat_dir), str(tmpdir))
    sas_counter = len([name for name in Path(sas7bdat_dir).iterdir() if name.suffix == 'sas7bdat'])
    convert_counter = len([name for name in Path(tmpdir).iterdir() if name.suffix == 'xml'])

    assert sas_counter == convert_counter


@pytest.mark.parametrize('exception', [
    ('sas7bdat conversion error - Valid extension for to_csv conversion is: .csv', ['.csv'], 'to_csv'),
    ('sas7bdat conversion error - Valid extensions for to_csv conversion are: .csv, .txt', ['.csv', '.txt'], 'to_csv'),
])
def test_file_extension_exception_message_is(exception):
    valid_message = exception[0]
    valid_extensions = exception[1]
    sas_converter = SASConverter()
    test_message = sas_converter._file_extension_exception_message(exception[2], valid_extensions)

    assert valid_message == test_message


def test_invalid_key_exception_message_no_optional():
    valid_message = 'Invalid key provided, expected keys are: sas7bdat_file, export_file'
    required_keys = ['sas7bdat_file', 'export_file']
    sas_converter = SASConverter()
    test_message = sas_converter._invalid_key_exception_message(required_keys=required_keys)

    assert valid_message == test_message


def test_invalid_key_exception_message_optional():
    valid_message = 'Invalid key provided, expected keys are: sas7bdat_file, export_file and optional keys are: root_node, first_node'
    required_keys = ['sas7bdat_file', 'export_file']
    optional_keys = ['root_node', 'first_node']
    sas_converter = SASConverter()
    test_message = sas_converter._invalid_key_exception_message(required_keys=required_keys, optional_keys=optional_keys)

    assert valid_message == test_message


@pytest.mark.parametrize('data', [
    (('.txt', '.csv',), '.xml'),
    (('.sas7bdat',), '.json'), 
])
def test_is_valid_extension_false(data):
    sas_converter = SASConverter()
    valid_extensions = data[0]
    file_extension = data[1]
    assert not sas_converter._is_valid_extension(valid_extensions, file_extension)


@pytest.mark.parametrize('data', [
    (('.txt', '.csv',), '.csv'),
    (('.sas7bdat',), '.sas7bdat'),
])
def test_is_valid_extension_true(data):
    sas_converter = SASConverter()
    valid_extensions = data[0]
    file_extension = data[1]
    assert sas_converter._is_valid_extension(valid_extensions, file_extension)


def test_to_csv(tmpdir):
    sas_converter = SASConverter()
    converted_file = Path(tmpdir) / 'file1.csv'
    expected_file = expected_dir / 'file1.csv'
    sas_converter.to_csv(sas_file1, converted_file)

    assert filecmp.cmp(converted_file, expected_file, shallow=False)


def test_to_dataframe():
    d = {
        'integer_row': [1.0, 2.0, 3.0, 4.0, 5.0,],
        'text_row': [
            'Some text',
            'Some more text',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc lobortis, risus nec euismod condimentum, lectus ligula porttitor massa, vel ornare mauris arcu vel augue. Maecenas rhoncus consectetur nisl, ac convallis enim pellentesque efficitur. Praesent tristique .  End of textlectus a dolor sodales, in porttitor felis auctor. Etiam dui mauris, commodo at venenatis eu, lacinia nec tellus. Curabitur dictum tincidunt convallis. Duis vestibulum mauris quis felis euismod bibendum. Nulla eget nunc arcu. Nam quis est urna. In eleifend ultricies ultrices. In lacinia auctor ex, sed commodo nisl fringilla sed. Fusce iaculis viverra eros, nec elementum velit aliquam non. Aenean sollicitudin consequat libero, eget mattis.',
            'Text',
            'Test',
        ],
        'float_row': [2.5, 17.23, 3.21, 100.9, 98.6,],
        'date_row': ['2018-01-02', '2018-02-05', '2017-11-21', '2016-05-19', '1999-10-25',]
    }

    df = pd.DataFrame(data=d)
    df['date_row'] = pd.to_datetime(df['date_row'])
    df = df[['integer_row', 'text_row', 'float_row', 'date_row']]
    sas_converter = SASConverter()
    sas_file = sas7bdat_dir / 'file1.sas7bdat'
    df_file = sas_converter.to_dataframe(sas_file)
    pd.testing.assert_frame_equal(df, df_file, check_datetimelike_compat=True)


def test_to_excel(tmpdir):
    sas_converter = SASConverter()
    sas_file = sas7bdat_dir / 'file1.sas7bdat'
    converted_file = Path(tmpdir) / 'file1.xlsx'
    expected_file = expected_dir / 'file1.xlsx'
    sas_converter.to_excel(sas_file, converted_file)

    df_expected = pd.read_excel(expected_file)
    df_converted = pd.read_excel(converted_file)

    pd.testing.assert_frame_equal(df_expected, df_converted)


def test_to_json(tmpdir):
    sas_converter = SASConverter()
    sas_file = sas7bdat_dir / 'file1.sas7bdat'
    converted_file = Path(tmpdir) / 'file1.json'
    expected_file = expected_dir / 'file1.json'
    sas_converter.to_json(sas_file, converted_file)

    assert filecmp.cmp(converted_file, expected_file, shallow=False)


def test_to_xml(tmpdir):
    sas_converter = SASConverter()
    sas_file = sas7bdat_dir / 'file1.sas7bdat'
    converted_file = Path(tmpdir) / 'file1.xml'
    expected_file = expected_dir / 'file1.xml'
    sas_converter.to_xml(sas_file, converted_file)

    assert filecmp.cmp(converted_file, expected_file, shallow=False)