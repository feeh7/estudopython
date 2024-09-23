vetor1 = [] #vetor 1
vetor2 = [] #vetor 2
vetor3 = [] #vetor multiplicação
print("Olá, digite 5 números em cada vetor, criarei um terceiro com o produto do vetor 1 e 2")

for i in range(5):
    vet = float(input(f"Digite o número {i + 1}: "))
    vetor1.append(vet)
print("Aqui está o resultado do vetor 1:")
print(vetor1)

for i in range(5):
    vet2 = float(input(f"Digite o número {i + 1}: "))
    vetor2.append(vet2)
print("Aqui está o resultado do vetor 2:")
print(vetor2)

for i in range(5):
    produto = vetor1[i] * vetor2[i]
    vetor3.append(produto)
 
print("Aqui está o resultado do vetor 3 (produto):")
print(vetor3)
