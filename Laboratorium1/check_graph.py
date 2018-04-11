def vertices_deg(vertices_neighbors):
    """Zwraca stopnie grafow w liscie"""
    deg = []
    vertices_neighbors = dict(vertices_neighbors)
    for neighbors in vertices_neighbors.values():
        deg.append(len(neighbors))
    return deg


def is_graph_full(degs):
    """Sprawdza czy graf jest pelny
    Jezeli stopnie wierzcholkow sa o jeden mniejsze od ilosci wierzcholkow, to graf jest pelny"""
    degs = list(degs)
    for value in degs:
        if value == len(degs) - 1:
            pass
        else:
            print "Ten graf nie jest pelny"
            return None
    print "Ten graf jest pelny"


def is_tree(degs, count_vertices):
    """Sprawdza czy graf jest drzewem
    Jezeli liczba wierzchlkow jest o 1 mniejsza od liczby krawedzi i ma przynajmniej 2 liscie, to jest to drzewo"""
    degs = list(degs)
    leafs = []
    for values in degs:
        if values == 1:
            leafs.append(values)
    if len(degs) == count_vertices + 1 and len(leafs) >= 2:
        print "To jest drzewo"
    else:
        print "To nie jest drzewo"


def is_graph_cycle(degs):
    """Sprawdza czy graf jest cyklem
    Jezeli wszyskie wierzcholki grafu maja stopien rowny 2, to graf jest cyklem"""
    degs = list(degs)
    for value in degs:
        if value != 2:
            print "Ten graf nie jest cyklem"
            return None
    print "Ten graf jest cyklem"


def is_graph_regular(degs):
    """Sprawdza czy graf jest grafem k-regularnym
    Jezeli wszystki wierzcholki sa 'k' stopnia, to graf jest k-regularny"""
    degs = list(degs)
    v1 = degs[0]
    for value in degs:
        if value != v1:
            print "Ten graf nie jest regularny"
            return None
    print "Ten graf jest %i-regularny" % v1

def DFS (graph):
    """Funkcja przyjmuje biblioteke z lista sasiadow dla kazdego wierzcholka.
    Przeszukuje graf w glab, lecz nic nie zwraca"""
    stack = []
    actual_position = None
    visited_vertices = []
    amount_vertices = len(graph.items())

    actual_position = 1
    stack.append(actual_position)
    visited_vertices.append(actual_position)
    while stack != []:
        for items in graph.values():
            set(items) & set(stack) #compare list


#Przykladowe grafy, gdzie klucz to wierzcholek a lista do niego przypisana - sasiedzi

example_tree = {'1': ['2', '3'], '2': ['1', '4', '5'], '3': ['1'], '4': ['2'], '5': ['2']}  # drzewo
example_tree_edges = 4
example_graph_full = {'1': ['2', '3', '4', '5'], '2': ['1', '3', '4', '5'], '3': ['1', '2', '4', '5'], '4': ['1', '2', '3', '5'],
                      '5': ['1', '2', '3', '4']}  # graf pelny 5-wierzcholkowy
example_graph_cycle = {'1': ['2', '6'], '2': ['1', '3'], '3': ['2', '4'], '4': ['3', '5'], '5': ['4', '6'],
                       '6': ['5', '1']}  # graf cykliczny 6-wierzcholkowy
example_graph_regular = {'1': ['2', '3'], '2': ['1', '3'], '3': ['1', '2'], '4': ['5', '6'], '5': ['4', '6'], '6': ['4', '5']}  # graf 2-regularny


graph = vertices_deg(example_tree)
is_tree(graph,example_tree_edges)
is_graph_full(graph)
is_graph_cycle(graph)
is_graph_regular(graph)
