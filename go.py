from urllib.request import urlopen
import datetime
import requests
import sched
import time
import json
import ast

requests.packages.urllib3.disable_warnings()
checkCode = ''
newx = ''
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
    'txtIdno': 'F222887581',
    'ddlBirthYear': '1962',
    'ddlBirthMonth': '12',
    'ddlBirthDay': '02',
    'txtVerifyCode': '2XZ1B5',
    'btnOK': '處理中..'
}

f = open('newxQuery.txt', 'r')
newxQuery = f.read()
newxQuery = json.loads(newxQuery)

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
    newxQuery.update(fixNewxQuery)
    r = requests.post(url, headers=newXHeader, params=_param, data = newxQuery, verify=False)
    firstPosition = r.text.index('RegistForm.aspx?newx') + 21
    lastPoisition = r.text.index('" id', firstPosition)
    newx = r.text[firstPosition:lastPoisition]   
    register()

def register() :
    url = "https://reg.ntuh.gov.tw/webadministration/RegistForm.aspx"
    _param = {
        'newx': newx
    }
    registerQuery['__VIEWSTATE'] = '/wEPDwUKLTg5ODA5MjQ5OA9kFgICAg9kFgICAQ9kFgoCBw9kFgICAw9kFgpmD2QWAgIBD2QWAgIBDw8WAh4EVGV4dAUYMTA5LjkuMiDmmJ/mnJ/kuIkg5LiK5Y2IZGQCAQ9kFgICAQ9kFgICAQ8PFgIfAAUJ5aSW56eR6YOoZGQCAg9kFgICAQ9kFgICAQ8PFgIfAAUp5pmu6YCa6ZaA6Ki6IOesrDA56Ki6ICjku6PnorzvvJogMTAzMjA5IClkZAIDD2QWAgIBD2QWAgIBDw8WAh8ABRHpmbPnn7PmsaAgIOmGq+W4q2RkAgQPZBYCAgEPZBYCAgEPDxYCHwAFFee4vemZouWNgC3opb/lnYAtMeaok2RkAgkPZBYCAgUPZBYKZg9kFgRmD2QWAgIDDxBkZBYBAgFkAgEPZBYGAgEPDxYCHwBlZGQCAw8PFgIeB1Zpc2libGVnZGQCBQ8PFgIfAGVkZAIBD2QWAgIBD2QWBgIBDxBkEBWYAQnoq4vpgbjmk4cG5YmNIDQyBuWJjSA0MQbliY0gNDAG5YmNIDM5BuWJjSAzOAbliY0gMzcG5YmNIDM2BuWJjSAzNQbliY0gMzQG5YmNIDMzBuWJjSAzMgbliY0gMzEG5YmNIDMwBuWJjSAyOQbliY0gMjgG5YmNIDI3BuWJjSAyNgbliY0gMjUG5YmNIDI0BuWJjSAyMwbliY0gMjIG5YmNIDIxBuWJjSAyMAbliY0gMTkG5YmNIDE4BuWJjSAxNwbliY0gMTYG5YmNIDE1BuWJjSAxNAbliY0gMTMG5YmNIDEyBuWJjSAxMQbliY0gMTAF5YmNIDkF5YmNIDgF5YmNIDcF5YmNIDYF5YmNIDUF5YmNIDQF5YmNIDMF5YmNIDIF5YmNIDEBMQEyATMBNAE1ATYBNwE4ATkCMTACMTECMTICMTMCMTQCMTUCMTYCMTcCMTgCMTkCMjACMjECMjICMjMCMjQCMjUCMjYCMjcCMjgCMjkCMzACMzECMzICMzMCMzQCMzUCMzYCMzcCMzgCMzkCNDACNDECNDICNDMCNDQCNDUCNDYCNDcCNDgCNDkCNTACNTECNTICNTMCNTQCNTUCNTYCNTcCNTgCNTkCNjACNjECNjICNjMCNjQCNjUCNjYCNjcCNjgCNjkCNzACNzECNzICNzMCNzQCNzUCNzYCNzcCNzgCNzkCODACODECODICODMCODQCODUCODYCODcCODgCODkCOTACOTECOTICOTMCOTQCOTUCOTYCOTcCOTgCOTkDMTAwAzEwMQMxMDIDMTAzAzEwNAMxMDUDMTA2AzEwNwMxMDgDMTA5FZgBAAQxODcwBDE4NzEEMTg3MgQxODczBDE4NzQEMTg3NQQxODc2BDE4NzcEMTg3OAQxODc5BDE4ODAEMTg4MQQxODgyBDE4ODMEMTg4NAQxODg1BDE4ODYEMTg4NwQxODg4BDE4ODkEMTg5MAQxODkxBDE4OTIEMTg5MwQxODk0BDE4OTUEMTg5NgQxODk3BDE4OTgEMTg5OQQxOTAwBDE5MDEEMTkwMgQxOTAzBDE5MDQEMTkwNQQxOTA2BDE5MDcEMTkwOAQxOTA5BDE5MTAEMTkxMQQxOTEyBDE5MTMEMTkxNAQxOTE1BDE5MTYEMTkxNwQxOTE4BDE5MTkEMTkyMAQxOTIxBDE5MjIEMTkyMwQxOTI0BDE5MjUEMTkyNgQxOTI3BDE5MjgEMTkyOQQxOTMwBDE5MzEEMTkzMgQxOTMzBDE5MzQEMTkzNQQxOTM2BDE5MzcEMTkzOAQxOTM5BDE5NDAEMTk0MQQxOTQyBDE5NDMEMTk0NAQxOTQ1BDE5NDYEMTk0NwQxOTQ4BDE5NDkEMTk1MAQxOTUxBDE5NTIEMTk1MwQxOTU0BDE5NTUEMTk1NgQxOTU3BDE5NTgEMTk1OQQxOTYwBDE5NjEEMTk2MgQxOTYzBDE5NjQEMTk2NQQxOTY2BDE5NjcEMTk2OAQxOTY5BDE5NzAEMTk3MQQxOTcyBDE5NzMEMTk3NAQxOTc1BDE5NzYEMTk3NwQxOTc4BDE5NzkEMTk4MAQxOTgxBDE5ODIEMTk4MwQxOTg0BDE5ODUEMTk4NgQxOTg3BDE5ODgEMTk4OQQxOTkwBDE5OTEEMTk5MgQxOTkzBDE5OTQEMTk5NQQxOTk2BDE5OTcEMTk5OAQxOTk5BDIwMDAEMjAwMQQyMDAyBDIwMDMEMjAwNAQyMDA1BDIwMDYEMjAwNwQyMDA4BDIwMDkEMjAxMAQyMDExBDIwMTIEMjAxMwQyMDE0BDIwMTUEMjAxNgQyMDE3BDIwMTgEMjAxOQQyMDIwFCsDmAFnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAl1kAgMPEGQQFQ0J6KuL6YG45pOHAjAxAjAyAjAzAjA0AjA1AjA2AjA3AjA4AjA5AjEwAjExAjEyFQ0AAjAxAjAyAjAzAjA0AjA1AjA2AjA3AjA4AjA5AjEwAjExAjEyFCsDDWdnZ2dnZ2dnZ2dnZ2cWAQIMZAIFDxBkEBUgCeiri+mBuOaThwIwMQIwMgIwMwIwNAIwNQIwNgIwNwIwOAIwOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNQIyNgIyNwIyOAIyOQIzMAIzMRUgAAIwMQIwMgIwMwIwNAIwNQIwNgIwNwIwOAIwOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNQIyNgIyNwIyOAIyOQIzMAIzMRQrAyBnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAgIPZBYEZg9kFgYCAw8PFgIeCEltYWdlVXJsBVxWYWxpZE51bWJlci5hc3B4P2NoZWNrQ29kZT1ZUUJ4QUdJQVZnQnRBRTBBVGdCaEFGRUFSd0JRQUU0QVJBQXZBSG9BTXdCYUFFa0Fid0JpQUZJQVp3QTlBRDBBMGRkAgcPDxYCHwAFBjJYWjFCNWRkAgkPDxYCHwAFAVlkZAIBD2QWAgIBDw9kFgIeCW9ua2V5ZG93bgUXZm5UcmFwS0QoYnRuT0ssIGV2ZW50KTtkAgMPZBYCZg9kFgICAw8PFgQeBF8hU0ICCB4JQmFja0NvbG9yCp4BZGQCBA9kFgJmD2QWAgIBD2QWAgIHDxBkZBYBZmQCCw8PFgIfAWhkFgICAQ9kFgQCAg9kFgICAw9kFgICAQ8QZGQWAWZkAgQPZBYCAgEPZBYYAgEPEGRkFgBkAgMPEGRkFgBkAgUPZBYCAgEPZBYGAgMPEGRkFgFmZAIFDxBkZBYBZmQCCw8PFgIfAGVkZAIJD2QWAgIBD2QWBgIDDxBkZBYBZmQCBQ8QZGQWAWZkAgsPDxYCHwBlZGQCEQ8QZGQWAGQCEw8QZGQWAGQCGw8QZGQWAGQCIw9kFgICAQ9kFgYCAw8QZGQWAWZkAgUPEGRkFgFmZAILDw8WAh8AZWRkAiUPZBYMZg9kFgICAQ9kFgICAQ8QZGQWAGQCAQ9kFgICAQ9kFgICAQ8QZGQWAGQCAg9kFgICAQ9kFgICAQ8QZGQWAGQCAw9kFgICAQ9kFgICAQ8QZGQWAGQCBA9kFgICAQ9kFgICAQ8QZGQWAGQCBQ9kFgICAQ9kFgICAQ8QZGQWAGQCJw9kFgICBA9kFgICAQ9kFgICAQ8QZGQWAGQCKQ9kFgQCBQ9kFgICAQ9kFgICAQ8QZGQWAGQCBg9kFgICAQ9kFgICAQ8QZGQWAGQCNQ8PFgIfAAUdMTA55bm0OeaciDLml6XkuIrljYgg56ysMDnoqLpkZAINDw8WAh8BaGRkAg8PDxYCHwFoZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFC2J0blJlTmV3TnVtxsH3w/w+7UMQ66FSawPvHc5sMC0='
    requests.post(url, headers=newXHeader, params=_param, data = registerQuery, verify=False)
    print('Done')


# def picToText():
#     img = Image.open('ValidNumber.gif')
#     img = img.convert("L")
#     img.save("test1.jpg")
#     text = pytesseract.image_to_string(img, lang='eng')
#     print(text)


# def getValiPic():
#     url = "https://reg.ntuh.gov.tw/WebAdministration/ValidNumber.aspx"
#     query = {
#         'checkCode': checkCode
#     }
#     r = requests.get(url, headers=checkCodeHeader, params=query ,verify=False)
#     img = Image.open(BytesIO(r.content))
#     if img.mode == "P":
#         img = img.convert('RGB')
#     img = img.crop((0, 0, 120, 45))
#     text = pytesseract.image_to_string(img, lang='eng')
#     print(text.strip())



getNewX()

f.close()