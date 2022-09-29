import random
import sys 
import time
import numpy as np
from fitness import *
from cruza import *
from ruleta import *


#Definicion de variables
seed = int(input("Igrese la semilla:"))
n = int(input("Igrese el numero de reinas:"))
p = int(input("Igrese la población:"))

p_cruza = 1
mutacion = 1
iteraciones = 100

print(seed, n, p, cruza, mutacion, iteraciones)


tiempo_proceso_ini = time.process_time()

np.random.seed(seed)

poblacion = np.zeros((p,n),int)

for k in range(p):
	poblacion[k]=np.arange(0,n)
	np.random.shuffle(poblacion[k])
    
print(poblacion)


f = FuncionFitness(poblacion, p, n)
print(f)

'''
def FuncionSeleccion(f):
    probabilidad = np.sum(f)
    print(probabilidad)
    probabilidades = f/probabilidad
    probabilities = [sum(probabilidades[:i+1]) 
    for i in range(len(probabilidades))]
    pr = probabilities
    print(pr)
    r = random.random()
    print(r)
    seleccionado = []
    for (i, individual) in enumerate(poblacion):
        if r <= pr[i]:
            seleccionado=list(individual)
            break
    return seleccionado
'''    
    

aaa = Seleccionar_padres(poblacion, f, n)
# a = cruza()
print(aaa)
""""
def cruza(padre1, padre2, p_cruza):
    r = np.random.random()
    if(r < p_cruza):
        m = np.random.randint(1, n)
        hijo1 = np.concatenate([padre1[:m], padre2[m:]])
        hijo2 = np.concatenate([padre2[m:], padre1[:m]])
    else:
        hijo1 = padre1.copy()
        hijo2 = padre2.copy()
    return hijo1, hijo2

cruza_padres = cruza(aaa[0], aaa[1],p_cruza)
print(cruza_padres)
"""
def crossover (p1, p2, p_cruza):
    c1, c2 = p1.copy (), p2.copy ()
    if(random.random()<p_cruza) :
        pt = np.random.randint (1, len (p1))
        print(pt)
        c1 = np.concatenate([p1[:pt], p2[pt:]])
        c2 = np.concatenate([p2[:pt], p1[pt:]])
    child1 = c1
    child2 = c2
    return [child1, child2]

cruza_padres = crossover(aaa[0], aaa[1], p_cruza)

print(cruza_padres)