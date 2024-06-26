# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

soma = 0
for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")
    i = 0
    for opcao in pergunta['Opções']:
        print(f"{i}) {opcao}")
        i += 1
    escolha_usuario = int(input("Escolha uma opçao: "))
    if pergunta['Opções'][escolha_usuario] == pergunta['Resposta']:
        soma += 1
        print("Acertou!")
    else:
        print("Errou...")   
print(f"Você acertou {soma} de 3 perguntas!")



