num1 = int(input("Informe um valor númerico: "))
num2 = int(input("Informe outro valor númerico: "))

try:
    resultado = num1 / num2
except Exception as erro:
    print("Houve algum erro: {erro.__class__}")
else:
    print(f"O resultado é {resultado}")
