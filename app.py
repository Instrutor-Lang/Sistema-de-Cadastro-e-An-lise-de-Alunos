import csv

# Módulo 4: Função para perguntar os campos que o usuário quer adicionar
def obter_campos_personalizados():
    print("Quais campos você deseja cadastrar? (ex: nome, idade, curso, nota)")
    campos = input("Separe os campos por vírgula: ").split(',')
    campos = [campo.strip() for campo in campos]
    return campos

# Módulo 4: Função para cadastrar alunos
def cadastrar_alunos(campos):
    alunos = []

    while True:
        aluno = {}
        for campo in campos:
            valor = input(f"Digite o valor para '{campo}': ")
            aluno[campo] = valor

        alunos.append(aluno)

        continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break

    return alunos

# Módulo 5: Função para salvar os dados em um arquivo CSV
def salvar_em_csv(alunos, campos, nome_arquivo='alunos.csv'):
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=campos)
            writer.writeheader()
            writer.writerows(alunos)
        print(f"\nDados salvos com sucesso em '{nome_arquivo}'!")
    except Exception as e:
        print("Erro ao salvar o arquivo:", e)

# Módulo 5: Função para ler e exibir os dados do CSV
def exibir_dados_csv(nome_arquivo='alunos.csv'):
    print("\n--- Dados Cadastrados ---\n")
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            reader = csv.DictReader(arquivo)
            for linha in reader:
                print(linha)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Erro ao ler o arquivo:", e)

# Módulo 2: Programa principal
def main():
    print("=== SISTEMA DE CADASTRO DE ALUNOS ===")
    
    campos = obter_campos_personalizados()
    alunos = cadastrar_alunos(campos)
    salvar_em_csv(alunos, campos)
    exibir_dados_csv()

# Execução do programa
if __name__ == "__main__":
    main()
