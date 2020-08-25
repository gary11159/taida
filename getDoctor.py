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
    "__EVENTTARGET": "ClinicListInEightDaysForSpecificDeptMain$ClinicListInSpecificAM$GridViewSpecificAMPM$_ctl6$MainDoctorTwo",
    "__EVENTARGUMENT": "",
    "__LASTFOCUS": "",
    "__VIEWSTATEGENERATOR": "ADFD2531",
    "DropDownDept": "",
}

_param = {
    'x': 'RABlAHAAdAA9AEQARQBOAFQAJgBIAG8AcwBwAD0AVAAwACYAUwB1AGIARABlAHAAdABDAG8AZABlAD0AJgBpAHMAUwB1AGIARABlAHAAdAA9AE4AJgB3AGUAZQBrAD0AMQAmAFMAbwByAHQAPQA1'
}

f = open('doctorViewState.txt', 'r')
newxQuery = f.read()
newxQuery = json.loads(newxQuery)
serviceQuery.update(newxQuery)

f1 = open('牙科.txt', 'w')

def getService(doctor):
    final = {}
    # for i in range(len(doctor)):
    #     if( doctor[0].getText() != '郭炳宏'):
    #         doctor.pop(0)
    #     else:
    #         break
    for item in doctor:
        try:
            if(len(item.getText()) > 3 ): continue 
            serviceQuery.update({
                "__EVENTTARGET": item.get('id').replace("_", "$").replace("$ctl", "_ctl")
            })
            url = 'https://reg.ntuh.gov.tw/webadministration/NewDoctorTableForSpecificDept.aspx'
            r = requests.post(url, headers=newXHeader, params=_param, data=serviceQuery,verify=False)
            firstPosition = r.text.index('ServiceIDSE')
            if ( r.text[firstPosition+12:firstPosition+19] == '" id="f' ): continue
            final.update({
                item.getText(): r.text[firstPosition+12:firstPosition+19]
            })
            print(r.text[firstPosition+12:firstPosition+19])
            f1.write( "\"" + item.getText() + '": "' + r.text[firstPosition+12:firstPosition+19] + '"\n') 
        except:
            print('出點問題繼續')
    print(final)

def getAllDoctor():
    url = 'https://reg.ntuh.gov.tw/webadministration/NewDoctorTableForSpecificDept.aspx'
    r = requests.get(url, headers=newXHeader, params=_param, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    temp = soup.find_all("a", id=re.compile('ClinicListInEightDaysForSpecificDeptMain_ClinicListInSpecificAM_GridViewSpecificAMPM__ctl'))
    doctor = []
    for item in temp:
        if( item.get('style') == 'text-decoration:none;' and item.get('onmouseout') == 'return cClick();'):
            doctor.append(item)
    getService(doctor)

if __name__ == "__main__":
    getAllDoctor()
    f.close()
    f1.close()