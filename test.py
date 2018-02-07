# encoding=utf-8
from network.Login import login
from network.Cookie import cookie
from network.Sorce import sorce
from network.CatchLesson import catchLesson
from ImageIdentification import IamgeProcess
from ImageIdentification import ImagePredict
import urllib
import warnings
warnings.filterwarnings("ignore")
'''
初始化参数
相关域名或ip的设定请在 BaseClass中设定
yzm_url="http://{}/CheckCode.aspx"
login_url="http://{}/default2.aspx"
xh:学号
pwd:密码
'''
__xh=''
__pwd=''
yzm_url="http://{}/CheckCode.aspx"
login_url="http://{}/default2.aspx"
'''
获取验证码及cookie
'''
cookies=cookie(yzm_url).getcookies()
'''
验证码的处理及识别
'''
IamgeProcess.process()
yzm=ImagePredict.predict()
print(u"识别验证码:{}".format(yzm.encode('utf-8')))
'''
开始尝试登陆
'''
l=login(login_url)
flag,cook,xh,xm=l.login(__xh,__pwd,yzm=yzm,cookies=cookies)
while flag==False:
    print(u"尝试重新登陆!")
    cookies = cookie(yzm_url).getcookies()
    IamgeProcess.process()
    yzm = ImagePredict.predict()
    print(u"识别验证码:{}".format(yzm.encode('utf-8')))
    m=login(login_url)
    flag, cook, xh, xm = m.login(__xh, __pwd, yzm=yzm, cookies=cookies)
'''
获取成绩,构造获取成绩的url，然后打印输出
'''
url = "http://{}/xscj.aspx?xh={}&xm={}&gnmkdm=N121604".format("{}", xh, urllib.quote_plus(xm.encode('gbk')))
s = sorce(url)
html = s.getsorce(cookies, xh, xm)
s.parserhtml(html)
'''
抢课，只抢限选课中的创新创业课，别的课自己调参数就行了 懒得写了
这个类很久以前写的，应该还能用，自己去类里面改请求去

http://{}/xf_xsqxxxk.aspx?xh={}&xm={}&gnmkdm=N121101".format({},xh,urllib.quote_plus(xm.encode('gbk')))
'''

url="http://{}/xf_xsqxxxk.aspx?xh={}&xm={}&gnmkdm=N121101".format("{}",xh,urllib.quote_plus(xm.encode('gbk')))
c=catchLesson(url,cookies,xh)
c.getvalues()
c.postacqurievalues()
flag=c.postvalues()
while not flag:
    flag=c.postvalues()