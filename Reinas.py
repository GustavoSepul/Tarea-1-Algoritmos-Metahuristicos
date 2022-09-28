import random
import sys 
import time
import numpy as np
from fitness import *


#Definicion de variables
seed = int(input("Igrese la semilla:"))
n = int(input("Igrese el numero de reinas:"))
p = int(input("Igrese la población:"))

cruza = 1
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

def FuncionSeleccion(f,p):
    probabilidad = np.sum(f)
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
            seleccionado.append(list(individual))
            break
    return seleccionado
    
selec = FuncionSeleccion(f,p)
print(selec)