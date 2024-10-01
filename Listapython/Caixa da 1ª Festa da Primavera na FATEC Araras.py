escolha = []

preco = [
    4, 10, 10, 15, 8, 2, 10, 6, 3, 5,
    12, 9, 9, 9, 9, 12, 12, 12, 4, 6
]

print("1 - Pastel", 
    "\n2 - Cachorro Quente", 
    "\n3 - Cuscuz", 
    "\n4 - Lanche Caipira", 
    "\n5 - Milho Cozido", 
    "\n6 - Pipoca", 
    "\n7 - Espetinho de Carne", 
    "\n8 - Refrigerante", 
    "\n9 - Água", 
    "\n10 - Água com Gás", 
    "\n11 - Bolo de Pote", 
    "\n12 - Bolo Bombom", 
    "\n13 - Coxinha de Morango", 
    "\n14 - Cone", 
    "\n15 - Cocada", 
    "\n16 - Espeto de Morango", 
    "\n17 - Caixa com 4 Brigadeiros", 
    "\n18 - Bolacha", 
    "\n19 - Brigadeiro Individual", 
    "\n20 - Trufas")

total = 0   

for i in range(20):
    item_desejado = input("Olá, esse é nosso cardápio! Quais item você deseja? Escreva o nome do alimento, quando quiser encerrar escreva 'sair': ")
    
    if item_desejado == 'sair':
        break
    
    if item_desejado not in [
        'Pastel', 'Cachorro Quente', 'Cuscuz', 'Lanche Caipira', 
        'Milho Cozido', 'Pipoca', 'Espetinho de Carne', 
        'Refrigerante', 'Água', 'Água com Gás', 
        'Bolo de Pote', 'Bolo Bombom', 'Coxinha de Morango', 
        'Cone', 'Cocada', 'Espeto de Morango', 
        'Caixa com 4 Brigadeiros', 'Bolacha', 
        'Brigadeiro Individual', 'Trufas']:
        print("Item não encontrado")
    else:
        escolha.append(item_desejado)
        
        juncao_preco = ["Pastel", "Cachorro Quente", "Cuscuz", "Lanche Caipira", 
                  "Milho Cozido", "Pipoca", "Espetinho de Carne", 
                  "Refrigerante", "Água", "Água com Gás", 
                  "Bolo de Pote", "Bolo Bombom", "Coxinha de Morango", 
                  "Cone", "Cocada", "Espeto de Morango", 
                  "Caixa com 4 Brigadeiros", "Bolacha", 
                  "Brigadeiro Individual", "Trufas"].index(item_desejado)
        
        total += preco[juncao_preco]
        print("O item escolhido foi: ")
        print(item_desejado)
        print(f"Valor de: {preco[juncao_preco]} reais")

print("Aqui está sua nota:", escolha)
print(f"Total a pagar: R${total}")


#esse código me deu um pouco mais de trabalho então pesquisei formas diferentes de fazer ele de uma forma..
#que não utilizasse tantos recursos que ainda não aprendi
#a única coisa diferente que usei foi o .index, ao meu entender ele faz uma junção da lista
# então pastel = 4, pois 4 é o primeiro item da lista preco 