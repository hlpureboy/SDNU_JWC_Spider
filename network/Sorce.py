# encoding=utf-8
import requests
from BaseClass import config
from bs4 import BeautifulSoup
import urllib
class sorce(config):
    def __init__(self,url):
        super(sorce,self).__init__(url)
        #self.headers['Referer']=self.url
    def getVaules(self,xh,xm,cookies):
        #url="http://210.44.14.37/xscj.aspx?xh={}&xm={}".format(xh,urllib.quote_plus(xm.encode('gbk')))
        #print url
        s=requests.session()
        s.cookies=cookies
        html = s.get(self.url,headers=self.headers)
        #print(html.content.decode('gbk'))
        soup = BeautifulSoup(html.content, 'html.parser', from_encoding='gbk')
        __Value = soup.find('input', {'type': 'hidden', 'name': '__VIEWSTATE'})
        return urllib.quote_plus(__Value.get('value'))
    def getsorce(self,cookies,xh,xm):
        #print(self.url)
        data = {'Button2': "",
                'txtZZCJ': '',
                'txtQSCJ': '',
                'ddlXQ': '',
                'ddlXN': '',
                '__VIEWSTATE': '',
                '__EVENTTARGET': '',
                '__EVENTARGUMENT': ''
                }
        data['__VIEWSTATE']=urllib.unquote_plus(self.getVaules(xh,xm,cookies))
        #print(data)
        s=requests.session()
        s.cookies=cookies
        content=s.post(self.url,headers=self.headers,data=data)
        html=content.content
        return html
    def parserhtml(self,html):
        soup=BeautifulSoup(html,"html.parser",from_encoding='gbk')
        #print(html.decode('gbk'))
        sources=soup.find('table',attrs={'class':'datelist','id':'DataGrid1'})
        #print(sources)
        for i in sources.find_all('tr'):
            s=i.find_all('td')
            #print(s[2].text.encode('utf-8'))
            #if s[2].text.encode('utf-8')==u'任选'.encode('utf-8'):
            print("{}:{}:{}").format(s[0].text.encode('utf-8'),s[1].text.encode('utf-8'),s[3].text.encode('utf-8'))