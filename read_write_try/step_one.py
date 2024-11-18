numeros = []

for i in range(5): 
    numero = float(input(f"Olá, digite o número {i + 1}: "))
    numeros.append(numero)

with open("database.txt", "w") as arquivo:
    for numero in numeros:
        arquivo.write(f"{numero}\n")

print("Verifique o arquivo 'database.txt'")
