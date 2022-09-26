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

print(f)