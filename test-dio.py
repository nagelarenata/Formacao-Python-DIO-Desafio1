
menu = """
[d] = Depósito
[s] = Saque
[e] = Extrato
[sair] = Sair
"""
saldo = 0
lista_deposito = []
lista_saque = []

while True:
    opcao = input(menu)

    if opcao == 'd':
        depositando = float(input(f'Digite o valor que você deseja depositar: '))
        if (depositando > 0):
            depositando_formatado = (f'R${depositando:.2f}')
            lista_deposito.append(depositando_formatado)
            saldo += depositando
        else:
            print('Não foi possível realizar o depósito.')
        continue

    elif opcao == 's':
        if (len(lista_saque) < 3):
            sacando = float(input(f'Digite o valor que você deseja sacar: '))
            sacando_formatado = (f'R${sacando:.2f}')
            if sacando <= 500 and sacando <= saldo:
                saldo -= sacando
                lista_saque.append(sacando_formatado)
            else:
               print('Não é possível realizar mais de 3 saques por dia ou sacar mais de R$500,00')
        else:
            print('Não é possível realizar mais de 3 saques por dia ou sacar mais de R$500,00')
        continue

    elif opcao == 'e':
        print(f'''
                Saldo : R${saldo:.2f}
                Saques: {lista_saque}
                Depósitos: {lista_deposito}
                ''')
        continue

    elif opcao == 'sair':
        break