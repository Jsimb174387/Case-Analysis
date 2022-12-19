import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels

sns.set(font_scale=0.5)

df = pd.read_csv("DSFinalDB")
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['volume'] = pd.to_numeric(df['volume'], errors='coerce')
df['case_volume'] = pd.to_numeric(df['case_volume'], errors='coerce')
df = df.dropna()
df['case_price'] = df['case_price'].astype(np.float32)
df['case_volume'] = df['case_volume'].astype(np.int32)
df['case_name'] = df['case_name'].astype(str)
df['hash_name'] = df['hash_name'].astype(str)
df['name'] = df['name'].astype(str)
df['wear'] = df['wear'].astype(str)
df['volume'] = df['volume'].astype(np.int32)

#print(df.head()) #show first few rows    
"""
heatmap = sns.heatmap(df.corr(),
                      vmin=-1,
                      vmax=1,
                      annot=True,
                      cmap='BrBG',
                      annot_kws={'size': 3}
                      )

plt.savefig("FinalDBheatmap.svg")
"""
sns.set(font_scale=1)
"""
df = df.drop('case_volume', axis=1)
df = df.drop('volume', axis=1)
df = df.drop('wear', axis=1)
df = df.drop('name', axis=1)
df = df.drop('hash_name', axis=1)
df_empty = pd.DataFrame({'price_max' : []})
df_empty['price_max'] = df.groupby(['case_name', 'case_price'])['price'].transform(max)
df = df.drop('price', axis=1)
df['price_max'] = df_empty['price_max']
df = df.drop_duplicates()

cor = sns.lmplot(data = df,
                 x = 'case_price',
                 y = 'price_max',
                 hue = 'case_name',
                 order = 1,
                 logistic = False,
                 y_jitter=0.03)

fig = cor.figure

fig.savefig('cormax.svg')
"""

df = df.drop('case_volume', axis=1)
df = df.drop('volume', axis=1)
df = df.drop('wear', axis=1)
df = df.drop('name', axis=1)
df = df.drop('hash_name', axis=1)
df_empty = pd.DataFrame({'price_max' : []})
df_empty['price_max'] = df.groupby(['case_name', 'case_price'])['price'].transform(max)
df = df.drop('price', axis=1)
df['price_max'] = df_empty['price_max']
df = df.drop_duplicates()

cor = plt.subplots()

cor = sns.lmplot(data = df,
                 x = 'case_price',
                 y = 'price_max',
                 hue = 'case_name')

cor = sns.regplot(data = df,
                    x = 'case_price',
                    y = 'price_max',
                    scatter = False)

fig = cor.figure

fig.savefig('cormax.svg')

"""
cases = ['chroma', 'chroma2', 'chroma3', 'danger', 'horizon', 'prisma', 'prisma2', 'spect', 's2']

sns.set(font_scale=1)

for case in cases:

    df = pd.read_csv(case + "final.csv")
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')
    df['case_volume'] = pd.to_numeric(df['case_volume'], errors='coerce')
    df = df.dropna()
    df['case_price'] = df['case_price'].astype(np.float32)
    df['case_volume'] = df['case_volume'].astype(np.int32)
    df['case_name'] = df['case_name'].astype(str)
    df['hash_name'] = df['hash_name'].astype(str)
    df['name'] = df['name'].astype(str)
    df['wear'] = df['wear'].astype(str)
    df['volume'] = df['volume'].astype(np.int32)
    df = df.head(300)

    plt.subplots(figsize = (10, 10))

    sca = sns.scatterplot(x ="price",
                     y ="name",
                     hue ="wear",
                     data = df
                     )

    fig = sca.figure

    fig.savefig(case + "FinalDBPlot.svg")
    """
