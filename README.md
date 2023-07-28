# sas7bdat-converter: Convert sas7bdat files into other formats

[![Tests Status](https://github.com/sanders41/sas7bdat-converter/workflows/Tests/badge.svg?branch=main&event=push)](https://github.com/sanders41/sas7bdat-converter/actions?query=workflow%3ATests+branch%3Amain+event%3Apush)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sanders41/sas7bdat-converter/main.svg)](https://results.pre-commit.ci/latest/github/sanders41/sas7bdat-converter/main)
[![Coverage](https://codecov.io/github/sanders41/sas7bdat-converter/coverage.svg?branch=main)](https://codecov.io/gh/sanders41/sas7bdat-converter)
[![PyPI version](https://badge.fury.io/py/sas7bdat-converter.svg)](https://badge.fury.io/py/sas7bdat-converter)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sas7bdat-converter?color=5cc141)](https://github.com/sanders41/sas7bdat-converter)

Converts proprietary sas7bdat and/or xport files from SAS into formats such as csv, json, and Excel useable
by other programs. Currently supported conversiaions are csv, Excel (xlsx format), json, Pandas
DataFrame, Parquet and XML.

Conversions can be done on either a single file, an entire directory, or a batch of specified files.

## Install

`pip install sas7bdat-converter`

If you would like to be able to convert to Excel files you will need to install with the extra Excel dependency.

`pip install sas7bdat-converter[excel]`

If you would like to be able to convert to Parquet files you will need to install with the extra parquet dependency.

`pip install sas7bdat-converter[parquet]`

If you would like to use Conda, it includes both the extras required to convert to Excel & Parquet files.

`conda install -c conda-forge sas7bdat-converter`

## Usage

In all cases either sas7bdat or xport files can be converted. Examples below all use the .sas7bdat
extension, xport files with a .xpt extension will also work.

* **batch_to_csv(file_dicts)** - Convert multiple sas7bdat files into csv files at once.
  * file_dicts = A list containing a dictionary for each file to convert. The dictionary is required
  to contain 'sas7bdat_file' containing the path and name for the sas7bdat file, and 'export_file'
  containing the path and name for the csv files. The csv file extension should be .csv. File paths
  can be sent as either strings or Path objects.
  * continue_on_error = If set to true processing of files in a batch will continue if there is a
  file conversion error instead of raising an exception. Default = False

  **Example**

  ```py
  import sas7bdat_converter

  file_dicts = [
    {
      'sas7bdat_file': '/path/to/sas7bdat/files/example_1.sas7bdat',
      'export_file': '/path/to/new/files/example_1.csv',
    },
    {
      'sas7bdat_file': '/path/to/sas7bdat/files/example_2.sas7bdat',
      'export_file': '/path/to/new/files/example_2.csv',
    },
  ]
  sas7bdat_converter.batch_to_csv(file_dicts)
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files\example_1.sas7bdat`.

* **batch_to_excel(file_dicts)** - Convert multiple sas7bdat files into Excel files at once.
  * file_dicts = A list containing a dictionary for each file to convert. The dictionary is required
  to contain 'sas7bdat_file' containing the path and name for the sas7bdat file, and 'export_file'
  containing the path and name for the excel files. The Excel file extension should be .xlsx. File
  paths can be sent as either strings or Path objects.
  * continue_on_error = If set to true processing of files in a batch will continue if there is a
  file conversion error instead of raising an exception. Default = False

  **Example**

  ```py
  import sas7bdat_converter

  file_dicts = [
    {
      'sas7bdat_file': '/path/to/sas7bdat/files/example_1.sas7bdat',
      'export_file': '/path/to/new/files/example_1.xlsx',
    },
    {
      'sas7bdat_file': '/path/to/sas7bdat/files/example_2.sas7bdat',
      'export_file': '/path/to/new/files/example_2.xlsx',
    },
  ]
  sas7bdat_converter.batch_to_excel(file_dicts)
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files\example_1.sas7bdat`.

* **batch_to_parquet(file_dicts)** - Convert multiple sas7bdat files into Parquet files at once.
  * file_dicts = A list containing a dictionary for each file to convert. The dictionary is required
  to contain 'sas7bdat_file' containing the path and name for the sas7bdat file, and 'export_file'
  containing the path and name for the perquet files. The Perquet file extension should be .perquet. File
  paths can be sent as either strings or Path objects.
  * continue_on_error = If set to true processing of files in a batch will continue if there is a
  file conversion error instead of raising an exception. Default = False

  **Example**

  ```py
  import sas7bdat_converter

  file_dicts = [
    {
      'sas7bdat_file': '/path/to/sas7bdat/files/example_1.sas7bdat',
      'export_file': '/path/to/new/files/example_1.parquet',
    },
    {
      'sas7bdat_file': '/path/to/sas7bdat/files/example_2.sas7bdat',
      'export_file': '/path/to/new/files/example_2.parquet',
    },
  ]
  sas7bdat_converter.batch_to_parquet(file_dicts)
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files\example_1.sas7bdat`.

* **batch_to_json(file_dicts)** - Convert multiple sas7bdat files into json files at once.
  * file_dicts = A list containing a dictionary for each file to convert. The dictionary is required
  to contain 'sas7bdat_file' containing the path and name for the sas7bdat file, and 'export_file'
  containing the path and name for the json files. The json file extension should be .json. File
  paths can be sent as either strings or Path objects.
  * continue_on_error = If set to true processing of files in a batch will continue if there is a
  file conversion error instead of raising an exception. Default = False

  **Example**

  ```py
  import sas7bdat_converter

  file_dicts = [
    {
      'sas7bdat_file': '/path/to/sas7bdat/files/example_1.sas7bdat',
      'export_file': '/path/to/new/files/example_1.json',
    },
    {
      'sas7bdat_file': '/path/to/sas7bdat/files/example_2.sas7bdat',
      'export_file': '/path/to/new/files/example_2.json',
    },
  ]
  sas7bdat_converter.batch_to_json(file_dicts)
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files\example_1.sas7bdat`.

* **batch_to_xml(file_dicts)** - Convert multiple sas7bdat files into XML files at once.
  * file_dicts = A list containing a dictionary for each file to convert. The dictionary is required
  to contain 'sas7bdat_file' containing the path and name for the sas7bdat file, and 'export_file'
  containing the path and name for the xml files. The XML file extension should be .xml. File paths
  can be sent as either strings or Path objects.
  * continue_on_error = If set to true processing of files in a batch will continue if there is a
  file conversion error instead of raising an exception. Default = False

  **Example**

  ```py
  import sas7bdat_converter

  file_dicts = [
    {
      'sas7bdat_file': '/path/to/sas7bdat/files/example_1.sas7bdat',
      'export_file': '/path/to/new/files/example_1.xml',
    },
    {
      'sas7bdat_file': '/path/to/sas7bdat/files/example_2.sas7bdat',
      'export_file': '/path/to/new/files/example_2.xml',
    },
  ]
  sas7bdat_converter.batch_to_xml(file_dicts)
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files\example_1.sas7bdat`.

* **dir_to_csv(dir_path, export_path=None)** - Convert all sas7bdat files in a directory into csv
files at once. File paths can be sent as either strings or Path objects.
  * dir_path = The dictionary that contains the sas7bdat file to convert.
  * export_path = Optional path for the converted files. If no path is supplied the new files will
  be put into the dir_path directory with the sas7bdat files. File paths can be sent as either
  strings or Path objects. Default = None
  * continue_on_error = If set to true processing of files in a batch will continue if there is a
  file conversion error instead of raising an exception. Default = False

  **Example**

  ```py
  import sas7bdat_converter

  # Option 1: put the converted files in the same directory as the sas7bdat files
  sas7bdat_converter.dir_to_csv('/path/to/sas7bdat/files')

  # Option 2: put the converted fiels in a diffferent directory
  sas7bdat_converter.dir_to_csv('/path/to/sas7bdat/files', 'path/for/new/files')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files`.

* **dir_to_excel(dir_path, export_path=None)** - Convert all sas7bdat files in a directory into
Excel files at once. File paths can be sent as either strings or Path objects.
  * dir_path = The dictionary that contains the sas7bdat file to convert.
  * export_path = Optional path for the converted files. If no path is supplied the new files will
  be put into the dir_path directory with the sas7bdat files Default = None
  * continue_on_error = If set to true processing of files in a batch will continue if there is a
  file conversion error instead of raising an exception. Default = False

  **Example**

  ```py
  import sas7bdat_converter

  # Option 1: put the converted files in the same directory as the sas7bdat files
  sas7bdat_converter.dir_to_excel('/path/to/sas7bdat/files')

  # Option 2: put the converted fiels in a diffferent directory
  sas7bdat_converter.dir_to_excel('/path/to/sas7bdat/files', 'path/for/new/files')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files`.

* **dir_to_json(dir_path, export_path=None)** - Convert all sas7bdat files in a directory into json
  files at once. File paths can be sent as either strings or Path objects.
  * dir_path = The dictionary that contains the sas7bdat file to convert.
  * export_path = Optional path for the converted files. If no path is supplied the new files will
  be put into the dir_path directory with the sas7bdat files. Default = None
  * continue_on_error = If set to true processing of files in a batch will continue if there is a
  file conversion error instead of raising an exception. Default = False

  **Example**

  ```py
  import sas7bdat_converter

  # Option 1: put the converted files in the same directory as the sas7bdat files
  sas7bdat_converter.dir_to_json('/path/to/sas7bdat/files')

  # Option 2: put the converted fiels in a diffferent directory
  sas7bdat_converter.dir_to_json('/path/to/sas7bdat/files', 'path/for/new/files')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files`.

* **dir_to_xml(dir_path, export_path=None)** - Convert all sas7bdat files in a directory into XML
  files at once. File paths can be sent as either strings or Path objects.
  * dir_path = The dictionary that contains the sas7bdat file to convert.
  * export_path = Optional path for the converted files. If no path is supplied the new files will
  be put into the dir_path directory with the sas7bdat files. Default = None
  * continue_on_error = If set to true processing of files in a batch will continue if there is a
  file conversion error instead of raising an exception. Default = False

  **Example**

  ```py
  import sas7bdat_converter

  # Option 1: put the converted files in the same directory as the sas7bdat files
  sas7bdat_converter.dir_to_xml('/path/to/sas7bdat/files')

  # Option 2: put the converted fiels in a diffferent directory
  sas7bdat_converter.dir_to_xml('/path/to/sas7bdat/files', 'path/for/new/files')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files`.

* **to_csv(sas7bdat_file, export_file)** - convert a sas7bdat file into a csv file. File path can be
  sent as either a string or Path objects.
  * sas7bdat_file = the path and name for sas7bdat file to convert.
  * export_file = the path and name for the csv file. The csv file extension should be .csv.

  **Example**

  ```py
  import sas7bdat_converter

  sas7bdat_converter.to_csv('/path/to/sas7bdat/file/example.sas7bdat', 'path/to/new/file/example.csv')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files\example.sas7bdat`.

* **to_dataframe(sas7bdat_file)** - Convert a sas7bdat file into a Pandas DataFrame. File path can
  be sent as either a string or Path objects.
  * sas7bdat_file = The path and name for sas7bdat file to convert.

  **Example**

  ```py
  import sas7bdat_converter

  sas7bdat_converter.to_dataframe('/path/to/sas7bdat/file/example.sas7bdat')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files\example_1.sas7bdat`.

* **to_excel(sas7bdat_file, export_file)** - convert a sas7bdat file into a Excel file. File path
  can be sent as either a string or Path objects.
  * sas7bdat_file = the path and name for sas7bdat file to convert.
  * export_file = the path and name for the Excel file. The Excel file extension should be .xlsx.

  **Example**

  ```py
  import sas7bdat_converter

  sas7bdat_converter.to_excel('/path/to/sas7bdat/file/example.sas7bdat',
  'path/to/new/file/example.xlsx')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files\example.sas7bdat`.

* **to_parquet(sas7bdat_file, export_file)** - convert a sas7bdat file into a Parquet file. File path
  can be sent as either a string or Path objects.
  * sas7bdat_file = the path and name for sas7bdat file to convert.
  * export_file = the path and name for the Parquet file. The Parquet file extension should be .parquet.

  **Example**

  ```py
  import sas7bdat_converter

  sas7bdat_converter.to_parquet('/path/to/sas7bdat/file/example.sas7bdat',
  'path/to/new/file/example.parquet')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files\example.sas7bdat`.

* **to_json(sas7bdat_file, export_file)** - convert a sas7bdat file into a json file. File path can
  be sent as either a string or Path objects.
  * sas7bdat_file = the path and name for sas7bdat file to convert.
  * export_file = the path and name for the json file. the json file extension should be .json.

  **Example**

  ```py
  import sas7bdat_converter

  sas7bdat_converter.to_json('/path/to/sas7bdat/file/example.sas7bdat', 'path/to/new/file/example.json')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files\example.sas7bdat`.

* **to_xml(sas7bdat_file, export_file, root_node='root', first_node='item')** - convert a sas7bdat
  file into a XML file. File path can be sent as either a string or Path objects.
  * sas7bdat_file = the path and name for sas7bdat file to convert.
  * export_file = the path and name for the XML file. The XML file extension should be .xlm.
  * root_node = The name to uses for the top level node. If no name is supplied "root" will be used.
  * first_node = The name to use for the first node under root. If no name is supplied "item" will be used.

  **Example**

  ```py
  import sas7bdat_converter

  sas7bdat_converter.to_xml('/path/to/sas7bdat/file/example.sas7bdat', 'path/to/new/file/example.xml')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like
  `c:\path\to\sas7bdat\files\example.sas7bdat`.

## Contributing

If you are interested in contributing to this project please see our [contributing guide](CONTRIBUTING.md)
