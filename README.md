📚 Sistema de Cadastro e Análise de Alunos
Este é um projeto didático em Python que simula um sistema de cadastro de alunos. O sistema permite personalizar os campos do cadastro, adicionar múltiplos registros, salvar os dados em um arquivo .csv e consultar os dados salvos. O projeto foi desenvolvido com fins educativos, cobrindo os módulos 2 a 5 do curso de Python.

🧠 Conteúdo Abordado
Este projeto reforça os seguintes tópicos:

Módulo	Conteúdo Trabalhado
Módulo 2	Entrada de dados, condicionais (if), loops (while), manipulação de strings
Módulo 3	Listas, dicionários, estruturas de repetição e iteração
Módulo 4	Criação e uso de funções, escopo de variáveis, organização de código
Módulo 5	Leitura e escrita de arquivos CSV, tratamento de exceções com try/except

🚀 Funcionalidades do Sistema
✅ Cadastro de alunos com campos personalizados (ex: nome, idade, curso, nota)

✅ Salvamento automático em arquivo .csv

✅ Consulta e exibição dos dados cadastrados

✅ Interface em linha de comando com input()

✅ Código modular e reutilizável com funções

📂 Estrutura do Projeto
bash
Copy
Edit
📁 cadastro_alunos/
├── alunos.csv              # Arquivo gerado automaticamente com os cadastros
└── main.py                 # Código principal do sistema
📥 Pré-requisitos
Você precisa ter o Python 3 instalado.

1. Instale o Python
Acesse: https://www.python.org/downloads/

2. Verifique se está instalado:
bash
Copy
Edit
python --version
▶️ Como Executar
Clone este repositório ou copie o código do arquivo main.py para sua máquina.

Abra o terminal (cmd, PowerShell ou terminal Linux).

Execute o script com:

bash
Copy
Edit
python main.py
🖥️ Exemplo de Uso
bash
Copy
Edit
=== SISTEMA DE CADASTRO DE ALUNOS ===
Quais campos você deseja cadastrar? (ex: nome, idade, curso, nota)
> nome, idade, curso, nota

Digite o valor para 'nome': João
Digite o valor para 'idade': 18
Digite o valor para 'curso': Python
Digite o valor para 'nota': 9.0

Deseja cadastrar outro aluno? (s/n): s

Digite o valor para 'nome': Maria
...

Dados salvos com sucesso em 'alunos.csv'!

--- Dados Cadastrados ---

{'nome': 'João', 'idade': '18', 'curso': 'Python', 'nota': '9.0'}
{'nome': 'Maria', 'idade': '22', 'curso': 'Python', 'nota': '7.5'}
📁 Conteúdo do Arquivo CSV Gerado
csv
Copy
Edit
nome,idade,curso,nota
João,18,Python,9.0
Maria,22,Python,7.5
🧩 Estrutura do Código
O código está dividido em funções para facilitar a organização e reutilização:

obter_campos_personalizados() – Pergunta ao usuário quais campos deseja usar

cadastrar_alunos(campos) – Recebe os dados dos alunos via input

salvar_em_csv(alunos, campos) – Salva os dados em um arquivo CSV

exibir_dados_csv() – Lê e exibe o conteúdo do CSV no terminal

main() – Função principal que organiza a execução

💡 Possíveis Melhorias
🔄 Adicionar menu de opções (Cadastrar, Consultar, Sair)

🧮 Cálculo automático de média e status (Aprovado, Recuperação, Reprovado)

💾 Exportar para JSON também

🛡️ Validação de dados (ex: idade como número, nota entre 0 e 10)

🖼️ Criar versão com interface gráfica usando Tkinter

🌐 Criar versão web usando Flask ou Django

👨‍🏫 Projeto Didático
Este projeto foi desenvolvido como parte do curso “Python: Do Iniciante ao Avançado” por Estevão Gabriel Oliveira, com o objetivo de integrar diversos conceitos de lógica e desenvolvimento com Python de forma prática e interativa.

