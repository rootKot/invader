from bs4 import BeautifulSoup
import requests
import dryscrape
import sys
import time

if 'linux' in sys.platform:
    dryscrape.start_xvfb()


class Invader:

    def __init__(self, url=None, headers=None, js=False):
        self.url = url
        self.headers = headers
        self.session = None
        if js is False:
            self.content = self.__get_content()
        else:
            self.content = self.__get_js_content()
        

    def __get_content(self):
        if self.url is None:
            return False

        url = self.url

        try:
            if self.headers is None:
                self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36'}

            resp = requests.get(url, headers=self.headers)
            content = resp.content
        except requests.exceptions.RequestException as e:
            print(e)
            return False

        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def __get_js_content(self):
        if self.url is None:
            return False
        
        url = self.url

        try:
            session = dryscrape.Session()
            session.set_attribute('auto_load_images', False)
            session.visit(url)
            self.session = session
            response = session.body()
        except Exception:
            return False

        soup = BeautifulSoup(response, 'html.parser')
        return soup


    def screenshot(self, path=''):
        if self.session is None:
            return False

        name = int(time.time())
        self.session.render('%s%s.png' % (path, name))


    def __extruct(self, items, field):
        res = []
        for item in items:
            if field == 'text':
                prepair = item.text
            else:
                prepair = item[field]

            res.append(prepair)

        if len(res) == 1 and type(res[0]) is str:
            return res[0] 

        return res

    def __take_not_wrapped_list(self, _dict):
        if self.content is False:
            return False

        res = []
        for key in _dict:
            items = self.content.select(_dict[key][0])
            _dict[key] = self.__extruct(items, _dict[key][1])

        for key in _dict:
            for i in range(0, len(_dict[key])):
                _res = {}
                for _key in _dict:
                    _res[_key] = _dict[_key][i]
                res.append(_res)
            break

        return res
        

    def take_list(self, selector=None, _dict={}):
        if selector is None: # if need to take list wihtout item wrapper
            return self.__take_not_wrapped_list(_dict)

        if self.content is False:
            return False

        res = []
       
        for item in self.content.select(selector):
            _res = {}
            for key in _dict:
                value = item.select(_dict[key][0])
                value = self.__extruct(value, _dict[key][1])
                _res[key] = value

            res.append(_res)

        return res


    def take(self, _arr):
        if self.content is False:
            return False

        items = self.content.select(_arr[0])
        res = self.__extruct(items, _arr[1])

        return res

