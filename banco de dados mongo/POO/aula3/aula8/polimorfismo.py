class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.__cpf = ""



    @property
    def cpf(self):
        return self. __cpf    
       

    @cpf.setter
    def cpf(self,valor):
        if len(valor) != 11:
            print("O CPF precisa ter 11 números e tem que ser somente números")

        elif valor.isnumeric():
            self.__cpf = valor
        else:
            print("Insira somente números")
           

    def exibirDados(self):
        print(f"Nome: {self.nome} ")
       # print(f"cpf: {self.__cpf} ")



class Aluno(Pessoa):
    def __init__(self,nome,matricula, curso="nenhum"):
        super().__init__(nome)# parametro self só é preciso se não for usar super()

        self.matricula = matricula
        self.curso = curso
    def exibirDados(self):

        super().exibirDados()
        print(f"Matricula: {self.matricula}")
        print(f"Curso: {self.curso}")

    
class Professor(Pessoa):
    def __init__(self,nome,salario,cargaHoraria):
        super().__init__(nome)
        self.salario = salario
        self.cargaHoraria = cargaHoraria
    
    def exibirDados(self):
        super().exibirDados()
        print(f"salario: R${self.salario}")
        print(f"Carga Horaria: {self.cargaHoraria}")

    