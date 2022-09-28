import random
import sys 
import time
import numpy as np
from fitness import *



seed = int(input("Igrese la semilla:"))
n = int(input("Igrese el numero de reinas:"))
p = int(input("Igrese la población:"))

print(seed,n,p)


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
    probabilidades = []
    probabilidad = np.sum(f)
    
    probabilidades.append(f/probabilidad)
    return probabilidades

pr = FuncionSeleccion(f,p)
print(pr[0])