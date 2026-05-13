# 📊 Análise de Dados com Python e Pandas

Projeto desenvolvido para estudos e aplicações de Análise de Dados utilizando Python e a poderosa biblioteca Pandas.

Este repositório aborda desde a instalação do ambiente até manipulação, limpeza, exploração e análise de dados de forma prática e detalhada.

---

# 🐍 O que é Python?

Python é uma linguagem de programação de alto nível, conhecida por sua sintaxe simples, legibilidade e grande utilização em:

- Ciência de Dados
- Inteligência Artificial
- Automação
- Desenvolvimento Web
- Análise de Dados
- Machine Learning

Python se tornou uma das principais linguagens do mercado devido à sua produtividade e vasta quantidade de bibliotecas.

---

# 📚 O que é Pandas?

Pandas é uma biblioteca do Python criada para manipulação e análise de dados.

Ela permite trabalhar com:

✅ Planilhas  
✅ Arquivos CSV  
✅ Dados em Excel  
✅ Bancos de dados  
✅ Tabelas estruturadas  

Com Pandas é possível:

- Ler dados
- Limpar informações
- Filtrar registros
- Criar análises
- Gerar estatísticas
- Organizar tabelas
- Transformar dados

---

# 🚀 Instalação do Python

## 1️⃣ Baixe o Python

Acesse o site oficial:

```bash
https://www.python.org/downloads/
```

## 2️⃣ Verifique a instalação

Abra o terminal e execute:

```bash
python --version
```

---

# ⚙️ Instalação do Pandas

## Instale utilizando o pip

```bash
pip install pandas
```

---

# 📦 Bibliotecas Recomendadas

Além do Pandas, é comum utilizar:

```bash
pip install numpy matplotlib seaborn openpyxl
```

### Explicação:

| Biblioteca | Função |
|---|---|
| Pandas | Manipulação de dados |
| NumPy | Operações matemáticas |
| Matplotlib | Criação de gráficos |
| Seaborn | Visualização de dados |
| Openpyxl | Leitura de arquivos Excel |

---

# 📂 Estrutura do Projeto

```bash
analise-dados-python/
│
├── datasets/
│
├── notebooks/
│
├── scripts/
│
├── imagens/
│
├── requirements.txt
│
└── README.md
```

---

# 📖 Conceitos Fundamentais do Pandas

---

# 🔹 DataFrame

O DataFrame é a principal estrutura do Pandas.

Ele funciona como uma tabela:

| Nome | Idade | Cidade |
|---|---|---|
| João | 25 | São Paulo |
| Maria | 30 | Campinas |

---

# 🔹 Series

Uma Series representa uma coluna única de dados.

Exemplo:

```python
import pandas as pd

idades = pd.Series([20, 25, 30])
print(idades)
```

---

# 📥 Importando o Pandas

```python
import pandas as pd
```

O `pd` é um apelido utilizado por convenção.

---

# 📄 Lendo Arquivos CSV

```python
import pandas as pd

df = pd.read_csv('dados.csv')

print(df)
```

---

# 📊 Visualizando os Dados

## Primeiras linhas

```python
df.head()
```

## Últimas linhas

```python
df.tail()
```

## Informações gerais

```python
df.info()
```

## Estatísticas básicas

```python
df.describe()
```

---

# 🧹 Limpeza de Dados

## Verificando valores nulos

```python
df.isnull().sum()
```

## Removendo valores nulos

```python
df.dropna()
```

## Preenchendo valores vazios

```python
df.fillna(0)
```

---

# 🔎 Filtrando Dados

## Exemplo:

```python
df[df['idade'] > 18]
```

---

# 📈 Criando Gráficos

```python
import matplotlib.pyplot as plt

df['vendas'].plot()
plt.show()
```

---

# 💾 Salvando Arquivos

## Exportar CSV

```python
df.to_csv('novo_arquivo.csv')
```

## Exportar Excel

```python
df.to_excel('dados.xlsx')
```

---

# 🧠 Principais Aplicações da Análise de Dados

- Business Intelligence
- Dashboards
- Relatórios
- Ciência de Dados
- Machine Learning
- Análise Financeira
- Marketing
- Automação empresarial

---

# 🎯 Objetivos do Projeto

- Aprender análise de dados
- Dominar a biblioteca Pandas
- Trabalhar com arquivos CSV e Excel
- Criar visualizações
- Manipular grandes volumes de dados
- Desenvolver habilidades em Data Science

---

# 🛠 Tecnologias Utilizadas

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# ▶️ Como Executar

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/analise-dados-python.git
```

## 2️⃣ Entre na pasta

```bash
cd analise-dados-python
```

## 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

## 4️⃣ Execute os scripts

```bash
python nome_do_arquivo.py
```

---

# 📚 Aprendizados

Neste projeto são praticados:

✅ Manipulação de dados  
✅ Limpeza de dados  
✅ Estatística básica  
✅ Visualização de dados  
✅ Automação de análises  
✅ Estruturação de projetos  

---

# 👨‍💻 Autor

Desenvolvido por **Raphael Campos Squilaro**

---

# 📜 Licença

Este projeto possui fins educacionais.
