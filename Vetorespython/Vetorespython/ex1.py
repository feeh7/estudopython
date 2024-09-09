somas = [] #vetor

print("Olá, Digite 10 números, então irei somar todos resultados e exibir a você!") #mensagem ao usuario

for i in range(10): #repetição da pergunta abaixo
    numero = float(input(f"Digite o número {i + 1}: "))
    somas.append(numero)
    soma = sum(somas) #soma 
    print(f"A soma dos números é : {soma}") #resultado
    
