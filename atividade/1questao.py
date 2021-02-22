cardapio = {
    'salgado': 4.90,
    'Suco': 3.00,
    'Refrigerante':4.00,
    'Hambuguer':7.20,
    'Doce':2.00,
    }
print("="*40)
print(f"{'Lanchonete':^40}")
print("="*40)

for chave, valor in cardapio.items():
    print(f"{chave:.<30}R${valor:>5}")
print("="*40)