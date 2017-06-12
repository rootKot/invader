#from bs4 import BeautifulSoup

""" TODO

take text from span, div

"""

class Content:

    def __init__(self, invader):
        self.invader = invader
        self.content = invader.content


    def find_p(self, words):
        cont = self.content
        # h tags
        hs = []
        for i in range(1, 7):
            hs.append('h%s' % i)
        hs = ', '.join(hs)
        
        tags = cont.select('p, %s' % hs)


        for i in range(0, len(words)):
            words[i] = words[i].lower()

        res = []

        for tag in tags:
            text = tag.text
            for word in words:
                _text = text.lower()
                if word in _text:
                    _res = {}
                    _res['text'] = text
                    for word in words:
                        _res[word] = _text.count(word)
                    res.append(_res)
                    break
        
        return res
