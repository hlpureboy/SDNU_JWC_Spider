# encoding=utf-8
import requests
from bs4 import BeautifulSoup
import urllib
class config(object):
    '''
    抽象出的父类
    '''
    def __init__(self,url):
        self.ip="210.44.14.34"
        self.url=url.format(self.ip)
        self.headers = {
            'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': self.ip,
            'Pragma': 'no-cache',
            'Referer': self.url,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
        }
    def getVaules(self,cookies=''):
        html = requests.get(self.url,headers=self.headers,cookies=cookies)
        soup = BeautifulSoup(html.content, 'html.parser', from_encoding='gbk')
        __Value = soup.find('input', {'type': 'hidden', 'name': '__VIEWSTATE'})
        return urllib.quote_plus(__Value.get('value'))
