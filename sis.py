import pickle
import random

# Linha 0: nomes
# Linha 1: cpf
# Linha 2: telefones
# Linha 3: data
# Linha 4: hora

matriz = [[], # Matriz de nomes 
          [], # Matriz de CPFs
          [], # Matriz de telefones
          [], # Matriz de datas
          []] # Matriz de hora

def carregar_dados():
    try:
        with open('dados.pkl', 'rb') as arquivo:
            matriz = pickle.load(arquivo)
    except FileNotFoundError:
        matriz = [[], [], [], [], []]
    return matriz

def salvar_dados(matriz):
    with open('dados.pkl', 'wb') as arquivo:
        pickle.dump(matriz, arquivo)

def cadastro(matriz):
    nome = input("Informe seu nome: ")
    matriz[0].append(nome)
    cpf = input("Informe seu cpf: ")
    matriz[1].append(cpf)
    telefone = input("Informe seu telefone: ")
    matriz[2].append(telefone)

def cadastra_data_hora(matriz, nome):
    index = matriz[0].index(nome)
    dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta"]
    dia = random.choice(dias_semana)
    matriz[3].append(dia)

def get_consulta(matriz, nome):
    index = matriz[0].index(nome)
    dia_consulta = matriz[3][index]
    return dia_consulta

# Carrega os dados salvos, se existirem
matriz = carregar_dados()

cadastro(matriz)
cadastra_data_hora(matriz, "Eduardo")
print(get_consulta(matriz, "Eduardo"))

# Salva os dados atualizados
salvar_dados(matriz)
