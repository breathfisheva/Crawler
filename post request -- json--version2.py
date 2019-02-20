'''
request 里的是json的话，我们用json.dumps来处理
'''


import requests
import json

url = "http://jinbao.pinduoduo.com/network/api/common/goodsList"

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Referer": "http://jinbao.pinduoduo.com/index?page=5",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }

pyload = {"keyword": "", "sortType": 0, "withCoupon": 0, "categoryId": 16, "pageNumber": 1, "pageSize": 60}
response = requests.post(url, data=json.dumps(pyload), headers=headers, verify=False).text

print(response)