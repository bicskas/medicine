#!/usr/bin/env python

from bs4 import BeautifulSoup
import database
import urllib.request
from urllib.parse import urljoin
from urllib.parse import urlparse
import ast
import tinydbtest

global visited
visited = []

global queue
queue = None
queue = []

global level
level = []

global oldalszam
oldalszam = 1

def clearSource(source):
    cleaned = str(source).replace("\n",'').replace("\',",'').replace(" ",'').replace("\'",'').replace("[",'').replace("]",'').replace("\"",'\'')
    return cleaned

def setBaseUrl(url):
    global baseurl
    baseurl = url


def setQeueRange(melyeg):
    for num in range(0, melyseg):
        queue.append([])
        level.append([])


def addToVisited(url):
    visited.append(url)


def addToQueue(szint, url):
    if not any(url in sublist for sublist in queue) and not url in visited:
        queue[szint].append(url)
        level[szint].append(url)


def removeFromQueue(szint, url):
    queue[szint].remove(url)


def getSzint(myList, v):
    for szint, x in enumerate(myList):
        if v in x:
            return (szint)


def getName(name):
    return str(urlparse(name).netloc).replace('www.', '')


# az adott oldal html részét adja vissza
def getParse(baseurl):
    url = baseurl
    tinydbtest.addToVisited(url)
    tinydbtest.updateTinySite(url)
    try:
        html_page = urllib.request.urlopen(url)
    except:
        html_page = ''
    # parse html
    parse = BeautifulSoup(html_page, 'lxml')
    global oldalszam
    print('Site downloaded: ' + url + ' Downloaded sites: ' + str(oldalszam))
    oldalszam += 1
    return parse


# az adott oldalon található linkek
def getURL(page):
    """

    :param page: html of web page (here: Python home page)
    :return: urls in that page
    """
    t_links = []
    links = []

    # for link in soup.findAll('a', attrs={'href': re.compile("^htt")}):
    for link in page.findAll('a'):
        if not link.get('href') is None and not link.get('href').startswith('#') and link.get(
                'href') != baseurl:
            t_links.append(urljoin(baseurl, link.get('href')))

    szint = getSzint(level, baseurl) + 1

    for l in t_links:
        if l.startswith('http') and not l in visited:
            links.append(l)
            addToQueue(szint, l)

    return links


# a getUrl alapján készít egy tömböt a linkekből
# def getSubLink(page):
#     sublinks = []
#     while True:
#         url, n = getURL(page)
#         page = page[n:]
#         if url:
#             sublinks.append(url)
#         else:
#             break
#     return sublinks


def kiir(sublinks):
    for i in range(len(sublinks)):
        path = urlparse(sublinks[i]).scheme + '://' + urlparse(sublinks[i]).netloc

        tinyName = urlparse(sublinks[i]).netloc + urlparse(sublinks[i]).path
        tinyVisited = tinydbtest.getTinySite(tinyName)
        tinydbtest.saveTiny(tinyName)

        currenturl = urlparse(sublinks[i]).netloc
        mainurl =  urlparse(baseurl).netloc
        if (currenturl != mainurl):
            database.elment(getName(sublinks[i]))
            database.addToBase(getName(baseurl), getName(sublinks[i]))
        elif (currenturl == mainurl and not tinyVisited):
            database.addSize()


# -----------------------------------------------------------------------------
urlfile = open("urls.txt","r")
lines = '{' + clearSource(urlfile.read()) + '}'
starturls = ast.literal_eval(lines)
urlfile.close()



melyseg = 4
database.graphOpen()
#database.deleteAll()

setQeueRange(melyseg)
# setBaseUrl(starturl)
for url, type in starturls.items():
    addToQueue(0, url)
    setBaseUrl(url)
    page = getParse(baseurl)
    database.elment(getName(baseurl), type)
    database.setBaseNode(getName(baseurl))
    # removeFromQueue(0, baseurl)
    kiir(getURL(page))
print(queue)
i = 5
while i < melyseg:
    for q in queue[i]:
        tinyName = urlparse(q).netloc + urlparse(q).path

        if not q in visited and not tinydbtest.inVisited(tinyName):
            setBaseUrl(q)
            database.setBaseNode(getName(q))
            # removeFromQueue(getSzint(level, q), q)
            try:
                page = getParse(baseurl)
                tinydbtest.addToVisited(tinyName)
                # print(baseurl, 'megnyitva')
                kiir(getURL(page))
            except:
                print('' + q)
                # break
    i += 1
