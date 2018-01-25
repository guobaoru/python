#coding:utf-8
import urllib.request#引入urllib包
response = urllib.request.urlopen("http://www.baidu.com/")#获取页面
htmlcode = response.read()#读取内容
format_ = htmlcode.decode('utf-8')#格式化
print(format_)#输出

##第一课，相当于hello world