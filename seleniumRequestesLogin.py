'''
在爬coursera上遇到了csrf验证，他的request里多了很多csrf的token。
有些网址是在html里直接写了token，这样我们只要访问一次登陆页面，拿到html的token，然后把token放到request请求里再模拟login。
有些网址的token是js动态生成的，有的我们可以找到js生成的规律然后自己生成token，有些很难找到规律，因为可能js是从某个请求返回的某个字段为基础然后生成token
coursera就是一个我找不到规律生成token然后用request请求无法模拟登陆的网址。

解决办法：
先用selenium登陆，然后获取cookie，然后把cookie传给requests，这样后面就可以用request请求了

步骤：
1.用selenium登陆
我们这里用输入获得用户名和密码，就不用明文写在代码里。

2.登陆成功后从driver.cookies中获得cookie的值

3.把cookie的值传给给request.session对象

4.关闭chromedriver

5.request.session对象获得cookie后，就可以用它来访问其他需要登陆才能访问的url

6.在命令行输入 python test.py 'username' 'password' 执行


'''

from selenium import webdriver
import sys,time,requests

# url
login_url = 'https://www.coursera.org/?authMode=login'
course_home_url = 'https://www.coursera.org/learn/algorithms-part1/home/welcome'

#1.用selenium登陆
#1.1 从输入中获取用户名和密码
user_name = sys.argv[1]
password = sys.argv[2]

#1.2 启动webdriver，打开url，模拟登陆
driver = webdriver.Chrome()
driver.get(login_url)

driver.find_element_by_xpath("//input[@type='email']").send_keys(user_name)
driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
driver.find_element_by_xpath("//button[@data-js='submit']").click()


#2.从driver中获取cookie列表（是一个列表，列表的每个元素都是一个字典）
cookies = driver.get_cookies()
#3.把cookies设给requests session对象
s = requests.Session()
for cookie in cookies:
    s.cookies.set(cookie['name'],cookie['value'])
#4.关闭driver
driver.close()

#5.用request.session.get来访问其他需要登陆才能访问的网址
response1 = s.get(course_home_url, verify=False)
response1_content = response1.text
print(response1.content)