maioremenor = [] #vetor

print("Olá, digite 10 números e irei mostrando-os para você todos eles do menor para o maior") #mensagem ao usuario
 
for i in range(10): #repetição da pergunta abaixo
    numero = float(input(f"Digite o número {i + 1}: "))
    maioremenor.append(numero)
    maioremenor.sort() #.sort(ordena do menor para maior)
    print("Números do menor para o maior:", maioremenor)