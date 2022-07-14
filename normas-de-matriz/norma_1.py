from math import fabs

class Norma_1:
    def __init__(self, matriz, linhas, colunas):
        self.matriz = matriz
        self.linhas = linhas
        self.colunas = colunas
        self.norma_1 = 0
    
    def calcularNorma_1(self):
        # Calcular(retornando) a norma_1: max(somatório(|aij|)i=1,2,...,m)j=1,2,...,n
        lista = []
        aux = 0
        for j in range(0, self.colunas):
            for i in range(0, self.linhas):
                # somatório(|aij|)i=1,2,...,m
                aux += fabs(self.matriz[i][j])
            # max(somatório(|aij|)i=1,2,...,n)j=1,2,...,n
            lista.append(aux)
            aux = 0
        self.norma_1 = max(lista)
        return self.norma_1