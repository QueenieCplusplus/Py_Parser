# Py_Parser
Pandas Tool

sqlacodegen mysql+pymysql://password:username@00.00.00.00:____/_____ --outfile ____.py

#------------------------------------------------------------------------------------------
# Downloader using wget

> code 

    import wget
    wget.download(url, 'c:/Users/queenie/Downloads/new_bond.ods')

> see 

<https://dzone.com/articles/simple-examples-of-downloading-files-using-python>

#------------------------------------------------------------------------------------------
# AOO parser using pyexcel_ods

> code 

     from pyexcel_ods import get_data

     def read_parse_aooSheet_content(path):
        
        aoo_sheet = get_data(path)
        curve_data = aoo_sheet['FormosaCurve'][3:4]
        print(curve_data)

#------------------------------------------------------------------------------------------
# Http headers Study

https://github.com/QueenieCplusplus/Http_header

> code usage 

<https://realpython.com/python-requests/>

#------------------------------------------------------------------------------------------
# Auth by Token

Bad Auth mechanism can lead to security vulnerabilities, so use Basic or Oauth instead of custom token. Reminder to use SSL by requests.get(url_string, verify=True)

    import requests 
    from requests.auth import AuthBase 
    # seems like a interface to be my Parent Class

    usage => requests.get(url, auth=TokenAuth('012345abc-token'))

    # to test url req-res chain using TokenAuth
    class TokenAuth(AuthBase):

        # to init the param to class
        def __init__(self, token):
            self.token = token

        def __call__(self, r):
            # add api token to header
            r.headers['X-TokenAuth'] = f'{self.token}' 
            return r

#------------------------------------------------------------------------------------------
# Session for Persistent Variable 

    import requests as req
    from getpass import getpass

    def connect_in_same_Session(url):

        with req.Session() as ss:

            ss.auth = ('username', getpass())

            response_in_session = ss.get(url)

        print(response_in_session.headers['Content-Type'], response.content.json())

#------------------------------------------------------------------------------------------
# URL Parser using time tool & string.format() with {}

> code

    import time as t
    year = t.localtime()[0]
    month = t.localtime()[1]
    day = t.localtime()[2]

    with year, month, day as y, m, d:
        print(y, m, d)

> code

    lt = t.localtime()
    zero = 0

    target_url = 'https://www.queen.org.tw/storage/info//{t[0]}/{t[0]}{zero}{t[1]}/{name}.{t[0]}{zero}{t[1]}{t[2]}-C.xls'.format(name=query_sheet, zero=zero, t=lt)

> usage

<http://dangerlover9403.pixnet.net/blog/post/207711846-%5Bpython%5D-day13---python-time-%E6%A8%A1%E7%B5%84>


#------------------------------------------------------------------------------------------
# Data Type Casts

* text 明文
   
         readline

* binaray 二進制位元組

         \x00\x01

* raw 毛資料串流 (means unbuffered)

* buffer, 緩存

  It inherits IOBase. But does't matter with file path as well.

> IO

<https://docs.python.org/3/library/io.html>


#------------------------------------------------------------------------------------------
# Streaming Data using os.BytesIO()

> to make binary data to be buffer like streaming, a nonstop sequence.

    import requsts
    from io import BytesIO
    import pandas as pd

    binaryData = response.content 
    bufferData = BytesIO(binaryData) 
    html-dataFrame = pd.read_html(bufferData)
    xls_dataFrame = pd.read_excel(bufferData, sheet_name=, header=, skiprows=)
    print(xls_dataFrame)
    print(xls_dataFrame.columns[0:13])
    print(xls_dataFrame.rows[3:4])

> reference

<https://docs.python.org/3/library/io.html>

> Type Cast


   bufferData = io.BytesIO(b"some initial binary data: \x00\x01") # (response.content)


#------------------------------------------------------------------------------------------
# Streaming Data using Streamz

> data flow

![streamz](https://streamz.readthedocs.io/en/latest/_images/simple.svg)

> operations on streaming

![ops](https://streamz.readthedocs.io/en/latest/_images/complex.svg)

![map](https://streamz.readthedocs.io/en/latest/_images/inc-dec-add-print.svg)

> tool 

<https://streamz.readthedocs.io/en/latest/>

#------------------------------------------------------------------------------------------
# Alternative

Other library modules may provide additional ways to create text (明文) or binary streams (二進制位元組串流). 
See socket.socket.makefile() for example.

#------------------------------------------------------------------------------------------
# Panda DataFrame Operation

see

<https://pandas.pydata.org/docs/user_guide/index.html>

