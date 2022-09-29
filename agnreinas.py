
import sys
import random
import time
import numpy as np
from fitness import *
import itertools


if len(sys.argv) == 5:
    semilla=int(sys.argv[1])
    tamaño_tablero=int(sys.argv[2])
    tamaño_poblacion=int(sys.argv[3])
    p_cruza = float(sys.argv[4])
    #p_mutacion = float(sys.argv[5])
  
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

def Seleccionar_padres(poblacion,valor_fitness):
  padres = []
  total = sum(valor_fitness)
  porcentaje_fitness = [x/total for x in valor_fitness]
  fitness_acumulado = []
  j = 0
  for i in porcentaje_fitness:
    j+=i
    fitness_acumulado.append(j)
  print(fitness_acumulado)
  for r in range(2):
    n_random = random.uniform(0, 1)
    print(n_random)
    individual = 0
    for q in fitness_acumulado:
      if(n_random<=q):
        padres.append(poblacion[individual])
        print(poblacion[individual])
        break
      individual+=1
      
  return padres
aaa = Seleccionar_padres(poblacion,f)


def cruza_padres(padre1, padre2, p_cruza):
    nc_random = np.random.random()

    if(nc_random < p_cruza):
        m = np.random.randint(1, tamaño_poblacion)
        hijo1 = np.concatenate([padre1[:m], padre2[m:]])
        hijo2 = np.concatenate([padre2[:m],padre1[m:]])
    else:
        hijo1 = padre1.copy()
        hijo2 = padre2.copy()

    return hijo1, hijo2


cruza = cruza_padres(aaa[0],aaa[1], p_cruza)

print(cruza)

def mutacion(individual, p_mutacion):
    nm_random = np.random.random()
    if(nm_random < p_mutacion):
        m = np.random.randint(1, tamaño_poblacion)
        individual[m] = np.random.randint(1, tamaño_poblacion)
    return individual



