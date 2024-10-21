nome = input("Olá, digite seu nome completo!: ")
email = input("Agora digite seu email etec!: ")
telefone = input("Agora seu telefone!: ")

with open("database.txt", "a") as arquivo:
    arquivo.write(f"{nome} - {email} - {telefone}\n")

print("Verifique o arquivo, 'database.txt'")