import numpy as np

def cruza(padre1, padre2, p_cruza):
    r = np.random.random()
    if(r < p_cruza):
        nc_random = np.random.randint(1, n)
        hijo1 = padre1([padre1[:nc_random], padre2[nc_random:]])
        hijo2 = padre2([padre2[nc_random:], padre1[:nc_random]])
    else:
        hijo1 = padre1.copy()
        hijo2 = padre2.copy()
    return hijo1, hijo2