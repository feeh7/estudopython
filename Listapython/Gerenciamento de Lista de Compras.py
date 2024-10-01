vetor = [1, 2, 3, 4, 5]
print("Olá, digite 5 itens para sua lista de compras!")

for i in range(5):
    compra = input(f"Digite o item {i + 1}: ")
    vetor[i] = compra
print("Aqui está sua lista de compras: ")
print(vetor)

resposta_usuario = input("Quer remover algo da lista? Responda com 'sim' ou 'não': ")

if resposta_usuario == "sim":
    print("Qual item deseja remover? Digite apenas o número do item que quer remover (1 a 5):")
    numero_escolhido = int(input("Digite aqui: "))
    
    if 1 <= numero_escolhido <= 5:
        vetor[numero_escolhido - 1] = "removido"
        print("Aqui está sua lista de compras atualizada:")
        print(vetor)

        decisao_item = input("Agora que você removeu um item da lista, deseja adicionar outro? Responda com 'sim' ou 'não': ")
        
        if decisao_item == "sim":
            item_novo = input("Qual item deseja adicionar? ")
            vetor[numero_escolhido - 1] = item_novo
            vetor.sort()
            print("Aqui está sua lista de compras atualizada com o novo item:")
            print(vetor)
        else:
            print("Ok, tenha um bom dia!")
    else:
        print("Esse número não é válido.")
else: 
    vetor.sort()
    print("Ok, aparentemente você não deseja mudar sua decisão, tenha um bom dia!")
    print(vetor)