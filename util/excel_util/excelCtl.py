# -*- coding: utf-8 -*-

import xlrd

class ExcelCtl(object):
    def __init__(self, filename):
        self.excel_obj = xlrd.open_workbook(filename)

    def get_table_by_index(self, sheet_index):
        return self.excel_obj.sheet_by_index(sheet_index)

    def get_table_by_name(self, sheet_name):
        return self.excel_obj.sheet_by_name(sheet_name)

    def get_cell_value(self, table, row, col):
        return table.cell(row, col).value

    def get_row_lenth(self, table):
        return table.nrows