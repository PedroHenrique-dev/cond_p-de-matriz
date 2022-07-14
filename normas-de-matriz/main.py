from matriz import Matriz

print('~'*50)
limite = 0
while limite < 1:
    limite = int(input('Defina o limite da matriz quadrática: '))
matriz = Matriz(limite, limite, )
matriz.mostrarMatriz()
print(f'norma_1: {matriz.getNorma_1()}')
print(f'norma_2: {matriz.getNorma_2()}')
print(f'norma_∞: {matriz.getNorma_inf()}')
print(f'norma_f: {matriz.getNorma_f()}')
print('~'*50)