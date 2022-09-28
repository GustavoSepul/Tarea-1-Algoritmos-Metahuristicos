
import sys
import random
import time
import numpy as np
from fitness import *


if len(sys.argv) == 4:
    semilla=int(sys.argv[1])
    tamaño_tablero=int(sys.argv[2])
    tamaño_poblacion=int(sys.argv[3])
  
    print(semilla,tamaño_tablero,tamaño_poblacion)
else:
    print("Error")
    print("Ingrese denuevo los parametros")
    sys.exit(0)

tiempo_proceso_ini = time.process_time()
np.random.seed(semilla)

poblacion = np.zeros((tamaño_poblacion,tamaño_tablero),int)

for k in range(tamaño_poblacion):
    poblacion[k]= np.arange(0,tamaño_tablero)
    np.random.shuffle(poblacion[k])

print(poblacion)

f = FuncionFitness(poblacion, tamaño_poblacion, tamaño_tablero)


print(f)

def FuncionSeleccion(f,tamaño_poblacion):
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
    
selec = FuncionSeleccion(f,tamaño_poblacion)
print(selec)

selec2= FuncionSeleccion(f,tamaño_poblacion)

print(selec2)