import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("q1_q17_dr24_koi_2025.10.20_14.41.01.csv")
df_filtrado = df[df['koi_disposition'].isin(['CONFIRMED','CANDIDATE'])].copy()

df_filtrado['tipo_planeta'] = pd.NA

def estima_massa(raio):
    if pd.isna(raio):
        return pd.NA
    if raio <= 1.5:  
        return raio**3  
    elif raio <= 4:  
        return 2.69 * (raio**0.93)
    else:  
        return 318 * (raio / 11.2)**1.0  

df_filtrado['planet_mass'] = df_filtrado['koi_prad'].apply(estima_massa)

df_filtrado.loc[df_filtrado['koi_prad'] <= 1.6, 'tipo_planeta'] = 'Rochoso'

df_filtrado.loc[
    (df_filtrado['koi_prad'] > 1.6) & (df_filtrado['planet_mass'] <= 10), 
    'tipo_planeta'
] = 'Super-Terra'

df_filtrado.loc[
    (df_filtrado['planet_mass'] > 17) & (df_filtrado['planet_mass'] <= 127), 
    'tipo_planeta'
] = 'Netuniano'

df_filtrado.loc[df_filtrado['planet_mass'] > 127, 'tipo_planeta'] = 'Gasoso'

##amostragem_p = df.head(50)

def planetas():
    tipos = df["koi_disposition"].value_counts().index
    valores = df["koi_disposition"].value_counts().values

    fig, ax = plt.subplots()
    plt.suptitle("Planetas Confirmados / Candidatos / Falsos Positivos")
    ax.grid(alpha=0.4)
    ax.set_axisbelow(True)
    barras = ax.bar(tipos, valores)
    ax.bar_label(barras)

    plt.show()

def estrelas():
    estrelas = df_filtrado["kepoi_name"].str[:6].drop_duplicates().tolist()
    print(f"Estrelas: {len(estrelas)}")

def planetasPorestrelas():
    planetas_por_estrela = df_filtrado["kepoi_name"].str[:6].value_counts()
    frequencia = planetas_por_estrela.value_counts().sort_index()

    fig, ax = plt.subplots()
    ax.bar(frequencia.index, frequencia.values)
    ax.bar_label(ax.containers[0])
    ax.grid(alpha=0.4)
    ax.set_axisbelow(True)

    plt.suptitle("Frequência de planetas por estrela")
    plt.xlabel("Número de planetas")
    plt.ylabel("Quantidade de estrelas")
    plt.show()

def tipoPlaneta():
    rochosos = (df_filtrado['tipo_planeta'] == 'Rochoso').sum()
    netunianos = (df_filtrado['tipo_planeta'] == 'Netuniano').sum()
    gasosos = (df_filtrado['tipo_planeta'] == 'Gasoso').sum()
    superterra = (df_filtrado['tipo_planeta'] == 'Super-Terra').sum()

    planetas = [rochosos, netunianos, gasosos, superterra]
    labels = ['Rochoso', 'Netuniano', 'Gasoso', 'Super-Terra']
    cores = ['olive', 'violet', 'lime', 'yellow']

    plt.figure(figsize=(6, 6))
    plt.pie(
        planetas,
        colors=cores,
        startangle=90,
        shadow=True,
        autopct='%1.1f%%',
        wedgeprops={'linewidth': 1, 'edgecolor': 'black'}
    )

    plt.legend(labels, loc='upper right')

    plt.title("Tipos de Planetas Detectados")
    plt.tight_layout()
    plt.show()

def relacaoPlanetaEstrela():
    temp_min = df_filtrado['koi_steff'].min()
    temp_max = df_filtrado['koi_steff'].max()

    intervalos = np.arange(temp_min, temp_max + 1000, 1000)
    
    df_filtrado.loc[:, 'faixa_temp'] = pd.cut(df_filtrado['koi_steff'], bins=intervalos)
    tabela = pd.crosstab(df_filtrado['faixa_temp'], df_filtrado['tipo_planeta'])
    ax = tabela.plot( kind='bar', stacked=True, figsize=(12,6), color=['olive','violet','lime','yellow','red'] )
    
    plt.xlabel("Faixa de temperatura das estrelas (K)")
    plt.ylabel("Número de planetas")
    plt.title("Distribuição de tipos de planetas por faixa de temperatura estelar")
    plt.legend(title="Tipo de planeta")
    plt.grid(alpha=0.3, axis='y')
    plt.show()
    
def tudo():
    planetas()
    estrelas()
    planetasPorestrelas()
    tipoPlaneta()
    relacaoPlanetaEstrela()

tudo()