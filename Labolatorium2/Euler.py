class Graph:

    def __init__(self, list_neighbors):
        self.list_neighbors = list_neighbors

    def DFS(self):
        """Przeszukuje graf w glab, sprawdza czy jest spojny"""

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

        def neighbors_substract_visited():
            "Odejmuje od sasiadow odwiedzone wierzcholki"
            for nums in vertices_visited:
                if nums in neighbors:
                    neighbors.remove(nums)

        l_edg = list_edges()
        actuall_vertices = None
        stack = []
        vertices_visited = []

        vertices_visited.append(actuall_vertices)
        stack.append(actuall_vertices)

        while stack != []:
            stack[-1] = actuall_vertices
            neighbors = neighbors_v(actuall_vertices)
            neighbors_substract_visited()

            if actuall_vertices in neighbors:
                vertices_visited.append(actuall_vertices)
                stack.append(actuall_vertices)
            else:
                stack.pop()
                
        return True  # zwraca true jezeli jest spojny

    def amount_vertices(self):
        """Zwraca liczbe wierzcholkow w grafie"""
        return len(set(self.list_neighbors))

    def degrees_vertices(self):
        """Zwraca liste kolejnych stopni wierzcholkow w grafie"""
        amount_ver = self.amount_vertices()
        list_neighbors = list(self.list_neighbors)
        list_degrees = [list_neighbors.count(items) for items in
                        range(amount_ver)]  # zlicza wierzcholki w liscie i dodaje do nowej listy
        return list_degrees

    def check_Euler(self):
        degrees = list(self.degrees_vertices())
        even = []
        for values in degrees:
            if values % 2 == 0:
                even.append(values)

        if (len(even) == self.amount_vertices()) and self.DFS():
            print "Graf jest eulerowski"
        else:
            print "Graf nie jest eulerowski"

    def check_half_Euler(self):
        odd = []
        degrees = list(self.degrees_vertices())
        for values in degrees:
            if values % 2 != 0:
                odd.append(values)

        if len(odd) <= 2 and self.DFS():
            print "Graf jest poleulerowski"
        else:
            print "Graf nie jest poleulerowski"

#Przykladowe wywolanie:
list_neighbors = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 1, 2, 1, 4, 1, 5, 2, 3, 2, 4, 3, 5, 4, 5] # graf poleulerowski z przykladu
graf = Graph(list_neighbors)
graf.check_Euler()
graf.check_half_Euler()
