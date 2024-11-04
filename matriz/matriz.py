nmraluno = int(input("Digitie o número de alunos: "))
nmrmat = int(input("Digitie o número de matérias: "))

matriz = [[0] * nmrmat for _ in range (nmraluno)]

for i in range (nmraluno): 
    print(f"Digite as notas do Aluno {i + 1} :")
    for j in range(nmrmat):
        matriz[i][j] = float(input(f"Nota{ j + i } : "))

print("\nMédia dos alunos")

for i in range(nmraluno):
    soma = 0
    for j in range(nmrmat):
        soma += matriz[i][j]
    media = soma / nmrmat
    print(f"Média do aluno {i + 1} : {media:.2f}")