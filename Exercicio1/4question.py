km = float(input("Quantos km o carro faz com 1litro? "))
restante = float(input("Quantos de combustivel ja no momento? "))
distancia = float(input("Qual a distancia que voce deseja percorree? "))

if distancia / km < restante:
    print("gasolina suficiente")
else:
    print("Voce vai precisar abastecer {:.2f}litros\n\n".format(distancia/km - restante))