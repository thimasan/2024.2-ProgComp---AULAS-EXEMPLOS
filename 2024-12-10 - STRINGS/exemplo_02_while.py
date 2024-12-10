'''
   EXEMPLO 02:
   Fazer um programa em que o usuário informe uma frase e em seguida
   o programa informe quantas vogais existem na frase digitada
'''

# Solicita ao usuário que informe uma frase
frase = input('Informe uma frase: ')

# Inicializa a variável que irá armazenar a quantidade de vogais
intQtVogais = 0

# Percorre cada caractere da frase digitada
intPosicao = 0
while intPosicao < len(frase):
   if frase[intPosicao].lower() in 'aeiouãõáéíóúàèìòùâêîôûäëïöü':
      intQtVogais += 1
   intPosicao += 1

# Informa ao usuário quantas vogais existem na frase digitada
print(f'A frase digitada possui {intQtVogais} vogais')