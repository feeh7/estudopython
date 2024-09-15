vetor = []
print("Olá, digite 10 números e irei ordená-los em ordem crescente (não repita números)")

for i in range(10):
    ordem = float(input(f"Digite o número {i + 1}: "))
    vetor.append(ordem)
vetor.sort()
print("Aqui está o resultado:")
print(vetor)
