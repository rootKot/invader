from invader import Invader
from invader.content import Content

url = 'https://duckduckgo.com/?q=who+is+obama&t=hb&ia=web'
invader = Invader(url, js=True)

res = invader.take_list('#links .result', {
    'title': ['.result__a', 'text'],
    'href': ['.result__a', 'href']
})

for link in res:
    invader = Invader(link['href'], True)
    cont = Content(invader.content)
    text = cont.find_text(['obama', 'president'])
    if text != '':
        print(text)
        break


