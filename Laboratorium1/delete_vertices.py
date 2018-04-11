def delete_vertice(graph, v_to_del):
    """Usuwa wierzcholek i jego krawedzie"""
    graph = dict(graph)
    v_to_del = str(v_to_del)
    for values in graph.values():
        try:
            values.remove(v_to_del)  #usun sasiadow o wartosci wierzcholka dla wszystich wierzcholkow grafu
        except ValueError:
            pass
    graph.pop(v_to_del) #usun wierzcholek
    return graph


#Przyklad:
example_tree = {'1': ['2', '3'], '2': ['1', '4', '5'], '3': ['1'], '4': ['2'], '5': ['2']}  # drzewo
print delete_vertice(example_tree, '1')

