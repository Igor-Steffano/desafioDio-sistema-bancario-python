#Devemos implementar apenas 3 operações: deposito, saque e extrato
#Todos os deposito devem ser armazenados em uma variavel e exibidos na operação de extrato
#Valores devem ser positivos

#OPERACAO SAQUE
#O sistema deve permitir realizar 3 saques diarios com limite maximo de R$ 500,00
#O sistema deve exibir uma mensagem inforando que não será possivel sacar o dinheiro por falta de saldo
#Todos os saques devem ser armazenados em uma cariavel e exibidos na operação extrato.

#OPERACAO DE EXTRATO
#Essa operação deve listar todos os depósitos e saques realizados na conta
#No fim da Listagem deve ser exibidos o saldo atual da conta.
#Os valores devem ser exibidos utilizndo o formato R$ xxx.xx exe: 1500.45 = R$ 1500.45

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> Digite sua opção aqui: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0: #Verificação se exite valor negativo
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}/n"
        else:
            print("Operação falhou! O valor informado é invalido.")
    
    elif opcao == "s":
        valor = float(print("Informe o valor do saque: "))

        excedeu_limite = valor > limite

        exceudeu_saques = numero_saques >= LIMITE_SAQUE

        if execedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque exede o limite.")
        
        elif exceudeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .f}/n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")

    
    elif opcao == "e":
        print("\n====================Extrato====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novmente a operação desejada.")