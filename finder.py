#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


def getParse(baseurl):
    url = baseurl
    response = requests.get(url)
    # parse html
    parse = str(BeautifulSoup(response.content, "lxml"))
    return parse


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


def kiir(sublinks):
    for i in range(len(sublinks)):
        print(sublinks[i])


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


baseurl = "http://kurzushalo.dev"
page = getParse(baseurl)
kiir(getSubLink(page))
