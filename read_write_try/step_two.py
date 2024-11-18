try: 
  with open("step_two.txt", "r") as arquivo:
    read = arquivo.read()
    print("Aqui está o contéudo do arquivo: ")
    print(read)
except FileNotFoundError:
    print("O arquivo não foi encontrado")
