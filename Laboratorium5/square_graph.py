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

    def square_graph(self):
        """Znajdz kwadrat grafu"""

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

        def add_square(act_v, neigh_v):
            """Dodaj kwadrat grafu"""
            for n in neigh_v:
                temp_neighs = neighbors_v(n)
                temp_neighs.remove(act_v)
                if temp_neighs != []:
                    for n2 in temp_neighs:
                        #if n2 not in neigh_v and act_v not in neigh_v:
                        l_square.append((act_v, n2))

        def sort_square(sqr):
            """Wyeleminuj powtarzajace sie elementy"""
            for v1, v2 in sqr:
                sqr.remove((v2, v1))
            return sqr

        l_neigh = self.list_neighbors
        l_ver = l_vertices(l_neigh)
        l_edg = list_edges()
        l_square = []

        while l_ver != []:
            actuall_vertices = l_ver[0]
            v_neigh = neighbors_v(actuall_vertices)
            add_square(actuall_vertices, v_neigh)
            l_ver.remove(actuall_vertices)

        sort_square(l_square)
        for items in l_square:
            l_edg.append(items)

        return l_edg

# Przykladowe wywolania:
graf1 = Graph(edg_list)
print graf1.square_graph()

# ln2 = [1,3,1,4,2,4]
# graf2 = Graph(ln2)
# print graf2.square_graph()
