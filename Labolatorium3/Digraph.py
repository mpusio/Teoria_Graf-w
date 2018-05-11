# Wypisje sasiadow, krawedzie wychodzace i przychodzace dla grafu skierowanego
class Graph:

    def __init__(self, list_neighbors):
        self.list_neighbors = list_neighbors

    def list_edges(self):
        """Zwraca nowa liste z parami wierzcholkow (krawedziami grafu): [(v1,v2),(v1,v3),...]"""
        list_edg = zip(self.list_neighbors[::2], self.list_neighbors[1::2])
        return list_edg

    def neighbors_v(self, v, l_edg):
        """"Zwraca liste sasiadow danego wierzcholka"""
        neigbors_v = []
        for pairs in l_edg:
            if pairs[0] == v:
                neigbors_v.append(pairs[1])
            elif pairs[1] == v:
                neigbors_v.append(pairs[0])
        return neigbors_v

    def amount_vertices(self):
        """Zwraca liczbe wierzcholkow w grafie"""
        return len(set(self.list_neighbors))

    def edg_out(self, v, l_edg):
        """Liczba krawedzi wychodzacych"""
        neigbors_v = []
        for pairs in l_edg:
            if pairs[0] == v:
                neigbors_v.append(pairs[1])
        return len(neigbors_v)

    def edg_in(self, v, l_edg):
        """Liczba krawedzi przychodzacych"""
        neigbors_v = []
        for pairs in l_edg:
            if pairs[1] == v:
                neigbors_v.append(pairs[1])
        return len(neigbors_v)

# Przykladowe wywolanie:
ln1 = [1, 2, 1, 4, 2, 3, 3, 4]

graf1 = Graph(ln1)
l_edg = graf1.list_edges()
for items in range(graf1.amount_vertices()):
    n_v = graf1.neighbors_v(items+1, l_edg)
    e_o = graf1.edg_out(items+1, l_edg)
    e_i = graf1.edg_in(items+1, l_edg)
    print "Wierzcholek %s ma sasiadow: %s, %s krawedzi wychodzacych, %s przychodzacych" % (items+1, n_v, e_o, e_i)
