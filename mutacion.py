import numpy as np

def mutacion(poblacion, p_mutacion):
    for i in range(len(poblacion)):
        nm_random = np.random.random()
        # print(nm_random)
        if(nm_random < p_mutacion):
            m = np.random.randint(0, len(poblacion.T)-1)
            n = np.random.randint(0, len(poblacion.T)-1)
            while m == n:
                n = np.random.randint(0, len(poblacion.T)-1)
            hijo_mut = poblacion[i]
            hijo_mut[m],hijo_mut[n] = hijo_mut[n],hijo_mut[m]
            poblacion[i] = hijo_mut
    return poblacion