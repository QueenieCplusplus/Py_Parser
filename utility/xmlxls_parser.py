# -*- coding: utf-8 -*-
'''
Created on 2020.02.24

@author: QueenPy
'''

from defusedxml.sax import parse
from xml.sax import ContentHandler
from namedlist import namedlist, FACTORY, NO_DEFAULT
from future.utils import iteritems
import pandas as pd
# call = namedlist('call', [('x',[])])
# c=call()
# c.x.apppend(3)
# c2=call()
# print(c2.x)

Data = namedlist('Data', [('attr', []), ('showDataList', FACTORY(list))])

Table = namedlist('Table', [('attr', []), ('name', None), ('showRowList', FACTORY(list))])

Row = namedlist('Row', [('attr', []), ('cells', FACTORY(list))])

Cell = namedlist('Cell', [('attr', []), ('showCellInfo', None)])

coll = {}


def xmlxls2pd(attachedDoc, table=0):
    xxh = XmlXlsHandler()
    if isinstance(attachedDoc, str):
        with open(attachedDoc, 'r') as ad:
            parse(ad, xxh)
    else:
        parse(attachecDoc, xxh)

    table = xxh.tables[table]
    header = table.showRowList[header]
    row = table.showRowList[:]
    col = {}

    def show_rows(cells):
        for cell in cells:
            index = cell.attr["ss:Index"]
            if index in index_columns:
                column = index_columns[index]
                if cell.data is not None:
                    data = cell.data.data
                    dtype = cell.data.attr.get("ss:Type", None)
                    if column in coll:
                        assert(coll[column] == dtype)
                    else:
                        coll[column] = dtype
                    yield column, data

    def show_items(rows):
        rows = iter(rows)

        while True:
            row = next(rows)
            cells = row.cells

            item = dict(show_rows(cells))

            merge_down = max(int(c.attr.get("ss:MergeDown", 0)) for c in cells)
            if merge_down > 0:
                merger = defaultdict(list)
                for i in range(merge_down):
                    # consumer rows to be merged
                    cells = next(rows).cells
                    for k, v in row_gen(cells):
                        merger[k].append(v)
                for k, v in merger.items():
                    v.insert(0, item[k])
                    item[k] = '\n'.join(v)
            yield item

    df = pd.DataFrame(show_items(rows))

    conversions = {None: lambda x: x,
               'DateTime': lambda x: pd.to_datetime(x, utc=True),
               'String': lambda x: x,
               'Number': pd.to_numeric}

    for col in df.columns:
        df[col] = conversions[coll[col]](df[col])
    return df

class XmlXlsHandler(ContentHandler):
    def __init__(self):
        self.data = None
        self.worksheet = None
        self.tables = []
        self.table = None
        self.row = None
        self.cell = None
        
        def _printData(self, atts):
            self.data = Data(atts)

        def _printTable(self, atts):
            self.table = Table(atts)

        def _printRow(self, atts):
            self.row = Row(atts)

        def _printCell(self, atts):
            self.cell = Cell(atts)

if __name__ == "__main__":
    
    new_test_doc = './test_file.xls'
    xmlxls2pd(attachedDoc=new_test_doc, table=2)

#Result
#UnicodeDecodeError: 
# 'cp950' codec can't decode byte 0xb1 in position 5 
#: illegal multibyte sequence