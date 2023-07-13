import pandas as pd


class Node:
    def __init__(self, key, val):
        self.left = None
        self.right = None
        self.key = key
        self.val = val

def insert(root, key, val):
    if root is None:
        return Node(key, val)
    else:
        if root.key < key:
            root.right = insert(root.right, key, val)
        else:
            root.left = insert(root.left, key, val)
    return root

def search_bst(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search_bst(root.right, key)
    return search_bst(root.left, key)


use_cols = ["NU_INSCRICAO", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_COR_RACA", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
data = pd.read_csv('MICRODADOS_ENEM_2019.csv', usecols=use_cols)
data = data.head(1000)


root = None
for index, row in data.iterrows():
    root = insert(root, row['NU_INSCRICAO'], row[1:])


result = search_bst(root, 420)
print(result.val if result else "Sem resultados")
