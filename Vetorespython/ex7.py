vetor = [] #vetor
print("Olá, digite 10 números. Irei remover os números duplicados e mostrar apenas o resultado.")

for i in range(10): #repetição
    numero = float(input(f"Digite o número {i + 1}: ")) 
    vetor.append(numero)

vetoruni = list(set(vetor)) #remove números duplicados, converte para conjunto que não permite duplicatas e volta para formato original

print("Aqui está o resultado!")
print(vetoruni)
