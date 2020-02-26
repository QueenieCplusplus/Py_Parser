# -*- coding: utf-8 -*-
'''
Created on 2020.02.20

@author: QueenPy
'''
import os, sys, logging
import wget
import requests
from io import BytesIO, StringIO
from urllib.parse import urlparse
import pandas as pd

def excelfile_downloader(input_url):
    # query_date=pd.Timestamp.now()
    # store_local=True

    # to do a custom header
    req_header = {'content_type' : 'application/vnd.ms-excel'}
    
    # to do a custom header with param
    req_param = {'data_date': '20200219'}


    #if-else to pass in the sheet_name as name and query_date as date in URL get process

    try:
        res = requests.get(url=input_url, headers = req_header, params = req_param)
        print(res.status_code, res.text, res.content)


    except requests.exceptions.HTTPError as e:
        logging.error(str(e))   
 
    new_file_being_dw = wget.download(url, 'c:/Users/queenie/Downloads/new_bond.xls')

    print(new_file_being_dw)

if __name__ == "__main__":

    test_url = ''

    # name = ' ', can be pass to the url param
    # target_url = 'https://.....xls'.format(name=name, date=query_date)

    getRes = excelfile_downloader(inputurl=test_url)

    print(getRes)
    #python -m download_bond_excel_data
    #result is (True, <_io.BytesIO object at 0x000001EB647ED468>)
    # requirs panda tool to do parsing
