# -*- coding: utf-8 -*-
'''
@File  : TEST.py
@Author: 汪先锦
@Date  : 2019-12-14 19:13
@Software: PyCharm
@Desc  :
'''
import time
import json
import hashlib
import  urllib.parse
from  JC_01 import do_getExcel,filePath
getexcel = do_getExcel.DoExcel()
class Sign:
    def testSignPost(self,URL,secretkey,body):
        timestamp=str(int(round(time.time() * 1000)))
        http_mathod="POST"
        A="bt-auth-appkey:3753367802"
        B="bt-auth-nonce:tqhw7fduqhorwg73"
        C="bt-auth-timestamp:{}".format(timestamp)
        JSON = str(json.dumps(body, sort_keys=True,ensure_ascii=False))
        DATA=http_mathod+URL+A+B+C+"json={}".format(JSON)+secretkey
        DATA.replace(' ','')
        SIGN=hashlib.sha256(DATA.encode("utf-8")).hexdigest()
        SIGN=urllib.parse.quote(SIGN)
        print(SIGN)
        return SIGN


if __name__ == '__main__':
    s = Sign()
    for item in getexcel.get_data(filePath.filePath('JC_01', 'sign.xlsx'), 'Sheet1'):
        s.testSignPost(URL=item['URL'], secretkey=item["secretkey"],body=eval(item['body']))
