print("===========Atividade=============")

item1 = float(input("Informe o valor do item 1:"))
item2 = float(input("Informe o valor do item 2:"))
item3 = float(input("Informe o valor do item 3:"))

total = item1 + item2 + item3

print("O valor total da compra e R$ {}".format(item1 + item2 + item3))
print(" O valor do desconto e R$ {}".format(total * 0.2))
print("Voce ira pagar um total de R$ {}".format(total - (total * 0.2)))