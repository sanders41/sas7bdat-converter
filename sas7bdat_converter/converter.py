import csv
import json
import numpy as np
import os
import pandas as pd
from xml.sax.saxutils import escape

class SASConverter:
    def batch_to_csv(self, file_dicts):
        required_keys = ('sas7bdat_file', 'export_file',)
        for file_dict in file_dicts:
            if len(set(file_dict).intersection(required_keys)) != len(required_keys):
                message = self.invalid_key_exception_message(required_keys=required_keys)
                raise KeyError(message)

            sas7bdat = file_dict['sas7bdat_file']
            export = file_dict['export_file']
            self.to_csv(sas7bdat_file=sas7bdat, export_file=export)

    def batch_to_excel(self, file_dicts):
        required_keys = ('sas7bdat_file', 'export_file',)
        for file_dict in file_dicts:
            if len(set(file_dict).intersection(required_keys)) != len(required_keys):
                message = self.invalid_key_exception_message(required_keys=allowed_keys)
                raise KeyError(message)

            sas7bdat = file_dict['sas7bdat_file']
            export = file_dict['export_file']
            self.to_excel(sas7bdat_file=sas7bdat, export_file=export)

    def batch_to_json(self, file_dicts):
        required_keys = ('sas7bdat_file', 'export_file',)
        for file_dict in file_dicts:
            if len(set(file_dict).intersection(required_keys)) != len(required_keys):
                message = self.invalid_key_exception_message(required_keys=allowed_keys)
                raise KeyError(message)

            sas7bdat = file_dict['sas7bdat_file']
            export = file_dict['export_file']
            self.to_json(sas7bdat_file=sas7bdat, export_file=export)

    def batch_to_xml(self, file_dicts):
        required_keys = ('sas7bdat_file', 'export_file',)
        optional_keys = ('root_node', 'first_node',)
        for file_dict in file_dicts:
            error = False
            if len(set(file_dict).intersection(required_keys)) != len(required_keys) or len(set(file_dict).intersection(required_keys)) > len(required_keys) + len(optional_keys):
                error = True
            elif len(set(file_dict).intersection(optional_keys)) != len(file_dict) - len(required_keys):
                error = True

            if error:
                message = self.invalid_key_exception_message(required_keys=required_keys, optional_keys=optional_keys)
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
                self.to_xml(sas7bdat_file=sas7bdat, export_file=export, root_node=root_node, first_node=first_node)
            elif root_node and not first_node:
                self.to_xml(sas7bdat_file=sas7bdat, export_file=export, root_node=root_node)
            elif not root_node and first_node:
                self.to_xml(sas7bdat_file=sas7bdat, export_file=export, first_node=first_node)
            else:
                self.to_xml(sas7bdat_file=sas7bdat, export_file=export)

    def dir_to_csv(self, dir_path, export_path=None):
        for file_name in os.listdir(dir_path):
            if file_name.endswith('.sas7bdat'):
                # file_name[:-9] removes .sas7bdat from the end of the file
                export_file = file_name[:-9] + '.csv'
                if export_path:
                    export_file = os.path.join(export_path, export_file)
                else:
                    export_file = os.path.join(dir_path, export_file)
                
                sas7bdat_file = os.path.join(dir_path, file_name)
                self.to_csv(sas7bdat_file, export_file)

    def dir_to_excel(self, dir_path, export_path=None):
        for file_name in os.listdir(dir_path):
            if file_name.endswith('.sas7bdat'):
                export_file = file_name[:-9] + ' .xlsx'
                if export_path:
                    export_file = os.path.join(export_path, export_file)
                else:
                    export_file = os.path.join(dir_path, export_file)
                
                sas7bdat_file = os.path.join(dir_path, file_name)
                self.to_excel(sas7bdat_file, export_file)

    def dir_to_json(self, dir_path, export_path=None):
        for file_name in os.listdir(dir_path):
            if file_name.endswith('.sas7bdat'):
                export_file = file_name[:-9] + ' .json'
                if export_path:
                    export_file = os.path.join(export_path, export_file)
                else:
                    export_file = os.path.join(dir_path, export_file)
                
                sas7bdat_file = os.path.join(dir_path, file_name)
                self.to_json(sas7bdat_file, export_file)

    def dir_to_xml(self, dir_path, export_path=None):
        for file_name in os.listdir(dir_path):
            if file_name.endswith('.sas7bdat'):
                export_file = file_name[:-9] + ' .xml'
                if export_path:
                    export_file = os.path.join(export_path, export_file)
                else:
                    export_file = os.path.join(dir_path, export_file)
                
                sas7bdat_file = os.path.join(dir_path, file_name)
                self.to_xml(sas7bdat_file, export_file)

    def file_extension_exception_message(self, conversion_type, valid_extensions):
        if len(valid_extensions) == 1:
            is_are = ('extension', 'is')
        else:
            is_are = ('extensions', 'are')

        extensions = ', '.join(valid_extensions)
        return 'sas7bdat conversion error - Valid {} for {} conversion {}: {}'.format(is_are[0], conversion_type, is_are[1], extensions)

    def invalid_key_exception_message(self, required_keys, optional_keys=None):
        required_keys = ', '.join(required_keys)
        if optional_keys:
            optional_keys = ', '.join(optional_keys)
            message = 'Invalid key provided, expected keys are: {} and optional keys are: {}'.format(required_keys, optional_keys)
        else:
            message = 'Invalid key provided, expected keys are: {}'.format(required_keys)

        return message

    def is_valid_extension(self, valid_extensions, file_extension):
        if file_extension in valid_extensions:
            return True
        else:
            return False

    def to_csv(self, sas7bdat_file, export_file):
        valid_extensions = ['.csv']
        file_extension = export_file[-4:].lower()

        if not self.is_valid_extension(valid_extensions, file_extension):
            error_message = self.file_extension_exception_message('to_csv', valid_extensions)
            raise AttributeError(error_message)

        df = self.to_dataframe(sas7bdat_file)
        df.to_csv(export_file, quoting=csv.QUOTE_NONNUMERIC, index=False)

    def to_dataframe(self, sas7bdat_file):
        df = pd.read_sas(sas7bdat_file)

        # convert binary strings to utf-8
        str_df = df.select_dtypes([np.object])
        if len(str_df.columns) > 0:
            str_df = str_df.stack().str.decode('utf-8').unstack()

            for col in str_df:
                df[col] = str_df[col]
            # end conversion to utf-8

        return df

    def to_excel(self, sas7bdat_file, export_file):
        valid_extensions = ['.xlsx']
        file_extension = export_file[-5:].lower()

        if not self.is_valid_extension(valid_extensions, file_extension):
            error_message = self.file_extension_exception_message('to_excel', valid_extensions)
            raise AttributeError(error_message)

        df = self.to_dataframe(sas7bdat_file)
        df.to_excel(export_file, index=False)

    def to_json(self, sas7bdat_file, export_file):
        valid_extensions = ['.json']
        file_extension = export_file[-5:].lower()

        if not self.is_valid_extension(valid_extensions, file_extension):
            error_message = self.file_extension_exception_message('to_json', valid_extensions)
            raise AttributeError(error_message)

        df = self.to_dataframe(sas7bdat_file)
        df.to_json(export_file)

    def to_xml(self, sas7bdat_file, export_file, root_node='root', first_node='item'):
        valid_extensions = ['.xml']
        file_extension = export_file[-4:].lower()
        
        if not self.is_valid_extension(valid_extensions, file_extension):
            error_message = self.file_extension_exception_message('to_xml', valid_extensions)
            raise AttributeError(error_message)

        df = self.to_dataframe(sas7bdat_file) 

        def row_to_xml(row):
            xml = ['  <{}>'.format(first_node)]
            for i, col_name in enumerate(row.index):
                text = row.iloc[i]
                if isinstance(text, str):
                    text = escape(text)

                xml.append('    <{0}>{1}</{0}>'.format(col_name, text))
            xml.append('  </{}>'.format(first_node))
            return '\n'.join(xml)
        res = '<?xml version="1.0" encoding="UTF-8"?>\n<{}>\n'.format(root_node)
        res = res + '\n'.join(df.apply(row_to_xml, axis=1)) + '\n</{}>'.format(root_node)
    
        with open(export_file, 'w') as f:
            f.write(res)
