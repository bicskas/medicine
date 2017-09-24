from py2neo import Graph, Node, Relationship
import py2neo
from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedObjects


class Site(GraphObject):
    __primarykey__ = 'name'

    name = Property()
    size = Property()

    link = RelatedTo('Site')


def deleteAll():
    graph = Graph(password="199402")
    graph.delete_all()


def elment(site):
    graph = Graph(password="199402")

    newSite = Site()
    newSite.name = site
    newSite.size = 1
    graph.push(newSite)


def addBase(base, site):
    graph = Graph(password="199402")

    basesite = Site.select(graph, base).first()
    basesite = basesite.__ogm__.node
    newsite = Site.select(graph, site).first()
    newsite = newsite.__ogm__.node
    graph.create(Relationship(basesite, 'LINK', newsite))
