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
p_cruza = float(input("Igrese la probabilidad de cruzar:"))
p_mutacion = float(input("Igrese la probabilidad de mutacion:"))
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

fit=FuncionFitness(poblacion, p, n)
max_value = max(fit)
mejor = fit.index(max_value)
print("Este es el mejor individuo tras: ",poblacion[mejor])
print("La cantidad de errores que tiene es de: ", (n*((n-1)/2))-max_value)