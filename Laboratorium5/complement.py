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

    def complement(self):
        """Znajdz dopelnienie grafu"""

        def list_edges():
            """Zwraca nowa liste z parami wierzcholkow (krawedziami grafu): [(v1,v2),(v1,v3),...]"""
            list_neighbors = list(self.list_neighbors)
            list_edg = zip(list_neighbors[::2], list_neighbors[1::2])
            return list_edg

        def neighbors_v(v):
            """"Zwraca liste sasiadow danego wierzcholka"""
            neigbors_v = []
            for pairs in l_edg:
                if pairs[0] == v:
                    neigbors_v.append(pairs[1])
                elif pairs[1] == v:
                    neigbors_v.append(pairs[0])
            return neigbors_v

        def l_vertices(ln):
            """Zwraca wierzcholki w grafie"""
            return list(set(ln))

        def not_neighbor(ln, act_v, neigh_v):
            """Zwraca nie sasiadow"""
            ln = list(set(ln))
            for n in neigh_v:
                ln.remove(n)
            ln.remove(act_v)
            return ln

        def complement_edges(not_neigh, act_v):
            for n in not_neigh:
                if [act_v, n] in new_edges or [n, act_v] in new_edges:
                    pass
                else:
                    new_edges.append([act_v, n])

        l_neigh = self.list_neighbors
        l_ver = l_vertices(l_neigh)
        l_edg = list_edges()
        new_edges = []

        while l_ver != []:
            actuall_vertices = l_ver[0]
            v_neigh = neighbors_v(actuall_vertices)
            n_n = not_neighbor(l_neigh, actuall_vertices, v_neigh)
            complement_edges(n_n, actuall_vertices)
            l_ver.remove(actuall_vertices)

        return new_edges


graf1 = Graph(edg_list)
print graf1.complement()
