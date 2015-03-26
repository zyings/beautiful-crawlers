#coding=utf-8

__author__ = 'zyings'

import requests
import json
import time
import urllib2
import re
import os

data = {'q':"",'viewFlag':"A",'sortType':"default",'searchStyle':"",
        'searchRegion':"city",'searchFansNum':"",'currentPage':"1","pageSize":"100"}

headers = {'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0",
           'Accept':"application/json, text/javascript, */*; q=0.01",
           'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
           'Referer':"http://mm.taobao.com/search_tstar_model.htm?spm=719.1001036.1998089564.7.Q9oPo6",
           'X-Requested-Width':"XMLHttpRequest"}

uid_list = list()
name_list = list()

def get_uid(data,headers):
    for i in xrange(1,2):
        data['currentPage'] = str(i)
        r = requests.post(url='http://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8',
                          data=data,headers=headers)
        for i in xrange(1,2):
            uid_list.append(r.json()['data']['searchDOList'][i]['userId'])
            name_list.append(r.json()['data']['searchDOList'][i]['realName'])
            
if __name__ == "__main__":
    get_uid(data,headers)
    Num = len(uid_list)
    for i in xrange(Num):
        url = 'http://mm.taobao.com/self/ai_show.htm?user_id='+str(uid_list[i-1])
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        page = response.read().decode('gbk');
        pattern = re.compile(r'\bhttp://img\d+.{10,150}\.jpg')
        items = pattern.findall(page)
        name = name_list[i-1]
        path = name_list[i-1]
        path = path.strip()
        isExists=os.path.exists(path)
        if not isExists:
            print 'Directory named ', path, 'is maked.' 
            os.makedirs(path)
        else:
            print 'Directory named ', path, 'exists!'

        for item in items:
            try:
                u = urllib2.urlopen(item)
                data = u.read()
                picname = str(time.time())
                f = open(name + r'/'+ picname ,'w')
                f.write(data)
                f.close()
            except urllib2.URLError,e:
                print e
