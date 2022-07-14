from matriz import Matriz

# Menu
print('~'*50)
limite = int(input('Defina o limite da matriz quadrática: '))
matriz = Matriz(limite, limite)
matriz.mostrarMatriz()
print(f'norma_{matriz.getNorma_p(1)}: {matriz.getNorma_p(0)}')
print('~'*50)