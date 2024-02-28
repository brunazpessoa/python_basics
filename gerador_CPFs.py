import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))


contador_regressivo1 = 10

soma1 = 0
for a in nove_digitos:
    soma1 += int(a) * contador_regressivo1
    contador_regressivo1 -= 1

produto1 = soma1 * 10
resto1 = produto1 % 11

digito_1 = resto1 if resto1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo2 = 11

soma2 = 0
for b in dez_digitos:
    soma2 += int(b) * contador_regressivo2
    contador_regressivo2 -= 1

produto2 = soma2 * 10
resto2 = produto2 % 11

digito_2 = resto2 if resto2 <= 9 else 0


cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
print(cpf_gerado)