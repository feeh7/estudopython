somas = []

print("Olá, Digite 10 números, então irei somar todos resultados e exibir a você!")

for i in range(10):
    numero = float(input(f"Digite o número {i + 1}: "))
    somas.append(numero)
    soma = sum(somas)
    print(f"A soma dos números é : {soma}")
    
