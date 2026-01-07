import pandas as pd
path = r"C:\Users\Millpark\Downloads\anime.csv"
df = pd.read_csv(path)
print('shape:', df.shape)
print('columns:', list(df.columns))
print('\nfirst 5 rows:')
print(df.head().to_string())
