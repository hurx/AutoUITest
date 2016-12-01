# -*- coding:utf-8 -*-

import cx_Oracle

class OracleCtl:
    def __init__(self, orcl_name, orcl_pwd, orcl):
        """
        make connection with remote oracle
        args:
            orcl_name: user name of remote oracle
            orcl_pwd: password  of remote orcle
            orcl : eg, 10.1.1.1:1521/orcl
        """
        con = cx_Oracle.connect(orcl_name, orcl_pwd, orcl)
        self.cur = con.cursor()

    def sql_execute(self, sql_statement, params=None):
        """
        execute sql statement, select or update statement. with commit at the end of sql.
        :arg
            sql_statment: sql statment  , type string
            params: params in sql statment , dictionary
        :return
            success return True, otherwise False.
        """
        try:
            if params is None:
                self.cur.execute(sql_statement)
            else:
                self.cur.execute(sql_statement, params)
            finish_with_commit = r'commit'
            self.cur.execute(finish_with_commit)
        except:
            return False
        else:
            return True

    def sql_execute_fetchone(self, sql_statement, params=None):
        """
        execute sql statment, get the first line
        :arg
            sql_statment: sql statment  , type string
            params: params in sql statment , dictionary
        :return
            a list of the first line, eg: ['1' , '2', '3']
        """
        result_list = []
        if params is None:
            self.cur.execute(sql_statement)
        else:
            self.cur.execute(sql_statement, params)
        sql_result = self.cur.fetchone()
        if sql_result is None:
            return result_list
        for element in sql_result:
            if isinstance(element, str):
                result_list.append(element.decode('gbk'))
            else:
                result_list.append(element)
        return result_list

    def sql_execute_fetchall(self, sql_statement, params=None):
        """
        execute sql statment, get all the result.
        :arg
            sql_statment: sql statment  , type string
            params: params in sql statment , dictionary
        :return
            a binary list of the result, eg: [['1' , '2', '3'],['4', '5', '6']]
        """
        result_list = []
        if params is None:
            self.cur.execute(sql_statement)
        else:
            self.cur.execute(sql_statement, params)
        sql_result = self.cur.fetchall()
        if sql_result is None:
            return result_list
        for item in sql_result:
            element_list = []
            for element in item:
                if isinstance(element, str):
                    element_list.append(element.decode('gbk'))
                else:
                    element_list.append(element)
            result_list.append(element_list)
        return result_list


