# -*- coding: utf-8 -*-
'''
Created on 2020.02.24

@author: QueenPy
'''
import pandas as pd
from streamz import Stream
from streamz.dataframe import DataFrames
import logging, re
import itertools
# (to do code today on 0224)
# from io import BytesIO, StringIO 
# abandon this above IO based tool due to no Path nor Buffer(Memory Register)  
# from urllib.parse import urlparse
# import requests

# create streaming object
st = Stream()

# create panda dataframe
df = pd.DataFrame()

# using streaming dataframe

def df2sdf_converter(df):
    sdf = DataFrames(stream=st, example=df) # stream , example, stream_type
    logging.info('conversion process now')
    show_spec_px = sdf[sdf.item == 'bond'].price.sum()
    print(show_spec_px)
    
def df2sdf_operator(st):
    op_stream = st.map(test_multiple_100(6)).sink(print)
    print(op_stream) # <sink: print>
    
def check_streaming_able_add_ele(n):
    s_ele = st.emit(n)
    print(s_ele)

def test_multiple_100(n):
    return n * 100

# to manage continuous sequence of data using iterators || generators
# (to do)

if __name__ == '__main__':
    sample_stream  = Stream() #upstream, upstreams, stream_name, loop, async, io
    sample_df = pd.DataFrame({'item':['bond', 'share'], 'price':[22, 33]})
    print(sample_df)
    df2sdf_converter(sample_df)
    df2sdf_operator(sample_stream)   

# python -m parse_stream_using_pd    
#    item  price
# 0   bond     22
# 1  share     33
# Streaming - elements like:
# 22
# <sink: print>