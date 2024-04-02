menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
opcao = ""

while True:
    if opcao not in ["d", "s", "e"]:
        opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor: "))
        if valor > 0:
            saldo += valor
            print("Deposito realizado com sucesso!")
            opcao = ""
        else:
            print("Insira um valor válido.")
            opcao = "d"
    elif opcao == "s":
        valor = float(input("Valor: "))
        if valor > 0:
            if valor > saldo:
                print("Você não tem saldo o suficiente.")
                opcao = ""
                continue
            if numero_saques < LIMITE_SAQUES:
                saldo -= valor
                numero_saques += 1
                print("Saque realizado com sucesso")
                opcao = ""
            else:
                print("Você não pode sacar mais do que 3 vezes no dia")
                opcao = ""
        else:
            print("Insira um valor válido.")
            opcao = "s"
        pass
    elif opcao == "e":
        print(f"R$ {saldo}")
        opcao = ""
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
