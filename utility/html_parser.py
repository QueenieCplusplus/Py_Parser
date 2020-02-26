# -*- coding: utf-8 -*-
'''
Created on 2020.02.20

@author: QueenPy
'''
import os, sys
import logging
# from sqlalchemy import func, exc
# from Api import d
# from Database.table import *
# from RMS.fair_value import *

from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup 

def open_webpage(url):

    try:
        html_res = urlopen(url)
        print(html_res)
    # <http.client.HTTPResponse object at 0x0000023EC7946508>

    except HTTPError as e:
        print(e)
        return None  

    try:
        bs = BeautifulSoup(html_res.read(), 'html.parser')
        bond_data_list = bs.findAll('ol', {'class':'breadcrumb'})
        for bond_data in bond_data_list:
            print(bond_data.get_text())
    
    except AttributeError as a:
        print(a)
        return None
    
    return bond_data_list

    # else:

if __name__ == '__main__':

    url = ''
    data = open_webpage(url)
    
    if data == None:
            print('no data occurs')
    else:
        print(data)


