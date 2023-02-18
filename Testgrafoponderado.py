import timeit
import grafo_ponderado as GRP
import instance_generador as ig

def testGrafo():
    grafo = ig.create_instance(10)
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
    print('Tiempo: '+(str(timeit.timeit("testGrafo()", setup="from __main__ import testGrafo", number=1))+' segundos'))