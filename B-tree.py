import pandas as pd
from blist import sorteddict


use_cols = ["NU_INSCRICAO", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_COR_RACA", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
data = pd.read_csv('MICRODADOS_ENEM_2019.csv', usecols=use_cols)


data = data.head(1000)


index = sorteddict()
for _, row in data.iterrows():
    if row['NU_IDADE'] not in index:
        index[row['NU_IDADE']] = []
    index[row['NU_IDADE']].append(row.to_dict())


def search_btree_index(index, age):
    if age in index:
        return index[age]
    else:
        return "Sem resultados"


print(search_btree_index(index, 18))
