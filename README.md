# 📊 Excel Analytics com Python

Projeto desenvolvido por **Raphael Campos Squilaro** para realizar análise de ocupação utilizando arquivos Excel com Python, através das bibliotecas **Pandas** e **OpenPyXL**.

---

# 🚀 Objetivo do Projeto

Este projeto lê uma planilha Excel contendo informações de ocupação, agrupa os dados por:

- Registro
- Nome

E soma a quantidade total de horas de ocupação de cada pessoa.

Ao final, o sistema exibe no terminal uma frase personalizada com o total de horas de cada registro.

---

# 🛠️ Tecnologias Utilizadas

- Python 3
- Pandas
- OpenPyXL
- Excel (.xlsx)

---

# 📂 Estrutura do Projeto

```bash
📁 projeto-analytics/
│
├── ocupacao.xlsx
├── analytics.py
└── README.md
```

---

# 📥 Instalação do Python

Caso ainda não tenha o Python instalado:

## Windows

1. Acesse:
   
   https://www.python.org/downloads/

2. Faça o download da versão mais recente.

3. Durante a instalação:
   - Marque a opção:
   
   ```bash
   Add Python to PATH
   ```

4. Finalize a instalação.

---

# 📦 Instalação das Bibliotecas

Após instalar o Python, abra o terminal ou CMD e execute:

```bash
pip install pandas openpyxl
```

---

# 📄 Estrutura da Planilha Excel

O arquivo `ocupacao.xlsx` deve possuir as seguintes colunas:

| Registro | Nome | Horas |
|----------|------|--------|
| 123 | João | 8 |
| 123 | João | 4 |
| 456 | Maria | 6 |

---

# 🧠 Explicação do Código

## 1. Importação do Pandas

```python
import pandas as pd
```

O Pandas é utilizado para leitura e manipulação de dados.

---

## 2. Leitura da Planilha Excel

```python
planilha = pd.read_excel('ocupacao.xlsx')
```

Aqui o Python lê o arquivo Excel e transforma os dados em um DataFrame.

---

## 3. Agrupamento dos Dados

```python
resultado = planilha.groupby(["Registro", "Nome"])["Horas"].sum()
```

O método:

```python
groupby()
```

agrupa os dados por:

- Registro
- Nome

Depois:

```python
sum()
```

soma todas as horas relacionadas a cada pessoa.

---

## 4. Exibição dos Resultados

```python
for (registro,nome), horas in resultado.items():
    print(f'O registro {registro} de {nome} têm {horas} horas de ocupação no SENAI')
```

O `for` percorre os dados agrupados e exibe o resultado no terminal.

---

# 💻 Código Completo

```python
#Author: Raphael Campos Squilaro
#Project: Excel painel analytics with python and imported of pandas and openpyxl

#realizing the imports for analytics
import pandas as pd

#read the excel's painel
planilha = pd.read_excel('ocupacao.xlsx')

#Group by name
resultado = planilha.groupby(["Registro" , "Nome"])["Horas"].sum()

#loop to display results
for (registro,nome), horas in resultado.items():
    print(f'O registro {registro} de {nome} têm {horas} horas de ocupação no SENAI')
```

---

# ▶️ Como Executar o Projeto

No terminal, dentro da pasta do projeto, execute:

```bash
python analytics.py
```

---

# ✅ Exemplo de Saída

```bash
O registro 123 de João têm 12 horas de ocupação no SENAI
O registro 456 de Maria têm 6 horas de ocupação no SENAI
```

---

# 📈 Possíveis Melhorias Futuras

- Exportar resultados para outro Excel
- Criar gráficos automáticos
- Criar dashboard com Power BI
- Interface gráfica com Tkinter
- Integração com banco de dados
- Automação de relatórios

---

# 👨‍💻 Autor

## Raphael Campos Squilaro

Projeto desenvolvido para estudos de análise de dados e automação com Python.
