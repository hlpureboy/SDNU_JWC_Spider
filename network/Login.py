# encoding=utf-8
import requests
from BaseClass import config
from bs4 import BeautifulSoup
import urllib
class login(config):
    def __init__(self,url):
        self.data = '''__VIEWSTATE={}&txtUserName={}&Textbox1=&TextBox2={}&txtSecretCode={}&RadioButtonList1=%D1%A7%C9%FA&Button1=&lbLanguage=&hidPdrs=&hidsc='''
        super(login,self).__init__(url)
    def login(self,xh,pwd,yzm,cookies):
        try:
            data=self.data.format(self.getVaules(cookies=cookies),xh, pwd, yzm)
            s=requests.session()
            s.cookies=cookies
            con = s.post(self.url, headers=self.headers, data=data)
            if con.url==self.url:
                print("验证码可能出现错误！请重新登陆")
                #print(con.content.decode('gbk'))
                return False,None,None,None,
            else:
                data=con.content
                soup=BeautifulSoup(data,'html.parser',from_encoding='gbk')
                xm=soup.find('span',attrs={'id':'xhxm'}).text[0:len(soup.find('span',attrs={'id':'xhxm'}))-3]
                #print("{},您正在使用创新创业选课抢课脚本!".format(xm.decode('utf-8')))
                #print(xm)
                return True,cookies,xh,xm
        except Exception, e:
            print(e.args)
            print(e.message)
            print e.__doc__
            print(u"出现错误！请重新登陆")
            return False,None,None,None,