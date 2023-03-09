#coding:utf-8
import requests

headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G955N Build/NRD90M.G955NKSU1AQDC)',
    'Host': 'res.o2nails.com',
    'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
}

response = requests.get('https://res.o2nails.com/resources/OPens/pens/B03_7.png', headers=headers, verify=False)
print(response.text)