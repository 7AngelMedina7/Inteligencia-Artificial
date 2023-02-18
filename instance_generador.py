import random

#Generardor de instancias para grafos ponderados
##num_nodos=100
def create_instance(num_nodos):
 instance={}
 for i in range(1,num_nodos+1):
    #Cuantos nodos adyacentes tiene el nodo i
    cuantos_adyacentes= random.randint(1,num_nodos-1)
    listas_nodos_adyacentes= random.sample(range(1,num_nodos),cuantos_adyacentes)
    while(i in listas_nodos_adyacentes):
        cuantos_adyacentes=random.randint(1,num_nodos-1)
        listas_nodos_adyacentes=random.sample(range(1,num_nodos),cuantos_adyacentes)

    lista_tuplas=[]
    for j in range(0,len(listas_nodos_adyacentes)):
        lista_tuplas.append((listas_nodos_adyacentes[j],random.randint(1,100)))
    instance[i]= lista_tuplas
 #print(instance)
 return (instance)    

