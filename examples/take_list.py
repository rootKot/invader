from invader import Invader

url = 'http://sisters.by/him/clothing/majki'
invader = Invader(url)

res = invader.take_list('.products-wrap > a', {
    'img_url': ['.pr-item-wrap > img', 'src'],
    'title': ['.pr-title', 'text']
})

print(res)

