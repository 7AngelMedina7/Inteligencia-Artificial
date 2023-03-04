import timeit
import grafo_ponderado as GRP
import instance_generador as ig


nodes_dict = {
    'A': {'adjacents': {'B': 8, 'C': 1}, 'weight': 10, 'value': 269},
    'B': {'adjacents': {'D': 9, 'E': 5}, 'weight': 55, 'value': 95},
    'C': {'adjacents': {'F': 3, 'G': 7}, 'weight': 10, 'value': 4},
    'D': {'adjacents': {'H': 2}, 'weight': 47, 'value': 60},
    'E': {'adjacents': {'I': 1}, 'weight': 5, 'value': 32},
    'F': {'adjacents': {'J': 1}, 'weight': 4, 'value': 23},
    'G': {'adjacents': {'J': 4, 'K': 5}, 'weight': 50, 'value': 72},
    'H': {'adjacents': {'K': 4}, 'weight': 8, 'value': 80},
    'I': {'adjacents': {'K': 1}, 'weight': 61, 'value': 62},
    'J': {'adjacents': {'K': 2}, 'weight': 85, 'value': 65},
    'K': {'adjacents': {}, 'weight': 87, 'value': 46}
}

instance = ig.create_instance(nodes_dict)
def testGrafo():
    grafo = ig.create_instance(instance)
    g = GRP.WeightedGraph(grafo)    # Crear el grafo con el diccionario de ejemplo
    while(len(g.isolatedNodes ())>0):
        grafo= ig.create_instance(10)
        g=GRP.WeightedGraph(grafo)

    print('Grafo')
    print(g)                    # Visualizar el grafo
    print('Iteración')
    for n in g:                 # Iterar sobre los nodos y arcos del grafo
        print(n)
        print(g.edges(n))
    print('Nodos:', g.nodes())  # Visualizar todos los nodos
    print('Arcos:', g.edges())  # Visualizar todos los arcos
    print('Arcos desde el nodo C:', g.edges('C'))   # Arcos desde un nodo

if __name__ == '__main__':
    print("*********************************************************************************************")
    testGrafo()
    ##print(str(timeit.timeit("testGrafo()", setup="from __main__ import testGrafo", number=1)))