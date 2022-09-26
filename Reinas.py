import random
import sys 
import time
import numpy as np


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
ValorFitness=[]
fitness=[]
for h in range(p):
    ValorFitness.append(0) 
    
def FuncionFitness(poblacion):
    for i in range(0, p):
        for j in range(0, n):
            for k in range(j+1, n):
                if poblacion[i][j]==poblacion[i][k]:
                    ValorFitness[i] += 1
                if poblacion[i][j]-poblacion[i][k] == j-k or poblacion[i][j]-poblacion[i][k] == k-j:
                    ValorFitness[i] += 1
                    
    for q in range(p):
        fitness.append(ValorFitness[q])
    return fitness

f = FuncionFitness(poblacion)

print(f)