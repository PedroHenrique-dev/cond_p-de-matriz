from math import pow, sqrt, fabs

class Norma_2:
    def __init__(self, matriz, linhas, colunas):
        self.matriz = matriz
        self.linhas = linhas
        self.colunas = colunas
        self.norma_2 = 0

    def calcularNorma_2(self):
        # Calcular(retornando) a magmax: raiz_2(max((somatório((|aij|)^2)j=1,2,...,m)i=1,2,...,n))
        lista = []
        aux = 0
        for i in range(0, self.linhas):
            for j in range(0, self.colunas):
                # somatório((|aij|)^2)j=1,2,...,m
                aux += pow(fabs(self.matriz[i][j]), 2)
            # (somatório((|aij|)^2)j=1,2,...,m)i=1,2,...,n
            lista.append(aux)
            aux = 0
        self.norma_2 = sqrt(max(lista))
        return self.norma_2