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
        print ip.extract_contacts()
        print
    def testExtractContactsVertical(self):
        ip = IntelliParser()
        ip.parse_excel('/Users/apple/Documents/DFC-website/DFC-website/DFC/intelliparser/samples/2012MSTCMediaVertical.xls')
        print ip.extract_contacts()
        print