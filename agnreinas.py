
import sys
import random
import time
import numpy as np


if len(sys.argv) == 4:
    semilla=int(sys.argv[1])
    tamaño_tablero=int(sys.argv[2])
    tamaño_población=int(sys.argv[3])
  
    print(semilla,tamaño_tablero,tamaño_población)
else:
    print("Error")
    print("Ingrese denuevo los parametros")
    sys.exit(0)

tiempo_proceso_ini = time.process_time()
np.random.seed(semilla)

poblacion = np.zeros((tamaño_población,tamaño_tablero),int)

for k in range(tamaño_población):
    poblacion[k]= np.arange(0,tamaño_tablero)
    np.random.shuffle(poblacion[k])

print(poblacion)

def fitness(tamaño_población):
    fitness = 0
    for i in range(len(tamaño_población)):
        fitness += tamaño_población[i] - tamaño_población[-i-1]
    return fitness

