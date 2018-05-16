# Koloruje graf na minimalna ilosc kolorow
# Skrypt do zmiany:
# COMMAND="python2 Alghoritm_LF.py $1"

# pobranie danych z flagami lub bez nich:
import sys
result = sys.argv[1] #flagi -c, -ch
if '/' in result: #jezeli nic nie podales, bedzie sciezka
    arg = sys.argv[1]
else:
    arg = sys.argv[2]

f = open(arg, mode='r')
a = f.read()
a = a.split()
edg_list = [int(item) for item in a]
f.close()

#klasa graf
class Graph:

    def __init__(self, list_neighbors):
        self.list_neighbors = list_neighbors

    def ColorGraph(self):
        """Przeszukuje graf w glab, sprawdza czy jest spojny"""
        def bubble_sort(l):
            for item in range(len(l) - 1):  # dl 5 [0,1,2,3,4]
                if l[item] > l[item + 1]:
                    l[item], l[item + 1] = l[item + 1], l[item]
                    bubble_sort(l)
            return l

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
            return set(neigbors_v)

        def check_color(all_neigh):
            """Sprawdz kolory sasiadow"""
            for v, c in vertices_colors:
                if v in all_neigh:
                    try:
                        l_colors.remove(c) #jezeli juz kolor zostal odjety
                    except ValueError:
                        pass

        def give_color(act_v):
            """Daj kolor dla aktualnego wierzcholka"""
            vertices_colors.append((act_v, l_colors[0]))

        def sort_by_degrees(l_neigh):
            """Oddaje nowa, posortowana liste po stopniach wierzcholkow"""
            list_v = []
            degree_and_v = []
            for v in set(l_neigh):
                degree = len(neighbors_v(v))
                degree_and_v.append((degree, v))

            degree_and_v = bubble_sort(degree_and_v)
            for pair in degree_and_v[::-1]:
                list_v.append(pair[1])
            return list_v

        def colored():
            """Kolejne kolorowanie LF"""
            colored_list = []
            for v, c in vertices_colors:
                colored_list.append(c)
            return colored_list

        def chromatic_number():
            """Liczb chromatyczna"""
            chromatic_list = []
            for v, c in vertices_colors:
                chromatic_list.append(c)
            return len(set(chromatic_list))


        l_ver = bubble_sort(list(set(self.list_neighbors))) # [0,1,2,3,4,5]
        l_edg = list_edges() # [(0,1),(0,4),(1,2),(1,4),(1,5),(2,3),(3,4),(3,5),(4,5)]
        l_deg = sort_by_degrees(self.list_neighbors) # [4,1,5,3,2,0]
        actual_vertices = self.list_neighbors[0]
        vertices_colors = [] # struktura [(v, c)], czyli [(vertices, color)]

        while l_deg != []:
            l_colors = range(len(l_ver))
            actual_vertices = l_deg[0]
            check_color(neighbors_v(actual_vertices))
            give_color(actual_vertices)
            l_deg.remove(actual_vertices)
        if '-ch' in result:
            print "Liczba chromatyczna: ", chromatic_number()
	    return " "
        if '-c' in result:
            print "Lista kolorowania: ", colored()
            return " "
        else:
            print "Lista kolorowania: ", colored()
            print "Liczba chromatyczna: ", chromatic_number()
            return " "

graf1 = Graph(edg_list)
print graf1.ColorGraph()
