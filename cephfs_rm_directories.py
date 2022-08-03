#!/usr/bin/python
# coding=utf-8

import requests
from requests.packages import urllib3

session = requests.session()
cephUrlList = ["https://ceph-mon1:8443/", "https://ceph-data1:8443/", "https://ceph-data2:8443/"]
for cephUrl in cephUrlList:
    cephAuthApi = "%s%s" % (cephUrl, "api/auth")
    
    head = {
    "Host": cephUrl.split("/")[2],
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": cephUrl,
    "Content-Type": "application/json",
    # "Cookie": "token="
    }
    
    authInfo = {
        "username": "",
        "password": ""
    }
    
    session.headers = head
    
    # 关闭取消 ssl 认证警告
    urllib3.disable_warnings()
    
    # 取消 ssl 认证
    data = session.post(cephAuthApi, json=authInfo, verify=False)
    try:
        token = data.json()["token"] if data.status_code in [200, 201] else None
        print(token)
        session.headers.update({"Cookie": "token=%s" % token})
        break
    except:
        print("Access Url [%s] Failed, status code: %s" % (cephUrl, data.status_code))

"""
head = {
"Host": cephUrl.split("/")[2],
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
"Accept": "application/json, text/plain, */*",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding": "gzip, deflate, br",
"Connection": "keep-alive",
"Referer": cephUrl,
"Content-Type": "application/json",
"Cookie": "token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjZXBoLWRhc2hib2FyZCIsImp0aSI6ImU3MTEwMGQ3LTJkMTAtNGQ5YS1hMDFhLTZlNmZiYTdhNWMxZSIsImV4cCI6MTYzMTEyMjQ0NSwiaWF0IjoxNjMxMDkzNjQ1LCJ1c2VybmFtZSI6ImFkbWluIn0.mY-WXuZmxSuJrFSN-HTwY982heHCuSNQwaVtghNbmm8"
}
"""




