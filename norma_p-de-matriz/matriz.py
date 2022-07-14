from norma_p import Norma_p
from random import randint

class Matriz:
    def __init__(self, linhas, colunas):
        # Armazenar os dados da matriz
        self.matriz = criarMatriz(linhas, colunas)
        self.linhas = linhas
        self.colunas = colunas
        self.goNorma_p = Norma_p(self.matriz, linhas, colunas)
        self.norma_p = self.goNorma_p.calcularNorma_p()

    def mostrarMatriz(self):
        print()
        print(f'Matriz {self.linhas}x{self.colunas}:')
        for i in range(self.linhas):
            print(self.matriz[i])
        print()
    
    def getNorma_p(self, position):
        return self.norma_p[position]

def criarMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        list.append(matriz, [0]*colunas)
    print(f'\nMatriz {linhas}x{colunas}')
    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = float(input('Digite o valor da matriz[{}][{}]: '.format(i, j)))
    return matriz