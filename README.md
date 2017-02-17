Invader
============
### Invader is a Python simple module for data grabbing from websites.

Invader is based on BeautifulSoup

---

Dependencies
============
* **[Requests](http://docs.python-requests.org/en/master/)**
* **[Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)**

Try yourself
============
Just download the zip and put **invader.py** in your project directory

Items list data grabbing example:

```python
from invader import Invader

url = 'http://sisters.by/him/clothing/majki'
invader = Invader(url)

res = invader.take_list('.products-wrap > a', {
    'img_url': ['.pr-item-wrap > img', 'src'],
    'title': ['.pr-title', 'text']
})

print(res)

```
the response will be a list of dictionaries wich containing each item's image url and title

```json
[
  {"img_url": ["/files/items/30735/icon_219x270.jpg"], "title": ["Поло  Vit 16 9713tr"]},
  {"img_url": ["/files/items/30734/icon_219x240.jpg"], "title": ["Поло  Vit 16 9713tr"]}
]
```

Here is some **[examples](https://github.com/rootKot/invader/tree/master/examples)** of usage

