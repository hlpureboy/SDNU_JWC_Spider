# encoding=utf-8
import requests
from bs4 import BeautifulSoup as BS
import base64
import urllib2
from BaseClass import config
class catchLesson(config):
    '''
    抢课类：只能抢任选课,类型自行修改
    '''
    def __init__(self,url,cookies,xh):
        self.url=url
        self.session=requests.session()
        self.session.cookies=cookies
        self.post_data_2 = {
            "__EVENTTARGET":"",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": "",
            "ddl_kcxz": "",
            "ddl_ywyl": u'无'.encode('gbk'),
            "ddl_kcgs": u'创新创业类'.encode('gbk'),
            "ddl_xqbs": "4",
            "ddl_sksj": u''.encode('gbk'),
            "TextBox1": u''.encode('gbk'),
            "dpkcmcGrid:txtChoosePage": "1",
            "dpkcmcGrid:txtPageSize": "15",
            "Button1": u'提交'.encode('gbk')
        }
        self.post_data_1={
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": "",
            "ddl_kcxz": "",
            "ddl_ywyl": u'无'.encode('gbk'),
            "ddl_kcgs": u'创新创业类'.encode('gbk'),
            "ddl_xqbs": "4",
            "ddl_sksj": u''.encode('gbk'),
            "TextBox1": u''.encode('gbk'),
            "dpkcmcGrid:txtChoosePage": "1",
            "dpkcmcGrid:txtPageSize": "15",
            "Button2": u'确定'.encode('gbk')
        }
        super(catchLesson,self).__init__(url)
        self.headers['Referer']="http://{}/xscj.aspx?xh={}".format(self.ip,xh)
    def parserhtml(self,html):
        suop=BS(html,'html.parser',from_encoding='gbk')
        #print(html.decode('gbk'))
        __EVENTTARGET = suop.find('input', attrs={'name': '__EVENTTARGET'}).get('value')
        __EVENTARGUMENT = suop.find('input', attrs={'name': '__EVENTARGUMENT'}).get('value')
        __VIEWSTATE = suop.find('input', attrs={'name': '__VIEWSTATE'}).get('value')
        #EVENTTARGET=urllib.quote_plus(__EVENTTARGET)
        #EVENTARGUMENT=urllib.quote_plus(__EVENTARGUMENT)
        #VIEWSTATE=urllib.quote_plus(__VIEWSTATE)
        self.kcmcGrid = suop.find_all('input', attrs={'type': "checkbox"})
        return __EVENTTARGET,__EVENTARGUMENT,__VIEWSTATE
    def getvalues(self):
        html_text=self.session.get(url=self.url,headers=self.headers)
        #解析html获取3个values
        self.__EVENTTARGET,self.__EVENTARGUMENT,self.__VIEWSTATE=self.parserhtml(html_text.content)
        #print(self.__VIEWSTATE)
    def postacqurievalues(self):
        self.post_data_1['__EVENTTARGET']=self.__EVENTTARGET
        self.post_data_1['__EVENTARGUMENT']=self.__EVENTARGUMENT
        self.post_data_1['__VIEWSTATE']=self.__VIEWSTATE
        html_text=self.session.post(self.url,headers=self.headers,data=self.post_data_1)
        self.__EVENTTARGET,self.__EVENTARGUMENT,self.__VIEWSTATE=self.parserhtml(html_text.content)
    def havacource(self,html):
        soup=BS(html,'html.parser',from_encoding='gbk')
        data = soup.find('table', attrs={'class': 'datelist', 'id': 'DataGrid2'})
        data_data = data.find_all('tr')
        if len(data_data) == 3:
            print u'您的选课积分已满,所选课程如下:',
            for i in range(1, 3):
                print(data_data[1].find('td').text),
                return True
        elif len(data_data) == 2:
            print(u'您现在选的课有:'),
            print(data_data[1].find('td').text),
            if u'创新创业类'==data_data[1].find_all('td')[9].text:
                return True
            else:
                return False
        else:
            print u"您还未选修任何课程"
            return False
    def postvalues(self):
        self.post_data_2['__EVENTTARGET']=self.__EVENTTARGET
        self.post_data_2['__EVENTARGUMENT']=self.__EVENTARGUMENT
        self.post_data_2['__VIEWSTATE']=self.__VIEWSTATE
        for i in self.kcmcGrid:
            self.post_data_2[i.get('name')] = 'on'
        html_text = self.session.post(self.url, headers=self.headers, data=self.post_data_2)
        #print(html_text.text)
        flag=self.havacource(html_text.text)
        return flag