import random
import sys 
import time
import numpy as np

if len(sys.argv) == 4:
    seed = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    print(seed, n, p)
else:
    print("error")

np.random.seed(seed)

poblacion = np.zeros((p,n),int)

for k in range(p):
    poblacion[k]=np.arange(0,n)
    np.random.shuffle(poblacion[k])
    
print(poblacion)