import pandas as pd

df = pd.read_csv("./dados/trabalho_avaliativo_pandas.csv")

# Exercício 1
# 1.1
# As 5 primeiras e as 5 últimas linhas do DataFrame.

print("\nPrimeiras 5 linhas: ")
print(df.head(5))
print("\nÚltimas 5 linhas: ")
print(df.tail(5))

# O tamanho do conjunto de dados em (linhas, colunas).
print(f"\nNúmero total de linhas\colunas - {df.shape}")

# Os tipos de dados originais de cada coluna.
print("\n\nTipo de variáveis Dados:")
print(df.dtypes)

# O resumo estatístico inicial.
print("\nResumo Estatístico(Média, Mín, Máx): ")
print(df.describe())

# 1.2
# Converter todos os nomes para minúsculas.
df.columns = df.columns.str.lower()

# Remover caracteres especiais como parênteses, cifrões, etc. usando a Expressão Regular.
df.columns = df.columns.str.replace(r"[^\w\s]", "", regex=True)

# REMOVER ESPAÇOS EM BRANCO
df.columns = df.columns.str.strip()

# Substituir espaços internos por underline (_) e remover espaços nas extremidades.
df.columns = df.columns.str.replace(r"\s+", "_", regex=True)

# RENOMEAR TABELAS
df.columns = df.columns.str.replace("renda_mensal_r", "renda_mensal")
df.columns = df.columns.str.replace("região", "regiao")
df.columns = df.columns.str.replace("consumo_kwh_mês", "consumo_kwh_mes")

# Exiba os novos nomes de colunas padronizados.
print(f"\nTabela Padronizada: ")
print(f"\n{df}")
