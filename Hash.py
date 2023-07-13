import pandas as pd


use_cols = ["NU_INSCRICAO", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_COR_RACA", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
data = pd.read_csv('MICRODADOS_ENEM_2019.csv', usecols=use_cols)


data = data.head(1000)


hash_table = data.set_index('NU_INSCRICAO').T.to_dict('list')


def search_hash_table(hash_table, inscricao):
    if inscricao in hash_table:
        return hash_table[inscricao]
    else:
        return "Sem resultados"

# Testando a pesquisa
print(search_hash_table(hash_table, 420))
