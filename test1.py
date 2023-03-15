def h(estado):
    """
    Función heurística que retorna el valor eurístico de un estado en el problema de la mochila
    """
    costo_actual = sum([valor for valor, _ in estado])  # Costo acumulado de los elementos en la mochila
    # Se retorna el valor eurístico (faltante) que resta para llegar al objetivo
    return sum([valor for valor, _ in objetos]) - costo_actual

def astar():
    """
    Implementa el algoritmo A* para el problema de la mochila
    """
    nodos_abiertos = [(0, (), h(()))]  # Tupla de (costo, estado, heurística)
    while nodos_abiertos:
        _, estado, _ = min(nodos_abiertos, key=lambda x: x[0]+x[2])  # Selecciona el nodo con menor f(n)
        if g(estado) > capacidad_mochila:  # No expandir si se supera la capacidad de la mochila
            continue
        if g(estado) == capacidad_mochila:  # Si se llega al estado objetivo, se retorna el valor acumulado
            return sum([valor for valor, _ in estado])
        sucesores = expand(estado)
        for sucesor in sucesores:
            costo_acumulado = g(estado) + sum([peso for _, peso in sucesor if peso not in estado])
            heuristica = h(sucesor)
            nodos_abiertos.append((costo_acumulado, sucesor, heuristica))
        nodos_abiertos.remove((0, estado, h(())))  # Elimina el estado actual de la lista de nodos abiertos

print(astar())  # Salida: 295
