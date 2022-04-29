from norma_2 import Norma_2
from inversa import Inversa

class Matriz:
    def __init__(self, linhas, colunas, binario):
        # Armazenar os dados da matriz
        self.matriz = criarMatriz(linhas, colunas)
        self.linhas = linhas
        self.colunas = colunas
        self.matrizAux = criarMatrizAux(self.matriz, self.linhas, self.colunas)
        self.matrizInversa = Inversa(self.matrizAux, self.linhas, self.colunas)
        self.inversa = self.matrizInversa.calcularInversa()
        self.goNorma_2 = Norma_2(self.matriz, self.linhas, self.colunas)
        self.matrizNorma_2 = self.goNorma_2.calcularNorma_2()
        self.magmin = self.goNorma_2.calcularMagmin()
        self.goNorma_2 = Norma_2(self.inversa, self.linhas, self.colunas)
        self.inversaNorma_2 = self.goNorma_2.calcularNorma_2()
        self.cond = 0
        # cond(A) = ||A||*||A^(-1)|| ou magmax(A)/magmin(A)
        if binario == 1:
            self.cond = self.matrizNorma_2 * self.inversaNorma_2
        else:
            self.cond = self.matrizNorma_2 / self.magmin

    def mostrarMatriz(self):
        print(f'Matriz {self.linhas}x{self.colunas}:')
        for i in range(self.linhas):
            print(self.matriz[i])
        print()
        
    def mostrarInversa(self):
        print(f'Matriz Inversa {self.linhas}x{self.colunas}:')
        for i in range(self.linhas):
            print(self.inversa[i])
        print()

    def getMatrizNorma_2(self):
        return self.matrizNorma_2
    
    def getInversaNorma_2(self):
        return self.inversaNorma_2
    
    def getLinhas(self):
        return self.linhas
    
    def getColunas(self):
        return self.colunas
    
    def getCond(self):
        return self.cond


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def criarMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        list.append(matriz, [0]*colunas)
    print(f'Matriz {linhas}x{colunas}')
    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = float(input('Digite o valor da matriz[{}][{}]: '.format(i, j)))
    return matriz

def criarMatrizAux(matriz, linhas, colunas):
    matrizAux = []
    for i in range(linhas):
        list.append(matrizAux, [0]*colunas*2)
    for i in range(linhas):
        for j in range(colunas):
            matrizAux[i][j] = matriz[i][j]
            if i == j:
                matrizAux[i][colunas+j] = 1 
    return matrizAux