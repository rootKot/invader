from invader import Invader

url = 'https://duckduckgo.com/?q=python&t=hb&ia=web'
invader = Invader(url, js=True)

res = invader.take_list('#links .result', {
    'title': ['.result__a', 'text'],
    'src': ['.result__a', 'href']
})


print(res)

