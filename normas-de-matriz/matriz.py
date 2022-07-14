from norma_1 import Norma_1
from norma_2 import Norma_2
from norma_inf import Norma_inf
from norma_f import Norma_f

class Matriz:
    def __init__(self, linhas, colunas):
        #Armazenar os dados da matriz
        self.matriz = criarMatriz(linhas, colunas)
        self.linhas = linhas
        self.colunas = colunas

        # norma_1
        self.goNorma_1 = Norma_1(self.matriz, linhas, colunas)
        self.norma_1 = self.goNorma_1.calcularNorma_1()
        
        # norma_2
        self.goNorma_2 = Norma_2(self.matriz, self.linhas, self.colunas)
        self.norma_2 = self.goNorma_2.calcularNorma_2()

        # norma_oo
        self.goNorma_inf = Norma_inf(self.matriz, linhas, colunas)
        self.norma_inf = self.goNorma_inf.calcularNorma_inf()

        # norma_frobenius
        self.goNorma_f = Norma_f(self.matriz, linhas, colunas)
        self.norma_f = self.goNorma_f.calcularNorma_f()

    def mostrarMatriz(self):
        print(f'\nMatriz {self.linhas}x{self.colunas}:')
        for i in range(0, self.linhas):
            print(self.matriz[i])
        print()
    
    def getNorma_1(self):
        return self.norma_1
    
    def getNorma_2(self):
        return self.norma_2

    def getNorma_inf(self):
        return self.norma_inf
    
    def getNorma_f(self):
        return self.norma_f

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def criarMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        list.append(matriz, [0]*colunas)
    print(f'\nMatriz {linhas}x{colunas}')
    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = float(input('Digite o valor da matriz[{}][{}]: '.format(i, j)))
    return matriz