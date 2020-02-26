# -*- coding: utf-8 -*-
'''
Created on 2020.02.21
Modified on 2020.02.26
@author: Queenie
'''

import pandas as pd
from io import BytesIO
from convert_url_unhardcode import url_convert_with_logicGate

# url parser will return http.response.content which is a Binary Raw Data
# Binary Raw shall type cast as Buffer using BytesIO

def extractor(query_table_name):

    res_data = url_convert_with_logicGate(query_table_name)
    print(type(res_data)) # shall be <class 'bytes'>
    
    buffer = BytesIO(res_data)
    df = pd.read_excel(buffer, sheet_name=0, header=None, skiprows=2, skipfooter=17)
    print(df)

    #df = pd.read_excel(buffer_data, sheet_name=0, header=None, skiprows=4)
    #print(df)

    #if query_table_name == 'FormosaCurve': # change phase depend on sheet_names

        #df = pd.read_excel(buffer_data)
        #xlrd.biffh.XLRDError: Unsupported format, 
        #or corrupt file: Expected BOF record; found b'raw_bin_'

    #else:
        #df = pd.DataFrame()
        #df = {}

if __name__ == '__main__':

    sheet_name = 'Formosa' # can be changed depend on sheet_name
    extractor(query_table_name=sheet_name)