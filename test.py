import random
import networkx as nx # Genera un grafo dirigido aleatorio con n nodos y m aristas
def generar_grafo_dirigido_aleatorio(n, m):
    # Crea un grafo vacío
    G = nx.DiGraph() # Agrega nodos al grafo
    for i in range(n):
        G.add_node(i) # Agrega aristas aleatorias al grafo
    for i in range(m):
        # Elige dos nodos aleatorios
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)     # Agrega una arista del nodo u al nodo v
        G.add_edge(u, v)
    return G # Ejemplo de uso
     
grafo = generar_grafo_dirigido_aleatorio(20, 40)
print(grafo.edges())
