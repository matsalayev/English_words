import requests
from bs4 import BeautifulSoup
from orderby import desc
def set_links():
    links = [
        'https://www.w3schools.com/html/',
        'https://www.w3schools.com/css/',
        'https://www.w3schools.com/js/',
        'https://www.w3schools.com/python/',
        'https://www.w3schools.com/sql/',
        'https://www.w3schools.com/php/',
        'https://www.w3schools.com/jquery/',
        'https://www.w3schools.com/java/',
        'https://www.w3schools.com/cpp/',
        'https://www.w3schools.com/w3css/',
        'https://www.w3schools.com/c/',
        'https://www.w3schools.com/cs/',
        'https://www.w3schools.com/r/',
        'https://www.w3schools.com/kotlin/',
        'https://www.w3schools.com/nodejs/',
        'https://www.w3schools.com/react/',
        'https://www.w3schools.com/js/',
        'https://www.w3schools.com/angular/',
        'https://www.w3schools.com/mysql/',
        'https://www.w3schools.com/xml/',
        'https://www.w3schools.com/sass/',
        'https://www.w3schools.com/icons/',
        'https://www.w3schools.com/css/',
        'https://www.w3schools.com/graphics/',
        'https://www.w3schools.com/graphics/',
        'https://www.w3schools.com/graphics/',
        'https://www.w3schools.com/nodejs/',
        'https://www.w3schools.com/cybersecurity/',
        'https://www.w3schools.com/colors/',
        'https://www.w3schools.com/git/',
        'https://www.w3schools.com/python/numpy/',
        'https://www.w3schools.com/python/pandas/',
        'https://www.w3schools.com/python/scipy/',
        'https://www.w3schools.com/asp/',
        'https://www.w3schools.com/accessibility/',
        'https://www.w3schools.com/appml/',
        'https://www.w3schools.com/go/',
        'https://www.w3schools.com/typescript/',
        'https://www.w3schools.com/django/',
        'https://www.w3schools.com/mongodb/',
        'https://www.w3schools.com/statistics/',
        'https://www.w3schools.com/datascience/',
        'https://www.w3schools.com/excel/',
        'https://www.w3schools.com/googlesheets/',
        'https://www.w3schools.com/ai/',
        ]
    return links
def get_page_links(url):
    try:
        result = list()
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        div = soup.find('div', {'class': 'w3-sidebar w3-collapse'})
        links = div.find_all('a')
        for link in links:
            t = url + str(link.get('href'))
            result.append(t)
        return result
    except:
        return
def get_words(url):
    response = requests.get(url)
    result = list()
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('div', {'class': 'w3-col l10 m12'})
    words = list()
    try:
        words += div.find_all('p')
        words += div.find_all('ul')
        words += div.find_all('h1')
        words += div.find_all('h2')
        words += div.find_all('h3')
    except:
        print(404)
    for word in words:
        tokens = word.text.strip().split()
        for token in tokens:
            token = str(token)
            b = list()
            index = 0
            for h in range(len(token)):
                if ord(token[h]) < 65 or 90 < ord(token[h]) < 97 or 122 < ord(token[h]):
                    b.append(token[index: h])
                    index = h + 1
            b.append(token[index: len(token)])
            for a in b:
                result.append(a.lower())
    return result
def list_words():
    _list = list()
    for link in set_links():
        for url in get_page_links(link):
            print(url)
            for j in get_words(url):
                if len(j) > 1:
                    try:
                        _list.append(j)
                    except:
                        continue
    return _list
count = dict()
words = set()
text = list_words()
for i in text:
    count[i] = 0
    words.add(i)
for i in text:
    count[i] += 1
files = []
for word in words:
    files.append({'words': word, 'count': int(count[word])})
for i in range(len(words)):
    file = open('words.txt', 'a')
    text = '\n' + list(sorted(files, key=desc('count'))[i].values())[0]
    file.write(text)
    file.close()