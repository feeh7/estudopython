reverso = []  # vetor
 
print("Olá, digite 10 números e irei mostrando-os para você todos eles na ordem inversa") #pergunta ao usuario
 
for i in range(10):  # repetição da pergunta abaixo
    numero = float(input(f"Digite o número {i + 1}: "))
    reverso.append(numero)
 
print("Números na ordem inversa:", reverso[::-1])