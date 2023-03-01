import re
import html
from urllib import parse
import requests

GOOGLE_TRANSLATE_URL = 'http://translate.google.com/m?q=%s&tl=%s&sl=%s'

def translate(text, to_language="auto", text_language="auto"):

    text = parse.quote(text)
    url = GOOGLE_TRANSLATE_URL % (text,to_language,text_language)
    response = requests.get(url)
    data = response.text
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr, data)
    if (len(result) == 0):
        return ""

    return html.unescape(result[0])

# vowels = ['e', 'a', 'u', 'o', 'i']

# print(sorted(vowels))


a= ['F:\\Downloads\\microsoft-azure-database-and-analytics\\05 -  Azure SQL Data Warehouse\\003 Module Introduction_cn.srt', 'F:\\Downloads\\microsoft-azure-database-and-analytics\\05 -  Azure SQL Data Warehouse\\006 Introduction_cn.srt', 'F:\\Downloads\\microsoft-azure-database-and-analytics\\05 -  Azure SQL Data Warehouse\\007 Why warehousing in cloud_cn.srt', 'F:\\Downloads\\microsoft-azure-database-and-analytics\\05 -  Azure SQL Data Warehouse\\008 Traditional vs Modern Warehouse architecture_cn.srt', 'F:\\Downloads\\microsoft-azure-database-and-analytics\\05 -  Azure SQL Data Warehouse\\009 What is Synapse Analytics Service_cn.srt', 'F:\\Downloads\\microsoft-azure-database-and-analytics\\05 -  Azure SQL Data Warehouse\\010 Demo Create Dedicated SQL Pool_cn.srt', 'F:\\Downloads\\microsoft-azure-database-and-analytics\\05 -  Azure SQL Data Warehouse\\032 Demo - Analyse data distribution before migration to azure_cn.srt']


b = [i.replace('_cn','_en') for i in a]
print(b)

    