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
    # site = Site()
    # site.name = base
    # site = graph.merge(site,'name')
    # print(site,basenode)


def deleteAll():
    graph.delete_all()


def elment(site, type=None):
    newSite = Site()
    newSite.name = site
    exist = graph.data("MATCH (s:Site) WHERE s.name = '" + site + "' RETURN s LIMIT 1")
    if not exist:
        if type is not None:
            newSite.ntype = type
        else:
            newSite.ntype = "undefined"

        if newSite.size is None:
            newSite.size = 1
        #print('Save: ', newSite)
        graph.push(newSite)


def addToBase(base, site):
    basesite = Site.select(graph, base).first()
    basesite = basesite.__ogm__.node
    newsite = Site.select(graph, site).first()
    newsite = newsite.__ogm__.node
    graph.create(Relationship(basesite, 'LINK', newsite))


def addSize():
    node = Site()
    exist = graph.data("MATCH (s:Site) WHERE s.name = '" + basenode + "' RETURN s LIMIT 1")
    # print(exist,'\n',exist[0],'\n',exist[0]['s']['name'])
    if exist:
        node.name = exist[0]['s']['name']
        node.size = exist[0]['s']['size'] + 1
        node.ntype = exist[0]['s']['ntype']
    # size = basenode.size
    # graph.merge(node)
    # node.size = size + 1
    graph.merge(node)
    # print(exist[0]['s']['size'], node)


def getNodes():
    nodes = graph.data("MATCH (a:Site) WHERE EXISTS(a.ntype) RETURN a.name, a.ntype, a.size")
    return nodes


def getEdges():
    #edges = graph.data("MATCH (s:Site)-[r:LINK]->(n:Site) WHERE EXISTS(s.ntype) RETURN s.name, n.name")
    edges = graph.data("MATCH (s:Site)-[r:LINK]->(n:Site) RETURN s.name, n.name")
    return edges
