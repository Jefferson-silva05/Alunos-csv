import csv

def add(arq, ID, nome, notas, media):
    novo_aluno = {"ID": ID, "NOME": nome, "1BIM": notas[0], "2BIM": notas[1], "3BIM": notas[2], "4BIM": notas[3], "MEDIA": media}
    fieldnames = ["ID", "NOME", "1BIM", "2BIM", "3BIM", "4BIM", "MEDIA"]
    
    # Valida se o arquivo já possui conteúdo para decidir se precisa escrever o cabeçalho
    precisa_cabecalho = True
    try:
        with open(arq, "r", newline="", encoding="utf-8") as a:
            leitor = csv.reader(a)
            if any(leitor):
                precisa_cabecalho = False
    except FileNotFoundError:
        pass
        
    try:
        with open(arq, "a", newline="", encoding="utf-8") as a:
            dados = csv.DictWriter(a, fieldnames=fieldnames)
            if precisa_cabecalho:
                dados.writeheader()
            dados.writerow(novo_aluno)
        return True
    except Exception as erro:
        print(f"ERRO! {erro}")
        return False
        
def lerArquivo(arq):
    try:
        with open(arq, "r", newline="", encoding="utf-8") as a:
            dados = csv.DictReader(a)
            return list(dados)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"ERRO ao ler o arquivo: {e}")
        return []
        
def Atualizar(arq, aluno_id, bimestre, nota):
    dados = lerArquivo(arq)
    if not dados:
        print("Erro: Nenhum dado encontrado ou arquivo inexistente.")
        return
        
    bi = str(bimestre) + "BIM"
    encontrado = False
    for linha in dados:
        if linha["ID"] == str(aluno_id):
            linha[bi] = str(nota)

            media = (
                float(linha["1BIM"]) +
                float(linha["2BIM"]) +
                float(linha["3BIM"]) +
                float(linha["4BIM"])
            ) / 4
            linha["MEDIA"] = str(round(media, 1))
            encontrado = True
            break
            
    if encontrado:
        salvar(arq, dados)
        print("Nota atualizada com sucesso!")
    else:
        print("ERRO! ID do aluno não encontrado.")

def salvar(arq, novos_dados):
    try:
        with open(arq, "w", newline="", encoding="utf-8") as a:
            fieldnames = ["ID", "NOME", "1BIM", "2BIM", "3BIM", "4BIM", "MEDIA"]
            dados = csv.DictWriter(a, fieldnames=fieldnames)
            dados.writeheader()
            dados.writerows(novos_dados)
    except Exception as e:
        print(f"ERRO ao salvar dados: {e}")
        
def excluir(arq, id_aluno):
    dados = lerArquivo(arq)
    if not dados:
        print("Erro: Nenhum dado encontrado ou arquivo inexistente.")
        return
        
    novos_dados = [linha for linha in dados if linha["ID"] != str(id_aluno)]
    
    if len(novos_dados) < len(dados):
        salvar(arq, novos_dados)
        print("Registro removido com sucesso!")
    else:
        print("ERRO! ID do aluno não encontrado.")