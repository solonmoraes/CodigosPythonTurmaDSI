peso = float(input("INFORME SEU PESO:"))
altura = float(input("INFORME SUA ALTURA:"))

imc = peso / altura**2

if imc <= 16:
    print("Magreva grave")
elif imc >16 and imc <=17:  
    print("Magreza moderada")
elif imc >17 and imc <=18.5:
    print("Magreza leve")
elif imc >18.5 and imc <=25:
    print("saudavel")
elif imc >25 and imc <=30:
    print("Sobrepeso")
elif imc >30 and imc <=35:
    print("Obesidade grau I")
elif imc >35 and imc <=40:
    print("Obesidade grau II(Severa)")
elif imc > 40:
    print("Obesidade grau III(morbido)")





