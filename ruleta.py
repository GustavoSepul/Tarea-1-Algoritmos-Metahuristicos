import numpy as np
import random
from fitness import *
from cruza import *


def Seleccionar_padres(poblacion, reinas, p_cruza, p):
    padres = np.arange(2 * reinas).reshape(2, reinas) #Matriz que contiene a los padres que pueden tener descendencia
    nuevageneracion = []
    valor_fitness = FuncionFitness(poblacion, p, reinas)
    total = sum(valor_fitness)
    porcentaje_fitness = [x/total for x in valor_fitness]

    while(len(nuevageneracion) != p):
        fitness_acumulado = []
        j = 0
        for i in porcentaje_fitness: #Se calculan los porcentajes de la ruleta
            j+=i
            fitness_acumulado.append(j)
        print(fitness_acumulado)
        padres.clear()
        for r in range(2):#Ciclo para guardar los padres a cruzar
            n_random = random.uniform(0, 1)
            print(n_random)
            individual = 0
            for q in fitness_acumulado:#Se toma al padre correspondiente para cruzar
                if(n_random<=q):
                    padres[r]=poblacion[individual]
                    print(poblacion[individual])
                    break
                individual+=1  
        if(len(nuevageneracion) == p-1):
            nuevageneracion.append(padres[0])
        else:
            x = random.uniform(0, 1)
            if(x < p_cruza):
                hijos = cruza_padres()
                nuevageneracion.append(hijos)

    return nuevageneracion