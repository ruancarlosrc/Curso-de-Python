menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual o valor do deposito?"))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido")

    elif opcao == "s":
        valor = float(input("Qual o valor do saque?"))
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saques_excedidos = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Você não tem saldo suficiente!")
        elif limite_excedido:
            print("O valor do saque excede o limite!")
        elif saques_excedidos:
            print("Número máximo de saques excedido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("O valor é inválido!")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida!")

        

