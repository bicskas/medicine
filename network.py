import database
import collections

import networkx as nx
import matplotlib.pyplot as plt

database.graphOpen()
nodes = database.getNodes()
edges = database.getEdges()
# print(nodes,'\n',edges)
G = nx.Graph()

for n in nodes:
    G.add_node(n['a.name'],ntype = n['a.ntype'])
    print(n['a.name'],'ntype =', n['a.ntype'])

for e in edges:
    G.add_edge(e['s.name'], e['n.name'])

for item in G.nodes(data=True):
    if item[1]['ntype'] == 'legal':
        G.node[item[0]]['viz'] = {'color': {'r': 255, 'g': 0, 'b': 0, 'a': 0}}
    elif item[1]['ntype'] == 'illegal':
        G.node[item[0]]['viz'] = {'color': {'r': 0, 'g': 255, 'b': 0, 'a': 0}}
    else:
            G.node[item[0]]['viz'] = {'color': {'r': 20, 'g': 20, 'b': 20, 'a': 0}}

nx.write_gexf(G, 'test.gexf')
# gráf kirajzolása
#nx.draw(G, node_size=12, alpha=0.8,with_labels=False, font_weight='normal',font_size='8', font_color='brown')
# plt.show(dpi=2000)
#plt.savefig("test.png",dpi=2000)
# sorted(d for n, d in G.degree())
# print(G.number_of_edges())


# ------------------------------------eloszlás kirajzolása a ábrával együtt------------------------------------
# degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
# # print "Degree sequence", degree_sequence
# dmax = max(degree_sequence)
# print(degree_sequence)
# plt.loglog(degree_sequence, 'b-', marker='H',markeredgecolor='g')
# plt.title("Degree rank plot")
# plt.ylabel("degree")
# plt.xlabel("rank")
# # plt.xscale('linear')
# # plt.yscale('linear')
#
# H = nx.Graph(G)
# # draw graph in inset
# plt.axes([0.45, 0.45, 0.45, 0.45])
# Hcc = sorted(nx.connected_component_subgraphs(H), key=len, reverse=True)[0]
# pos = nx.spring_layout(Hcc)
# plt.axis('off')
# nx.draw_networkx_nodes(Hcc, pos, node_size=20)
# nx.draw_networkx_edges(Hcc, pos, alpha=0.4)
# plt.show()
# # plt.savefig("test.png",dpi=2000)

# ---------------------------histogram------------------------------------------------
# degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# # print "Degree sequence", degree_sequence
# degreeCount = collections.Counter(degree_sequence)
# deg, cnt = zip(*degreeCount.items())
#
# fig, ax = plt.subplots()
# plt.bar(deg, cnt, width=0.80, color='b')
#
# plt.title("Degree Histogram")
# plt.ylabel("Count")
# plt.xlabel("Degree")
# ax.set_xticks([d + 0.4 for d in deg])
# ax.set_xticklabels(deg)
#
# # draw graph in inset
# plt.axes([0.4, 0.4, 0.5, 0.5])
# Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]
# pos = nx.spring_layout(G)
# plt.axis('off')
# nx.draw_networkx_nodes(G, pos, node_size=20)
# nx.draw_networkx_edges(G, pos, alpha=0.4)
#
# plt.show()
