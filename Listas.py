pessoas = ["Fabio","Carlos","Regina","Vanuza"]


print(type(pessoas))

print(pessoas)

pessoas[1] = "Sergio"
# adicionar elementoas
pessoas.append("Sarah")# adiciona no final
pessoas.insert(2,"Flavio")#adiciona em qualquer lugar

for chave, valor in enumerate(pessoas):
    print(f"{chave:.<5}{valor}")

#removendo elementos
pessoas.pop()#remove o ultimo elemento
pessoas.pop(1)#remove qualquer posiçao
pessoas.remove("Flavio")

print(pessoas)

#copiando listas
pessoasBkp = pessoas
pessoasBkp.append("jeronimo")
print("\n\n",pessoas)
print(pessoasBkp,"\n\n")


pessoas.clear()#limpa alista 
del(pessoas)#excluir a variavel ou lista
print(pessoas,"\n\n")
