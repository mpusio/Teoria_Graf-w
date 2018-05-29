import sys

#runTest.sh
f = open(sys.argv[1], mode='r')
a = f.read()
a = a.split()
for item in a:
    if item == '{}':
	a.remove(item)
edg_list = [int(item) for item in a]
f.close()

#kod prawidlowy
class Graph:

    def __init__(self, list_neighbors):
        self.list_neighbors = list_neighbors

    def edge_grahp(self):
        """Znajdz dopelnienie grafu"""

        def list_edges():
            """Zwraca nowa liste z parami wierzcholkow (krawedziami grafu): [(v1,v2),(v1,v3),...]"""
            list_neighbors = list(self.list_neighbors)
            list_edg = zip(list_neighbors[::2], list_neighbors[1::2])
            return list_edg

        def neighbors_edges(edge): #[1, 2]
            """Zwraca sasiednie krawedzie wzgledem aktualnej krawedzi"""
            neigh_edges =[]
            for pairs in l_edg:
                if pairs[0] == edge[0]:
                    neigh_edges.append(pairs)
                elif pairs[0] == edge[1]:
                    neigh_edges.append(pairs)
                elif pairs[1] == edge[0]:
                    neigh_edges.append(pairs)
                elif pairs[1] == edge[1]:
                    neigh_edges.append(pairs)

            neigh_edges.remove(edge)
            return neigh_edges

        def add_edge(act_edg, edge_neigh):
            for items in edge_neigh:
                new_edges.append([act_edg, items])


        def l_vertices(ln):
            """Zwraca wierzcholki w grafie"""
            return list(set(ln))

        l_neigh = self.list_neighbors
        l_ver = l_vertices(l_neigh)
        l_edg = list_edges()
        new_edges = []

        while l_edg != []:
            actual_edge = l_edg[0]
            e_neigh = neighbors_edges(actual_edge)
            add_edge(actual_edge,e_neigh)
            l_edg.remove(actual_edge)

        return new_edges

# Przykladowe wywolania:
graf1 = Graph(edg_list)
print graf1.edge_grahp()
# ln2 = [1, 3, 2, 3, 3, 4, 3, 5]
# graf2 = Graph(ln2)
# print graf2.edge_grahp()
