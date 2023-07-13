import pandas as pd


use_cols = ["NU_INSCRICAO", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_COR_RACA", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
data = pd.read_csv('MICRODADOS_ENEM_2019.csv', usecols=use_cols)


data = data.sort_values('NU_NOTA_MT').reset_index(drop=True)


def interpolation_search(data, column, value):
    low = 0
    high = len(data) - 1

    while low <= high and value >= data.loc[low, column] and value <= data.loc[high, column]:
        index = low + int(((float(high - low) / (data.loc[high, column] - data.loc[low, column])) * (value - data.loc[low, column])))

        if data.loc[index, column] == value:
            return data[data[column] == value]

        if data.loc[index, column] < value:
            low = index + 1

        else:
            high = index - 1

    return "No results found"


print(interpolation_search(data, 'NU_NOTA_MT', 600.0))
