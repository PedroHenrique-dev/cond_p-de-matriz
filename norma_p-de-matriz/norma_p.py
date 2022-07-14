from math import pow, fabs

class Norma_p:
    def __init__(self, matriz, linhas, colunas):
        self.matriz = matriz
        self.linhas = linhas
        self.colunas = colunas
        self.norma_p = 0
    
    def calcularNorma_p(self):
        # Calcular(retornando) a norma_p: raiz_p(max((somatório((|aij|)^p)j=1,2,...,m)i=1,2,...,n))
        lista = []
        aux = 0
        p = int(input('\nDefina o valor da norma_(p): '))
        for i in range(self.colunas):
            for j in range(self.linhas):
                # (|aij|)^p)j=1,2,...,m
                aux += pow(fabs(self.matriz[i][j]), p)
            # ((somatório((|aij|)^p)j=1,2,...,m)i=1,2,...,n)
            lista.append(aux)
            aux = 0
        self.norma_p = pow(max(lista), 1/p)
        return self.norma_p, p