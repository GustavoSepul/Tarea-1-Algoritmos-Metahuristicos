import random
import sys 
import time
import numpy as np
from fitness import *


if len(sys.argv) == 4:
    seed=int(sys.argv[1])
    n=int(sys.argv[2])
    p=int(sys.argv[3])
  
    print(seed,n,p)
else:
    print("Error")
    print("Ingrese denuevo los parametros")
    sys.exit(0)

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
print(aaa)