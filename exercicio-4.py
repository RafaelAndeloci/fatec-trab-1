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

# Exercício 4

fig, ax = plt.subplots(2, 2, figsize=(7, 5))

# 4.1 Cartão KPI

# Contando os clientes ativos:
total_clientes_ativos = len(df)

# Colocando estilos e background
ax[0, 0].axis("off")
fig.set_facecolor("#B0B8BD")
rect = plt.Rectangle(
    (0, 0), 1, 1, clip_on=False, linewidth=3, edgecolor="#E0E0E0", facecolor="#27A4ED"
)
ax[0, 0].add_patch(rect)

# Texto da quantidade de clientes ativos
ax[0, 0].text(
    0.5,
    0.42,
    f"{total_clientes_ativos}",
    fontsize=32,
    fontweight="bold",
    color="#FFFFFF",
    ha="center",
    va="center",
    clip_on=True,
    transform=ax[0, 0].transAxes,
)

# Texto do titulo
ax[0, 0].text(
    0.5,
    0.82,
    "Total de Clientes Ativos",
    fontsize=13,
    fontweight="bold",
    color="#000000",
    ha="center",
    va="center",
    clip_on=True,
    transform=ax[0, 0].transAxes,
)

# 4.2 Gráfico de linha/série temporal

# Formatando os dois formatos de data presentes na coluna DATA cadastro
datas = df["DATA cadastro"].astype("string").str.strip()
df["DATA cadastro"] = pd.Series(pd.NaT, index=df.index, dtype="datetime64[ns]")

# usando regex para ajudar na formatação das datas
formato_iso = datas.str.match(r"^\d{4}-\d{2}-\d{2}$", na=False)
df.loc[formato_iso, "DATA cadastro"] = pd.to_datetime(
    datas[formato_iso], format="%Y-%m-%d", errors="coerce"
)
df.loc[~formato_iso, "DATA cadastro"] = pd.to_datetime(
    datas[~formato_iso], format="%d/%m/%Y", errors="coerce"
)

# Remove registros sem data ou consumo e ordena pelo mês do cadastro.
dados_consumo = df.dropna(subset=["DATA cadastro", "Consumo_kWh (mês)"]).sort_values(
    "DATA cadastro"
)

tempo_cons_kwh_mes = dados_consumo["DATA cadastro"].to_numpy()
consumo_kwh_mes = dados_consumo["Consumo_kWh (mês)"].to_numpy()
# Renderizando o gráfico
ax[0, 1].plot(
    tempo_cons_kwh_mes,
    consumo_kwh_mes,
    color="#E85D04",
    marker="o",
    linewidth=2,
    markersize=4,
)
# Na hora de apresentar colocando no eixo x formatado as datas com mês e ano
ax[0, 1].xaxis.set_major_formatter(mdates.DateFormatter("%m/%Y"))
ax[0, 1].set_title("Consumo por mês")
ax[0, 1].tick_params(axis="x", rotation=45)

# 4.3 Gráfico de barras
# usando o groupby pela categoria e projetando o consumo médio
# e removendo itens não registrados
consumo_medio_categoria = (
    df.dropna(subset=["Categoria_Cliente", "Consumo_kWh (mês)"])
    .groupby("Categoria_Cliente")["Consumo_kWh (mês)"]
    .mean()
    .sort_values()
)

# renderizando
ax[1, 0].barh(
    consumo_medio_categoria.index,
    consumo_medio_categoria.values,
    color="#2A9D8F",
)
ax[1, 0].set_title("Consumo médio por categoria")
ax[1, 0].set_xlabel("Consumo médio (kWh)")
ax[1, 0].set_ylabel("Categoria do cliente")

# 4.4 Gráfico de pizza
# Pegando os clientes por região, excluindo os sem registro  e formatando
clientes_por_regiao = (
    df["Região"].dropna().astype(str).str.strip().value_counts().head(5)
)

# Renderizando
ax[1, 1].pie(
    clientes_por_regiao.values,
    labels=clientes_por_regiao.index,
    autopct="%1.1f%%",
)
ax[1, 1].set_title("Clientes por região")

fig.tight_layout(pad=3.0)

# No final mostrando todos os plots
plt.show()
