import numpy as np

def rectification(hijos, n):
    arr = np.arange(0,n)
    for i in range(len(hijos)):
        repetidos = [x for y, x in enumerate(hijos[i]) if x in hijos[i][:y]]
        opciones = [k for k in arr if k not in hijos[i]] 
        for j in arr:
            if hijos[i][j] in repetidos: 
                repetidos.remove(hijos[i][j])
                hijos[i][j] = np.random.choice(opciones,1)
                opciones.remove(hijos[i][j])
    return hijos


