# -*- coding: utf-8 -*-
'''
Created on 2020.02.21
Modified on 2020.02.26
@author: QueenPy
'''
import os, sys
import logging, re
import time as t 
import datetime as d 
import requests as req
from urllib.parse import urlparse as p

#from io import BytesIO, StringIO

def url_convert_with_logicGate(query_key_4_test):

    # to add exception catcher

    try:

        # !!! {TO-DO} !!!  
        # to add if-else-logicalGate
        # url_converter(query_sheet=query_key_4_test)

        yesterday_data = url_converter_yesterday(query_sheet_subtract_1day=query_key_4_test)
        return yesterday_data
        
    except req.exceptions.HTTPError as e:
        logging.error(str(e))
        return 1

def url_converter(query_sheet):

    lt = t.localtime()
    zero = 0
 
    target_url = 'https://www....//{t[0]}/{t[0]}{zero}{t[1]}/{name}.{t[0]}{zero}{t[1]}{t[2]}-C.xls'.format(name=query_sheet, zero=zero, t=lt)
    # print(target_url)

    #req.headers['Accept'] = 'application/vnd.ms-excel'
    res = req.get(url=target_url, timeout=500)

    print(res.url, res.status_code)
    print(res.headers['Content-Type'], res.headers['Date'])
    return res.content

# param may be query_sheet, as a polymorphism
def url_converter_yesterday(query_sheet_subtract_1day):
    # to do yesterday

    y_d =d.date.today() + d.timedelta(-1) # arg of timedelta is days
    #print('yesterday is', y_d)

    # using .strftime()
    y_Y, y_M, y_D = y_d.strftime("%Y"), y_d.strftime("%m"), y_d.strftime("%d")
    #print(y_Y, y_M, y_D)

                  
    target_url_y = 'https://www..../internationalbond//{y_y}/{y_y}{y_m}/{name}.{y_y}{y_m}{y_d}-C.xls'.format(name=query_sheet_subtract_1day, y_y=y_Y, y_m=y_M, y_d=y_D)

    res = req.get(url=target_url_y, timeout=600)

    print(res.url, res.status_code)
    print(res.headers['Content-Type'], res.headers['Date'])
    print(type(res.content)) #<class 'bytes'>
    return res.content
    # application/vnd.ms-excel Wed, 26 Feb 2020 02:10:56 GMT

        # res = req.get(target_url)
        # print(res.content) #binary data type
        # 4\xbb\xa5\xe4\xb8\x8a\xe3\x80\x82 \r\n

        # .json() result in json obj
        # raise JSONDecodeError("Expecting value", s, err.value) from None
        # json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    
    #else:

        #alter_to_url = to home page
        #res = req.get(url=alter_to_url, timeout=100)
        #print('back to main page', res.status_code)

if __name__ == "__main__":

    # query_word = ''
    ## html_converter(query_file=query_word)
    ## html_converter()
    query_key_4_test = 'Formosa'
    # if file nit post today, then the req will be redirect , and status code will be 300   
    # 
    url_convert_with_logicGate(query_key_4_test) 
