# 📊 Excel Analytics com Python, Pandas e OpenPyXL

Projeto desenvolvido em Python para realizar análise de dados em planilhas Excel utilizando as bibliotecas Pandas e OpenPyXL.

O sistema lê uma planilha contendo registros de ocupação, agrupa os dados por matrícula e nome, soma as horas e exibe um relatório organizado no terminal.

---

# 🚀 Funcionalidades

✅ Leitura de arquivos Excel  
✅ Manipulação de dados com Pandas  
✅ Agrupamento de informações  
✅ Soma automática de horas  
✅ Relatório em console  
✅ Automação de análise de dados  

---

# 🐍 O que é Python?

Python é uma linguagem de programação moderna, simples e poderosa, muito utilizada em:

- Ciência de Dados
- Automação
- Inteligência Artificial
- Desenvolvimento Web
- Análise de Dados

Sua sintaxe simples facilita o aprendizado e aumenta a produtividade.

---

# 📚 O que é Pandas?

Pandas é uma biblioteca do Python especializada em:

- Manipulação de dados
- Leitura de planilhas
- Organização de tabelas
- Análise de informações
- Tratamento de dados

Ela trabalha principalmente com:

## 🔹 DataFrame

Estrutura semelhante a uma tabela Excel:

| Registro | Nome | Horas |
|---|---|---|
| 1001 | João | 5 |
| 1001 | João | 3 |
| 1002 | Maria | 4 |

---

# 📘 O que é OpenPyXL?

OpenPyXL é uma biblioteca usada para:

✅ Ler arquivos `.xlsx`  
✅ Criar planilhas Excel  
✅ Editar células  
✅ Automatizar relatórios  

O Pandas utiliza o OpenPyXL internamente para manipular arquivos Excel.

---

# 🛠 Tecnologias Utilizadas

- Python 3.x
- Pandas
- OpenPyXL

---

# ⚙️ Instalação do Python

## 1️⃣ Baixe o Python

Acesse:

```bash
https://www.python.org/downloads/
```

## 2️⃣ Verifique a instalação

```bash
python --version
```

---

# 📦 Instalação das Bibliotecas

## Instale o Pandas

```bash
pip install pandas
```

## Instale o OpenPyXL

```bash
pip install openpyxl
```

---

# 📂 Estrutura do Projeto

```bash
excel-analytics/
│
├── ocupacao.xlsx
├── main.py
├── requirements.txt
└── README.md
```

---

# ▶️ Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/excel-analytics.git
```

## 2️⃣ Entre na pasta

```bash
cd excel-analytics
```

## 3️⃣ Instale as dependências

```bash
pip install pandas openpyxl
```

## 4️⃣ Execute o projeto

```bash
python main.py
```

---

# 🧠 Explicação Detalhada do Código

---

# 📥 Importação do Pandas

```python
import pandas as pd
```

O `pd` é apenas um apelido para facilitar a escrita do código.

---

# 📄 Leitura da Planilha Excel

```python
planilha = pd.read_excel('ocupacao.xlsx')
```

Aqui o Pandas:

✅ Abre o arquivo Excel  
✅ Lê os dados  
✅ Converte tudo em um DataFrame  

---

# 🔎 Agrupamento dos Dados

```python
resultado = planilha.groupby(["Registro", "Nome"])["Horas"].sum()
```

## O que acontece aqui?

### `groupby()`

Agrupa os dados por:

- Registro
- Nome

### `["Horas"]`

Seleciona apenas a coluna de horas.

### `.sum()`

Realiza a soma das horas agrupadas.

---

# 📊 Exemplo Visual

## Dados da planilha:

| Registro | Nome | Horas |
|---|---|---|
| 1001 | João | 5 |
| 1001 | João | 3 |
| 1002 | Maria | 4 |

---

## Resultado:

| Registro | Nome | Total de Horas |
|---|---|---|
| 1001 | João | 8 |
| 1002 | Maria | 4 |

---

# 🔁 Loop para Exibição

```python
for (registro, nome), horas in resultado.items():
```

O loop percorre cada linha agrupada.

---

# 🖥 Exibição do Resultado

```python
print(f'O registro {registro} de {nome} têm {horas} horas de ocupação no SENAI')
```

Exemplo:

```bash
O registro 1001 de João têm 8 horas de ocupação no SENAI
```

---

# 📚 Conceitos Aprendidos

✅ Leitura de Excel com Python  
✅ Manipulação de DataFrames  
✅ Agrupamento de dados  
✅ Soma de valores  
✅ Loops em Python  
✅ Automação de relatórios  

---

# 🎯 Objetivos do Projeto

- Aprender análise de dados
- Trabalhar com planilhas Excel
- Utilizar Pandas na prática
- Automatizar processos
- Melhorar lógica de programação

---

# 💡 Possíveis Melhorias Futuras

- Interface gráfica
- Exportação automática de relatórios
- Gráficos com Matplotlib
- Dashboard interativo
- Filtros avançados
- Integração com banco de dados

---

# 👨‍💻 Autor

Desenvolvido por **Raphael Campos Squilaro**

---

# 📜 Licença

Este projeto possui fins educacionais.
