#!/usr/bin/env python
from random import randint

import requests
from bs4 import BeautifulSoup
import network
import urllib.request
from urllib.parse import urljoin
import env
import re

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


# az adott oldal html részét adja vissza
def getParse(baseurl):
    url = baseurl
    addToVisited(url)
    html_page = urllib.request.urlopen(url)
    try:
        pass
    except ValueError:
        print()
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
        if l.startswith('http') and not l in visited and not l in queue[szint]:
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
    # print(baseurl)
    for i in range(len(sublinks)):
        # print(sublinks[i])
        network.elment(sublinks[i])
        network.addToBase(baseurl, sublinks[i])


starturl = "http://oae.kgergo.fwl.hu"
melyseg = 5
setQeueRange(melyseg)
setBaseUrl(starturl)
addToQueue(0, baseurl)
page = getParse(baseurl)
# getURL(page)
network.deleteAll()
network.elment(baseurl)
removeFromQueue(0, baseurl)
kiir(getURL(page))
# print('ELSŐ RÉSZ:', visited)
i = 0
print(level)
while i < melyseg:
    for q in queue[i]:
        if not q in visited:
            setBaseUrl(q)
            removeFromQueue(getSzint(level, q), q)
            page = getParse(baseurl)
            kiir(getURL(page))
    i = i + 1
