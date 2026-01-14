import os

# Configurações inicias

saldo = 1000.0
logado = False

print("=======BEM VINDO AO PYTHON BANK=======")

# Loop principal do sistema
while True:
    if not logado:
        entrada_senha = int(input("Digite sua senha para acessar sua conta: "))
        if entrada_senha == 1234:
            logado = True
            print("Login realizado com sucesso!")
        else:
            print("Senha incorreta. Tente novamente.")
        continue

    print("\nMenu de opções:")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
        input("\nTecle ENTER para voltar ao menu...")
        continue

    elif opcao == 2:
        valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(
                f"Depósito de R$ {float(valor_deposito):.2} realizado com sucesso!")
            input("\nTecle ENTER para voltar ao menu...")
            continue
        else:
            print("Valor inválido para depósito.")
            input("\nTecle ENTER para voltar ao menu...")
            continue

    elif opcao == 3:
        valor_saque = float(input("Digite o valor a ser sacado: R$ "))
        if 0 < valor_saque <= saldo:
            saldo -= valor_saque
            print(f"Saque de R$ {valor_saque:.2} realizado com sucesso!")
            input("\nTecle ENTER para voltar ao menu...")
            continue
        else:
            print("Saldo insuficiente ou valor inválido para saque.")
            input("\nTecle ENTER para voltar ao menu...")
            continue

    elif opcao == 4:
        print("Saindo da conta. Obrigado por usar o Python Bank!")
        break  # encerra o looping principal
