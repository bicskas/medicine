from py2neo import Graph, Node, Relationship
import py2neo
from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedObjects
import env


class Site(GraphObject):
    __primarykey__ = 'name'

    name = Property()
    size = Property()

    link = RelatedTo('Site', 'Link')


def graphOpen():
    global graph
    graph = Graph(password=env.DB_PASSWORD)


def setBaseNode(base):
    global basenode
    basenode = Site.select(graph, base).first()


def deleteAll():
    graph.delete_all()


def elment(site):
    newSite = Site()
    newSite.name = site
    newSite.size = 1
    graph.push(newSite)


def addToBase(base, site):
    basesite = Site.select(graph, base).first()
    basesite = basesite.__ogm__.node
    newsite = Site.select(graph, site).first()
    newsite = newsite.__ogm__.node
    graph.create(Relationship(basesite, 'LINK', newsite))


def addSize():
    basenode.size += 1
    print(basenode.name, basenode.size)
    graph.push(basenode)

def getNodes():
    nodes = graph.data("MATCH (a:Site) RETURN a.name ")
    return nodes

def getEdges():
    edges = graph.data("MATCH (s:Site)-[r:LINK]->(n:Site) RETURN s.name, n.name")
    return edges
