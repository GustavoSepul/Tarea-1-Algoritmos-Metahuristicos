import random
import sys 
import time
import numpy as np

seed = 1
n = 8
p = 8
print(seed, n, p)

np.random.seed(seed)

poblacion = np.zeros((p,n),int)

for k in range(p):
    poblacion[k]=np.arange(0,n)
    np.random.shuffle(poblacion[k])
    
print(poblacion)
