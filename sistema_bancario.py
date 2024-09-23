menu = """
--------------------------------------------
Bem-vindo ao Sistema Bancário!

Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

>>> """

saldo = 0
limite_por_saque = 500
extrato = ""
saques_realizados = 0
limite_saque_diario = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input("\nInforme o valor do depósito: R$"))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
            print(f"\nDepósito de R${valor_deposito:.2f} realizado com sucesso!")
        else:
            print("\nPermitido apenas valor positivo!")

    elif opcao == 's':
        if saques_realizados >= limite_saque_diario:
            print("\nLimite de saques diários atingido!")
        else:
            valor_saque = float(input("\nInforme o valor do saque: R$"))
            if valor_saque > saldo:
                print("\nSaldo insuficiente!")
            elif valor_saque > limite_por_saque:
                print(f"\nValor do saque excede o limite diário de R${limite_por_saque:.2f}!")
            elif valor_saque > 0:
                saldo -= valor_saque
                saques_realizados += 1
                extrato += f"Saque: R${valor_saque:.2f}\n"
                print(f"\nSaque de R${valor_saque:.2f} realizado com sucesso!")
            else:
                print("\nPermitido apenas valor positivo!")

    elif opcao == 'e':
        if not extrato:
            print("\nNão foram realizadas movimentações!")
        else:
            print("\n=========== EXTRATO BANCÁRIO ===========:")
            print(extrato)
            print(f"\nSaldo atual: R${saldo:.2f}")

    elif opcao == 'q':
        print("\nObrigado por usar nosso sistema bancário!")
        break

    else:
        print("\nOpção inválida, tente novamente!")
