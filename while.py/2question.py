cont = 0
while True:
    valor = int(input("Informe o valor numerico qualquer: "))
    
    if valor == 0:
        break
    if cont==0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
    cont += 1

    print(f"O maior valor e {maior} e o menor e {menor}\n\n")
