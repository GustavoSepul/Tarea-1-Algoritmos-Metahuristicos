import numpy as np
import sys
import random
import time
""" np.zeros np.aranger np.random.seed np.random.shuffle"""

if len(sys.argv) == 4:
    semilla=int(sys.argv[1])
    n=int(sys.argv[2])
    p=int(sys.argv[3])
    print(semilla,n,p)
else:
    print("Error")
    print("Ingrese denuevo los parametros")
    sys.exit(0)

np.random.seed(semilla)

  



