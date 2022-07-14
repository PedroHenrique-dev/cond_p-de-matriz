from matriz import Matriz

# Menu
print('~'*50)
limite = 0
while limite < 1:
    limite = int(input('Defina o limite da matriz quadrática: '))
binario = -1
while binario != 1 and binario != 2:
    binario = int(input('\nFormas de calcular o cond(A):\n    1. ||A||*||A^(-1)||    2. magmax(A)/magmin(A)\n\nEscolha a formula: '))
print()
matriz = Matriz(limite, limite, binario)
print()
matriz.mostrarMatriz()
matriz.mostrarInversa()
print(f'norma_2 da matriz: {matriz.getMatrizNorma_2()}')
print(f'norma_2 da inversa: {matriz.getInversaNorma_2()}')
print(f'\ncond_2(matriz): {matriz.getCond()}')
print('~'*50)