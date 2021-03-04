while True:
    try:
        salario = float(input("Informe seu salario: "))

    except Exception as erro:
        print("Informe um valor decimal correto")

    else:
        break
    
print(f"Seu salário é: R${salario}")