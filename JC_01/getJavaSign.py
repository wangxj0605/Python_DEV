#coding=utf-8

import jpype

import os.path

import requests
import json


def add_sign(api,parameters,method):

    # 初始化一个sign
    sign_dict = {
        "bt-auth-sign" : "",
        "bt-auth-timestamp" : ""
    }

    # 将maven打的jar包移动到resources目录下来
    # os.system("cp /Users/gyliang/gw/APItestForGW/target/*.jar %s"%
    #           os.path.join(os.getcwd()[0:os.getcwd().rfind('/')],"resources/"))

    # 在resources目录中找到加密算法的jar包文件
    jar_path = os.path.join(os.getcwd()[0:os.getcwd().rfind('/')],
                            "resources/APItestForGW-1.0-SNAPSHOT-jar-with-dependencies.jar")
    print(jar_path)
    jvm_path = jpype.getDefaultJVMPath()
    jpype.startJVM(jvm_path, "-ea", "-Djava.class.path=%s" % jar_path)

    print("start success")

    JClass = jpype.JClass('com.gw.requestPre.SignTest')
    instance = JClass()


    # 根据request的不同方法，调用算法中的不同java方法
    if method == 'GET':
        # generateSignOfGet的传参方式的参数为HashMap类型
        sign_dict['bt-auth-sign'] = instance.generateSignOfGet(api, parameters).get("sign")
        sign_dict['bt-auth-timestamp'] = instance.generateSignOfGet(api, parameters).get("timestamp")
    else:
        # generateSignOfPost的传参方式的参数为String类型
        sign_dict['bt-auth-sign'] = instance.generateSignOfPost(api, str(parameters)).get("sign")
        sign_dict['bt-auth-timestamp'] = instance.generateSignOfPost(api, str(parameters)).get("timestamp")

    return sign_dict



if __name__ == '__main__':
    url = "/call-center-service/v1.0/api/m/member/membershipadd";

    parameters  = {
        "engineId": "00000T1102T000252",
        "serviceStartdate": "2020-06-30T03:55:02.756Z",
        "serviceStopdate": "2020-12-30T03:55:02.756Z",
        "vehicalColor": "black",
        "vehicalType": "03",
        "marketCountry": "86",
        "vehicalPhone": "+86188888888",
        "vehicleNumber": "泸B:A8888",
        "vin": "00000T1102T000252",
        "channelId": "GW-EC-S17602EC-PRODUCT",
        "serviceComber": "CB1000001",
        "extenalId": "kjkj"
    }



    print(add_sign(url,parameters,'POST'))

    # h = {
    #     "bt-auth-appKey": "1592523063",
    #     "bt-auth-timestamp": "1601282665640",
    #     "bt-auth-sign" : "906ad6cee7081cc31b52195d8050a79d5547ce8a9748a37f9ba63644646eab7a"
    # }

    # r = requests.request('POST',url="https://sg2-third-system-test.gwmyun.com/call-center-service/v1.0/api/m/member/membershipadd",
    #                      json=parameters,headers=h)
    #
    # resp = json.loads(r.text)
    # print(resp)

