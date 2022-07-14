from math import fabs

class Norma_inf:
    # Norma_infinita
    def __init__(self, matriz, linhas, colunas):
        self.matriz = matriz
        self.linhas = linhas
        self.colunas = colunas
        self.norma_inf = 0
    
    def calcularNorma_inf(self):
        # Calcular(retornando) a norma_infinito: max(somatório(|aij|)j=1,2,...,n)i=1,2,...,m
        lista = []
        aux = 0
        for i in range(0, self.colunas):
            for j in range(0, self.linhas):
                #s omatório(|aij|)j=1,2,...,n
                aux += fabs(self.matriz[i][j])
            # max(somatório(|aij|)j=1,2,...,n)i=1,2,...,m
            lista.append(aux)
            aux = 0
        self.norma_inf = max(lista)
        return self.norma_inf