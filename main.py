saldo = 0

while True:

    print("\n===== GERENCIADOR FINANCEIRO =====")
    print("1 - Adicionar salário")
    print("2 - Adicionar gasto")
    print("3 - Ver saldo")
    print("4 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":

        valor = float(input("Digite o salário: "))

        saldo += valor

        print(f"Salário de R${valor:.2f} adicionado!")

    elif op == "2":

        print("\nCategorias:")
        print("1 - Comida")
        print("2 - Transporte")
        print("3 - Lazer")

        categoria = input("Escolha a categoria: ")

        valor = float(input("Digite o valor do gasto: "))

        saldo -= valor

        if categoria == "1":
         print(f"Gasto com comida: R${valor:.2f}")

        elif categoria == "2":
            print(f"Gasto com transporte: R${valor:.2f}")

        elif categoria == "3":
            print(f"Gasto com lazer: R${valor:.2f}")

        else:
            print(f"Gasto de R${valor:.2f}")

    elif op == "3":

        print(f"\nSeu saldo atual é: R${saldo:.2f}")
    
    elif op == "4":

        print("Encerrando programa...")
        break