import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels

sns.set(font_scale=0.5)

df = pd.read_csv("s2final.csv")

df['steam_price'] = pd.to_numeric(df['steam_price'], errors='coerce')
df['floatdb_price'] = pd.to_numeric(df['floatdb_price'], errors='coerce')
df = df.dropna()

#print(df.head()) #show first few rows    

heatmap = sns.heatmap(df.corr(),
                      vmin=-1,
                      vmax=1,
                      annot=True,
                      cmap='BrBG',
                      annot_kws={'size': 3}
                      )

plt.savefig("colormap.svg")

plt.subplots(figsize = (10, 10))


cor = sns.lmplot(x ="steam_price",
                 y ="floatdb_price",
                 hue ="wear",
                 data = df,
                 order = 1,
                 logistic=False,
                 y_jitter=.03)


cor.savefig("Cor4.svg")
