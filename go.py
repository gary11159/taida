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

requests.packages.urllib3.disable_warnings()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

checkCode = ''
newx = ''
valiNum = ''
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
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

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
    'ServiceIDSE': '4306633'
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

f = open('newxQuery.txt', 'r')
newxQuery = f.read()
newxQuery = json.loads(newxQuery)

def getValiPic():
    global valiNum
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
    valiNum = text.strip()
    print(valiNum)

def getCheckCode():
    global checkCode
    url = "https://reg.ntuh.gov.tw/WebAdministration/Query.aspx"
    r = requests.get(url, headers=checkCodeHeader, verify=False)
    firstPosition = r.text.index('checkCode') + 10
    lastPoisition = r.text.index('alt', firstPosition) - 2
    checkCode = r.text[firstPosition:lastPoisition]

def getNewX():
    global newx
    url = "https://reg.ntuh.gov.tw/webadministration/ClinicListUnderSpecificTemplateIDSE.aspx"
    fixNewxQuery.update(newxQuery)
    r = requests.post(url, headers=newXHeader, params=serviceQuery, data = fixNewxQuery, verify=False)
    firstPosition = r.text.index('RegistForm.aspx?newx') + 21
    lastPoisition = r.text.index('" id', firstPosition)
    newx = r.text[firstPosition:lastPoisition]   

# 掛號
def register(viewState, valiNum) :
    url = "https://reg.ntuh.gov.tw/webadministration/RegistForm.aspx"
    _param = {
        'newx': newx
    }
    registerQuery['txtVerifyCode'] = valiNum
    registerQuery['__VIEWSTATE'] = viewState
    r = requests.post(url, headers=newXHeader, params=_param, data = registerQuery, verify=False)

# 獲取醫生底下資訊
def getNewxHeader():
    url = 'https://reg.ntuh.gov.tw/webadministration/ClinicListUnderSpecificTemplateIDSE.aspx'
    r = requests.post(url, headers=newXHeader, params=serviceQuery, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    buildFixNewQuery(soup)

# 建置fixNewQuery資料
def buildFixNewQuery(soup):
    # 場次
    session = 3

    # 掛第幾場次
    fixNewxQuery.update({
        '__EVENTTARGET': 'DoctorServiceListInSeveralDaysTemplateIDSE$GridViewDoctorServiceList$_ctl' + str(session) + '$AdminTextShow',
        '__EVENTARGUMENT': '',
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
    register(viewState, valiNum)


getNewxHeader()
getNewX()
getViewState()

f.close()