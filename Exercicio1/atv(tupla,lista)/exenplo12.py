def calculaImposto(sal,imposto = 20):
    imposto = imposto/100 #  CALCULA A PORCENTAGEN DO VALOR!
    novoSalario = sal - (sal * imposto)
   
   # print(f"O seu salario bruto é R${sal} com 20% de imposto fica R$ {novoSalario}")
    return novoSalario


salario = float(input("Informe o seu salario: "))
# desconto = float(input("Qual o valor da porcentagem do imposto: "))

print(f" Seu salario liquido é R${calculaImposto(salario,30)}") 