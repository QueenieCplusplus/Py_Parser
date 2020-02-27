# 0220.2/25. 13:00, created by Queenie
# 0220.2/27. 09:00, modified by Queenie

import logging
import pandas as pd
# from DB.table import *
# from FlaskApp import instanceOfSQLAlchemy as fi
from sqlalchemy import func, exc
from dateutil.relativedelta import relativedelta

# A
# <lambda> (r)
# variable = lambda param: {           } if param else empty object
row_to_dic = lambda row: { col.name: str(getattr(row, col.name)) for col in row.__table__.columns} if row else {}

def query_and_insert(item, start_time=s, end_time=e):
    
    # B
    # make a session connection with DB and using sql statement called query(), then filter() by condition, and render all()
    query_result = fi.session.query(AttrMapping).filter(AttrMapping.table_name==CatFood.__tablename__).all()

    # C = A + B
    pd_data_frame = pd.DataFrame([ row_to_dic(row) for row in query_result ])

    # an empty array called list in Python
    list_data_frame = []

    # for-in-loop
    # panda got ist iterrows() method
    for idx, row in pd_date_frame.iterrows(): # ?????idex?????

        data = {'item': [item],
                'fields': [row['attr']],
                #'start_time': start_time.strftime('%Y/%m/%d'),
                #'end_time': end_time.strftime('%Y/%m/%d')
                }
        
        # http request using POST method
        post_a_data = requests.post("http://:30000//", json=data)

    # verification
    if list_data_frame not == "" or ! == []:

        new_data_frame = pd.concat(list_data_frame, axis=1).sort_index()
        return new_data_frame
        
# for-loop, variable is row in records
# Try ok, then d.session.bulk_insert_mapping(CatFood, records) # seems like that records is row data.
# Try ok, then d.session.commit()
# Catch Exception to make d.session.rollback() 

if __name__ == '__main__':
    item = 'QueenPy' # type something.
    query_and_insert(item)
    # param can design 2nd & 3rd optional or default arg
    # such as start_time & end_time

# Python 空值
None
False
0
0.0
0L
''
()
[]
{}