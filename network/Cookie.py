# encoding=utf-8
from BaseClass import config
import requests
class cookie(config):
    def getcookies(self):
        content=requests.get(self.url,headers=self.headers)
        with open('./cache/yzm.png', 'wb') as f:
            f.write(content.content)
        return content.cookies
