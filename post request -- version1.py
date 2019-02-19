'''
requests是一个python的第三方库，比python内置的urllib库更人性化，更好用。

1.构造request 的header信息
2.构造request 的body信息 （form-data， json， raw ） 我们这里处理的是form-data
3.发送login请求：
利用requests.post方法发送post请求， 注意如果是遇到https网址会报ssl的错误，解决办法是verified=False
4.获取login成功后的cookie信息：
利用requests.post.cookies获取cookie信息
5.访问其他需要登陆才能访问的页面：
利用requests.post/ requests.get方法，把cookie传给cookies参数。

'''

import requests


login_url = "https://smartuat2.englishtown.com/login/secure.ashx"
mypage_url = "https://smartuat2.englishtown.com/ecplatform/page/mypage"

#1. request - headers
user_agent = r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
headers_data = {
    'User-Agnet': user_agent,
    'Connection': 'keep-alive'}

#2. request - body [form-data]
login_data ={}
login_data['username'] = 'stest53552'
login_data['password'] = '1'
login_data['p'] = 'ec'

#3. login
resp = requests.post(login_url, data=login_data, headers=headers_data, verify=False)  #for https request set verify=False to fix SSL error
#get login cookie
cookies_data = resp.cookies

#4. use login cookie to visit other page
mypage = requests.get(mypage_url, cookies=cookies_data, verify=False)

#5. get mypage html
print(mypage.content)