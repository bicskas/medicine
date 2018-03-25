from tinydb import TinyDB, Query
import datetime


# url = 'asd.hu'
#
# trySite = db.search(Site.url == url)
# if not trySite:
#     db.insert({'url': url, 'time': 'today'})
#
# result = db.search(Site.url == 'HS65X3XS9hp09e4MImLJy7k3OPW9Cw')
# print(result)
db = TinyDB('tinydbs/medicine.json')
Site = Query()

def saveTiny(url):
    trySite = getTinySite(url)
    if not trySite:
        db.insert({'url': url, 'time': str(datetime.datetime.now().time())})

def getTinySite(url):
    site = db.search(Site.url == url)
    return site