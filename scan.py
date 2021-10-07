import requests
import os
import sys
from lxml import etree
import datetime
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import coloar

headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}

list=['/1.zip','/admin','/manager','/phpmyadmin','/www.zip','/wwwroot.zip','/webadmin','/manage','/.git','/user/admin',
      '/2.rar','/1.rar','/2.zip','/phpinfo.php','/env','/info','/dede','/ht','/admin.zip','/api','/upload','/uploads']

def line(i):
    f = open("urls.txt", "r")
    lines = f.readlines()
    url = []
    for line in lines:
        urls = line.replace('\n', '')
        url.append(urls)
    if i < len(lines):
        return url[i],i,len(lines)
    else:
        coloar.printDarkWhite('全部扫描完成！\n')
        f = open(r'urls.txt', 'a+')
        f.truncate(0)
        time.sleep(2)
        sys.exit()

def scan(url,counts):
 try:
    count = counts + 1
    coloar.printDarkWhite('[+]开始扫描:'+url+'\n')
    name = url.replace('http://', '').replace('https://', '').replace('/', '')
    for i in range(len(list)):
        time.sleep(0.1)
        urls = url + list[i]
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        code = requests.get(urls,headers=headers,verify=False,timeout=5)
        html = requests.get(urls,headers=headers,verify=False,timeout=5).content
        xml = etree.HTML(html)
        title = xml.xpath('/html/head/title/text()')
        if code.status_code == 200:
            coloar.printDarkGreen("[+]命中链接:"+urls+'  Status_Code='+str(code.status_code)+'  '+str(title)+'\n')
            f = open(name+'.txt','a')
            f.write(urls+'  '+str(code.status_code)+'  '+str(title)+'\n')

        elif code.status_code == 302:
            coloar.printDarkYellow("[+]命中链接:"+urls+'  Status_Code='+str(code.status_code)+'  '+str(title)+'\n')
            f = open(name + '.txt', 'a')
            f.write(urls+'  '+str(code.status_code)+'  '+str(title)+'\n')

        elif code.status_code == 403:
            coloar.printDarkRed("[+]命中链接:"+urls+'  Status_Code='+str(code.status_code)+'  '+str(title)+'\n')
            f = open(name + '.txt', 'a')
            f.write(urls+'  '+str(code.status_code)+'  '+str(title)+'\n')

        else:
            coloar.printDarkGray("[-]匹配失败:"+urls+'  Status_Code='+str(code.status_code)+'  '+str(title)+'\n')
    f.close()
    coloar.printDarkWhite('[+]'+url+' 扫描完成！\n')
    success = count
    print('')
    scan(line(success)[0],count)

 except Exception:
    print('')
    coloar.printRed('[-]'+url+'连接超时,自动读取下一个url。\n')
    print('')
    scan(line(count)[0],count)

def start():
    scan(line(0)[0],0)
