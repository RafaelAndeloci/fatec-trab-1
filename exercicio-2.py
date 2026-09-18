import pandas as pd
import math

df = pd.read_csv("./dados/trabalho_avaliativo_pandas.csv")

# Formatando globalmente todos os valores numéricos com duas casas decimais
pd.options.display.float_format = "{:,.2f}".format

# Removendo Espaços do começo e do final dos headers das colunas
df.columns = df.columns.str.strip()

# Formatando colunas
df["Renda Mensal (R$)"] = df["Renda Mensal (R$)"].astype(float)
df["Região"] = df["Região"].fillna("Não Informado")
df["ID_CLIENTE"] = df["ID_CLIENTE"].fillna("Não Informado")

# Exercício 2
# 2.1
# Relatório de Nulos: Crie um DataFrame explicativo exibindo a quantidade total e a porcentagem (%)
# de valores nulos para cada coluna.
total_nulos = df.isna().sum()
print(f"\nQuantidade total de nulos: \n{total_nulos}")

# %
perc_nulos = (df.isna().sum() / len(df)) * 100
print(f"\nPercentual de nulos por coluna: \n {perc_nulos}")

# 2.2
# Regra A (Identificador Único): Identifique a coluna de chave primária (id_cliente).
linhas = df.isna().any(axis=1)

# Remova as linhas onde o identificador único é nulo.
df = df.dropna(subset=["ID_CLIENTE"])
print(f"\nLinhas removidas: \n{df}")

# Regra C (Limite de Tolerância): Identifique a coluna que possui mais de 50% de
# dados ausentes e faça a remoção completa da coluna.
df = df.drop(columns=["Observações (Feedback)"])
print(f"\nColuna removida: \n{df}")

# 2.3
# Calcule o Coeficiente de Assimetria (das colunas numéricas contínuas (altura_cm e renda_mensal_brl).
# IDENTIFICAÇÃO DE DISTRIBUIÇÃO - HISTOGRAMA
coe_ass_alt = df["Altura (cm)"].skew()
coe_ass_renda = df["Renda Mensal (R$)"].skew()

coe_ass = math.floor(coe_ass_alt * 10) / 10
coe_ass_renda = math.floor(coe_ass_renda * 10) / 10
print(f"\nCoeficiente de assimetria - Altura: {coe_ass}")
print(f"\nCoeficiente de assimetria - Renda: {coe_ass_renda}")

# Se o coeficiente estiver entre -0.5 e 0.5 (distribuição simétrica/normal), impute os nulos com a MÉDIA.
# Se o coeficiente for menor que -0.5 ou maior que 0.5 (distribuição assimétrica/outliers), impute os nulos com a MEDIANA

# MEDIA
media_altura = df["Altura (cm)"].mean()
media_renda = df["Renda Mensal (R$)"].mean()
# MEDIANA
mediana_altura = df["Altura (cm)"].median()
mediana_renda = df["Renda Mensal (R$)"].median()

# ALTURA
# MOTIVOS:
#
if coe_ass >= -0.5 and coe_ass <= 0.5:
    df["Altura (cm)"] = df["Altura (cm)"].fillna(media_altura)
    print(f"\nMédia aplicada devido os valores serem equilibrados - Altura: \n{df}")
else:
    df["Altura (cm)"] = df["Altura (cm)"].fillna(mediana_altura)
    print(
        f"\nMediana aplicada devido os valores serem muito discrepantes - Altura: \n{df}"
    )

# RENDA
# MOTIVOS:
#
if coe_ass_renda >= -0.5 and coe_ass_renda <= 0.5:
    df["Renda Mensal (R$)"] = df["Renda Mensal (R$)"].fillna(media_renda)
    print(f"\nMédia aplicada devido os valores serem equilibrados - Renda: \n{df}")
else:
    df["Renda Mensal (R$)"] = df["Renda Mensal (R$)"].fillna(mediana_renda)
    print(
        f"\nMediana aplicada devido os valores serem muito discrepantes -  Renda: \n{df}"
    )

# 2.4
# Para a coluna categórica (regiao), identifique o valor mais frequente utilizando a MODA (preencha as lacunas ausentes).
moda_regiao = df["Região"].mode()[0]
df["Região"] = df["Região"].fillna(moda_regiao)

print(f"Moda aplicada:\n{df}")

df["DATA cadastro"] = df["DATA cadastro"].str.replace("-", "/", regex=True)

# 2.5
# Converta a coluna de data de cadastro para o tipo datetime.
df["DATA cadastro"] = pd.to_datetime(
    df["DATA cadastro"], format="mixed", dayfirst=True, errors="coerce"
)

# Para a coluna contínua temporal (consumo_kwh_mes), aplique o preenchimento sequencial para preservar a tendência.
df["Consumo_kWh (mês)"] = df["Consumo_kWh (mês)"].ffill()

print(f"\n Tabela tratada:\n{df}")

# Salvando a base tratada sem criar uma coluna de índice extra.
# (Salvo em ./dados/dados_tratados.csv)
df.to_csv("./dados/dados_tratados.csv", index=False)
