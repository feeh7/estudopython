vetor = []
print("Digite 10 números, irei calcular a média deles e mostrar ao úsuario!")

for i in range(10): #repetição
    media = float(input(f"Digite o número {i + 1}: "))
    vetor.append(media)

# calcular a media dos números
media = sum(vetor) / len(vetor)

# mostra a média
print(f"A média dos números digitados é")
print(media)