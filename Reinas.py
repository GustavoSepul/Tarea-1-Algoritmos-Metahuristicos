import random
import sys 
import time
import numpy as np
from ruleta import *
from rectificacion import *
from mutacion import *


# Definicion de variables
# seed = int(input("Igrese la semilla:"))
# n = int(input("Igrese el numero de reinas:"))
# p = int(input("Igrese la población:"))
# p_cruza = float(input("Igrese la probabilidad de cruzar:"))
# p_mutacion = float(input("Igrese la probabilidad de mutacion:"))
# iteraciones = int(input("Igrese la cantidad de iteraciones:"))
if len(sys.argv) == 7:
    seed = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    p_cruza = float(sys.argv[4])
    p_mutacion = float(sys.argv[5])
    iteraciones = int(sys.argv[6])
    print(seed, n, p, p_cruza, p_mutacion, iteraciones)
else:
    print("error")
    sys.exit(0)


print(seed, n, p, p_cruza, p_mutacion, iteraciones)
tiempo_proceso_ini = time.process_time()

np.random.seed(seed)

poblacion = np.zeros((p,n),int)
for k in range(p):
	poblacion[k]=np.arange(0,n)
	np.random.shuffle(poblacion[k])
print(poblacion)

while iteraciones > 0:
    fit=FuncionFitness(poblacion, p, n)
    max_value = max(fit)
    if(max_value == (n*((n-1)/2))):
        break

    poblacion = Seleccionar_padres(poblacion, n, p_cruza, p)
    # print(i, poblacion)
    rectification(poblacion)
    # print(i, poblacion)
    mutacion(poblacion, p_mutacion)
    # print(i, poblacion)
    iteraciones= iteraciones -1

fit=FuncionFitness(poblacion, p, n)
max_value = max(fit)
mejor = fit.index(max_value)
print("Este es el mejor individuo: ",poblacion[mejor])
print("La cantidad de choques que tiene es de: ", (n*((n-1)/2))-max_value)
print("Tiempo de busqueda: ", tiempo_proceso_ini)