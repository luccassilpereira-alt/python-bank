#Criando a classe Conta para representar uma conta bancária

def fazer_login():
    titular = ""
    senha = ""
    print("\n=== ÁREA DE ACESSO ===")

    tentativas = 3

    while tentativas > 0:
        print("1. Criar conta")
        print("2. Fazer login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titular = input("Digite o nome do titular: ")
            senha = input("Digite a sua senha: ")
            print(f"Conta criada para {titular}.\n")

        if opcao == "2":
                login_titular = input("Digite o nome do titular: ")
                login_senha = input("Digite a sua senha: ")
                if login_titular == titular and login_senha == senha:    
                    print(f"\nBem-vindo, {titular}! Acesso liberado✅.")
                    return True
                else:
                    tentativas -= 1
                    print(f"Login incorreto. Tentativas restantes: {tentativas}")

        if opcao == "3":
             print("Saindo do sistema. Até logo!")
             return False
        
        if tentativas == 0:
            print("Número de tentativas excedido. Acesso bloqueado.")
            return False

def menu():
      
      saldo = 0.0

      while True:

        print("\n=== MENU ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver saldo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
                print("\nDepositar selecionado.")
                # Lógica para depositar
                print (f"Saldo atual: R${saldo:.2f}")
            
                valor = input("Digite o valor a depositar: ")
                saldo += float(valor)
                print(f"Valor de R${valor} depositado. Saldo atual: R${saldo:.2f}\n")

                input("Pressione Enter para continuar...")

        if opcao == "2":
                print("\nSacar selecionado.")
                # Lógica para sacar

                print (f"Saldo atual: R${saldo:.2f}")

                valor = input("Digite o valor a sacar: ")
                if float(valor) > saldo:
                    print("Saldo insuficiente para realizar o saque.")
                else:
                    saldo -= float(valor)
                    print(f"Valor de R${valor} sacado. Saldo atual: R${saldo:.2f}\n")

                input("Pressione Enter para continuar...")

        if opcao == "3":
                print("\nVer saldo selecionado.")
                # Lógica para ver saldo
                print(f"Saldo atual: R${saldo:.2f}\n")

                input("Pressione Enter para continuar...")

        if opcao == "4":
                print("Saindo do sistema. Até logo!")
                break


