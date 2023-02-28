#coding:utf-8

import os
import re
import urllib.request
import urllib.parse
import json
import time
import html
from urllib import parse
import requests
import time
import random

def parse_srt_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    
    # 将字幕按时间码和文本内容分割
    sections = re.split(r'\n\s*\n', data)
    subtitles = []
    for section in sections:
        # 获取时间码和文本内容
        match = re.match(r'(\d+)\n(\d+:\d+:\d+,\d+)\s*-->\s*(\d+:\d+:\d+,\d+)\s*\n(.*)', section, re.DOTALL)
        if match:
            subtitle = {
                'index': int(match.group(1)),
                'start_time': match.group(2),
                'end_time': match.group(3),
                'text': match.group(4).strip(),
            }
            subtitles.append(subtitle)
    
    return subtitles

def translation_youdao(content):
            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
            data={}
            data['i']= content
            data['from']= 'AUTO'
            data['to']='AUTO'
            data['smartresult'] ='dict'
            data['client']= 'fanyideskweb'
            data['salt']= '16216671697475'
            data['sign']= '4b12fe85554d481a2d40331d2b07847f'
            data['ts']= '1621667169747'
            data['bv']= 'cda1e53e0c0eb8dd4002cefc117fa588'
            data['doctype']= 'json'
            data['version']= '2.1'
            data['keyfrom']= 'fanyi.web'
            data['action']= 'FY_BY_REALTlME'
            data = urllib.parse.urlencode(data).encode('utf-8')#data信息要和发送的信息格式一致
            response = urllib.request.urlopen(url,data)
            html = response.read().decode('utf-8')
            target =json.loads(html)
            return target



def translate_google(text, to_language="auto", text_language="auto"):
    GOOGLE_TRANSLATE_URL = 'http://translate.google.com/m?q=%s&tl=%s&sl=%s'
    text = parse.quote(text)
    url = GOOGLE_TRANSLATE_URL % (text,to_language,text_language)
    response = requests.get(url)
    data = response.text
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr, data)
    if (len(result) == 0):
        return ""
    return html.unescape(result[0])


def translate_subtitles_yd(subtitles):   
    for subtitle in subtitles:
        text = subtitle['text']
        trans = translation_youdao(text).get("translateResult",[])[0][0].get('tgt','')
        print(trans)
        subtitle['translation'] =trans
    return subtitles

def translate_subtitles_gl(subtitles):   
    for subtitle in subtitles:
        
        text = subtitle['text']
        print(text)
        # trans =translate_google(text, "zh-CN","en")
        # print(trans)
        # subtitle['translation'] =trans
        # rdt = random.randint(0,1)
        # if rdt==0:
        #     rdt= 0.5
        # time.sleep(rdt)


    return subtitles

def write_srt_file(subtitles, filename):
    with open(filename, 'w',encoding='utf-8') as f:
        for subtitle in subtitles:
            f.write(f"{subtitle['index']}\n")
            f.write(f"{subtitle['start_time']} --> {subtitle['end_time']}\n")
            f.write(f"{subtitle['text']}\n") ##enlish
            f.write(f"{subtitle['translation']}\n\n") ##chinese


def read_srt_files(folder):
    srt_files = glob.glob(os.path.join(folder, '*.srt'))
    subtitles = []

    for file in srt_files:
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()

        sections = data.split('\n\n')

        for section in sections:
            lines = section.strip().split('\n')

            index = int(lines[0])
            start_time, end_time = lines[1].split(' --> ')
            text = '\n'.join(lines[2:])

            subtitles.append({
                'file': file,
                'index': index,
                'start_time': start_time,
                'end_time': end_time,
                'text': text,
            })

    return subtitles





if __name__ == '__main__':
    # 读取srt文件

    # folder_path = r"F:\Downloads\microsoft-azure-database-and-analytics\05 -  Azure SQL Data Warehouse"
    folder_path = r"F:\Downloads\microsoft-azure-database-and-analytics\04 -   Azure SQL Database"

    srt_files_en = [os.path.join(root, file) 
                for root, dirs, files in os.walk(folder_path) 
                for file in files 
                if file.endswith('_en.srt')]

    srt_files_cn = [os.path.join(root, file) 
                for root, dirs, files in os.walk(folder_path) 
                for file in files 
                if file.endswith('_cn.srt')]

    fail_files =[]

    left_join = sorted(set(srt_files_en)-set(srt_files_cn))

    for i in left_join:
        try:
            print(i)
            subtitles = parse_srt_file(i)
            # # # 翻译英文字幕
            subtitles = translate_subtitles_gl(subtitles)
            # ##写入中英双语字幕
            # write_srt_file(subtitles, i.replace("_en","_cn"))
        except:
            print("翻译失败")
            fail_files.append(i)

