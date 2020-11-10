import requests
import uuid
import time
uuid=str(uuid.uuid4()).replace("-",'')+'1234'
def test_yuankong():
	url='https://sg-bt-app-gateway-test.gwmyun.com/app-api/api/v1.0/vehicle/T5/sendCmd'
	headers={
		"rs":"2",
		"brand":"1",
		"terminal":"GW_APP_Haval",
		"beanId":"2843103354490019840",
		"Content-Type":"application/json",
		"port":"OJ0008",
		"enterpriseId":"CC01",
		"operatorRole":	"1",
		"iccid"	:"99999",
		"channel":"APP",
		"deviceId":"1234qwer",
		"cVer":"3.4.5",
		"regionCode":'SG',
        "systemType":"2",
        "accessToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDExNzk1OTksImlhdCI6MTYwMTA5MzE5OSwiaXNzIjoiZ3d0IFNlcnZlciIsImJlYW5JZCI6IjI4NDMxMDMzNTQ0OTAwMTk4NDAiLCJyb2xlQ29kZSI6ImFkbWluIiwiY2hhbm5lbCI6IkZENVZXMDJOSkNMUCJ9.AFSc7MNMpnlux1YxmqNAOj1l7wvVLhpapHYu4o1ks71zFAQLxOSuWDVht86b9zPThmndG1KuJ0hh2CVJgsXFfEmXhBVAl6V19ylwqxySO_y8MTD5ql7K0qAG248yZLrz5NBJL0wXoYhPbQAJhNsAo6GXYg8e7ZhWyBaIYEiwMlHkMrrbZGfcmPA1l-Kc-T8Sf-7YyYEy0o3DA0iBp_OAWHXcWmobjE1FjypJmnkzAK0ywyNpUnSNidi6tqiof_I1tWE7jcjktJKfF38QvSLFhLIpux-NI9TvQTRHotl8NJk9gOn5LhFvv3EOFTc_SdeKzJNBCe774v2SelRinB3bRirpee66yc8"
	}
	body={
		"agreementVersion": "",
		"deviceType": 1,
		"instructions": {
			"0x05": {
				"operationTime": "0",
				"switchOrder": "2"
			}
		},
		"remoteType": "0",
		"securityPassword": "96e79218965eb72c92a549dd5a330112",
		"seqNo": uuid,
		"type": 2,
		"vin": "LGW11604867960001"
		}
	r=requests.post(url=url,headers=headers,json=body)
	print(r.text)
	time.sleep(15)
	return body["seqNo"]
def result(seqNo):
	url='https://sg-bt-app-gateway-test.gwmyun.com/app-api/api/v1.0/vehicle/getRemoteCtrlResultT5?seqNo={}'.format(seqNo)
	headers={
		"rs":"2",
		"brand":"1",
		"terminal":"GW_APP_Haval",
		"beanId":"2843103354490019840",
		"Content-Type":"application/json",
		"port":"OJ0008",
		"enterpriseId":"CC01",
		"operatorRole":	"1",
		"iccid"	:"99999",
		"channel":"APP",
		"deviceId":"1234qwer",
		"cVer":"3.4.5",
		"regionCode":'SG',
        "systemType":"2",
        "accessToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDEzODQyMDQsImlhdCI6MTYwMTI5NzgwNCwiaXNzIjoiZ3d0IFNlcnZlciIsImJlYW5JZCI6IjI4NDMxMDMzNTQ0OTAwMTk4NDAiLCJyb2xlQ29kZSI6ImFkbWluIiwiY2hhbm5lbCI6IkZENVZXMDJOSkNMUCJ9.AhItGZa6YHABYqcGnoi2Elj8X8WkE58u3aCHhHUD8ghb4ywC_dc1sektQAIcYgGedKfL_o1S92KlxWqioSOqKh9J2m-Fu5SxCMcHj9F4DKmdR7Z1cY-FcEmDa1xaqS1eTJPJsVrOEgExqE_MAm-2LobzEyKcuwtMaH77zVydLJWG7gyQrMVjvBoWlm8aU5NV_TgQ0z8z1fhHPZV4Dwna7lCjnxvBuEdaWa67SZuPpxw86GEF3PIQUgsgrVp6Dj0NQJ7OwzR-yYETd-sFv6_hry8ErHMb8v5a0NOPqqg8MpXVsLxB4qtaBEocLe5YlPPZf3soKbeUKMPbosYiq4fXwv05l41-Llw"
	}
	r=requests.get(url=url,headers=headers)
	print(r.text)

def getapp():
	url='https://sg-bt-app-gateway-test.gwmyun.com/app-api/api/v1.0/complaintsComments/findLastVersion?type=Android&versionNum=0.0.1'
	headers={
		"rs":"2",
		"brand":"1",
		"terminal":"GW_APP_Haval",
		"beanId":"2843103354490019840",
		"Content-Type":"application/json",
		"port":"OJ0008",
		"enterpriseId":"CC01",
		"operatorRole":	"1",
		"iccid"	:"99999",
		"channel":"APP",
		"deviceId":"1234qwer",
		"cVer":"3.4.5",
		"regionCode":'SG',
        "systemType":"2",
        "accessToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDExNzk1OTksImlhdCI6MTYwMTA5MzE5OSwiaXNzIjoiZ3d0IFNlcnZlciIsImJlYW5JZCI6IjI4NDMxMDMzNTQ0OTAwMTk4NDAiLCJyb2xlQ29kZSI6ImFkbWluIiwiY2hhbm5lbCI6IkZENVZXMDJOSkNMUCJ9.AFSc7MNMpnlux1YxmqNAOj1l7wvVLhpapHYu4o1ks71zFAQLxOSuWDVht86b9zPThmndG1KuJ0hh2CVJgsXFfEmXhBVAl6V19ylwqxySO_y8MTD5ql7K0qAG248yZLrz5NBJL0wXoYhPbQAJhNsAo6GXYg8e7ZhWyBaIYEiwMlHkMrrbZGfcmPA1l-Kc-T8Sf-7YyYEy0o3DA0iBp_OAWHXcWmobjE1FjypJmnkzAK0ywyNpUnSNidi6tqiof_I1tWE7jcjktJKfF38QvSLFhLIpux-NI9TvQTRHotl8NJk9gOn5LhFvv3EOFTc_SdeKzJNBCe774v2SelRinB3bRirpee66yc8"
	}
	r=requests.get(url=url,headers=headers)
	print(r.text)
if __name__ == '__main__':
	# result(seqNo=test_yuankong())
    #   result(seqNo="AC1B1884DCB34F30BE2EBC33102C02FA1234")
	getapp()