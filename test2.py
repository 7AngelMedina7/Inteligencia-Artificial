import random

# Lista de letras que se usarán como nodos
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# Número de nodos en el grafo
num_nodos = 10

# Crear una lista de adyacencia vacía
grafo = {letra: [] for letra in letras}

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
            grafo[nodo_i].append(nodo_j)

# Imprimir el grafo generado
print(grafo)