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

fixNewxQuery = {
    '__EVENTTARGET': 'DoctorServiceListInSeveralDaysTemplateIDSE$GridViewDoctorServiceList$_ctl3$AdminTextShow',
    '__EVENTARGUMENT': '',
    '__VIEWSTATEGENERATOR': '259B12C8',
    'HiddenDeptCode': 'SURG',
    'HiddenFieldHospCode': 'T0',
    'HiddenFieldSubDeptCode': '01',
    'HiddenFieldAMPM': '1',
    'DoctorServiceListInSeveralDaysTemplateIDSE:GridViewDoctorServiceList:_ctl2:HospitalCode': 'T0',
    'DoctorServiceListInSeveralDaysTemplateIDSE:GridViewDoctorServiceList:_ctl2:ServiceIDSE': '4308484',
    'DoctorServiceListInSeveralDaysTemplateIDSE:GridViewDoctorServiceList:_ctl2:ServiceEncryptCode': 'T0SURG0920200826',
    'DoctorServiceListInSeveralDaysTemplateIDSE:GridViewDoctorServiceList:_ctl2:FirstVisitQuotaFlag': 'n',
    'DoctorServiceListInSeveralDaysTemplateIDSE:GridViewDoctorServiceList:_ctl3:HospitalCode': 'T0',
    'DoctorServiceListInSeveralDaysTemplateIDSE:GridViewDoctorServiceList:_ctl3:ServiceIDSE': '4318153',
    'DoctorServiceListInSeveralDaysTemplateIDSE:GridViewDoctorServiceList:_ctl3:ServiceEncryptCode': 'T0SURG0920200902',
    'DoctorServiceListInSeveralDaysTemplateIDSE:GridViewDoctorServiceList:_ctl3:FirstVisitQuotaFlag': 'n'
}

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
    'txtVerifyCode': 'LF66JH',
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
    _param = {
        'ServiceIDSE': '4308484'
    }
    fixNewxQuery.update(newxQuery)
    r = requests.post(url, headers=newXHeader, params=_param, data = fixNewxQuery, verify=False)
    firstPosition = r.text.index('RegistForm.aspx?newx') + 21
    lastPoisition = r.text.index('" id', firstPosition)
    newx = r.text[firstPosition:lastPoisition]   
    register()

def register() :
    url = "https://reg.ntuh.gov.tw/webadministration/RegistForm.aspx"
    _param = {
        'newx': newx
    }
    registerQuery['txtVerifyCode'] = valiNum
    registerQuery['__VIEWSTATE'] = '/wEPDwUKLTg5ODA5MjQ5OA9kFgICAg9kFgICAQ9kFgoCBw9kFgICAw9kFgpmD2QWAgIBD2QWAgIBDw8WAh4EVGV4dAUYMTA5LjkuMiDmmJ/mnJ/kuIkg5LiK5Y2IZGQCAQ9kFgICAQ9kFgICAQ8PFgIfAAUJ5aSW56eR6YOoZGQCAg9kFgICAQ9kFgICAQ8PFgIfAAUp5pmu6YCa6ZaA6Ki6IOesrDA56Ki6ICjku6PnorzvvJogMTAzMjA5IClkZAIDD2QWAgIBD2QWAgIBDw8WAh8ABRHpmbPnn7PmsaAgIOmGq+W4q2RkAgQPZBYCAgEPZBYCAgEPDxYCHwAFFee4vemZouWNgC3opb/lnYAtMeaok2RkAgkPZBYCAgUPZBYKZg9kFgRmD2QWAgIDDxBkZBYBAgFkAgEPZBYGAgEPDxYCHwBlZGQCAw8PFgIeB1Zpc2libGVnZGQCBQ8PFgIfAGVkZAIBD2QWAgIBD2QWBgIBDxBkEBWYAQnoq4vpgbjmk4cG5YmNIDQyBuWJjSA0MQbliY0gNDAG5YmNIDM5BuWJjSAzOAbliY0gMzcG5YmNIDM2BuWJjSAzNQbliY0gMzQG5YmNIDMzBuWJjSAzMgbliY0gMzEG5YmNIDMwBuWJjSAyOQbliY0gMjgG5YmNIDI3BuWJjSAyNgbliY0gMjUG5YmNIDI0BuWJjSAyMwbliY0gMjIG5YmNIDIxBuWJjSAyMAbliY0gMTkG5YmNIDE4BuWJjSAxNwbliY0gMTYG5YmNIDE1BuWJjSAxNAbliY0gMTMG5YmNIDEyBuWJjSAxMQbliY0gMTAF5YmNIDkF5YmNIDgF5YmNIDcF5YmNIDYF5YmNIDUF5YmNIDQF5YmNIDMF5YmNIDIF5YmNIDEBMQEyATMBNAE1ATYBNwE4ATkCMTACMTECMTICMTMCMTQCMTUCMTYCMTcCMTgCMTkCMjACMjECMjICMjMCMjQCMjUCMjYCMjcCMjgCMjkCMzACMzECMzICMzMCMzQCMzUCMzYCMzcCMzgCMzkCNDACNDECNDICNDMCNDQCNDUCNDYCNDcCNDgCNDkCNTACNTECNTICNTMCNTQCNTUCNTYCNTcCNTgCNTkCNjACNjECNjICNjMCNjQCNjUCNjYCNjcCNjgCNjkCNzACNzECNzICNzMCNzQCNzUCNzYCNzcCNzgCNzkCODACODECODICODMCODQCODUCODYCODcCODgCODkCOTACOTECOTICOTMCOTQCOTUCOTYCOTcCOTgCOTkDMTAwAzEwMQMxMDIDMTAzAzEwNAMxMDUDMTA2AzEwNwMxMDgDMTA5FZgBAAQxODcwBDE4NzEEMTg3MgQxODczBDE4NzQEMTg3NQQxODc2BDE4NzcEMTg3OAQxODc5BDE4ODAEMTg4MQQxODgyBDE4ODMEMTg4NAQxODg1BDE4ODYEMTg4NwQxODg4BDE4ODkEMTg5MAQxODkxBDE4OTIEMTg5MwQxODk0BDE4OTUEMTg5NgQxODk3BDE4OTgEMTg5OQQxOTAwBDE5MDEEMTkwMgQxOTAzBDE5MDQEMTkwNQQxOTA2BDE5MDcEMTkwOAQxOTA5BDE5MTAEMTkxMQQxOTEyBDE5MTMEMTkxNAQxOTE1BDE5MTYEMTkxNwQxOTE4BDE5MTkEMTkyMAQxOTIxBDE5MjIEMTkyMwQxOTI0BDE5MjUEMTkyNgQxOTI3BDE5MjgEMTkyOQQxOTMwBDE5MzEEMTkzMgQxOTMzBDE5MzQEMTkzNQQxOTM2BDE5MzcEMTkzOAQxOTM5BDE5NDAEMTk0MQQxOTQyBDE5NDMEMTk0NAQxOTQ1BDE5NDYEMTk0NwQxOTQ4BDE5NDkEMTk1MAQxOTUxBDE5NTIEMTk1MwQxOTU0BDE5NTUEMTk1NgQxOTU3BDE5NTgEMTk1OQQxOTYwBDE5NjEEMTk2MgQxOTYzBDE5NjQEMTk2NQQxOTY2BDE5NjcEMTk2OAQxOTY5BDE5NzAEMTk3MQQxOTcyBDE5NzMEMTk3NAQxOTc1BDE5NzYEMTk3NwQxOTc4BDE5NzkEMTk4MAQxOTgxBDE5ODIEMTk4MwQxOTg0BDE5ODUEMTk4NgQxOTg3BDE5ODgEMTk4OQQxOTkwBDE5OTEEMTk5MgQxOTkzBDE5OTQEMTk5NQQxOTk2BDE5OTcEMTk5OAQxOTk5BDIwMDAEMjAwMQQyMDAyBDIwMDMEMjAwNAQyMDA1BDIwMDYEMjAwNwQyMDA4BDIwMDkEMjAxMAQyMDExBDIwMTIEMjAxMwQyMDE0BDIwMTUEMjAxNgQyMDE3BDIwMTgEMjAxOQQyMDIwFCsDmAFnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAn5kAgMPEGQQFQ0J6KuL6YG45pOHAjAxAjAyAjAzAjA0AjA1AjA2AjA3AjA4AjA5AjEwAjExAjEyFQ0AAjAxAjAyAjAzAjA0AjA1AjA2AjA3AjA4AjA5AjEwAjExAjEyFCsDDWdnZ2dnZ2dnZ2dnZ2cWAQILZAIFDxBkEBUfCeiri+mBuOaThwIwMQIwMgIwMwIwNAIwNQIwNgIwNwIwOAIwOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNQIyNgIyNwIyOAIyOQIzMBUfAAIwMQIwMgIwMwIwNAIwNQIwNgIwNwIwOAIwOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNQIyNgIyNwIyOAIyOQIzMBQrAx9nZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZGQCAg9kFgRmD2QWBgIDDw8WAh4ISW1hZ2VVcmwFXFZhbGlkTnVtYmVyLmFzcHg/Y2hlY2tDb2RlPVpnQkVBR3dBVWdCWUFGb0FhQUJCQUM4QU9BQTNBSGtBUXdBMEFIVUFVd0FyQUhZQWNnQjBBSFFBWndBOUFEMEEwZGQCBw8PFgIfAAUGTEY2NkpIZGQCCQ8PFgIfAAUBWWRkAgEPZBYCAgEPD2QWAh4Jb25rZXlkb3duBRdmblRyYXBLRChidG5PSywgZXZlbnQpO2QCAw9kFgJmD2QWAgIDDw8WBB4EXyFTQgIIHglCYWNrQ29sb3IKngFkZAIED2QWAmYPZBYCAgEPZBYCAgcPEGRkFgFmZAILDw8WAh8BaGQWAgIBD2QWBAICD2QWAgIDD2QWAgIBDxBkZBYBZmQCBA9kFgICAQ9kFhgCAQ8QZGQWAGQCAw8QZGQWAGQCBQ9kFgICAQ9kFgYCAw8QZGQWAWZkAgUPEGRkFgFmZAILDw8WAh8AZWRkAgkPZBYCAgEPZBYGAgMPEGRkFgFmZAIFDxBkZBYBZmQCCw8PFgIfAGVkZAIRDxBkZBYAZAITDxBkZBYAZAIbDxBkZBYAZAIjD2QWAgIBD2QWBgIDDxBkZBYBZmQCBQ8QZGQWAWZkAgsPDxYCHwBlZGQCJQ9kFgxmD2QWAgIBD2QWAgIBDxBkZBYAZAIBD2QWAgIBD2QWAgIBDxBkZBYAZAICD2QWAgIBD2QWAgIBDxBkZBYAZAIDD2QWAgIBD2QWAgIBDxBkZBYAZAIED2QWAgIBD2QWAgIBDxBkZBYAZAIFD2QWAgIBD2QWAgIBDxBkZBYAZAInD2QWAgIED2QWAgIBD2QWAgIBDxBkZBYAZAIpD2QWBAIFD2QWAgIBD2QWAgIBDxBkZBYAZAIGD2QWAgIBD2QWAgIBDxBkZBYAZAI1Dw8WAh8ABR0xMDnlubQ55pyIMuaXpeS4iuWNiCDnrKwwOeioumRkAg0PDxYCHwFoZGQCDw8PFgIfAWhkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQULYnRuUmVOZXdOdW31OAggNUP42gljHtQAeIVQzyHPbA=='
    r = requests.post(url, headers=newXHeader, params=_param, data = registerQuery, verify=False)

getCheckCode()
getValiPic()
getNewX()
f.close()