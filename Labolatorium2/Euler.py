#Sprawdz czy graf jest Eulerowski lub poleulerowski

def DFS(list_neighbors, l_edg):
    """Przeszukuje graf w glab, sprawdza czy jest spojny"""
    list_vertices = list(set(list_neighbors))
    actuall_vertices = None
    stack = []
    vertices_visited = []

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


    actuall_vertices = list_vertices[0]
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

    return True #zwraca true jezeli jest spojny


def list_edges(list_neighbors):
    """Zwraca nowa liste z parami wierzcholkow (krawedziami grafu): [(v1,v2),(v1,v3),...]"""
    list_neighbors = list(list_neighbors)
    list_edg = zip(list_neighbors[::2], list_neighbors[1::2])
    return list_edg


def amount_vertices(list_neighbors):
    """Zwraca liczbe wierzcholkow w grafie"""
    return len(set(list_neighbors))


def degrees_vertices(list_neighbors, amount_ver):
    """Zwraca liste kolejnych stopni wierzcholkow w grafie"""
    list_neighbors = list(list_neighbors)
    list_degrees = [list_neighbors.count(items) for items in range(amount_ver)] #zlicza wierzcholki w liscie i dodaje do nowej listy
    return list_degrees

def check_Euler(degrees):
    degrees = list(degrees)
    for values in degrees:
        if values % 2 != 0:
            return False
    return True

def check_half_Euler(degrees):
    odd =[]
    degrees = list(degrees)
    for values in degrees:
        if values % 2 != 0:
            odd.append(values)

    if len(odd) > 2:
        return False
    else:
        return True


list_neighbors = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 1, 2, 1, 4, 1, 5, 2, 3, 2, 4, 3, 5, 4, 5] # graf poleulerowski z przykladu

ver_amount = amount_vertices(list_neighbors)
degs_v = degrees_vertices(list_neighbors, ver_amount)
l_edg = list_edges(list_neighbors)
first_condition = DFS(list_neighbors, l_edg)

if check_Euler(degs_v) and  DFS(list_neighbors, l_edg):
    print "Graf jest eulerowski"
elif check_half_Euler(degs_v) and DFS(list_neighbors, l_edg):
    print "Graf jest poleulerowski"
else:
    print "Graf nie jest eulerowski jak rowniez nie jest poleulerowski"
