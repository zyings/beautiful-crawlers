#-*- coding:utf_8 -*-

__author__ = 'zyings'

import requests
import json
import re
import os
import time

note_url = list()

headers = {'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0",
           'Accept':"application/json, text/javascript, */*; q=0.01",
           'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
           'Referer':"http://top.mogujie.com/top/share/user?uid=1ocne&ptp=1.NcdLDXm2.u2e4Keo4.22.C7davd",
           'X-Requested-Width':"XMLHttpRequest"}
           
data = {'uid':'',
        'mbook':'',
        'topTid':'0'}
        
def get_url():
    for h in xrange(1,3): # number 3 can be replaced by i in xrange(2,61) as there are 60 pages of girls in www.mogujie.com
        for i in xrange(1,11):
            url = 'http://www.mogujie.com/style/topindexapi/'+ str(h) + '/' + str(i)
            response = requests.get(url)
            for j in xrange(1,12):
                note_url.append(response.json()['result']['html'][j]['noteUrl'])

def get_pic():
    for t in note_url:
        picUrl = 'http://www.mogujie.com'+str(t)
        print picUrl
        response2 = requests.get(picUrl,data = data, headers = headers)
        pattern = re.compile(r'src="(.{50,150}[5-9][0-9]{2}.[0-9]{3,4}\.jpg)"')
        pics = re.findall(pattern,response2.text)
        #print pics
        #print pics
        name = re.search(r'<title>(.{1,70})</title>',response2.text).group(1).split(' ')[-3]
        name = name.strip()
        isExists=os.path.exists(name)
        # Judge the results
        if not isExists:
        # if the directory doesn't exist then make it
            print 'Directory named', name, 'is maked. ' 
            # make the directory
            os.makedirs(name)
        else:
            # if the directory exists, don't make it
            print 'Directory named', name, 'exists!'
  
        for pic in pics:
            r = requests.get(pic)
            f = open(name + r'/'  + str(time.time()),'wb')
            f.write(r.content)
            f.close
            
if __name__ == "__main__":
    get_url()
    get_pic()
