# Koloruje graf na 2 kolory i sprawdza czy jest dwudzielny
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
            """Odejmuje od sasiadow odwiedzone wierzcholki"""
            for nums in vertices_visited:
                if nums in neighbors:
                    neighbors.remove(nums)

        def give_color(act_v, neigh):
            """Daj kolor dla aktualnego wierzcholka"""
            if act_v in color_x: # jezeli aktualny wierzcholek posiada kolor X
                color_y.append(neigh) # daj jego sasiadowi kolor Y
            elif act_v in color_y: # jezeli aktualny wierzcholek posiada kolor Y
                color_x.append(neigh) # daj jego sasiadowi kolor X

        def check_color(act_v, all_neighs):
            """Sprawdza czy aktualny wierzcholek nie posiada sasiadow z tym samym kolorem"""
            for n in all_neighs:
                if (act_v in color_x and n in color_x) or (act_v in color_y and n in color_y):
                    print "Graf nie jest dwudzielny, wierzcholek %s ma ten sam kolor co %s" % (act_v, n)
                    exit()

        l_ver = sorted(list(set(self.list_neighbors)))
        l_edg = list_edges()
        actual_vertices = self.list_neighbors[0]
        stack = []
        vertices_visited = []
        color_x = [] #kolor 1
        color_y = [] #kolor 2

        vertices_visited.append(actual_vertices)
        stack.append(actual_vertices)
        color_x.append(actual_vertices)

        while True:
            # Warunki, gdyby graf nie byl spojny
            if stack == [] and sorted(vertices_visited) != l_ver:  # jezeli jest cos jeszcze do przeszukania
                a = [x for x in l_ver if x not in vertices_visited]
                stack.append(a[0])
                vertices_visited.append(a[0])
                color_x.append(a[0])
            elif stack == [] and sorted(vertices_visited) == l_ver:  # jezeli przeszukales wszystko
                print "Graf jest dwudzielny"
                print 'x =', color_x
                print 'y =', color_y
                return None

            actual_vertices = stack[-1]
            neighbors = neighbors_v(actual_vertices)
            neighbors_substract_visited()

            if neighbors != []: #jezeli wierzcholek posiada sasiadow
                give_color(actual_vertices, sorted(neighbors)[0]) #daj jego sasiadowi kolor
                actual_vertices = sorted(neighbors)[0] #sasiad pierwszy w kolejnosci jest aktualnym wierzcholkiem
                check_color(actual_vertices, neighbors_v(actual_vertices))  # sprawdz czy wszyscy sasiedzi nie maja tego samego koloru
                vertices_visited.append(actual_vertices)
                stack.append(actual_vertices)
            else:
                stack.pop()

# Przykladowe wywolania:
# Wiecej przykladow:
ln1 = [1, 2, 1, 4, 2, 3, 3, 4] # graf dwudzielny spojny x=[1, 3], y=[2, 4]
ln2 = [1, 2, 1, 5, 2, 3, 3, 4, 4, 5] # grf nie-dwudzielny spojny x=[1, 3, 5], y=[2, 4]
ln3 = [1, 2, 1, 4, 2, 3, 3, 4, 5, 6] # graf dwudzielny, niespojny x=[1, 3] + 5/6,  y=[2,4] + 5/6
ln4 = [1, 2, 1, 3, 2, 3, 4, 5] # graf nie-dwudzielny niespojny x=[1,3] +4/5 y=[2] + 4/5
ln5 = [1, 2, 1, 3, 2, 4, 2, 5, 3, 6, 5, 7] # graf dwudzielny, spojny (drzewo) x = [1,4,5,6] y = [2,3,7]
ln6 = [1, 2, 1, 3, 1, 4, 2, 3, 2, 4, 3, 4] # graf niedwudzielny, spojny (pelny) x = [1,3] y = [2,4]
ln7 = [1, 2, 1, 4, 2, 3, 3, 4, 5] # samotny wierzcholek, ktory mozna rowniez pokolorowac

#graf1 = Graph(ln1)
#graf2 = Graph(ln2)
#graf3 = Graph(ln3)
#graf4 = Graph(ln4)
#graf5 = Graph(ln5)
#graf6 = Graph(ln6)
#graf7 = Graph(ln7)


#print "------------graf1"
#graf1.DFS()
#print "------------graf2"
#raf2.DFS()
#print "------------graf3"
#graf3.DFS()
#print "------------graf4"
#graf4.DFS()
#print "------------graf5"
#graf5.DFS()
#print "------------graf6"
#graf6.DFS()
#print "------------graf7"
#graf7.DFS()
