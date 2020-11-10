# -*- coding: utf-8 -*-
'''
@File  : testCase.py
@Author: 汪先锦
@Date  : 2019-12-14 19:13
@Software: PyCharm
@Desc  :
'''
import requests
import time
import pprint

from JC_01 import TEST, do_getExcel, filePath

Sign=TEST.Sign()
getexcel = do_getExcel.DoExcel()
def test_会员第一次备案():
    for item in getexcel.get_data(filePath.filePath('JC_01', 'sign.xlsx'), 'Sheet1'):
        # Sign.testSignPost( URL=item['URL'],secretkey=item["secretkey"],body=eval(item['body']))
        headers={
            "Content-Type": "application/json",
            "bt-auth-sign":Sign.testSignPost(URL=item['URL'],secretkey=item["secretkey"],body=eval(item['body'])),
            "bt-auth-appkey":"1592523063",
            "bt-auth-nonce":"tqhw7fduqhorwg73",
            "bt-auth-timestamp":str(int(round(time.time() * 1000)))
        }

        url="http://sg-third-system-test.gwmyun.com/call-center-service/v1.0/ecall/carInformationRecord"
        r=requests.post(url=url,headers=headers,json=eval(item['body']))

        print(headers)
        pprint.pprint(r.json())
if __name__ == '__main__':
    test_会员第一次备案()