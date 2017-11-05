#!/usr/bin/env python
from random import randint

import requests
from bs4 import BeautifulSoup
import network
import env


# az adott oldal html részét adja vissza
def getParse(baseurl):
    url = baseurl
    response = requests.get(url)
    # parse html
    parse = str(BeautifulSoup(response.content, "lxml"))
    return parse


# az adott oldalon található linkek
def getURL(page):
    """

    :param page: html of web page (here: Python home page)
    :return: urls in that page
    """
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote


# a getUrl alapján készít egy tömböt a linkekből
def getSubLink(page):
    sublinks = []
    while True:
        url, n = getURL(page)
        page = page[n:]
        if url:
            sublinks.append(url)
        else:
            break
    return sublinks


def kiir(sublinks):
    for i in range(len(sublinks)):
        print(sublinks[i])
        network.elment(sublinks[i])
        network.addToBase(baseurl, sublinks[i])


baseurl = "http://ferling.hu"
visited = []
page = getParse(baseurl)
network.deleteAll()
network.elment(baseurl)
kiir(getSubLink(page))
