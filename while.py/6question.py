from datetime import date 

anoAtual = date.today().year
while True:
    nascimento = int(input("Informe o ano de seu nascimento: "))

    idade = anoAtual - nascimento

    if idade >= 18:
        print(f"Voce possui {idade} anos, prossiga com a inscriçao\n")
        break
    else:
        print(f"Voce possui {idade} anos, voce ainda nao pode se inscrever\n")
        