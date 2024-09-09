maioremenor = []

print("Olá, digite 10 números e irei mostrar para você todos eles do menor para o maior")

for i in range(10):
    numero = float(input(f"Digite o número {i + 1}: "))
    maioremenor.append(numero)
    maioremenor.sort()
    print("Números do menor para o maior:", maioremenor)