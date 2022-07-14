from math import pow, sqrt

class Norma_f:
    # Norma_Frobenius
    def __init__(self, matriz, linhas, colunas):
        self.matriz = matriz
        self.linhas = linhas
        self.colunas = colunas
        self.norma_f = 0
    
    def calcularNorma_f(self):
        # Calcular(retornando) a norma_Frobenius: raiz_quadrada(somatório(somatório((|aij|)^2)j=1,2,...,m)i=1,2,...,n)
        aux = 0
        for i in range(0, self.colunas):
            # somatório(somatório((|aij|)^2)i=1,2,...,m)j=1,2,...,n
            for j in range(0, self.linhas):
                # somatório((|aij|)^2)j=1,2,...,n
                aux += pow(self.matriz[i][j], 2)
        self.norma_f = sqrt(aux)
        return self.norma_f