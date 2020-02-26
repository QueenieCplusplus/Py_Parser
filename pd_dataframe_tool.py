# -*- coding: utf-8 -*-
'''
Created on 2020.02.21
Modified on 2020.02.26
Work Day = 4 days
@author: QueenPy
'''
import pandas as pd
from io import BytesIO
from content_type_parser import url_convert_with_logicGate

# url parser will return http.response.content which is a Binary Raw Data
# Binary Raw shall type cast as Buffer using BytesIO

def extractor(query_table_name):

    if query_table_name == 'Formosa': # change phase depend on sheet_names

        res_data = url_convert_with_logicGate(query_table_name)
        print(type(res_data.content)) # shall be <class 'bytes'>
    
        buffer = BytesIO(res_data.content)
        df = pd.read_excel(buffer, sheet_name=0, header=None, skiprows=2, skipfooter=17)
        print(df[1:3])

    else:
        df_empty = pd.DataFrame()
        df_empty = {}
        print(df_empty)

if __name__ == '__main__':

    sheet_name = 'FormosaCurve' # can be changed depend on sheet_name
    extractor(query_table_name=sheet_name)