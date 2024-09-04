#olá, irei comentar sobre meu código para mostrar minha linha de raciocinio!


alunos = int(input("Quantos alunos terão a média calculada? ")) #utilizei o input para perguntar a quantidade de alunos que serão calculados
print(f"Agora escreva o nome e duas notas dos {alunos} alunos") #apenas mostrei o que irei fazer

infoalunos = []    

for i in range(alunos): #base do codigo, no for irei fazer com que o programa veja quantos numeros tem na variavel alunos, fazendo assim, perguntando essa quantidade de vezes nomes de alunos e suas notas
    nome = input(f"Nome do aluno {i+1}: ")
    nota1 = float(input(f"Nota 1 do aluno {nome}: "))
    nota2 = float(input(f"Nota 2 do aluno {nome}: "))
    media = (nota1 + nota2) / 2
    infoalunos.append((nome, media))

print("\nTabela de Médias:")   #informações da tabeça final, aqui utilizei tecnicas de espaçamento para ficar com uma melhor visualização
print(f"{'Nome':<20}{'Média':<10}")
for nome, media in infoalunos:
    status = "aprovado" if media >= 7 else "reprovado"
    print(f"{nome:20}{media:<10.2f} {status}")
