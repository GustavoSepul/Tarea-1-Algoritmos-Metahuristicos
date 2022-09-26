
def FuncionFitness(poblacion, p, n):
    ValorFitness=[]
    fitness=[]
    for h in range(p):
        ValorFitness.append(0) 
    for i in range(0, p):
        for j in range(0, n):
            for k in range(j+1, n):
                if poblacion[i][j]==poblacion[i][k]:
                    ValorFitness[i] += 1
                if poblacion[i][j]-poblacion[i][k] == j-k or poblacion[i][j]-poblacion[i][k] == k-j:
                    ValorFitness[i] += 1
                    
    for q in range(p):
        fitness.append(ValorFitness[q])
    return fitness