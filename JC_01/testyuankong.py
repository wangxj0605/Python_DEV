import requests


def test_yuankong(seqNo):
    url='https://sg-bt-app-gateway-test.gwmyun.com/app-api/api/v1.0/vehicle/getRemoteCtrlResultT5?seqNo=%s(seqNo)'%seqNo
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
    print(r.json())
if __name__ == '__main__':
    seqNo="34631C1B39EC49D7A59D2BBDDF8C2B911234"
    test_yuankong(seqNo)