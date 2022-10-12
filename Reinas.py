import random
import sys 
import time
import numpy as np
from ruleta import *
from rectificacion import *
from mutacion import *

if len(sys.argv) == 7:
    seed = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    p_cruza = int(sys.argv[4])
    p_mutacion = int(sys.argv[5])
    iteraciones = int(sys.argv[6])
    print(seed, n, p, p_cruza, p_mutacion, iteraciones)
    if(seed < 0):
        print("Error: El número de la semilla debe ser positivo\nIngrese un numero de semilla positivo")
        sys.exit(0)
    if(n < 4):
        print("Error: El tamaño del tablero debe ser mayor a 3\nIngrese un tamaño de tablero mayor a 3")
        sys.exit(0)
    if(p < 3):
        print("Error: El tamaño de la población debe ser mayor a 2\nIngrese un tamaño de población mayor a 2")
        sys.exit(0)
    if(p_cruza > 100 or p_cruza < 0):
        print("Error: La probabilidad de cruza debe ser entre 0 y 100\nIngrese una probabilidad de cruza entre 0 y 100")
        sys.exit(0)
    if(p_cruza > 100 or p_cruza < 0):
        print("Error: La probabilidad de mutación debe ser entre 0 y 100\nIngrese una probabilidad de mutación entre 0 y 100")
        sys.exit(0)    
else:
    print("Error: Los datos ingresados no son validos, ingrese los datos de la siguiente manera:")
    print("python.exe .\Reinas.py semilla tamaño_tablero tamaño_población probabilidad_cruza probabilidad_mutación número_iteraciones")
    sys.exit(0)


p_cruza = p_cruza/100
p_mutacion = p_mutacion/100

tiempo_proceso_ini = time.process_time()
i = 0
np.random.seed(seed)

poblacion = np.zeros((p,n),int)
for k in range(p):
	poblacion[k]=np.arange(0,n)
	np.random.shuffle(poblacion[k])
print("Poblacion inicial :")
print(poblacion)

while iteraciones > 0:
    fit=FuncionFitness(poblacion, p, n)
    max_value = max(fit)
    if(max_value == (n*((n-1)/2))):
        break

    poblacion = Seleccionar_padres(poblacion, n, p_cruza, p)
    # print(i, poblacion)
    rectification(poblacion,n)
    # print(i, poblacion)
    mutacion(poblacion, p_mutacion)
    # print(i, poblacion)
    iteraciones= iteraciones -1
    i=i+1

fit=FuncionFitness(poblacion, p, n)
max_value = max(fit)
mejor = np.where(fit==max_value)
print("Este es el mejor individuo tras", i,"iteraciones: \n",poblacion[mejor[0][0]])
print("La cantidad de choques que tiene es de: ", int((n*((n-1)/2))-max_value))
print("Tiempo de busqueda: ", tiempo_proceso_ini, "segundos")