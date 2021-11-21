import pandas as pd

lotto  = pd.read_csv('../Data/data/LOTTO.csv')
print(lotto.astype)
print()
print(lotto[::-1])
print()
print(lotto.iloc[10:16,1:5])