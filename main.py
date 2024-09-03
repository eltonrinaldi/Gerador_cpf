import sys
import random

print(f'{20*'*'} Gerador de CPF {20*'*'}\n')


digitos = ''
contagem_regressiva = 10
digito_1 = 0
digito_final = ''


for r in range(9):
    digitos += str(random.randint(0,9))


for digito in digitos:
    digito_1 += int(digito) * contagem_regressiva
    contagem_regressiva -= 1
    
digito_1 = (digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

digito_final += str(digito_1)
digitos += str(digito_1)

contagem_regressiva = 11
digito_2 = 0

for digito2 in digitos:
    digito_2 += int(digito2) * contagem_regressiva
    contagem_regressiva -= 1
    
digito_2 = (digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

digito_final += str(digito_2)
digitos += str(digito_2)


print(digitos)


