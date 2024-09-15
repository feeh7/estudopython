vetor1 = [] #vetor1
vetor2 = [] #vetor2
vetor3 = [] #vetor3

print("Olá, digite 5 elementos em cada vetor. Após digitar, mostrarei os elementos intercalados em um terceiro vetor!")

#repetição, faz a pergunta 5 vezes para o úsuario responder e salvar no vetor1 
for i in range(5):
    numero = float(input(f"Digite o número {i + 1} para o vetor 1: "))
    vetor1.append(numero)

#repetição, faz a pergunta 5 vezes para o úsuario responder e salvar no vetor2
for i in range(5):
    numero2 = float(input(f"Digite o número {i + 1} para o vetor 2: "))
    vetor2.append(numero2)

# faz com que os vetores sejam intercalados, irei colocar no print, no vetor3
for i in range(5):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

# Imprimir o vetor intercalado
print("Agora olhe os valores digitados, porém estão intercalados entre o vetor 1 e o vetor 2:")
print(vetor3)
