pessoas = {"nome":"Bruno":"idade":21"endereço":"turu"}

print(pessoas)

print(f"Olá {pessoas['nome']}, voce tem {pessoas['idade']} anos e mora no bairro {pessoas['bairro']}\n\n)

#print(type(pessoas))
print(pessoas.key())# exibindo as chaves
print(pessoas.values())#exibindo o conteudo
print(pessoas.itens())#exibindo os itens (chave e valor)

for chave in pessoas.keys():
    print(f"{chave.title()} = {valor}")# .title() - deixa 1ª letra em maiuscula
print(f"O tamanho do dicionario e {len(pessoas)}")
# inserindo mais uma chave e valor
pessoas.update({'sexo:'m'})
print(pessoas)
print("\n\n")

pessoas.get("idade")
print("\n\n")

#preencher uma lista com dicionarios
lista = []
for cont in range(0,2):
    pessoas["nome"] = input("informe o sue nome: ")
    pessoas["idade"] = int(input("Imforme dua idade: "))
    pessoas["bairro"] = input("informe seu bairro: ")
    pessoas["sexo"] = input("Informe seu sexo: ")

lista,append(pessoas.copy())# copiando dicionario dentro de uma lista
    lista.append(pessoas)

    print(lista)