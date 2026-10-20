# Sistema de Gerenciamento de Alunos

Projeto desenvolvido em Python para cadastrar e gerenciar alunos e suas notas escolares por meio de um menu interativo no terminal. Os dados são armazenados em um arquivo CSV.

## Funcionalidades

- **Adicionar aluno:** cadastra o nome do aluno e suas quatro notas bimestrais.
- **Listar alunos:** exibe os alunos cadastrados e suas respectivas notas.
- **Atualizar nota:** permite alterar a nota de um bimestre específico usando o ID do aluno.
- **Remover aluno:** exclui um aluno cadastrado por meio do seu ID.
- **Gerar IDs automaticamente:** atribui um identificador aos novos alunos.
- **Validar entradas:** verifica campos vazios, valores numéricos e notas entre 0 e 10.

## Tecnologias utilizadas

- Python
- CSV para armazenar os dados dos alunos.
- Módulo nativo `csv`.

## Estrutura do projeto

```text
sistema-alunos/
├── main.py
├── modulo.py
├── arquivo.py
├── alunos.csv
└── README.md
```

- `main.py`: contém o menu principal e controla as operações do sistema.
- `modulo.py`: reúne funções de entrada e validação de dados, além da criação automática de IDs.
- `arquivo.py`: contém as funções para adicionar, ler, atualizar, salvar e excluir registros.
- `alunos.csv`: arquivo utilizado para armazenar os dados dos alunos.

## Como executar

**Requisito:** Python instalado no computador.

1. Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

2. Acesse a pasta do projeto:

```bash
cd sistema-alunos
```

3. Execute o arquivo principal:

```bash
python main.py
```
