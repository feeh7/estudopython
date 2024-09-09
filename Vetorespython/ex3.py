numerospares = []
 
print("Digite 15 números, irei mostrar somente os números pares!")
 
for i in range(15):
    numero = float(input(f"Digite o número {i + 1}: "))
    if (numero % 2) == 0:
        numerospares.append(numero)
 
print("Números pares:", numerospares)