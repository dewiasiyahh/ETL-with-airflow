import pandas as pd
from sqlalchemy import create_engine

user      = 'postgres'
password  = 'postgres'
hostname  = '127.0.0.1'
database  = 'postgres'
port      = '5436'
conn_string = f'postgresql://{user}:{password}@{hostname}:{port}/{database}'
engine      = create_engine(conn_string)
conn        = engine.connect()

# ---------- Buat Ambil dan jadiin Table di database------
df = pd.read_csv('https://raw.githubusercontent.com/salbifaza/datasets/main/diamond/diamonds.csv')
df = df[['carat','color','clarity']]
df.to_sql("diamond",engine, if_exists='replace')

# ---------- Ngambil di database buat jadi dataframe ----------
query   = "SELECT * FROM pet"
df_read = pd.read_sql(query,engine)
df_read.head()