opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar" "[2] Extrato" "[0] Sair"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")