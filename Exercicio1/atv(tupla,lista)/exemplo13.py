def calculaImposto(sal, imposto = False):
    if imposto:
        desconto = float(input("Qual a porcentagem do imposto: "))
    else:
         desconto = 20

    desconto = desconto/100
    return sal - (sal * desconto)


salario = float(input("Informe o seu salario: "))

print(f"Seu salario com desconto é: R${calculaImposto(salario,True)}")