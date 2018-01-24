#!/usr/bin/env python
from random import randint

import requests
from bs4 import BeautifulSoup
import network
import urllib.request
from urllib.parse import urljoin
from urllib.parse import urlparse

global visited
visited = []

global queue
queue = []

global level
level = []


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
    if not url in queue and not url in visited:
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
    addToVisited(url)
    html_page = urllib.request.urlopen(url)
    # parse html
    parse = BeautifulSoup(html_page, 'lxml')
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
        if (path != baseurl):
            network.elment(getName(sublinks[i]))
            network.addToBase(getName(baseurl), getName(sublinks[i]))
        elif (path == baseurl):
            network.addSize()


# -----------------------------------------------------------------------------
starturl = "http://www.pte.hu"
melyseg = 4

setQeueRange(melyseg)
setBaseUrl(starturl)
addToQueue(0, baseurl)

page = getParse(baseurl)

network.graphOpen()
network.deleteAll()
network.elment(getName(baseurl))
network.setBaseNode(getName(baseurl))
removeFromQueue(0, baseurl)
kiir(getURL(page))

i = 0
while i < melyseg:
    for q in queue[i]:
        if not q in visited:
            setBaseUrl(q)
            network.setBaseNode(getName(q))
            removeFromQueue(getSzint(level, q), q)
            try:
                page = getParse(baseurl)
                print(baseurl, 'megnyitva')
                kiir(getURL(page))
            except:
                print('Hiba a megnyitáskor: ' + q)
                # break

    i += 1

print(visited)
