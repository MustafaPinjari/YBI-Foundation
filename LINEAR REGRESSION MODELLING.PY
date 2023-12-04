import pandas as pd
df = pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Salary%20Data.csv')

df.head()
df.info()
df.describe()
df.columns()