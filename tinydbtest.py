import tinydb
import datetime


# url = 'asd.hu'
#
# trySite = db.search(Site.url == url)
# if not trySite:
#     db.insert({'url': url, 'time': 'today'})
#
# result = db.search(Site.url == 'HS65X3XS9hp09e4MImLJy7k3OPW9Cw')
# print(result)
db = tinydb.TinyDB('tinydbs/medicine.json')
visiteddb = tinydb.TinyDB('tinydbs/visiteddb.json')
Site = tinydb.Query()
Visited = tinydb.Query()


def saveTiny(url):
    trySite = getTinySite(url)
    if not trySite:
        db.insert({'url': url, 'visited' : 0,'time': str(datetime.datetime.now().time())})

def getTinySite(url):
    site = db.search(Site.url == url)
    return site

def updateTinySite(url):
    db.upsert({'url': url, 'visited' : 1,'time': str(datetime.datetime.now().time())},Site.url == url)

def addToVisited(url):
    tryVisited = inVisited(url)
    if not tryVisited:
        visiteddb.insert({'url': url, 'time': str(datetime.datetime.now().time())})

def inVisited(url):
    visited_site = visiteddb.search(Visited.url == url)
    if visited_site:
        return True
    else:
        return False
