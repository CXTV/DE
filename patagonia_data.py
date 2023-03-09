
import requests

cookies = {
    'secure_customer_sig': '',
    'localization': 'NZ',
    '_cmp_a': '%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22merchant_geo%22%3A%22AU%22%2C%22sale_of_data_region%22%3Afalse%7D',
    '_orig_referrer': 'https%3A%2F%2Fwww.google.com%2F',
    '_landing_page': '%2F%3Fgclid%3DCj0KCQiApKagBhC1ARIsAFc7Mc7P55ErWgryuLCH6qdckAtwUCOElSsmmrrzP4_SV-5hDO_WrV3AGPgaArKgEALw_wcB',
    '_y': 'f2579630-1e78-48eb-aaa4-f03191905cac',
    '_s': 'fc445291-f7fd-44c2-bead-7897c3f34f8c',
    '_shopify_y': 'f2579630-1e78-48eb-aaa4-f03191905cac',
    '_shopify_s': 'fc445291-f7fd-44c2-bead-7897c3f34f8c',
    '_shopify_sa_p': 'gclid%3DCj0KCQiApKagBhC1ARIsAFc7Mc7P55ErWgryuLCH6qdckAtwUCOElSsmmrrzP4_SV-5hDO_WrV3AGPgaArKgEALw_wcB',
    '_fbp': 'fb.2.1678351077316.958598178',
    '_schn': '_bj549o',
    '_scid': 'c84d472b-13f9-49b4-92a6-7aaf9de7aaad',
    '_sp_ses.ff1f': '*',
    '_gid': 'GA1.3.1850278127.1678351078',
    '_gac_UA-151822859-1': '1.1678351078.Cj0KCQiApKagBhC1ARIsAFc7Mc7P55ErWgryuLCH6qdckAtwUCOElSsmmrrzP4_SV-5hDO_WrV3AGPgaArKgEALw_wcB',
    '_gcl_aw': 'GCL.1678351078.Cj0KCQiApKagBhC1ARIsAFc7Mc7P55ErWgryuLCH6qdckAtwUCOElSsmmrrzP4_SV-5hDO_WrV3AGPgaArKgEALw_wcB',
    '_gcl_au': '1.1.12712765.1678351078',
    '_omappvp': 'oQCSWBFMWeHNSVfMhb6hgfVLKzR4c1WMhV09sWbzR9itMPDFHQTfIJAHg1MRMCcjChxcCvdri8XYs5uL0A3M7K0YdHm2OsTC',
    '_clck': 'ebmmga|1|f9r|0',
    'nostojs': 'autoload',
    '2c.cId': '64099adb7b275a53684ae892',
    '_sctr': '1|1678273200000',
    '__zlcmid': '1EnlepX6RyCVzhX',
    '_shopify_sa_t': '2023-03-09T08%3A43%3A06.102Z',
    '_omappvs': '1678351386119',
    '_ga': 'GA1.1.900382987.1678351078',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2NzgzNTEwNzgsInZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cucGF0YWdvbmlhLmNvLm56Lz9nY2xpZD1DajBLQ1FpQXBLYWdCaEMxQVJJc0FGYzdNYzdQNTVFcldncnl1TENINnFkY2tBdHdVQ09FbFNzbW1ycnpQNF9TVi01aERPX1dyVjNBR1BnYUFyS2dFQUx3X3djQiJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY3ODM1MTM4NiwidmFsdWUiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5wYXRhZ29uaWEuY28ubnovP2djbGlkPUNqMEtDUWlBcEthZ0JoQzFBUklzQUZjN01jN1A1NUVyV2dyeXVMQ0g2cWRja0F0d1VDT0VsU3NtbXJyelA0X1NWLTVoRE9fV3JWM0FHUGdhQXJLZ0VBTHdfd2NCIn19',
    '_ga_7CQ74E75GC': 'GS1.1.1678351077.1.1.1678351386.59.0.0',
    '_clsk': '10qyrit|1678351386960|20|1|v.clarity.ms/collect',
    'recently_viewed': '6703711846469%2C6815789776965%2C6815774048325%2C4345481560133%2C6629233852485',
    'keep_alive': 'c49ff054-0b2b-4647-bf75-4cb99e99190f',
    '_sp_id.ff1f': 'c6b15dc807b53a69.1678351077.1.1678351396.1678351077',
}

headers = {
    'authority': 'www.patagonia.co.nz',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'secure_customer_sig=; localization=NZ; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22merchant_geo%22%3A%22AU%22%2C%22sale_of_data_region%22%3Afalse%7D; _orig_referrer=https%3A%2F%2Fwww.google.com%2F; _landing_page=%2F%3Fgclid%3DCj0KCQiApKagBhC1ARIsAFc7Mc7P55ErWgryuLCH6qdckAtwUCOElSsmmrrzP4_SV-5hDO_WrV3AGPgaArKgEALw_wcB; _y=f2579630-1e78-48eb-aaa4-f03191905cac; _s=fc445291-f7fd-44c2-bead-7897c3f34f8c; _shopify_y=f2579630-1e78-48eb-aaa4-f03191905cac; _shopify_s=fc445291-f7fd-44c2-bead-7897c3f34f8c; _shopify_sa_p=gclid%3DCj0KCQiApKagBhC1ARIsAFc7Mc7P55ErWgryuLCH6qdckAtwUCOElSsmmrrzP4_SV-5hDO_WrV3AGPgaArKgEALw_wcB; _fbp=fb.2.1678351077316.958598178; _schn=_bj549o; _scid=c84d472b-13f9-49b4-92a6-7aaf9de7aaad; _sp_ses.ff1f=*; _gid=GA1.3.1850278127.1678351078; _gac_UA-151822859-1=1.1678351078.Cj0KCQiApKagBhC1ARIsAFc7Mc7P55ErWgryuLCH6qdckAtwUCOElSsmmrrzP4_SV-5hDO_WrV3AGPgaArKgEALw_wcB; _gcl_aw=GCL.1678351078.Cj0KCQiApKagBhC1ARIsAFc7Mc7P55ErWgryuLCH6qdckAtwUCOElSsmmrrzP4_SV-5hDO_WrV3AGPgaArKgEALw_wcB; _gcl_au=1.1.12712765.1678351078; _omappvp=oQCSWBFMWeHNSVfMhb6hgfVLKzR4c1WMhV09sWbzR9itMPDFHQTfIJAHg1MRMCcjChxcCvdri8XYs5uL0A3M7K0YdHm2OsTC; _clck=ebmmga|1|f9r|0; nostojs=autoload; 2c.cId=64099adb7b275a53684ae892; _sctr=1|1678273200000; __zlcmid=1EnlepX6RyCVzhX; _shopify_sa_t=2023-03-09T08%3A43%3A06.102Z; _omappvs=1678351386119; _ga=GA1.1.900382987.1678351078; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2NzgzNTEwNzgsInZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cucGF0YWdvbmlhLmNvLm56Lz9nY2xpZD1DajBLQ1FpQXBLYWdCaEMxQVJJc0FGYzdNYzdQNTVFcldncnl1TENINnFkY2tBdHdVQ09FbFNzbW1ycnpQNF9TVi01aERPX1dyVjNBR1BnYUFyS2dFQUx3X3djQiJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY3ODM1MTM4NiwidmFsdWUiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5wYXRhZ29uaWEuY28ubnovP2djbGlkPUNqMEtDUWlBcEthZ0JoQzFBUklzQUZjN01jN1A1NUVyV2dyeXVMQ0g2cWRja0F0d1VDT0VsU3NtbXJyelA0X1NWLTVoRE9fV3JWM0FHUGdhQXJLZ0VBTHdfd2NCIn19; _ga_7CQ74E75GC=GS1.1.1678351077.1.1.1678351386.59.0.0; _clsk=10qyrit|1678351386960|20|1|v.clarity.ms/collect; recently_viewed=6703711846469%2C6815789776965%2C6815774048325%2C4345481560133%2C6629233852485; keep_alive=c49ff054-0b2b-4647-bf75-4cb99e99190f; _sp_id.ff1f=c6b15dc807b53a69.1678351077.1.1678351396.1678351077',
    'if-none-match': 'cacheable:e6b4417d2aacbc14235eb60b225b14dd',
    'referer': 'https://www.patagonia.co.nz/collections/mens',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

params = {
    'nosto_source': 'cmp',
    'nosto': '1347401254',
}

response = requests.get(
    'https://www.patagonia.co.nz/products/mens-calcite-jacket-84986-brlg',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)