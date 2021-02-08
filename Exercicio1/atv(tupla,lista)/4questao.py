from os import system
frutas = list()

for cont in range(1,6):
    frutas.append(input("Informe um nome de fruta: "))

while True:
    system("cls")
    print(f"{'Lista de Frutas':}*^30\n")

    for indice, itens in enumerate(frutas):
        print(f"{indice:.<10} {itens}")
    print("\n")
    print("0. terminar")
    print("1. inserir uma fruta")
    print("2. excluir uma fruta")
    op = int(input("O que deseja fazer:"))

    if op ==0:
        break
    elif op == 1:
        frutas.append(input("Informe uma nova fruta: "))
    elif op == 2:
        valor = int(input("Qual a posição da fruta desejada remover?"))
        frutas.pop(valor)
