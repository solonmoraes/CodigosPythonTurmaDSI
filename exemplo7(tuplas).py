pessoas = ("Carlos","Mario","Luiza","Felipe")

print(type(pessoas))
print(pessoas)


for itens in pessoas:
    print(itens)

print("Luiza esta na posição", pessoas.index("Luiza"))

for indice,itens in enumerate(pessoas):
    print(f"{indice:_<10}{itens}")