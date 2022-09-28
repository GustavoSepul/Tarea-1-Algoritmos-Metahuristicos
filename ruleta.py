import numpy as np
import random


def Seleccionar_padres(poblacion,valor_fitness):
    padres = np.arange(8).reshape(2, len(poblacion))
    total = sum(valor_fitness)
    porcentaje_fitness = [x/total for x in valor_fitness]
    fitness_acumulado = []
    j = 0
    for i in porcentaje_fitness:
        j+=i
        fitness_acumulado.append(j)
    print(fitness_acumulado)
    for r in range(2):
        n_random = random.uniform(0, 1)
        print(n_random)
        individual = 0
        for q in fitness_acumulado:
            if(n_random<=q):
                padres[r]=poblacion[individual]
                print(poblacion[individual])
                break
            individual+=1
        
    return padres