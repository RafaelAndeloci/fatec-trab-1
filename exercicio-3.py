import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("./dados/trabalho_avaliativo_pandas.csv")

# Formatando globalmente todos os valores numéricos com duas casas decimais
pd.options.display.float_format = "{:,.2f}".format

# Removendo Espaços do começo e do final dos headers das colunas
df.columns = df.columns.str.strip()

# Formatando colunas
df["Renda Mensal (R$)"] = df["Renda Mensal (R$)"].astype(float)
df["Região"] = df["Região"].fillna("Não Informado")
df["ID_CLIENTE"] = df["ID_CLIENTE"].fillna("Não Informado")

# Exercício 3 - Agrupamento e Agregação

# 3.1
renda_media = df.groupby("Região")["Renda Mensal (R$)"].mean()
print("Renda Mensal Por Região:\n", renda_media, "\n")

total_compras = df.groupby("Região")["Qtd_Compras_Ano"].sum()
print("Total de compras no ano por região:\n", total_compras, "\n")

total_clientes = df.groupby("Região")["ID_CLIENTE"].count()
print("Total de clientes por região:\n", total_clientes, "\n")

# 3.2

clientes_ouro_platinum = df.loc[
    (df["Consumo_kWh (mês)"] > 150)
    & ((df["Categoria_Cliente"] == "Ouro") | (df["Categoria_Cliente"] == "Platinum")),
    ["ID_CLIENTE", "Categoria_Cliente", "Consumo_kWh (mês)"],
]

print(
    "Clientes da categoria Ouro ou Platinum que possuem consumo superior "
    "a 150 kWh:\n",
    clientes_ouro_platinum,
    "\n",
)

