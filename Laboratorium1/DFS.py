def DFS(graph):
    """Funkcja przyjmuje biblioteke z lista sasiadow dla kazdego wierzcholka.
    Przeszukuje graf w glab, zwraca kolejnosc odwiedzanych wierzcholkow"""
    stack = []
    actual_position = '1'
    stack.append(actual_position)
    visited_vertices = []

    while True:
        for neighbors in graph.values():
            try:
                neighbors.remove(actual_position) #usun sasiadow o wartosci aktualnej pozycji dla wszystich wierzcholkow grafu
            except ValueError:
                pass

        visited_vertices.append(actual_position) #odwiedzone wierzcholki

        try:
            actual_position = min(graph[actual_position])  #przejdz do sasiada o najnizszym numerze
        except ValueError:
            stack.remove(actual_position)  # sciagamy ze stosu na stos
            if stack == []:
                return visited_vertices
            actual_position = stack.pop(-1)  # ustaw z wierzchu stosu pozycje aktualna

        stack.append(actual_position)  # dajemy na stos aktualna pozycje


#Przyklady:
example_tree = {'1': ['2', '3'], '2': ['1', '4', '5'], '3': ['1'], '4': ['2'], '5': ['2']}  # drzewo
print DFS(example_tree)

example_graph_full = {'1': ['2', '3', '4', '5'], '2': ['1', '3', '4', '5'], '3': ['1', '2', '4', '5'], '4': ['1', '2', '3', '5'],
                      '5': ['1', '2', '3', '4']}  # graf pelny 5-wierzcholkowy
print DFS(example_graph_full)