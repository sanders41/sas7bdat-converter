import filecmp
import os
import pandas as pd
import shutil
import unittest
import xlrd
from sas7bdat_converter.converter import SASConverter

class ConverterTestCase(unittest.TestCase):
    def setUp(self):
        current_dir = os.path.dirname(__file__)

        if not os.path.isdir(os.path.join(current_dir, 'data/converted_files')):
            os.mkdir(os.path.join(current_dir, 'data/converted_files'))

        self.converted_dir = os.path.join(current_dir, 'data/converted_files')
        self.expected_dir = os.path.join(current_dir, 'data/expected_files')
        self.sas7bdat_dir = os.path.join(current_dir, 'data/sas7bdat_files/')

    def tearDown(self):
        shutil.rmtree(self.converted_dir)

    def test_batch_to_csv(self):
        sas_file1 = os.path.join(self.sas7bdat_dir, 'file1.sas7bdat')
        converted_file1 = os.path.join(self.converted_dir, 'file1.csv')
        sas_file2 = os.path.join(self.sas7bdat_dir, 'file2.sas7bdat')
        converted_file2 = os.path.join(self.converted_dir, 'file2.csv')
        sas_file3 = os.path.join(self.sas7bdat_dir, 'file3.sas7bdat')
        converted_file3 = os.path.join(self.converted_dir, 'file3.csv')

        file_dict = [{'sas7bdat_file': sas_file1, 'export_file': converted_file1}, {'sas7bdat_file': sas_file2, 'export_file': converted_file2}, {'sas7bdat_file': sas_file3, 'export_file': converted_file3}]

        sas_converter = SASConverter()
        sas_converter.batch_to_csv(file_dict)

        files_created = False

        if os.path.isfile(converted_file1) and os.path.isfile(converted_file2) and os.path.isfile(converted_file3):
            files_created = True

        self.assertTrue(files_created, msg='All expected csv files were not created')

    def test_batch_to_excel(self):
        sas_file1 = os.path.join(self.sas7bdat_dir, 'file1.sas7bdat')
        converted_file1 = os.path.join(self.converted_dir, 'file1.xlsx')
        sas_file2 = os.path.join(self.sas7bdat_dir, 'file2.sas7bdat')
        converted_file2 = os.path.join(self.converted_dir, 'file2.xlsx')
        sas_file3 = os.path.join(self.sas7bdat_dir, 'file3.sas7bdat')
        converted_file3 = os.path.join(self.converted_dir, 'file3.xlsx')

        file_dict = [{'sas7bdat_file': sas_file1, 'export_file': converted_file1}, {'sas7bdat_file': sas_file2, 'export_file': converted_file2}, {'sas7bdat_file': sas_file3, 'export_file': converted_file3}]

        sas_converter = SASConverter()
        sas_converter.batch_to_excel(file_dict)

        files_created = False

        if os.path.isfile(converted_file1) and os.path.isfile(converted_file2) and os.path.isfile(converted_file3):
            files_created = True

        self.assertTrue(files_created, msg='All expected Excel files were not created')

    def test_batch_to_json(self):
        sas_file1 = os.path.join(self.sas7bdat_dir, 'file1.sas7bdat')
        converted_file1 = os.path.join(self.converted_dir, 'file1.json')
        sas_file2 = os.path.join(self.sas7bdat_dir, 'file2.sas7bdat')
        converted_file2 = os.path.join(self.converted_dir, 'file2.json')
        sas_file3 = os.path.join(self.sas7bdat_dir, 'file3.sas7bdat')
        converted_file3 = os.path.join(self.converted_dir, 'file3.json')

        file_dict = [{'sas7bdat_file': sas_file1, 'export_file': converted_file1}, {'sas7bdat_file': sas_file2, 'export_file': converted_file2}, {'sas7bdat_file': sas_file3, 'export_file': converted_file3}]

        sas_converter = SASConverter()
        sas_converter.batch_to_json(file_dict)

        files_created = False

        if os.path.isfile(converted_file1) and os.path.isfile(converted_file2) and os.path.isfile(converted_file3):
            files_created = True

        self.assertTrue(files_created, msg='All expected json files were not created')

    def test_batch_to_xml(self):
        sas_file1 = os.path.join(self.sas7bdat_dir, 'file1.sas7bdat')
        converted_file1 = os.path.join(self.converted_dir, 'file1.xml')
        sas_file2 = os.path.join(self.sas7bdat_dir, 'file2.sas7bdat')
        converted_file2 = os.path.join(self.converted_dir, 'file2.xml')
        sas_file3 = os.path.join(self.sas7bdat_dir, 'file3.sas7bdat')
        converted_file3 = os.path.join(self.converted_dir, 'file3.xml')

        file_dict = [{'sas7bdat_file': sas_file1, 'export_file': converted_file1}, {'sas7bdat_file': sas_file2, 'export_file': converted_file2}, {'sas7bdat_file': sas_file3, 'export_file': converted_file3}]

        sas_converter = SASConverter()
        sas_converter.batch_to_xml(file_dict)

        files_created = False

        if os.path.isfile(converted_file1) and os.path.isfile(converted_file2) and os.path.isfile(converted_file3):
            files_created = True

        self.assertTrue(files_created, msg='All expected xml files were not created')

    def test_file_extension_exception_message_is(self):
        valid_message = 'sas7bdat conversion error - Valid extension for to_csv conversion is: .csv'
        valid_extensions = ['.csv']
        sas_converter = SASConverter()
        test_message = sas_converter.file_extension_exception_message('to_csv', valid_extensions)

        self.assertEqual(valid_message, test_message)

    def test_file_extenstion_exception_message_are(self):
        valid_message = 'sas7bdat conversion error - Valid extensions for to_csv conversion are: .csv, .txt'
        valid_extensions = ['.csv', '.txt']
        sas_converter = SASConverter()
        test_message = sas_converter.file_extension_exception_message('to_csv', valid_extensions)

        self.assertEqual(valid_message, test_message)

    def test_invalid_key_exception_message_no_optional(self):
        valid_message = 'Invalid key provided, expected keys are: sas7bdat_file, export_file'
        required_keys = ['sas7bdat_file', 'export_file']
        sas_converter = SASConverter()
        test_message = sas_converter.invalid_key_exception_message(required_keys=required_keys)

        self.assertEqual(valid_message, test_message)

    def test_invalid_key_exception_message_optional(self):
        valid_message = 'Invalid key provided, expected keys are: sas7bdat_file, export_file and optional keys are: root_node, first_node'
        required_keys = ['sas7bdat_file', 'export_file']
        optional_keys = ['root_node', 'first_node']
        sas_converter = SASConverter()
        test_message = sas_converter.invalid_key_exception_message(required_keys=required_keys, optional_keys=optional_keys)

        self.assertEqual(valid_message, test_message)

    def test_is_valid_extension_multiple_false(self):
        sas_converter = SASConverter()
        valid_extensions = ['.txt', '.csv']
        file_extension = '.xml'
        self.assertFalse(sas_converter.is_valid_extension(valid_extensions, file_extension))

    def test_is_valid_extension_multiple_true(self):
        sas_converter = SASConverter()
        valid_extensions = ['.txt', '.csv']
        file_extension = '.csv'
        self.assertTrue(sas_converter.is_valid_extension(valid_extensions, file_extension))

    def test_is_valid_extenstion_single_false(self):
        sas_converter = SASConverter()
        valid_extensions = ['.sas7bdat']
        file_extension = '.json'
        self.assertFalse(sas_converter.is_valid_extension(valid_extensions, file_extension))

    def test_is_valid_extenstion_single_true(self):
        sas_converter = SASConverter()
        valid_extensions = ['.sas7bdat']
        file_extension = '.sas7bdat'
        self.assertTrue(sas_converter.is_valid_extension(valid_extensions, file_extension))

    def test_to_csv(self):
        sas_converter = SASConverter()
        sas_file = os.path.join(self.sas7bdat_dir, 'file1.sas7bdat')
        converted_file = os.path.join(self.converted_dir, 'file1.csv')
        expected_file = os.path.join(self.expected_dir, 'file1.csv')
        sas_converter.to_csv(sas_file, converted_file)

        self.assertTrue(filecmp.cmp(converted_file, expected_file, shallow=False), msg='The generated csv file doesn\'t match the expected')

    def test_to_dataframe(self):
        d = {'integer_row': [1.0, 2.0, 3.0, 4.0, 5.0], 'text_row': ['Some text', 'Some more text', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc lobortis, risus nec euismod condimentum, lectus ligula porttitor massa, vel ornare mauris arcu vel augue. Maecenas rhoncus consectetur nisl, ac convallis enim pellentesque efficitur. Praesent tristique .  End of textlectus a dolor sodales, in porttitor felis auctor. Etiam dui mauris, commodo at venenatis eu, lacinia nec tellus. Curabitur dictum tincidunt convallis. Duis vestibulum mauris quis felis euismod bibendum. Nulla eget nunc arcu. Nam quis est urna. In eleifend ultricies ultrices. In lacinia auctor ex, sed commodo nisl fringilla sed. Fusce iaculis viverra eros, nec elementum velit aliquam non. Aenean sollicitudin consequat libero, eget mattis.', 'Text', 'Test'], 'float_row': [2.5, 17.23, 3.21, 100.9, 98.6], 'date_row': ['2018-01-02', '2018-02-05', '2017-11-21', '2016-05-19', '1999-10-25']}
        df = pd.DataFrame(data=d)
        df['date_row'] = pd.to_datetime(df['date_row'])
        df = df[['integer_row', 'text_row', 'float_row', 'date_row']]
        sas_converter = SASConverter()
        sas_file = os.path.join(self.sas7bdat_dir, 'file1.sas7bdat')
        df_file = sas_converter.to_dataframe(sas_file)
        pd.testing.assert_frame_equal(df, df_file, check_datetimelike_compat=True)

    def test_to_excel(self):
        sas_converter = SASConverter()
        sas_file = os.path.join(self.sas7bdat_dir, 'file1.sas7bdat')
        converted_file = os.path.join(self.converted_dir, 'file1.xlsx')
        expected_file = os.path.join(self.expected_dir, 'file1.xlsx')
        sas_converter.to_excel(sas_file, converted_file)

        df_expected = pd.read_excel(expected_file)
        df_converted = pd.read_excel(converted_file)

        pd.testing.assert_frame_equal(df_expected, df_converted)

    def test_to_json(self):
        sas_converter = SASConverter()
        sas_file = os.path.join(self.sas7bdat_dir, 'file1.sas7bdat')
        converted_file = os.path.join(self.converted_dir, 'file1.json')
        expected_file = os.path.join(self.expected_dir, 'file1.json')
        sas_converter.to_json(sas_file, converted_file)

        self.assertTrue(filecmp.cmp(converted_file, expected_file, shallow=False), msg='The generated json file doesn\'t match the expected')

    def test_to_xml(self):
        sas_converter = SASConverter()
        sas_file = os.path.join(self.sas7bdat_dir, 'file1.sas7bdat')
        converted_file = os.path.join(self.converted_dir, 'file1.xml')
        expected_file = os.path.join(self.expected_dir, 'file1.xml')
        sas_converter.to_xml(sas_file, converted_file)

        self.assertTrue(filecmp.cmp(converted_file, expected_file, shallow=False), msg='The generated xml file doesn\'t match the expected')

if __name__ == '__main__':
    unittest.main()
                                                                  
