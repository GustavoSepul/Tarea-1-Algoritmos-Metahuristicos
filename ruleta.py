import numpy as np
import random
from fitness import *
from cruza import *


def Seleccionar_padres(poblacion, reinas, p_cruza, p):
    padres = np.arange(2 * reinas).reshape(2, reinas) #Matriz que contiene a los padres que pueden tener descendencia
    nuevageneracion = np.arange(p*reinas).reshape(p, reinas)      
    # print(padres)
    valor_fitness = FuncionFitness(poblacion, p, reinas)
    total = sum(valor_fitness)
    porcentaje_fitness = [x/total for x in valor_fitness]
    ngcont = 0

    while(ngcont < p):
        fitness_acumulado = []
        j = 0
        for i in porcentaje_fitness: #Se calculan los porcentajes de la ruleta
            j+=i
            fitness_acumulado.append(j)
        # print(fitness_acumulado)
        primerpadre = -1
        padres_cont = 0 
        while(padres_cont != 2):
            n_random = random.uniform(0, 1)
            # print(n_random)
            individual = 0
            for q in fitness_acumulado:#Se toma al padre correspondiente para cruzar
                if(n_random<=q and individual != primerpadre):
                    padres[padres_cont]=poblacion[individual]
                    # print(poblacion[individual])
                    primerpadre = individual
                    padres_cont += 1
                    break
                individual+=1  
        if(ngcont == p-1):
            nuevageneracion.append(padres[0])
        else:
            x = random.uniform(0, 1)
            if(x < p_cruza):
                hijos = cruza_padres(padres)
                nuevageneracion[ngcont] = hijos[0]
                ngcont += 1
                nuevageneracion[ngcont] = hijos[1]
                ngcont += 1

    return nuevageneracion