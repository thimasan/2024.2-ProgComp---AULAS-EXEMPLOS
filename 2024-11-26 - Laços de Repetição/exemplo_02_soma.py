'''
   Exemplo 02: Calculando e exibindo a soma dos 100 primeiros números inteiros positivos
'''

soma = 0
x    = 1

while x <= 100:
   soma += x
   x += 1

print(f'A soma dos 100 primeiros números inteiros positivos é {soma}.')