from arquivo import *
from modulo import *

arq = "alunos.csv"

while True:
    cabecalho(["Adicionar Aluno", "Listar Alunos", "Atualizar Nota", "Remover Aluno", "Sair"])
    opc = leiaInt("Sua Opção: ")
    
    match opc:
        case 1:
            print("-="*23)
            nome = validText("Nome do Aluno(a): ")
            notas = validNota()
            ID = criarId(arq)
            if add(arq, ID, nome, notas):
                print(f"Aluno {nome} adicionado com sucesso!")
            print("-="*23)
        case 2:
            print("-="*23)
            dados = lerArquivo(arq)
            if not dados:
                print("Nenhum aluno cadastrado.")
            else:
                for linha in dados:
                    print(f"ID: {linha['id']} | Nome: {linha['nome']} | Notas: {linha['1BIMESTRE']}, {linha['2BIMESTRE']}, {linha['3BIMESTRE']}, {linha['4BIMESTRE']}")
            print("-="*23)

            
        case 3:
            print("-="*23)
            dados = lerArquivo(arq)
            if not dados:
                print("ERRO! Nenhum aluno cadastrado.")
            else:
                id_aluno = leiaInt("ID do aluno(a): ")
                
                # Cria uma lista apenas com os IDs existentes convertidos para int
                ids_validos = [int(linha["id"]) for linha in dados]
                
                if id_aluno in ids_validos:
                    bimestre = leiaInt("Deseja mudar a nota de qual Bimestre (1 a 4): ")
                    if 1 <= bimestre <= 4:
                        nota = leiaFloat("Nova nota do Aluno(a): ")
                        Atualizar(arq, id_aluno, bimestre, nota)
                    else:
                        print("ERRO! Bimestre inválido! Digite de 1 a 4.")
                else:
                    print("ERRO! Aluno não encontrado.")
            print("-="*23)
        case 4:
            dados = lerArquivo(arq)
            if not dados:
                print("ERRO! Nenhum aluno cadastrado.")
            else:
                id_aluno = leiaInt("ID do Aluno(a) para remover: ")
                ids_validos = [int(linha["id"]) for linha in dados]
                
                if id_aluno in ids_validos:
                    excluir(arq, id_aluno)
                else:
                    print("ERRO! Aluno não encontrado.")
        case 5:
            print("Saindo...")
            break
        case _:
            print("ERRO! Opção inválida. Escolha entre 1 e 5.")