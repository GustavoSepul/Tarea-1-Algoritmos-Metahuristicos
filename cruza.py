import numpy as np
import random

def cruza_padres (p1, p2, p_cruza):
    c1, c2 = p1.copy (), p2.copy ()
    if(random.random()<p_cruza) :
        pt = np.random.randint (1, len (p1))
        print(pt)
        c1 = np.concatenate([p1[:pt], p2[pt:]])
        c2 = np.concatenate([p2[:pt], p1[pt:]])
    child1 = c1
    child2 = c2
    return [child1, child2]

