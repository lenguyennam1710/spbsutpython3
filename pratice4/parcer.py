import requests
from bs4 import BeautifulSoup
 
req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(req.text, "lxml")

f = open('parce.txt', 'w')
f.write(str(soup.title))
 
f.write(str(soup.title.name))
 
f.write(str(soup.title.string))

f.write(str(soup.h1))
 
f.write(str(soup.h1.string))
 
f.write(str(soup.h1['class']))
 
f.write(str(soup.h1['id']))
 
f.write(str(soup.h1.attrs))
 
soup.h1['class'] = 'firstHeading, mainHeading'
soup.h1.string.replace_with("Python - Programming Language")
del soup.h1['lang']
del soup.h1['id']
 
f.write(str(soup.h1))

for sub_heading in soup.find_all('h2'):
    f.write(str(sub_heading.text))

f.write(str(soup.p.contents))
 
f.write(str(soup.p.contents[10]))
 
for child in soup.p.children:
    f.write(str(child.name))
# b
# None
# a
# None
# a
# None
# ....

f.write(str(soup.p.parent.name))
# div
 
for parent in soup.p.parents:
    f.write(str(parent.name))
# div
# div
# div
# body
# html
# [document]

f.write(str(soup.head.next_sibling))
# '\n'
 
f.write(str(soup.p.a.next_sibling))
# ' for '
 
f.write(str(soup.p.a.previous_sibling))
# ' is a widely used '
 
f.write(str(soup.p.b.previous_sibling))
# None
print ('Success!')