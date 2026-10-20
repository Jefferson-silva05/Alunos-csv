import csv

def cabecalho(text):
    for n, v in enumerate(text):
        print(f"[ {n+1} ] {v}")
    print("-="*23)
    
def leiaInt(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("ERRO! Digite um valor Inteiro válido!")
            
def leiaFloat(msg):
    while True:
        try:
            nova_nota = float(input(msg))
            if 0 <= nova_nota <= 10:
                return nova_nota
            else:
                print("DIGITE A NOVA NOTA DE 0 A 10")
        except ValueError:
            print("ERRO! Digite um valor Numérico válido!")
            
def validText(msg):  
    while True:
        nome = str(input(msg)).strip()
        if nome:
            return nome
        print("ERRO! O campo não pode estar em branco!")
        
def validNota():
    notas = []
    while True:
        if len(notas) == 4:
            return notas
        try:
            nota = float(input(f"nota do {len(notas)+1}° bimestre: "))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("DIGITE A NOTA DE 0 A 10")
        except Exception as e:
            print(f"ERRO! {e}")
            
def criarId(arq):
    try:
        with open(arq, "r", encoding="utf-8", newline="") as a:
            dados = list(csv.DictReader(a))
            if not dados:
                return 1
            maior_id = max(int(linha["id"]) for linha in dados)
            return maior_id + 1
    except (FileNotFoundError, ValueError, KeyError):
        return 1