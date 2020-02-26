# -*- coding: utf-8 -*-
'''
Code by Q on 2020.02.26 wed.
@author: QueenPy
'''

import requests
import pandas as pd
from urllib.parse import urlparse
import itertools
#from flask import instanceOfFlask

def require_user_name(name='queenPy', query_date=pd.Timestamp.now()):

    if name=='queenPy':
        url = ''.format(name=name, date=query_date)
        content_type = 'text/html'
    else:
        url = ''.format(name=name, date=query_date)
        content_type = 'application/vnd.ms-excel'
    try:
        response = requests.get(url=url, timeout=200)
        response.status_code==200 and response.headers['content-type']==content_type:
        return False, '' # or buffer
    except requests.exceptions.HTTPError as e:
        logging.error(str(e))    
        return False, '' # or buffer
      
def pet_data_parser(name='Queen', query_date=pd.Timestamp.now()):
    lambda_name = lambda p: method_name
    
    try:
        success, buffer = require_user_name(name=name, query_date=query_date) # success???

        if success:

            if name=='GreyCat':
                df = pd.read_excel(buffer, sheet_name=, header=, skiprows=)
                df.columns = ['ItemCode','Name','Amount','Coupon','ValidDate']
                df['Amount'] = df['Amount'].apply(lambda_name)

            else name=='BlackCat':
                df = pd.read_excel(buffer, sheet_name=, header=, skiprows=, skipfooter=)
                if df.shape[1]==14:
                    df.columns = ['ItemCode','ItemName','Amount','Coupon','Price']
                elif df.shape[1]==15:
                    df.columns = ['ItemCode','ItemName','Amount','Coupon','Price']
                df['Amount'] = df['Amount'].apply(lambda_name)


            df['timestamp'] = query_date.normalize()
            df.replace({'-': None}, inplace=True)
            df = df.loc[df['ItemCode'].str.match('[A-Z0-9]+$')==True,:]
            df = df.where((pd.notnull(df)), None)

        else:
            df = pd.DataFrame([])

    except Exception as e:
        logging.error(str(e))    
        return pd.DataFrame([])

    else:
        return df

if __name__ == "__main__":

    with pd.option_context('display.max_rows', None, 'display.max_columns', 7):

        name = 'Poupou'

        for date in pd.date_range(start=pd.to_datetime('2020/02/03'), end=pd.to_datetime('2020/02/23')).tolist():
            df = pet_data_parser(query_date=date)
