class Pessoa:
    # atributo
    nome = "José"
    idade = 45
    altura = 1.65

    # método
    def falar(self, texto):
        print("texto ")

    def calculaAno(self,idade):
        anoAtual = date.today().year
        print(f"Voce nasceu no ano de {anoAtual - idade}"
        )

#Criando um objeto

alguem = Pessoa()

print(alguem.nome)
alguem.falar("tô vivo !!")

#Criando outro obejeto

fulano = Pessoa()
fulano.nome = "Joana"
print"(fulano.nome)

fulano.calculaAno(50)