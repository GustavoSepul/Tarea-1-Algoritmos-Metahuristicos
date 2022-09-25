import random
import sys 
import time
import numpy as np

seed = 1
n = 8
p = 4

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
    
def FitnessFunction(poblacion):
    for i in range(0, 4):
        for j in range(0, 7):
            for k in range(j+1, 8):
                if poblacion[i][j]==poblacion[i][k]:
                    ValorFitness[i] += 1
                if poblacion[i][j]-poblacion[i][k] == j-k or poblacion[i][j]-poblacion[i][k] == k-j:
                    ValorFitness[i] += 1
                    
    for q in range(p):
        fitness.append(ValorFitness[q])
    return fitness

f = FitnessFunction(poblacion)

print(f)