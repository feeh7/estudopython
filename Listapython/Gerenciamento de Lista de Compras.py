vetor = [1, 2, 3, 4, 5]
print("Olá, digite 5 itens para sua lista de compras!")

for i in range(5):
    compra = input(f"Digite o item {i + 1}: ")
    vetor[i] = compra

print("Aqui está sua lista de compras: ")
print(vetor)


resposta_usuario = input("Quer remover algo da lista? Responda com 1 para sim e 2 para não: ")

if resposta_usuario == 1:
   print("Qual item deseja remover?")
else: 
   print("Ok, aparentemente você não deseja mudar sua decisão, tenha um bom dia!")