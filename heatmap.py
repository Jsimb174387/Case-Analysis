import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels

sns.set(font_scale=0.5)

df = pd.read_csv("DSFinalDB")
df['case_price'] = df['case_price'].str.replace(',', '')
df['case_price'] = df['case_price'].str.replace('$', '')
df['case_volume'] = df['case_volume'].str.replace(',', '')
df['case_volume'] = df['case_volume'].str.replace('"', '')
df['case_price'] = df['case_price'].astype(float)
df['case_volume'] = df['case_volume'].astype(int)
df['case_name'] = df['case_name'].astype(str)
df['hash_name'] = df['hash_name'].astype(str)
df['name'] = df['name'].astype(str)
df['wear'] = df['wear'].astype(str)
df['volume'] = df['volume'].astype(int)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df = df.dropna()
df.info(memory_usage = "deep")

#print(df.head()) #show first few rows    

heatmap = sns.heatmap(df.corr(),
                      vmin=-1,
                      vmax=1,
                      annot=True,
                      cmap='BrBG',
                      annot_kws={'size': 3}
                      )

plt.savefig("FinalDBheatmap.svg")

plt.subplots(figsize = (10, 10))


cor = sns.lmplot(x ="case_price",
                 y ="price",
                 hue ="case_name",
                 data = df,
                 order = 1,
                 logistic=False,
                 y_jitter=.03)


cor.savefig("FinalDBPlot.svg")
