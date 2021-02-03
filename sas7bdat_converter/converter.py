import csv
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from xml.sax.saxutils import escape

import numpy as np
import pandas as pd

logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s")
logging.root.setLevel(level=logging.INFO)
logger = logging.getLogger(__name__)

__file_dict_required_keys = [
    "sas7bdat_file",
    "export_file",
]


def batch_to_csv(
    file_dicts: List[Dict[str, Union[str, Path]]],
    continue_on_error: bool = False,
) -> None:
    """
    Converts a batch of sas7bdat and/or xpt files to csv files.

    Args:
        file_dicts: A list dictionaries containing the files to convert. The dictionary should
                    contain the keys 'sas7bdat_file' (containing the path and name to the sas7bdat
                    file) and 'export_file' containing the path and name of the export csv).
                    Example: file_dict = [{
                                              'sas7bdat_file': 'sas_file1.sas7bdat',
                                              'export_file': 'converted_file1.csv',
                                          },
                                          {
                                              'sas7bdat_file': 'sas_file2.sas7bdat',
                                              'export_file': 'converted_file2.csv',
                                          }]
        continue_on_error: If set to true processing of files in a batch will continue if there is
                    a file conversion error instead of raising an exception. Default = False
    """
    for file_dict in file_dicts:
        _rise_on_invalid_file_dict(file_dict)

        xpt = _format_path(file_dict["sas7bdat_file"])
        export = _format_path(file_dict["export_file"])
        try:
            to_csv(sas7bdat_file=xpt, export_file=export)
        except:  # noqa: E722
            if continue_on_error:
                logger.info(f"Error converting {xpt}")
            else:
                raise


def batch_to_excel(
    file_dicts: List[Dict[str, Union[str, Path]]],
    continue_on_error: bool = False,
) -> None:
    """
    Converts a batch of sas7bdat and/or xpt files to xlsx files.

    Args:
        file_dicts: A list of dictionaries containing the files to convert. The dictionary should
                    contain the keys 'sas7bdat_file' (containing the path and name to the sas7bdat
                    file) and 'export_file' containing the path and name of the export xlsx).
                    Example: file_dict = [{
                                              'sas7bdat_file': 'sas_file1.sas7bdat',
                                              'export_file': 'converted_file1.xlsx',
                                          },
                                          {
                                              'sas7bdat_file': 'sas_file2.sas7bdat',
                                              'export_file': 'converted_file2.xlxs',
                                          }]
        continue_on_error: If set to true processing of files in a batch will continue if there is
                    a file conversion error instead of raising an exception. Default = False
    """
    for file_dict in file_dicts:
        _rise_on_invalid_file_dict(file_dict)

        sas7bdat = _format_path(file_dict["sas7bdat_file"])
        export = _format_path(file_dict["export_file"])
        try:
            to_excel(sas7bdat_file=sas7bdat, export_file=export)
        except:  # noqa: 722
            if continue_on_error:
                logger.info(f"Error converting {sas7bdat}")
            else:
                raise


def batch_to_json(
    file_dicts: List[Dict[str, Union[str, Path]]],
    continue_on_error: bool = False,
) -> None:
    """
    Converts a batch of sas7bdat and/or xpt files to json files.

    Args:
        file_dicts: A list dictionaries containing the files to convert. The dictionary should
                    contain the keys 'sas7bdat_file' (containing the path and name to the sas7bdat
                    file) and 'export_file' containing the path and name of the export json).
                    Example: file_dict = [{
                                              'sas7bdat_file': 'sas_file1.sas7bdat',
                                              'export_file': 'converted_file1.json',
                                          },
                                          {
                                              'sas7bdat_file': 'sas_file2.sas7bdat',
                                              'export_file': 'converted_file2.json',
                                          }]
        continue_on_error: If set to true processing of files in a batch will continue if there is
                    a file conversion error instead of raising an exception. Default = False
    """
    for file_dict in file_dicts:
        _rise_on_invalid_file_dict(file_dict)

        sas7bdat = _format_path(file_dict["sas7bdat_file"])
        export = _format_path(file_dict["export_file"])
        try:
            to_json(sas7bdat_file=sas7bdat, export_file=export)
        except:  # noqa: 722
            if continue_on_error:
                logger.info(f"Error converting {sas7bdat}")
            else:
                raise


def batch_to_xml(
    file_dicts: List[Dict[str, Union[str, Path]]],
    continue_on_error: bool = False,
) -> None:
    """
    Converts a batch of sas7bdat and/or xpt files to xml files.

    Args:
        file_dicts: A list dictionaries containing the files to convert. The dictionary should
                    contain the keys 'sas7bdat_file' (containing the path and name to the sas7bdat
                    file) and 'export_file' containing the path and name of the export xml).
                    Optinallly the dictionary can also contain 'root_node' (containing the name for
                    the root node in the xml file, and 'first_node' (containing the name for the
                    first node in the xml file).
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
        continue_on_error: If set to true processing of files in a batch will continue if there is
                    a file conversion error instead of raising an exception. Default = False
    """
    optional_keys = [
        "root_node",
        "first_node",
    ]
    for file_dict in file_dicts:
        error = False
        if len(set(file_dict).intersection(__file_dict_required_keys)) != len(
            __file_dict_required_keys
        ) or len(set(file_dict).intersection(__file_dict_required_keys)) > len(
            __file_dict_required_keys
        ) + len(
            optional_keys
        ):
            error = True
        elif len(set(file_dict).intersection(optional_keys)) != len(file_dict) - len(
            __file_dict_required_keys
        ):
            error = True

        if error:
            message = _invalid_key_exception_message(
                required_keys=__file_dict_required_keys, optional_keys=optional_keys
            )
            raise KeyError(message)

        sas7bdat = _format_path(file_dict["sas7bdat_file"])
        export = _format_path(file_dict["export_file"])
        root_node = None
        first_node = None
        if "root_node" in file_dict:
            root_node = file_dict["root_node"]
        if "first_node" in file_dict:
            first_node = file_dict["first_node"]

        try:
            if root_node and first_node:
                to_xml(
                    sas7bdat_file=sas7bdat,
                    export_file=export,
                    root_node=str(root_node),
                    first_node=str(first_node),
                )
            elif root_node:
                to_xml(sas7bdat_file=sas7bdat, export_file=export, root_node=str(root_node))
            elif first_node:
                to_xml(sas7bdat_file=sas7bdat, export_file=export, first_node=str(first_node))
            else:
                to_xml(sas7bdat_file=sas7bdat, export_file=export)
        except:  # noqa: 722
            if continue_on_error:
                logger.info(f"Error converting {sas7bdat}")
            else:
                raise


def dir_to_csv(
    dir_path: Union[str, Path],
    export_path: Optional[Union[str, Path]] = None,
    continue_on_error: bool = False,
) -> None:
    """
    Converts all sas7bdat and/or xpt files in a directory into csv files.

    args:
        dir_path: The path to the directory that contains the sas7bdat files
                for conversion.
        export_path (optional): If used this can specify a new directory to create
                the converted files into. If not supplied then the files will be
                created into the same directory as dir_path. Default = None
        continue_on_error: If set to true processing of files in a batch will continue if there is
                a file conversion error instead of raising an exception. Default = False
    """
    _walk_dir("csv", dir_path, continue_on_error, export_path)


def dir_to_excel(
    dir_path: Union[str, Path],
    export_path: Optional[Union[str, Path]] = None,
    continue_on_error: bool = False,
) -> None:
    """
    Converts all sas7bdat and/or xpt files in a directory into xlsx files.

    args:
        dir_path: The path to the directory that contains the sas7bdat files
                for conversion.
        export_path (optional): If used this can specify a new directory to create
                the converted files into. If not supplied then the files will be
                created into the same directory as dir_path. Default = None
        continue_on_error: If set to true processing of files in a batch will continue if there is
                a file conversion error instead of raising an exception. Default = False
    """
    _walk_dir("xlsx", dir_path, continue_on_error, export_path)


def dir_to_json(
    dir_path: Union[str, Path],
    export_path: Optional[Union[str, Path]] = None,
    continue_on_error: bool = False,
) -> None:
    """
    Converts all sas7bdat and/or xpt files in a directory into json files.

    args:
        dir_path: The path to the directory that contains the sas7bdat files
                for conversion.
        export_path (optional): If used this can specify a new directory to create
                the converted files into. If not supplied then the files will be
                created into the same directory as dir_path. Default = None
        continue_on_error: If set to true processing of files in a batch will continue if there is
                a file conversion error instead of raising an exception. Default = False
    """
    _walk_dir("json", dir_path, continue_on_error, export_path)


def dir_to_xml(
    dir_path: Union[str, Path],
    export_path: Optional[Union[str, Path]] = None,
    continue_on_error: bool = False,
) -> None:
    """
    Converts all sas7bdat and/or xpt files in a directory into xml files.

    args:
        dir_path: The path to the directory that contains the sas7bdat files
                for conversion.
        export_path (optional): If used this can specify a new directory to create
                the converted files into. If not supplied then the files will be
                created into the same directory as dir_path. Default = None
        continue_on_error: If set to true processing of files in a batch will continue if there is
                a file conversion error instead of raising an exception. Default = False
    """
    _walk_dir("xml", dir_path, continue_on_error, export_path)


def to_csv(sas7bdat_file: Union[str, Path], export_file: Union[str, Path]) -> None:
    """
    Converts a sas7bdat and/or xpt file into a csv file.

    args:
        sas7bdat_file: The name, including the path, for the sas7bdat file.
        export_file: The name, including the path, for the export file.
    """
    valid_extensions = (".csv",)
    file_extension = Path(export_file).suffix

    if not _is_valid_extension(valid_extensions, file_extension):
        error_message = _file_extension_exception_message("to_csv", valid_extensions)
        raise AttributeError(error_message)

    df = to_dataframe(sas7bdat_file)
    df.to_csv(export_file, quoting=csv.QUOTE_NONNUMERIC, index=False)


def to_dataframe(sas7bdat_file: Union[str, Path]) -> pd.DataFrame:
    """
    Converts a sas7bdat and/or xpt file into a pandas dataframe.

    args:
        sas7bdat_file: The name, including the path, for the sas7bdat file.

    return:
        A pandas dataframe containing the data from the sas7bdat file.
    """
    df = pd.read_sas(sas7bdat_file)

    # convert binary strings to utf-8
    str_df = df.select_dtypes([np.dtype(object)])
    if len(str_df.columns) > 0:
        str_df = str_df.stack().str.decode("utf-8").unstack()

        for col in str_df:
            df[col] = str_df[col]
    # end conversion to utf-8

    return df


def to_excel(sas7bdat_file: Union[str, Path], export_file: Union[str, Path]) -> None:
    """
    Converts a sas7bdat and/or xpt file into a xlsx file.

    args:
        sas7bdat_file: The name, including the path, for the sas7bdat file.
        export_file: The name, including the path, for the export file.
    """
    valid_extensions = (".xlsx",)
    file_extension = Path(export_file).suffix

    if not _is_valid_extension(valid_extensions, file_extension):
        error_message = _file_extension_exception_message("to_excel", valid_extensions)
        raise AttributeError(error_message)

    df = to_dataframe(sas7bdat_file)
    try:
        df.to_excel(export_file, index=False)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "The optional dependency openpyxl is required in order to convert to an Excel file"
        )


def to_json(sas7bdat_file: Union[str, Path], export_file: Union[str, Path]) -> None:
    """
    Converts a sas7bdat and/or xpt file into a json file.

    args:
        sas7bdat_file: The name, including the path, for the sas7bdat file.
        export_file: The name, including the path, for the export file.
    """
    valid_extensions = (".json",)
    file_extension = Path(export_file).suffix

    if not _is_valid_extension(valid_extensions, file_extension):
        error_message = _file_extension_exception_message("to_json", valid_extensions)
        raise AttributeError(error_message)

    df = to_dataframe(sas7bdat_file)
    df.to_json(export_file)


def to_xml(
    sas7bdat_file: Union[str, Path],
    export_file: Union[str, Path],
    root_node: str = "root",
    first_node: str = "item",
) -> None:
    """
    Converts a sas7bdat and/or xpt file into a xml file.

    args:
        sas7bdat_file: The name, including the path, for the sas7bdat file.
        export_file: The name, including the path, for the export file.
        root_node: The name to use for the root node in the xml file.
        first_node: The name to use for the fist node in the xml file.
    """
    valid_extensions = (".xml",)
    file_extension = Path(export_file).suffix

    if not _is_valid_extension(valid_extensions, file_extension):
        error_message = _file_extension_exception_message("to_xml", valid_extensions)
        raise AttributeError(error_message)

    df = to_dataframe(sas7bdat_file)

    def row_to_xml(row: pd.DataFrame) -> str:
        xml = [f"  <{first_node}>"]
        for i, col_name in enumerate(row.index):
            text = row.iloc[i]
            if isinstance(text, str):
                text = escape(text)

            xml.append(f"    <{col_name}>{text}</{col_name}>")
        xml.append(f"  </{first_node}>")
        return "\n".join(xml)

    res = f'<?xml version="1.0" encoding="UTF-8"?>\n<{root_node}>\n'
    res = res + "\n".join(df.apply(row_to_xml, axis=1)) + f"\n</{root_node}>"

    with open(export_file, "w") as f:
        f.write(res)


def _file_extension_exception_message(conversion_type: str, valid_extensions: Tuple[str]) -> str:
    if len(valid_extensions) == 1:
        is_are = ("extension", "is")
    else:
        is_are = ("extensions", "are")

    extensions = ", ".join(valid_extensions)
    return f"sas7bdat conversion error - Valid {is_are[0]} for {conversion_type} conversion {is_are[1]}: {extensions}"  # noqa: E501


def _invalid_key_exception_message(
    required_keys: List[str], optional_keys: Optional[List[str]] = None
) -> str:
    required_keys_joined: str = ", ".join(required_keys)
    if optional_keys:
        optional_keys_joined: str = ", ".join(optional_keys)
        message = f"Invalid key provided, expected keys are: {required_keys_joined} and optional keys are: {optional_keys_joined}"  # noqa: E501
    else:
        message = f"Invalid key provided, expected keys are: {required_keys_joined}"

    return message


def _is_valid_extension(valid_extensions: Tuple[str], file_extension: str) -> bool:
    return file_extension in valid_extensions


def _format_path(path: Union[str, Path]) -> str:
    return str(path) if isinstance(path, Path) else path


def _rise_on_invalid_file_dict(file_dict: Dict[str, Union[str, Path]]) -> None:
    if len(set(file_dict).intersection(__file_dict_required_keys)) != len(
        __file_dict_required_keys
    ):
        message = _invalid_key_exception_message(required_keys=__file_dict_required_keys)
        raise KeyError(message)


def _walk_dir(
    file_type: str,
    dir_path: Union[str, Path],
    continue_on_error: bool,
    export_path: Optional[Union[str, Path]] = None,
) -> None:
    path = dir_path if isinstance(dir_path, Path) else Path(dir_path)
    for file_name in path.iterdir():
        if file_name.suffix in [".sas7bdat", ".xpt"]:
            export_file = Path(f"{file_name.stem}.{file_type}")
            if export_path:
                export_file = Path(export_path).joinpath(export_file)
            else:
                export_file = path.joinpath(export_file)

            sas7bdat_file = path.joinpath(file_name)

            try:
                if file_type == "csv":
                    to_csv(str(sas7bdat_file), str(export_file))
                elif file_type == "json":
                    to_json(str(sas7bdat_file), str(export_file))
                elif file_type == "xlsx":
                    to_excel(str(sas7bdat_file), str(export_file))
                elif file_type == "xml":
                    to_xml(str(sas7bdat_file), str(export_file))
            except:  # noqa: 722
                if continue_on_error:
                    logger.info(f"Error converting {sas7bdat_file}")
                else:
                    raise
