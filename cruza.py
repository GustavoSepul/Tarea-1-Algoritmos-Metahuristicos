import numpy as np
import random

def cruza_padres (padres):
    c1 = padres[0] 
    c2 = padres[1]
    hijos = []
    
    pt = np.random.randint (1, len (padres.T))
    # print(pt)
    c1 = np.concatenate([padres[0][:pt], padres[1][pt:]])
    c2 = np.concatenate([padres[1][:pt], padres[0][pt:]])
    hijos = np.append(hijos, c1)
    hijos = np.append(hijos, c2)
    return hijos

