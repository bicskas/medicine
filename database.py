#!/usr/bin/env python

import networkx as nx

from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "199402"))
session = driver.session()

'''if session.run("MATCH (a:Site) WHERE a.name = {name} "
                "RETURN a.name AS name, a.title AS title",
                {"name": "Nulladik"}):
    print('Már létezik')
else:'''
session.run("CREATE (a:Site {name: {name}, title: {title}})",
            {"name": "Első", "title": "Első oldal"})

result = session.run("MATCH (a:Site) WHERE a.name = {name} "
                     "RETURN a.name AS name, a.title AS title",
                     {"name": "Nulladik"})
print(result)
for record in result:
    print("%s %s" % (record["title"], record["name"]))


session.close()
