extrato = []
limiteQtdSaques = 3
limiteValorSaque = 500.00
qtdSaques = 0
saldoConta = 0.0

def extratoConta():
    print(f'        {str(" Extrato ").center(30, "-")}\n')

    for item in extrato:
        if item['transacao'] == 'saque':
            print(f"{str(item['transacao']) + 3*' '} : - R$ {round(float(item['valor']), 2)}")
        else:
            print(f"{str(item['transacao'])} :   R$ {round(float(item['valor']), 2)}")

    print(f'\nSaldo conta: R$ {round(saldoConta, 2)}')     
    print('\n\n')


    
while True:
    try:
        opcao = input(f"""
            {str(" Menu ").center(30, "-")}
        
        Opcoes:

        [1] Extrato
        [2] Saque
        [3] Deposito
        [0] Sair

    Digite uma opcao => """)

        #EXTRATO CONTA
        if int(opcao) == 1:
            extratoConta()
        
        #SAQUE
        elif int(opcao) == 2:
            valor = float(input(f"""
            {str(" Saque ").center(30, "-")}  
        
        Digite o valor que deseja sacar => R$ """))
            if saldoConta < valor:
                print('Saldo indisponivel')
            elif valor > limiteValorSaque:
                print(f'''
                    Valor maximo de R$ {limiteValorSaque} atingido !!
                    Tente novamente
                    ''')
            elif qtdSaques >= limiteQtdSaques:
                print(f'''
                    Limite de {limiteQtdSaques} saques diarios atingido !!
                    Tente novamente amanha
                    ''')
            else:
                saldoConta -= valor
                novo = {
                    'transacao' : 'saque',
                    'valor' : valor
                }
                extrato.append(novo)
                print('Saque realizado com sucesso !!')
                qtdSaques += 1

        #DEPOSITO
        elif int(opcao) == 3:

            valor = float(input(f"""
            {str(" Deposito ").center(30, "-")}

        Digite o valor que deseja depositar => R$ """))
            
            saldoConta += valor
            novo = {
                'transacao' : 'deposito',
                'valor' : valor
            }
            
            extrato.append(novo)
            print('Deposito realizado com sucesso !!')

        #SAIR
        elif int(opcao) == 0:
            break
    except:
        print("Digite uma opcao valida !!")