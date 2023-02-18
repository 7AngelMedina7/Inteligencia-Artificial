import grafo_dirigido as GRD
import random
import timeit


# Lista de letras que se usarán como nodos
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
# Número de nodos en el grafo
num_nodos = 10
# Crear una lista de adyacencia vacía
grafo1 = {letra: [] for letra in letras}
# Agregar arcos aleatorios al grafo
for i in range(num_nodos):
    for j in range(num_nodos):
        # Se agrega un arco desde el nodo i al nodo j con una probabilidad del 25%
        if random.random() < 0.25:
            # Se utiliza la función random.choice() para seleccionar dos nodos aleatorios de la lista letras
            nodo_i = random.choice(letras)
            nodo_j = random.choice(letras)
            # Asegurarse de que el nodo de origen y destino no sean iguales
            while nodo_j == nodo_i:
                nodo_j = random.choice(letras)
            # Agregar el arco al grafo
            grafo1[nodo_i].append(nodo_j)
# Imprimir el grafo generado
grafo = grafo1
print(grafo1)
def testDirectedGraph():
    g = GRD.DirectedGraph(grafo)    #Crear el grafo con el diccionario de ejemplo
    print('Grafo')
    print(g)                    # Visualizar el grafo
    print('Iteración')
    for n in g:                 # Iterar sobre los nodos y arcos del grafo
        print(n)
        print(g.edges(n))
    print('Nodos:', g.nodes())  # Visualizar todos los nodos
    print('Arcos:', g.edges())  # Visualizar todos los arcos
    print('Arcos desde el nodo C:', g.edges('A'))   # Arcos desde un nodo A
    
if __name__ == '__main__':
    print("*********************************************************************************************")
    print('Tiempo: '+(str(timeit.timeit("testDirectedGraph()", setup="from __main__ import testDirectedGraph", number=1))+' segundos'))