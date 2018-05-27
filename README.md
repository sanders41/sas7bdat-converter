# sas7bdat_converter: Convert sas7bdat files into other formats
Converts proprietary sas7bdat files from SAS into formats such as csv and XML useable by other programs. Currently supported conversiaions are csv, Excel (xlsx format), json, Pandas DataFrame, and XML.

Conversions can be done on either a single file or a batch of files.

## Usage
* **batch_to_csv(file_dicts)** - Convert multiple sas7bdat files into csv files at once.
  * file_dicts = A list containing a dictionary for each file to convert. The dictionary is required to contain 'sas7bdat_file' containing the path and name for the sas7bdat file, and 'export_file' containing the path and name for the csv files. The csv file extension should be .csv.

  #### Example
  ```
  from sas7bdat_converter.converter import SASConverter

  file_dicts = [{'sas7bdat_file': '/path/to/sas7bdat/files/example_1.sas7bdat', 'export_file': '/path/to/new/files/example_1.csv'
                {'sas7bdat_file': '/path/to/sas7bdat/files/example_2.sas7bdat', 'export_file': '/path/to/new/files/example_2.csv']
  sas_converter = SASConverter()
  sas_converter.batch_to_csv(file_dicts)
  ```
  
  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like `c:\path\to\sas7bdat\files\example_1.sas7bdat`.

* **batch_to_excel(file_dicts)** - Convert multiple sas7bdat files into Excel files at once.
  * file_dicts = A list containing a dictionary for each file to convert. The dictionary is required to contain 'sas7bdat_file' containing the path and name for the sas7bdat file, and 'export_file' containing the path and name for the excel files. The Excel file extension should be .xlsx.

  #### Example
  ```
  from sas7bdat_converter.converter import SASConverter

  file_dicts = [{'sas7bdat_file': '/path/to/sas7bdat/files/example_1.sas7bdat', 'export_file': '/path/to/new/files/example_1.xlsx'
                {'sas7bdat_file': '/path/to/sas7bdat/files/example_2.sas7bdat', 'export_file': '/path/to/new/files/example_2.xlsx']
  sas_converter = SASConverter()
  sas_converter.batch_to_excel(file_dicts)
  ```
  
  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like `c:\path\to\sas7bdat\files\example_1.sas7bdat`.

* **batch_to_json(file_dicts)** - Convert multiple sas7bdat files into json files at once.
  * file_dicts = A list containing a dictionary for each file to convert. The dictionary is required to contain 'sas7bdat_file' containing the path and name for the sas7bdat file, and 'export_file' containing the path and name for the json files. The json file extension should be .json.

  #### Example
  ```
  from sas7bdat_converter.converter import SASConverter

  file_dicts = [{'sas7bdat_file': '/path/to/sas7bdat/files/example_1.sas7bdat', 'export_file': '/path/to/new/files/example_1.json'
                {'sas7bdat_file': '/path/to/sas7bdat/files/example_2.sas7bdat', 'export_file': '/path/to/new/files/example_2.json']
  sas_converter = SASConverter()
  sas_converter.batch_to_json(file_dicts)
  ```
  
  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like `c:\path\to\sas7bdat\files\example_1.sas7bdat`.

* **batch_to_xml(file_dicts)** - Convert multiple sas7bdat files into XML files at once.
  * file_dicts = A list containing a dictionary for each file to convert. The dictionary is required to contain 'sas7bdat_file' containing the path and name for the sas7bdat file, and 'export_file' containing the path and name for the xml files. The XML file extension should be .xml.

  #### Example
  ```
  from sas7bdat_converter.converter import SASConverter

  file_dicts = [{'sas7bdat_file': '/path/to/sas7bdat/files/example_1.sas7bdat', 'export_file': '/path/to/new/files/example_1.xml'
                {'sas7bdat_file': '/path/to/sas7bdat/files/example_2.sas7bdat', 'export_file': '/path/to/new/files/example_2.xml']
  sas_converter = SASConverter()
  sas_converter.batch_to_xml(file_dicts)
  ```
  
  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like `c:\path\to\sas7bdat\files\example_1.sas7bdat`.

* **to_csv(sas7bdat_file, export_file)** - convert a sas7bdat file into a csv file.
  * sas7bdat_file = the path and name for sas7bdat file to convert.
  * export_file = the path and name for the csv file. The csv file extension should be .csv.

  #### Example
  ```
  from sas7bdat_converter.converter import sasconverter

  sas_converter = sasconverter()
  sas_converter.to_csv('/path/to/sas7bdat/file/example.sas7bdat', 'path/to/new/file/example.csv')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like `c:\path\to\sas7bdat\files\example.sas7bdat`.

* **to_dataframe(sas7bdat_file)** - Convert a sas7bdat file into a Pandas DataFrame.
  * sas7bdat_file = The path and name for sas7bdat file to convert.

  #### Example
  ```
  from sas7bdat_converter.converter import SASConverter

  sas_converter = SASConverter()
  sas_converter.to_dataframe('/path/to/sas7bdat/file/example.sas7bdat')
  ```
  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like `c:\path\to\sas7bdat\files\example_1.sas7bdat`.
  
* **to_excel(sas7bdat_file, export_file)** - convert a sas7bdat file into a Excel file.
  * sas7bdat_file = the path and name for sas7bdat file to convert.
  * export_file = the path and name for the Excel file. The Excel file extension should be .xlsx.

  #### Example
  ```
  from sas7bdat_converter.converter import sasconverter

  sas_converter = sasconverter()
  sas_converter.to_excel('/path/to/sas7bdat/file/example.sas7bdat', 'path/to/new/file/example.xlsx')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like `c:\path\to\sas7bdat\files\example.sas7bdat`.

* **to_json(sas7bdat_file, export_file)** - convert a sas7bdat file into a json file.
  * sas7bdat_file = the path and name for sas7bdat file to convert.
  * export_file = the path and name for the json file. the json file extension should be .json.

  #### Example
  ```
  from sas7bdat_converter.converter import sasconverter

  sas_converter = sasconverter()
  sas_converter.to_json('/path/to/sas7bdat/file/example.sas7bdat', 'path/to/new/file/example.json')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like `c:\path\to\sas7bdat\files\example.sas7bdat`.

* **to_xml(sas7bdat_file, export_file, root_node='root', first_node='item')** - convert a sas7bdat file into a XML file.
  * sas7bdat_file = the path and name for sas7bdat file to convert.
  * export_file = the path and name for the XML file. The XML file extension should be .xlm.
  * root_node = The name to uses for the top level node. If no name is supplied "root" will be used.
  * first_node = The name to use for the first node under root. If no name is supplied "item" will be used.

  #### Example
  ```
  from sas7bdat_converter.converter import sasconverter

  sas_converter = sasconverter()
  sas_converter.to_json('/path/to/sas7bdat/file/example.sas7bdat', 'path/to/new/file/example.xml')
  ```

  **Note:** Example uses Mac/Linux type file paths. For Windows use paths like `c:\path\to\sas7bdat\files\example.sas7bdat`.
