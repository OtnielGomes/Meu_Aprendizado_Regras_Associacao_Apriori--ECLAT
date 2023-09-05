import pandas as pd
from pyECLAT import ECLAT

# Pre-processing
marketplace_data = pd.read_csv('mercado.csv', header=None)
print(marketplace_data)
eclat = ECLAT(data=marketplace_data)

print(eclat.df_bin)
print(eclat.uniq_)

indexes, support = eclat.fit(min_support=0.3, min_combination=1,
                             max_combination=3)

print(indexes)
print(support)