temp = []
mes = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")
media = 0

for cont in range(1,13):
    temp.append(float(input(f"Informe a temperatura do mes {cont}:")))

media = sum(temp)/cont

for indice,cont in enumerate (temp):
    if cont > media:
        print(f"{mes[indice]:.<10}: {cont}") 