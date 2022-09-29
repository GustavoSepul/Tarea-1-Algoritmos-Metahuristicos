import numpy as np
import random


def Seleccionar_padres(poblacion, valor_fitness, reinas):#,cruza
    padres = np.arange(2 * reinas).reshape(2, reinas) #Matriz que contiene a los padres que pueden tener descendencia

    
    total = sum(valor_fitness)
    porcentaje_fitness = [x/total for x in valor_fitness]
    fitness_acumulado = []
    j = 0
    for i in porcentaje_fitness: #Se calculan los porcentajes de la ruleta
        j+=i
        fitness_acumulado.append(j)
    print(fitness_acumulado)
    seleccionados = []
    seleccionados.clear()
    for r in range(2):#Ciclo para guardar los padres a cruzar
        n_random = random.uniform(0, 1)
        print(n_random)
        individual = 0
        for q in fitness_acumulado:#Se toma al padre correspondiente para cruzar
            if(n_random<=q):
                padres[r]=poblacion[individual]
                seleccionados.append(individual)
                print(poblacion[individual])
                break
            individual+=1   
    '''
    x = random.uniform(0, 1)
    if(x < cruza):
        cruzar()
        poblacion.pop(seleccionados[0])
        poblacion.pop(seleccionados[1])
    '''    
    return padres