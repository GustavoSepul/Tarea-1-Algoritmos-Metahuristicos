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
    

aaa = Seleccionar_padres(poblacion,f)
# a = cruza()
print(aaa)