from random import randint

def sorteio(valor):
    aleatorio = randint(1,100)
    palpite = 1 #contador

    while valor != aleatorio:
        if valor > aleatorio:
            print("O seu aplpite é maior do que o  valor sorteado")
        elif valor < aleatorio:
            print("Seu palpite é menor do que o  valor sorteado ")
        palpite +=1
        valor = int(input("Informe um novo palpite:"))

    print("Parabéns voce acertou o número com {palpite} palpites")



numero = int(input("Diga um palpite de um numero de um número entre 1 e 100: "))
sorteio(numero)