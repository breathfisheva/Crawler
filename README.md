
introduce Crawler from simple to complex

1.simple post request to login website
2.selenium + requestes to login website

Note:
1.csrf
有些网址加了CSRF防御，在页面中会存csrf的token，有一部分token是存在页面的html文档里，处理方法，是访问一次这个页面分析页面获得token，然后第二次访问带上这个token。
参考：https://www.jianshu.com/p/d73e971da41c

有一部分是js生成的，就需要找到js生成的规律原则，然后自己用一样的原则生成token。
参考：https://segmentfault.com/a/1190000000657305

2.选择用selenium + request方式
https://www.cnblogs.com/c-x-a/p/8564616.html
https://www.jianshu.com/p/eb3df224045c# Crawler