import random
import timeit

def knapsack_ihb(capacity, weights, values, max_iterations):
    n = len(weights)
    # Punto de partida: solución aleatoria
    best_selection = [random.randint(0, 1) for _ in range(n)]
    best_value = sum([v for v, s in zip(values, best_selection) if s])
    # Iterar varias veces mejorando la solución actual
    for k in range(1, max_iterations+1):
        # Obtener las k mejores soluciones vecinas
        neighbors = []
        for i in range(n):
            neighbor = best_selection.copy()
            neighbor[i] = 1 - neighbor[i]
            value = sum([v for v, s in zip(values, neighbor) if s])
            if value > best_value:
                neighbors.append((value, neighbor))
        neighbors = sorted(neighbors, reverse=True)[:k]
        # Elegir una solución vecina al azar
        if len(neighbors) > 0:
            best_value, best_selection = random.choice(neighbors)
    # Devolver la mejor solución encontrada
    return best_value, best_selection

def main():
    weights = [84,83,43,4,44,6,82,92,25,83,56,18,58,14,48,70,96,32,68,92]
    # primero
    values = [91,72,90,46,55,8,35,75,61,15,77,40,63,75,61,15,77,40,63,75,29,75,29,75,17,78,40,44]
    capacity = 269
    max_iterations = 100
    best_value, best_selection = knapsack_ihb(capacity, weights, values, max_iterations)
    print("Mejor valor de la mochila:", best_value)
    print("Elementos seleccionados:")
    for i, x in enumerate(best_selection):
        if x:
            print("- Elemento", i+1, "(peso:", weights[i], ", valor:", values[i], ")")

if __name__ == '__main__':
    print('Tiempo: '+(str(timeit.timeit("main()", setup="from __main__ import main", number=1))+' segundos'))
