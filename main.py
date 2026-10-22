from arquivo import *
from modulo import *

arq = "alunos.csv"

while True:
    cabecalho(["Adicionar Aluno", "Listar Alunos", "Atualizar Nota", "Remover Aluno", "Sair"])
    opc = leiaInt("Sua Opção: ")
    
    match opc:
        case 1: # ADD
            print("-="*23)
            nome = validText("Nome do Aluno(a): ")
            notas = validNota()
            media = sum(notas) / 4
            ID = criarId(arq)
            if add(arq, ID, nome, notas, round(media,1)):
                print(f"Aluno {nome} adicionado com sucesso!")
            print("-="*23)
        case 2: # LISTAR TODOS OS ALUNOS
            print("-="*23)
            dados = lerArquivo(arq)
            if not dados:
                print("Nenhum aluno cadastrado.")
            else:
                for linha in dados:
                    print(f"ID: {linha['ID']} | Nome: {linha['NOME']} | Notas: {linha['1BIM']}, {linha['2BIM']}, {linha['3BIM']}, {linha['4BIM']} | Media: {linha['MEDIA']}")
            print("-="*23)

            
        case 3: # ATUALIZAR NOTA
            print("-="*23)
            dados = lerArquivo(arq)
            if not dados:
                print("ERRO! Nenhum aluno cadastrado.")
            else:
                id_aluno = leiaInt("ID do aluno(a): ")
                
                # Cria uma lista apenas com os IDs existentes convertidos para int
                ids_validos = [int(linha["ID"]) for linha in dados]
                
                if id_aluno in ids_validos:
                    bimestre = leiaInt("Deseja mudar a nota de qual Bimestre (1 a 4): ")
                    if 1 <= bimestre <= 4:
                        nota = leiaFloat("Nova nota do Aluno(a): ")
                        Atualizar(arq, id_aluno, bimestre, nota) #MUDAR A NOTA REQUEER MUDAR A MEDIA TAMBEM
                    else:
                        print("ERRO! Bimestre inválido! Digite de 1 a 4.")
                else:
                    print("ERRO! Aluno não encontrado.")
            print("-="*23)
        case 4: # EXCLUIR ALUNO
            dados = lerArquivo(arq)
            if not dados:
                print("ERRO! Nenhum aluno cadastrado.")
            else:
                id_aluno = leiaInt("ID do Aluno(a) para remover: ")
                ids_validos = [int(linha["ID"]) for linha in dados]
                
                if id_aluno in ids_validos:
                    excluir(arq, id_aluno)
                else:
                    print("ERRO! Aluno não encontrado.")
        case 5: # SAIR DO PROGRAMA
            print("Saindo...")
            break
        case _: # CASO NENHUMA OPC FOR SELECIONADA
            print("ERRO! Opção inválida. Escolha entre 1 e 5.")