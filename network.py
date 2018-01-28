import database
import networkx as nx
import matplotlib.pyplot as plt

database.graphOpen()
nodes = database.getNodes()
edges = database.getEdges()
# print(nodes,'\n',edges)
G = nx.Graph()

for n in nodes:
    G.add_node(n['a.name'])

for e in edges:
    G.add_edge(e['s.name'], e['n.name'])

#gráf kirajzolása
# nx.draw(G, node_size=12, alpha=0.8,with_labels=True, font_weight='normal',font_size='8', font_color='brown',node_color='cyan',edge_color='gray')
# plt.show(dpi=2000)
# # plt.savefig("test.png",dpi=2000)
# # sorted(d for n, d in G.degree())
# print(G.number_of_edges())



# eloszlás kirajzolása a ábrával együtt
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
# print "Degree sequence", degree_sequence
dmax = max(degree_sequence)

plt.loglog(degree_sequence, 'b-', marker='H',markeredgecolor='g')
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")

# draw graph in inset
plt.axes([0.45, 0.45, 0.45, 0.45])
Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]
pos = nx.spring_layout(Gcc)
plt.axis('off')
nx.draw_networkx_nodes(Gcc, pos, node_size=20)
nx.draw_networkx_edges(Gcc, pos, alpha=0.4)

plt.show()
