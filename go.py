from IPython.display import display, clear_output
from urllib.request import urlopen
import pandas as pd
import datetime
import requests
import sched
import time
import json
from PIL import Image
import pytesseract
from io import BytesIO

requests.packages.urllib3.disable_warnings()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
checkCode = ''

checkCodeHeader = {
    'Host': 'reg.ntuh.gov.tw',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://reg.ntuh.gov.tw',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://reg.ntuh.gov.tw/WebAdministration/Query.aspx',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': '__utma=218787014.1820628005.1597902821.1597902821.1597902821.1; __utmc=218787014; __utmz=218787014.1597902821.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ASP.NET_SessionId=ynohny55hvnbiq45qiklgn45'
}


def getCheckCode():
    global checkCode
    url = "https://reg.ntuh.gov.tw/WebAdministration/Query.aspx"
    r = requests.get(url, headers=checkCodeHeader, verify=False)
    firstPosition = r.text.index('checkCode') + 10
    lastPoisition = r.text.index('alt', firstPosition) - 2
    checkCode = r.text[firstPosition:lastPoisition]


def picToText():
    img = Image.open('ValidNumber.gif')
    img = img.convert("L")
    img.save("test1.jpg")
    text = pytesseract.image_to_string(img, lang='eng')
    print(text)


def getValiPic():
    url = "https://reg.ntuh.gov.tw/WebAdministration/ValidNumber.aspx"
    query = {
        'checkCode': checkCode
    }
    r = requests.get(url, headers=checkCodeHeader, params=query ,verify=False)
    img = Image.open(BytesIO(r.content))
    if img.mode == "P":
        img = img.convert('RGB')
    img = img.crop((0, 0, 120, 45))
    text = pytesseract.image_to_string(img, lang='eng')
    print(text.strip())

def order():


getCheckCode()
getValiPic()
# picToText()
