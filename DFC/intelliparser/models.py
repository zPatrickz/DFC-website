# -*- coding: utf-8 -*-


__version__ = '0.1'


from django.db import models
import os
class LexicalAnalyzer(object):
    TYPE_EMAIL = 1
    TYPE_MOBILE = 2
    TYPE_GRADE = 3
    TYPE_DEPARTMENT = 4
    TYPE_QQ = 5
    TYPE_TITLE = 6
    TITLE_NAME = 1
    TITLE_DEPARTMENT = 2
    TITLE_GRADE = 3
    TITLE_MOBILE = 4
    TITLE_EMAIL = 5
    def __init__(self):
        pass
    
    @classmethod
    # parameter text - text to analyze
    # return the type of the text
    def get_type(cls,text):
        import numbers
        if isinstance(text, numbers.Number):
            pass
        else:
            if cls.get_title_type(text) is not None:
                return cls.TYPE_TITLE
    
    @classmethod
    # parameter text - text to analyze
    # return the type of the text
    def get_title_type(cls,text):
        text = text.replace(" ", "") #remove whitespace
        if u'姓名' in text or 'name' in text.lower():
            return cls.TITLE_NAME
        elif u'院系' in text or 'depart' in text.lower():
            return cls.TITLE_DEPARTMENT
        elif u'手机' in text or u'电话' in text or 'mobile' in text.lower():
            return cls.TITLE_MOBILE
        elif u'邮箱' in text or u'电邮' in text or 'mail' in text.lower():
            return cls.TITLE_EMAIL
        else:
            return None
            
    @classmethod
    # parameter text - text to analyze
    # return True if the type is TYPE_TITLE
    def is_title(cls,text):
        if cls.get_type(text) == cls.TYPE_TITLE:
            return True
        return False
            
class IntelliParser(object):
    def __init__(self):
        self.wb = None
        self.doc_type = None
    # parameter doc - path of the doc
    # return none
    def parse(self,doc):
        if os.path.splitext(doc)[1] == '.xls' or os.path.splitext(doc)[1] == '.xlsx':
            self.parse_excel(doc)
            
    # parameter doc - path of the doc
    # return none
    def parse_excel(self,doc):
        #Excell document, using xlutils
        from xlrd import open_workbook
        self.wb = open_workbook(doc)           
        self.doc_type = 'excel' 
    
    # return a list of contacts information  
    #        None if doc is not loaded or is not excel
    def extract_contacts(self):
        if self.wb is None or not self.doc_type == 'excel':
            return None 
        for ws in self.wb.sheets():
            # Process each sheet
            if ws.nrows == 0 or ws.ncols == 0:
                continue
            # Find out the title row or column
            row_dic = {}
            col_dic = {}
            for r in range(ws.nrows):
                for c in range(ws.ncols):
                    if LexicalAnalyzer.is_title(ws.cell(r,c).value):
                        if r in row_dic:
                            row_dic[r] += 1
                        else:
                            row_dic[r] = 1
                        if c in col_dic:
                            col_dic[c] += 1
                        else:
                            col_dic[c] = 1
            max_row = 0
            max_row_count = 0
            max_col = 0
            max_col_count = 0
            for r in row_dic:
                if row_dic[r]>max_row_count:
                    max_row_count = row_dic[r]
                    max_row = r
            for c in col_dic:
                if col_dic[c]>max_col_count:
                    max_col_count = col_dic[c]
                    max_col = c
            
            contacts = []
            if max_row_count > max_col_count:
                # Titles in a row, locate titles and prepare title information
                title_dic = {}# key - title type, value - title column index
                for c in range(ws.ncols):
                    if LexicalAnalyzer.is_title(ws.cell(max_row,c).value):
                        title_dic[LexicalAnalyzer.get_title_type(ws.cell(max_row,c).value)] = c

                # Extract contact information, row by row
                for r in range(max_row+1,ws.nrows):
                    person_contact = {}
                    for title_type in title_dic:
                        person_contact[title_type] = ws.cell(r,title_dic[title_type])
                    contacts.append(person_contact)
            else:
                # Titles in a column, locate titles and prepare title information
                title_dic = {}# key - title type, value - title row index
                for r in range(ws.nrows):
                    if LexicalAnalyzer.is_title(ws.cell(r,max_col).value):
                        title_dic[LexicalAnalyzer.get_title_type(ws.cell(r,max_col).value)] = r
                        
                # Extract contact information, column by column
                for c in range(max_col+1,ws.ncols):
                    person_contact = {}
                    for title_type in title_dic:
                        person_contact[title_type] = ws.cell(title_dic[title_type],c)
                    contacts.append(person_contact)
            return contacts