import csv
import json
import numpy as np
import pandas as pd

from pathlib import Path
from typing import Dict, List, Optional, Tuple
from xml.sax.saxutils import escape


__file_dict_required_keys = ['sas7bdat_file', 'export_file',]


def batch_to_csv(file_dicts: List[Dict[str, str]]) -> None:
    """
    Converts a batch of sas7bdat files to csv files.

    Args:
        file_dicts: A list dictionaries containing the files to convert. The dictionary should
                    contain the keys 'sas7bdat_file' (containing the path and name to the sas7bdat file)
                    and 'export_file' containing the path and name of the export csv). 
                    Example: file_dict = [{'sas7bdat_file': 'sas_file1.sas7bdat', 'export_file': 'converted_file1.csv'},
                                          {'sas7bdat_file': 'sas_file2.sas7bdat', 'export_file': 'converted_file2.csv'}]
    """
    for file_dict in file_dicts:
        if len(set(file_dict).intersection(__file_dict_required_keys)) != len(__file_dict_required_keys):
            message = _invalid_key_exception_message(required_keys=__file_dict_required_keys)
            raise KeyError(message)

        sas7bdat = file_dict['sas7bdat_file']
        export = file_dict['export_file']
        to_csv(sas7bdat_file=sas7bdat, export_file=export)


def batch_to_excel(file_dicts: List[Dict[str, str]]) -> None:
    """
    Converts a batch of sas7bdat files to xlsx files.

    Args:
        file_dicts: A list of dictionaries containing the files to convert. The dictionary should
                    contain the keys 'sas7bdat_file' (containing the path and name to the sas7bdat file)
                    and 'export_file' containing the path and name of the export xlsx). 
                    Example: file_dict = [{'sas7bdat_file': 'sas_file1.sas7bdat', 'export_file': 'converted_file1.xlsx'},
                                          {'sas7bdat_file': 'sas_file2.sas7bdat', 'export_file': 'converted_file2.xlxs'}]
    """
    for file_dict in file_dicts:
        if len(set(file_dict).intersection(__file_dict_required_keys)) != len(__file_dict_required_keys):
            message = _invalid_key_exception_message(required_keys=__file_dict_required_keys)
            raise KeyError(message)

        sas7bdat = file_dict['sas7bdat_file']
        export = file_dict['export_file']
        to_excel(sas7bdat_file=sas7bdat, export_file=export)


def batch_to_json(file_dicts: List[Dict[str, str]]) -> None:
    """
    Converts a batch of sas7bdat files to json files.

    Args:
        file_dicts: A list dictionaries containing the files to convert. The dictionary should
                    contain the keys 'sas7bdat_file' (containing the path and name to the sas7bdat file)
                    and 'export_file' containing the path and name of the export json). 
                    Example: file_dict = [{'sas7bdat_file': 'sas_file1.sas7bdat', 'export_file': 'converted_file1.json'},
                                          {'sas7bdat_file': 'sas_file2.sas7bdat', 'export_file': 'converted_file2.json'}]
    """
    for file_dict in file_dicts:
        if len(set(file_dict).intersection(__file_dict_required_keys)) != len(__file_dict_required_keys):
            message = _invalid_key_exception_message(required_keys=__file_dict_required_keys)
            raise KeyError(message)

        sas7bdat = file_dict['sas7bdat_file']
        export = file_dict['export_file']
        to_json(sas7bdat_file=sas7bdat, export_file=export)


def batch_to_xml(file_dicts: List[Dict[str, str]]) -> None:
    """
    Converts a batch of sas7bdat files to xml files.

    Args:
        file_dicts: A list dictionaries containing the files to convert. The dictionary should
                    contain the keys 'sas7bdat_file' (containing the path and name to the sas7bdat file)
                    and 'export_file' containing the path and name of the export xml). Optinallly 
                    the dictionary can also contain 'root_node' (containing the name for the root
                    node in the xml file, and 'first_node' (containing the name for the first node
                    in the xml file).
                    Examples: file_dict = [{'sas7bdat_file': 'sas_file1.sas7bdat', 
                                            'export_file': 'converted_file1.xlsx'},
                                           {'sas7bdat_file': 'sas_file2.sas7bdat', 
                                            'export_file': 'converted_file2.xlxs'}]

                              file_dict = [{'sas7bdat_file': 'sas_file1.sas7bdat', 
                                            'export_file': 'converted_file1.xml',
                                            'root_node': 'my_root',
                                            'first_node': 'my_first'},
                                           {'sas7bdat_file': 'sas_file2.sas7bdat',
                                            'export_file': 'converted_file2.xml',
                                            'root_node': 'another_root',
                                            'first_node': 'another_first'}]
    """
    optional_keys = ['root_node', 'first_node',]
    for file_dict in file_dicts:
        error = False
        if (len(set(file_dict).intersection(__file_dict_required_keys)) != len(__file_dict_required_keys) or
                len(set(file_dict).intersection(__file_dict_required_keys)) > len(__file_dict_required_keys) + len(optional_keys)):
            error = True
        elif len(set(file_dict).intersection(optional_keys)) != len(file_dict) - len(__file_dict_required_keys):
            error = True

        if error:
            message = _invalid_key_exception_message(required_keys=__file_dict_required_keys, optional_keys=optional_keys)
            raise KeyError(message)

        sas7bdat = file_dict['sas7bdat_file']
        export = file_dict['export_file']
        root_node = None
        first_node = None
        if 'root_node' in file_dict:
            root_node = file_dict['root_node']
        if 'first_node' in file_dict:
            first_node = file_dict['first_node']

        if root_node and first_node:
            to_xml(sas7bdat_file=sas7bdat, export_file=export, root_node=root_node, first_node=first_node)
        elif root_node:
            to_xml(sas7bdat_file=sas7bdat, export_file=export, root_node=root_node)
        elif first_node:
            to_xml(sas7bdat_file=sas7bdat, export_file=export, first_node=first_node)
        else:
            to_xml(sas7bdat_file=sas7bdat, export_file=export)


def dir_to_csv(dir_path: str, export_path: Optional[str]=None) -> None:
    """
    Converts all sas7bdat files in a directory into csv files.

    args:
        dir_path: The pah to the directory that contains the sas7bdat files
                for conversion.
        export_path (optional): If used this can specify a new directory to create
                the converted files into. If not supplied then the files will be
                created into the same directory as dir_path.
    """
    for file_name in Path(dir_path).iterdir():
        if file_name.suffix == '.sas7bdat':
            export_file = Path(f'{file_name.stem}.csv')
            if export_path:
                export_file = Path(export_path).joinpath(export_file)
            else:
                export_file = Path(dir_path).joinpath(export_file)
            
            sas7bdat_file = Path(dir_path).joinpath(file_name)
            to_csv(str(sas7bdat_file), str(export_file))


def dir_to_excel(dir_path: str, export_path: Optional[str]=None) -> None:
    """
    Converts all sas7bdat files in a directory into xlsx files.

    args:
        dir_path: The path to the directory that contains the sas7bdat files
                for conversion.
        export_path (optional): If used this can specify a new directory to create
                the converted files into. If not supplied then the files will be
                created into the same directory as dir_path.
    """
    for file_name in Path(dir_path).iterdir():
        if file_name.suffix == '.sas7bdat':
            export_file = Path(f'{file_name.stem}.xlsx')
            if export_path:
                export_file = Path(export_path).joinpath(export_file)
            else:
                export_file = Path(dir_path).joinpath(export_file)
            
            sas7bdat_file = Path(dir_path).joinpath(file_name)
            to_excel(str(sas7bdat_file), str(export_file))


def dir_to_json(dir_path: str, export_path: Optional[str]=None) -> None:
    """
    Converts all sas7bdat files in a directory into json files.

    args:
        dir_path: The path to the directory that contains the sas7bdat files
                for conversion.
        export_path (optional): If used this can specify a new directory to create
                the converted files into. If not supplied then the files will be
                created into the same directory as dir_path.
    """
    for file_name in Path(dir_path).iterdir():
        if file_name.suffix == '.sas7bdat':
            export_file = Path(f'{file_name.stem}.json')
            if export_path:
                export_file = Path(export_path).joinpath(export_file)
            else:
                export_file = Path(dir_path).joinpath(export_file)
            
            sas7bdat_file = Path(dir_path).joinpath(file_name)
            to_json(str(sas7bdat_file), str(export_file))


def dir_to_xml(dir_path: str, export_path: Optional[str]=None) -> None:
    """
    Converts all sas7bdat files in a directory into xml files.

    args:
        dir_path: The path to the directory that contains the sas7bdat files
                for conversion.
        export_path (optional): If used this can specify a new directory to create
                the converted files into. If not supplied then the files will be
                created into the same directory as dir_path.
    """
    for file_name in Path(dir_path).iterdir():
        if file_name.suffix == '.sas7bdat':
            export_file = Path(f'{file_name.stem}.xml')
            if export_path:
                export_file = Path(export_path).joinpath(export_file)
            else:
                export_file = Path(dir_path).joinpath(export_file)
            
            sas7bdat_file = Path(dir_path).joinpath(file_name)
            to_xml(str(sas7bdat_file), str(export_file))


def _file_extension_exception_message(conversion_type: str, valid_extensions: Tuple[str]) -> str:
    if len(valid_extensions) == 1:
        is_are = ('extension', 'is')
    else:
        is_are = ('extensions', 'are')

    extensions = ', '.join(valid_extensions)
    return f'sas7bdat conversion error - Valid {is_are[0]} for {conversion_type} conversion {is_are[1]}: {extensions}'


def _invalid_key_exception_message(required_keys: List[str], optional_keys: Optional[List[str]]=None) -> str:
    required_keys_joined: str = ', '.join(required_keys)
    if optional_keys:
        optional_keys_joined: str = ', '.join(optional_keys)
        message = f'Invalid key provided, expected keys are: {required_keys_joined} and optional keys are: {optional_keys_joined}'
    else:
        message = f'Invalid key provided, expected keys are: {required_keys_joined}'

    return message


def _is_valid_extension(valid_extensions: Tuple[str], file_extension: str) -> bool:
    return file_extension in valid_extensions


def to_csv(sas7bdat_file: str, export_file: str) -> None:
    """
    Converts a sas7bdat file into a csv file.

    args:
        sas7bdat_file: The name, including the path, for the sas7bdat file.
        export_file: The name, including the path, for the export file.
    """
    valid_extensions = ('.csv',)
    file_extension = Path(export_file).suffix

    if not _is_valid_extension(valid_extensions, file_extension):
        error_message = _file_extension_exception_message('to_csv', valid_extensions)
        raise AttributeError(error_message)

    df = to_dataframe(sas7bdat_file)
    df.to_csv(export_file, quoting=csv.QUOTE_NONNUMERIC, index=False)


def to_dataframe(sas7bdat_file: str) -> pd.DataFrame:
    """
    Converts a sas7bdat file into a pandas dataframe.

    args:
        sas7bdat_file: The name, including the path, for the sas7bdat file.

    return:
        A pandas dataframe containing the data from the sas7bdat file.
    """
    df = pd.read_sas(sas7bdat_file)

    # convert binary strings to utf-8
    str_df = df.select_dtypes([np.object])
    if len(str_df.columns) > 0:
        str_df = str_df.stack().str.decode('utf-8').unstack()

        for col in str_df:
            df[col] = str_df[col]
    # end conversion to utf-8

    return df


def to_excel(sas7bdat_file: str, export_file: str) -> None:
   """
   Converts a sas7bdat file into a xlsx file.

   args:
       sas7bdat_file: The name, including the path, for the sas7bdat file.
       export_file: The name, including the path, for the export file.
   """
   valid_extensions = ('.xlsx',)
   file_extension = Path(export_file).suffix

   if not _is_valid_extension(valid_extensions, file_extension):
       error_message = _file_extension_exception_message('to_excel', valid_extensions)
       raise AttributeError(error_message)

   df = to_dataframe(sas7bdat_file)
   df.to_excel(export_file, index=False)


def to_json(sas7bdat_file: str, export_file: str) -> None:
    """
    Converts a sas7bdat file into a json file.

    args:
        sas7bdat_file: The name, including the path, for the sas7bdat file.
        export_file: The name, including the path, for the export file.
    """
    valid_extensions = ('.json',)
    file_extension = Path(export_file).suffix

    if not _is_valid_extension(valid_extensions, file_extension):
        error_message = _file_extension_exception_message('to_json', valid_extensions)
        raise AttributeError(error_message)

    df = to_dataframe(sas7bdat_file)
    df.to_json(export_file)

def to_xml(sas7bdat_file: str, export_file: str, root_node: str='root', first_node: str='item') -> None:
    """
    Converts a sas7bdat file into a xml file.

    args:
        sas7bdat_file: The name, including the path, for the sas7bdat file.
        export_file: The name, including the path, for the export file.
        root_node: The name to use for the root node in the xml file.
        first_node: The name to use for the fist node in the xml file.
    """
    valid_extensions = ('.xml',)
    file_extension = Path(export_file).suffix
    
    if not _is_valid_extension(valid_extensions, file_extension):
        error_message = _file_extension_exception_message('to_xml', valid_extensions)
        raise AttributeError(error_message)

    df = to_dataframe(sas7bdat_file) 


    def row_to_xml(row):
        xml = [f'  <{first_node}>']
        for i, col_name in enumerate(row.index):
            text = row.iloc[i]
            if isinstance(text, str):
                text = escape(text)

            xml.append(f'    <{col_name}>{text}</{col_name}>')
        xml.append('  </{first_node}>')
        return '\n'.join(xml)
    res = f'<?xml version="1.0" encoding="UTF-8"?>\n<{root_node}>\n'
    res = res + f'\n'.join(df.apply(row_to_xml, axis=1)) + '\n</{root_node}>'

    with open(export_file, 'w') as f:
        f.write(res)
