
import pandas as pd
path_to_data = 'U1_twitterdataset.csv'
data = pd.read_csv(path_to_data)
data.head()


df_dropped = data.drop('Birthplace', axis=1)
df_dropped.head()


data.groupby('Sex').agg({'Political_party': 'count'})


data.iloc[:5,8]


desc = data["Name"].describe()
desc

df_row_dropped = data.drop(2, axis=0)
df_row_dropped.head()


data.columns
df_renamed = data.rename(columns={'Account_ID': 'Id'})
df_renamed.head()


