import random
import sys 
import time
import numpy as np
from ruleta import *
from rectificacion import *
from mutacion import *


#Definicion de variables
seed = int(input("Igrese la semilla:"))
n = int(input("Igrese el numero de reinas:"))
p = int(input("Igrese la población:"))
p_cruza = int(input("Igrese la probabilidad de cruzar:"))
p_mutacion = int(input("Igrese la probabilidad de mutacion:"))
iteraciones = int(input("Igrese la cantidad de iteraciones:"))

print(seed, n, p, p_cruza, p_mutacion, iteraciones)
tiempo_proceso_ini = time.process_time()

np.random.seed(seed)

poblacion = np.zeros((p,n),int)
for k in range(p):
	poblacion[k]=np.arange(0,n)
	np.random.shuffle(poblacion[k])
print(poblacion)


for i in range(iteraciones):
    poblacion = Seleccionar_padres(poblacion, n, p_cruza, p)
    # print(i, poblacion)
    rectification(poblacion)
    # print(i, poblacion)
    mutacion(poblacion, p_mutacion)
    # print(i, poblacion)

#seleccionFinal()




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
