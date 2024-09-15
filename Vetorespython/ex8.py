vetor = []
print("Olá, digite 5 números e irei deslocar todos elementos do vetor para a direita, assim o último elemento vai para a primeira posição!")

for i in range(5): # repetição
    direita = float(input(f"Digite o número {i + 1}: "))
    vetor.append(direita)

if len(vetor) > 0: # ve se a lista tem um número maior que 0, para assim executar
    ultimoel = vetor[-1] # o -1 signica pegar o ultimo elemento
    for i in range(len(vetor) - 1, 0, -1): # passa o elemento para direita
        vetor[i] = vetor[i - 1]
    vetor[0] = ultimoel # coloca o último elemento na primeira posição

print("Aqui está o resultado:")
print(vetor)
