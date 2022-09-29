import numpy as np
def mutacion(hijo_rec, p_mutacion):
    nm_random = np.random.random()
    print(nm_random)
    if(nm_random < p_mutacion):
        m = np.random.randint(0, hijo_rec.size)
        n = np.random.randint(0, hijo_rec.size)
        while m == n:
            n = np.random.randint(0, hijo_rec.size)
        hijo_rec[m],hijo_rec[n] = hijo_rec[n],hijo_rec[m]
    return hijo_rec

padres = np.arange(3 * 4).reshape(3, 4)
print(padres[0].size)
print(padres[0])
aa = mutacion(padres[0],0.5)
print(aa)