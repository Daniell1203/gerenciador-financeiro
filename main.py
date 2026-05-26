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