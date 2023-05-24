
# Linha 0: nomes
# Linha 1: cpf
# Linha 3: números

matriz = [["eduarda", "eduardo"],
        ["124.982.904-51", "568,365.704-36"],
          ["9996985245", "7854254421582698"]]

def cadastro(matriz):
    nome = input("Informe seu nomes: ")
    matriz[0].append(nome)
    cpf = input("Informe seu cpf: ")
    matriz[1].append(cpf)  
    telefone = input("Informe seu telefone: ")
    matriz[2].append(telefone)

cadastro(matriz)
print(matriz[0][2])
print(matriz[1][2])
print(matriz[2][2])



        


       

