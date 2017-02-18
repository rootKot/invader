Invader
============
### Invader is a Python simple module for data grabbing from websites. Also with JavaScript support!

Invader is based on BeautifulSoup and dryscrape

---

Dependencies
============
* **[Requests](http://docs.python-requests.org/en/master/)**
* **[Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)**
* **[Dryscrape](https://github.com/niklasb/dryscrape)**

Try yourself
============
* download the zip and put **invader.py** in your project directory
* install all dependecies if you haven't


Items list data grabbing example:

```python
from invader import Invader

url = 'https://duckduckgo.com/?q=python&t=hb&ia=web'
invader = Invader(url, js=True)

res = invader.take_list('#links .result', {
    'title': ['.result__a', 'text'],
    'src': ['.result__a', 'href']
})

print(res)

```
the response will be a list of dictionaries wich containing each item's image url and title

```json
[
    {'title': 'Welcome to Python.org', 'src': 'https://www.python.org/'},
    {'title': 'Python (programming language) - Wikipedia', 'src': 'https://en.wikipedia.org/wiki/Python_%28programming_language%29'},
    {'title': 'Python | Codecademy', 'src': 'https://www.codecademy.com/learn/python'}
]
```

Here is some **[examples](https://github.com/rootKot/invader/tree/master/examples)** of usage


Documentation
============

First of all create import Invader class from invader.
Create instance of Invader and pass for argument the url address of website, and js=True if need to support javascript.

```python
from invader import Invader
invader = Invader('http://some.site', js=True)
```

After that, content of website content will be getted and saved in instace.

For now, there is a only two public functions.
**take()** and **take_list()**

### take()
 For example if you have a link address of a concrete topic page of some forum, and you need to just pull topic title, or you need to get a list with all pictures sources, then you easly can use this function.
**take()** function receives a one list argument, where first element of a list is a CSS selector of a html element, and second is a thing that needs you to take, and returns a list with results.

```python
res = invader.take(['.content .topic-title', 'text'])
```
in this example, we getting text of the element with class topic-title.
Also you can take some attribute value from the element.

```python
res = invader.take(['.content .topic-title a', 'href'])
```
the result will be:

```python
http://some.site/link
```


### take_list()
If you need to get each item's information of some shoping site, then use this function!
**take_list()** function receives a two arguments. First one is a string with selector of item wrapper element.
Second argument is a dictionary with keys and with their selectors and things that we need (text, src, href, etc.)

```python
res = invader.take_list('.products-wrap > a', {
    'img_url': ['.pr-item-wrap > img', 'src'],
    'title': ['.pr-title', 'text']
})
```
the response will be a list of dictionaries wich containing each item's image_url and title

```json
[
  {"img_url": "/files/items/30735/icon_219x270.jpg", "title": "Поло  Vit 16 9713tr"},
  {"img_url": "/files/items/30734/icon_219x240.jpg", "title": "Поло  Vit 16 9713tr"}
]
```

also you can leave first argument None, if items havn't wrapper element, and just go one by one.
**But Warning!** Be careful in that case!
Be sure that each item have the same html elements that you want to get! Otherwise the order will be destroyed, and result going to be wrong.

