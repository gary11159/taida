from urllib.request import urlopen
import datetime
import requests
import sched
import time
import json
import ast
from PIL import Image
import pytesseract
from io import BytesIO
import re
from bs4 import BeautifulSoup
import base64
import threading

requests.packages.urllib3.disable_warnings()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

newx = ''
valiNum = ''
viewState = ''

newXHeader = { 
    'Host': 'reg.ntuh.gov.tw',
    'Origin': 'https://reg.ntuh.gov.tw',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive'
}

serviceQuery = {
    'ServiceIDSE': '4309855'
}

fixNewxQuery = {}

registerQuery = {
    'scrollLeft': '0',
    'scrollTop': '0',
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATEGENERATOR': 'A291BFFA',
    'radInputNum': '1',
    'txtIdno': 'F129328672',
    'ddlBirthYear': '1995',
    'ddlBirthMonth': '11',
    'ddlBirthDay': '15',
    'txtVerifyCode': '',
    'btnOK': '處理中..'
}

def getNewX():
    global newx
    url = "https://reg.ntuh.gov.tw/webadministration/ClinicListUnderSpecificTemplateIDSE.aspx"
    r = requests.post(url, headers=newXHeader, params=serviceQuery, data = fixNewxQuery, verify=False)
    firstPosition = r.text.index('RegistForm.aspx?newx') + 21
    lastPoisition = r.text.index('" id', firstPosition)
    newx = r.text[firstPosition:lastPoisition]   

# 掛號
def register() :
    url = "https://reg.ntuh.gov.tw/webadministration/RegistForm.aspx"
    _param = {
        'newx': newx
    }
    registerQuery['txtVerifyCode'] = valiNum
    registerQuery['__VIEWSTATE'] = viewState
    r = requests.post(url, headers=newXHeader, params=_param, data = registerQuery, verify=False)

# 獲取醫生底下資訊
def getNewxHeader(session):
    url = 'https://reg.ntuh.gov.tw/webadministration/ClinicListUnderSpecificTemplateIDSE.aspx'
    r = requests.post(url, headers=newXHeader, params=serviceQuery, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    buildFixNewQuery(soup, session)

# 建置fixNewQuery資料
def buildFixNewQuery(soup, session):
    # 掛第幾場次
    fixNewxQuery.update({
        '__EVENTTARGET': 'DoctorServiceListInSeveralDaysTemplateIDSE$GridViewDoctorServiceList$_ctl' + str(session) + '$AdminTextShow',
        '__EVENTARGUMENT': '',
    })

    # VIEWSTATE
    _viewstate = soup.find("input", id="__VIEWSTATE") # 這是蒐集資料的viewstate
    fixNewxQuery.update({
        '__VIEWSTATE': _viewstate.get('value')
    })
    
    # VIEWSTATEGENERATOR
    generator = soup.find_all("input", id="__VIEWSTATEGENERATOR")
    fixNewxQuery.update({
        '__VIEWSTATEGENERATOR': generator[0].get('value')
    })

    # 科別
    dept = soup.find_all("input", {"type":"hidden", "id": re.compile('Hidden')})
    for item in dept:
        fixNewxQuery.update({
            item.get('id'): item.get('value')
        })

    # 場次資料
    data = soup.find_all("input", id=re.compile("DoctorServiceListInSeveralDaysTemplateIDSE_GridViewDoctorServiceList__"))
    for item in data :
        fixNewxQuery.update({
            item.get('name'): item.get('value')
        })

# 獲取viewState
def getViewState():
    global viewState
    global valiNum
    url = 'https://reg.ntuh.gov.tw/webadministration/RegistForm.aspx'
    _param = {
        'newx': newx
    }
    r = requests.get(url, headers=newXHeader, params=_param, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    firstViewState = soup.find("input", id="__VIEWSTATE").get('value')
    registerQuery.update({
        '__VIEWSTATE': firstViewState,
        '__EVENTTARGET': 'radInputNum$1'
    })

    r = requests.post(url, headers=newXHeader, params=_param, data=registerQuery, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    firstViewState = soup.find("input", id="__VIEWSTATE").get('value')
    registerQuery.update({
        '__VIEWSTATE': firstViewState,
        '__EVENTTARGET': 'ddlBirthMonth'
    })
    r = requests.post(url, headers=newXHeader, params=_param, data=registerQuery, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    viewState = soup.find("input", id="__VIEWSTATE").get('value')
    valiNum = str(base64.b64decode(viewState))
    first = valiNum.index('\\x02\\x07\\x0f\\x0f\\x16\\x02\\x1f\\x00\\x05\\x06') + 40
    valiNum = valiNum[first:first+6]

# 先取得viewState
def collectData():
    print("蒐集資料中...")
    # 場次
    session = 2
    getNewxHeader(session)
    getNewX()
    getViewState()

if __name__ == "__main__":
    # 搜尋資料
    collectData()
    input('已準備好資料，Enter後自動掛號')
    # 建立 10 個子執行緒
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target = register))
        threads[i].start()
    # 等待所有子執行緒結束
    for i in range(10):
        threads[i].join()