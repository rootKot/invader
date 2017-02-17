from invader import Invader

url = 'https://habrahabr.ru/post/321292/'
invader = Invader(url)
 
text = invader.take(['.content.html_format', 'text'])
img = invader.take(['.content.html_format img', 'src'])

print(text)
print(img)

