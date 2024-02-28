
import re
import sys

#utilizando re.sub, o programa irá ler a entrada do usuário, desconsiderando quaisquer outros caracteres que não sejam números
entrada = input('CPF: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada       )

#para avaliar se a entrada possui valores repetidos (sequencial):
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

#Se os dados forem sequenciais, o cpf é inválido, portanto o programa não irá adiante
if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()
nove_numeros = cpf[:9]
contador_regressivo1 = 10

soma1 = 0
for a in nove_numeros:
    soma1 += int(a) * contador_regressivo1
    contador_regressivo1 -= 1

produto1 = soma1 * 10
resto1 = produto1 % 11

digito_1 = resto1 if resto1 <= 9 else 0
print(f'O primeiro dígito é {digito_1}')

dez_numeros = cpf[:10]
contador_regressivo2 = 11

soma2 = 0
for b in dez_numeros:
    soma2 += int(b) * contador_regressivo2
    contador_regressivo2 -= 1

produto2 = soma2 * 10
resto2 = produto2 % 11

digito_2 = resto2 if resto2 <= 9 else 0
print(f'O segundo dígito é {digito_2}')


#validar o cpf
cpf_gerado = f'{nove_numeros}{digito_1}{digito_2}'
if cpf == cpf_gerado: 
    print(f'CPF {cpf} é válido')
else:
    print(f'CPF {cpf} inválido')