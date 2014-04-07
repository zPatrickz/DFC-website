from django.test import TestCase
from intelliparser.models import *

class ParserMethodTests(TestCase):
    
    def setUp(self):
        pass
        
    def testParseExcel(self):
        ip = IntelliParser()
        ip.parse_excel('/Users/apple/Documents/DFC-website/DFC-website/DFC/intelliparser/samples/2012MSTCMedia.xls')
        ip = IntelliParser()
        ip.parse_excel('/Users/apple/Documents/DFC-website/DFC-website/DFC/intelliparser/samples/2012MSTCMedia.xlsx')
        
    def testExtractContactsHorizontal(self):
        ip = IntelliParser()
        ip.parse_excel('/Users/apple/Documents/DFC-website/DFC-website/DFC/intelliparser/samples/2012MSTCMedia.xls')
        contacts = ip.extract_contacts()
        for contact in contacts:
            print contact
        print
        print
    def testExtractContactsVertical(self):
        ip = IntelliParser()
        ip.parse_excel('/Users/apple/Documents/DFC-website/DFC-website/DFC/intelliparser/samples/2012MSTCMediaVertical.xls')
        contacts = ip.extract_contacts()
        for contact in contacts:
            print contact
        print
        print
    def testRealSheets(self):
        ip = IntelliParser()
        
        ip.parse_excel('/Users/apple/Documents/DFC-website/DFC-website/DFC/intelliparser/samples/DFCNanjingContacts.xls')
        contacts = ip.extract_contacts()
        for contact in contacts:
            print contact
        print
        print
        
        ip.parse_excel('/Users/apple/Documents/DFC-website/DFC-website/DFC/intelliparser/samples/MingzhiBookHouse.xlsx')
        contacts = ip.extract_contacts()
        for contact in contacts:
            print contact
        print
        print
        
        ip.parse_excel('/Users/apple/Documents/DFC-website/DFC-website/DFC/intelliparser/samples/volstartupsummit.xlsx')
        contacts = ip.extract_contacts()
        for contact in contacts:
            print contact
        print
        print