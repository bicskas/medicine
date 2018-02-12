from py2neo import Graph, Node, Relationship
import py2neo
from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedObjects
import env


class Site(GraphObject):
    __primarykey__ = 'name'

    name = Property()
    size = Property()
    ntype = Property()

    link = RelatedTo('Site', 'Link')


def graphOpen():
    global graph
    graph = Graph(password=env.DB_PASSWORD)


def setBaseNode(base):
    global basenode
    basenode = base
    #site = Site()
    #site.name = base
    #site = graph.merge(site,'name')
    #print(site,basenode)


def deleteAll():
    graph.delete_all()


def elment(site):
    newSite = Site()
    newSite.name = site
    newSite.ntype = "undefined"
    # newSite.size = 1
    # graph.push(newSite)
    graph.merge(newSite, "name",newSite.name)
    if newSite.size is None:
        newSite.size = 1
        graph.push(newSite)


def addToBase(base, site):
    basesite = Site.select(graph, base).first()
    basesite = basesite.__ogm__.node
    newsite = Site.select(graph, site).first()
    newsite = newsite.__ogm__.node
    graph.create(Relationship(basesite, 'LINK', newsite))


def addSize():
    #node = basenode
    #size = basenode.size
    #graph.merge(node)
    #node.size = size + 1
    #graph.push(node)
    a = 12


def getNodes():
    nodes = graph.data("MATCH (a:Site) WHERE EXISTS(a.ntype) RETURN a.name, a.ntype")
    return nodes


def getEdges():
    edges = graph.data("MATCH (s:Site)-[r:LINK]->(n:Site) WHERE EXISTS(s.ntype) RETURN s.name, n.name")
    return edges
