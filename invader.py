#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests


class Invader:

    def __init__(self, url=None):
        self.url = url
        self.content = self.get_content()
        

    def get_content(self):
        if self.url is None:
            print('No url!')
            return False

        url = self.url
        try:
            resp = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
            return False

        soup = BeautifulSoup(resp.content, 'html.parser')
        return soup


    def extruct(self, items, field):
        res = []
        for item in items:
            if field == 'text':
                prepair = item.text
            else:
                prepair = item[field]

            res.append(prepair)


        return res

    def __take_not_wrapped_list(self, _dict):
        if self.content is False:
            return False

        res = []
        for key in _dict:
            items = self.content.select(_dict[key][0])
            _dict[key] = self.extruct(items, _dict[key][1])

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
                value = self.extruct(value, _dict[key][1])
                _res[key] = value

            res.append(_res)

        return res


    def take(self, _arr):
        if self.content is False:
            return False

        items = self.content.select(_arr[0])
        res = self.extruct(items, _arr[1])

        return res


