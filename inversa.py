class Inversa:
    def __init__(self, matriz, linhas, colunas):
        # Armazenar os dados da matriz inversa
        # Recebe uma matriz B=[A|I]
        self.matriz = matriz
        self.linhas = linhas
        self.colunas = colunas

    def calcularInversa(self):
        multiplicador = 0
        pivor = 0
        # Método de Gauss-Jordan aplicado em B
        while pivor < self.linhas and pivor < self.colunas:
            multiplicador = 1/self.matriz[pivor][pivor]
            for j in range(self.colunas*2):
                self.matriz[pivor][j] *= multiplicador
            for i in range(0, self.linhas):
                if pivor != i:
                    multiplicador = self.matriz[i][pivor]
                    for j in range(self.colunas*2):
                        self.matriz[i][j] -= multiplicador*self.matriz[pivor][j]
            pivor += 1
        # Temos B[I|A^(-1)]
        # Criar matriz nula que amanazenará A^(-1)
        inversa = construirMatrizNula(self.linhas, self.colunas)
        # Transportar os valores de A^(-1) para a matriz inversa
        for i in range(self.linhas):
            for j in range(self.colunas):
                inversa[i][j] = self.matriz[i][self.colunas+j]
        # Retornar A(-1)
        return inversa

def construirMatrizNula(linhas, colunas):
    matriz = []
    for i in range(linhas):
        list.append(matriz, [0]*colunas)
    return matriz