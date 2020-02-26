# -*- coding: utf-8 -*-
'''
Created on 2020.02.21
Modified on 2020.02.26
@author: QueenPy
'''

import requests as req
import logging, re
from io import BytesIO, StringIO
#listen to Buffer or Binaray Data, such as http.response.content
#from requests.exception importHTTPError
from getpass import getpass
from requests.auth import AuthBase # seems like a interface to be my Parent Class
from requests.exceptions import Timeout
import pandas as pd

# return with response.content which a binary raw, shall using BytesIO to Type Cast as Buffer
def send_receive_http_header(url):

    try:
        response = req.get(url, timeout=(100,500)) # timeout=(2, 5)connect in 2 seconds & rcv in 5 sec
    except Timeout as e:
        print(e) # catch and print timeout exception

    # return session.request(method=method, url=url, **kwargs)
    # TypeError: request() got an unexpected keyword argument 'timout'
    
    # usage => req.get(url, auth=TokenAuth('012345abc-token'))

    # %()s means a thread name ------
    # time_option_set = '%(asctime)s'
    # logging,basicConfig(format=time_option_set)
    #-----------------------------------------------

    # small logical gate
    if response.status_code == 200:
        logging.info('success, 200')
        return response.content

    elif response.status_code == 404:
        print('not found, 404')

    else:
        print('you got nothing, plz check url asap!')

    ## test results in status_code, headers['Content-Type'], content, text as below

    #print(response.status_code, logging.info('connection is not good at all.'))
    
    ## print(response.json()) #response.text, response.content
    # raise JSONDecodeError("Expecting value", s, err.value) from None
    
    #print(response.headers['Content-Type'])

    # print(response.content) 
    # Buffer or Binary
    # respone in raw bytes (二進位) data type
    # result: 00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00

    response.encoding = 'utf-8' #options
    ### print(response.text) # response in json format (明文)
    # result : ������������    

    # json object
    # print(response.json())
    # result : Document=BDdos209/&H00000000 (人類易讀格式)
    # raise JSONDecodeError("Expecting value", s, err.value) from None
    # json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

    # {'Date': 'Fri, 21 Feb 2020 01:38:45 GMT', 
    # 'Server': 'Apache', 
    # 'X-XSS-Protection': '1;mode=block', 
    # 'Vary': 'Origin', 
    # 'Content-Security-Policy': "frame-ancestors 'self' *.twse.com.tw *.tdcc.com.tw digitalprocesssys-epassbook.cdn.hinet.net 
    # http://digitalprocesssyst-epassbook.cdn.hinet.net;", 
    # 'X-Frame-Options': 'SAMEORIGIN', 
    # 'Cache-Control': 
    # 'max-age=600, private, must-revalidate', 
    # 'Keep-Alive': 'timeout=5, max=100', 
    # 'Connection': 'Keep-Alive', 
    # 'Transfer-Encoding': 'chunked', 
    # 'Content-Type': 'text/html'}

    # Modify the call back from getting API
    # pass value in param, request target URL
    # a dictionary data type
    # response = req.get(url, params = { } )
    ## response_in_detail = req.get(url, params = {'l' : 'zh-tw'})


    # the case to use the Session Object by using Session Class
    # is when storing the variable in persistent way such as Auth Token
    # if connection in same session, then no bother to re-connect for multi-req ~

def bufferOrBinary2pdDF(url_parse):
    temp_bf = send_receive_http_header(url=url_parse)
    b = BytesIO(temp_bf)
    # df_html = pd.read_html(b)
    # raise ValueError("No tables found")
    # ValueError: No tables found

    # input using panda param options to get specific data columns & rows 
    df_xls = pd.read_excel(b, sheet_name=0, header=None, skiprows=2, skipfooter=17)

    print(df_xls)
    print(df_xls[1:3])

def connect_in_same_Session(url):

    with req.Session() as ss:

        ss.auth = ('username', getpass())

        response_in_session = ss.get(url, timeout=200)

    print(response_in_session.headers['Content-Type'], response_in_session.content.json())
         # usage => req.get(url, auth=TokenAuth('012345abc-token'))


# Http Msg Body
def pass_data_to_server(url, data):

    # data can be a dictionary or list of tuples
    req.post(url, data)

# Http Msg Body
def send_json_2_server(url, doc):

    json_doc = doc.json()
    req.post(url, json=json_doc[0][1])

# Unit Test for Post Method called
def test_post_method(url, test_data):

     res = req.post(url, json=test_data)
     json_res = res.json()
     print('response without jsonify', res)
     print('response has its jsonify data called json obj',json_res['data'])
     # {"name": "QueenPy"}
     # response without jsonify <Response [200]>
     # response has its jsonify data called json obj {"name": "QueenPy"}

# to test url req-res chain using TokenAuth
class TokenAuth(AuthBase):

    # to init the param to class
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        # add api token to header
        r.headers['X-TokenAuth'] = f'{self.token}' 
        return r

if __name__ == '__main__':
    
    url_addr = ''
    # <Response [200]> None

    # url_toTest_param = ''
    # success, 200

    url_for_xls_doc = 'https//...xls'
    url4Test = 'https://http....org/post'
    dict_data_4_test = {'name': 'QueenPy'}

    # send_receive_http_header(url=url_addr)
    # send_receive_http_header(url=url_toTest_param)
    ## send_receive_http_header(url=url_for_xls_doc)
    # application/vnd.ms-excel
    ## send_receive_http_header(url=)
    #connect_in_same_Session(url=url_addr)
    #test_post_method(url=url4Test, test_data=dict_data_4_test)

    bufferOrBinary2pdDF(url_for_xls_doc)

    ## bufferOrBinary2pdDF(daily_bond_url)
