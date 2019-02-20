'''
使用BeautifulSoup来解析html
参考：https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/

我们这里是让html按照标准的缩进格式的结构输出
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
'''

from selenium import webdriver
from bs4 import BeautifulSoup
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

#6.使用beautifulSoup让按照标准的缩进格式的结构输出
soup = BeautifulSoup(response1_content, 'html.parser')
print(soup.prettify())
# print(response1.content)