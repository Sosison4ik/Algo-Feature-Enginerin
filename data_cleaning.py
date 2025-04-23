import pandas as pd
import numpy as np
df = pd.read_csv('GooglePlayStore_wild.csv')


#df['Size']=df['Installs'].apply(lambda x: float(x.replace('M', '').replace('K', '')))
print(df.info())

# Выведи информацию о всем DataFrame, чтобы узнать какие столбцы нуждаются в очистке
# Выведи информацию о всем DataFrame, чтобы узнать, какие столбцы нуждаются в очистке
# Сколько в датасете приложений, у которых не указан ('NaN') рейтинг ('Rating')?
print('\n')
print(df['Rating'].isna().sum())
# Замени пустое значение ('NaN') рейтинга ('Rating') для таких приложений на -1.
df['Rating'] = df['Rating'].fillna(-1)
print('После замены пустых значений')
print(df['Rating'].isna().sum())
# Определи, какое ещё значение размера ('Size') хранится в датасете помимо Килобайтов и Мегабайтов, замени его на -1.
# Преобразуй размеры приложений ('Size') в числовой формат (float). Размер всех приложений должен измеряться в Мегабайтах.
def convert_size(size_str):
    size_str = size_str.strip()
    if size_str.endswith('M'):
        try:
            return float(size_str[:-1])
        except ValueError:
            return -1
    elif size_str.endswith('k') or size_str.endswith('K'):
        try:
            return float(size_str[:-1]) / 1024
        except ValueError:
            return -1
    else:
        return -1
    
df['Size'] = df['Size'].apply(convert_size)

# Чему равен максимальный размер ('Size') приложений из категории ('Category') 'TOOLS'?
print('\n')
print(df[df['Category'] == 'TOOLS']['Size'].max())

# Бонусные задания
# Замени тип данных на целочисленный (int) для количества установок ('Installs').
# В записи количества установок ('Installs') знак "+" необходимо игнорировать.
# Т.е. если в датасете количество установок равно 1,000,000+, то необходимо изменить значение на 1000000
print('\n')
df['Installs']=df['Installs'].apply(lambda x: int(x.replace(',','').replace('+', '')))
print(df['Installs'].dtypes)

# Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом,
# посчитай среднее количество установок ('Installs') в каждой группе. Результат округли до десятых.
# В полученной таблице найди ячейку с самым большим значением. 
# К какой возрастной группе и типу приложений относятся данные из этой ячейки?
grouped = df.groupby(['Category', 'Content Rating'])['Installs'].mean().round(1)
grouped_df = grouped.reset_index()

max_idx = grouped.idxmax()
max_value = grouped.max()

print(max_value)
print(f"Категория '{max_idx[0]}' возрастная группе '{max_idx[1]}'")
# У какого приложения не указан тип ('Type')? Какой тип там необходимо записать в зависимости от цены?
mask = df['Type'].isna()
df.loc[mask, 'Type'] = df.loc[mask, 'Price'].apply(lambda x: 'Free' if x == 0 else 'Paid')
print(df)
# Выведи информацию о всем DataFrame, чтобы убедиться, что очистка прошла успешно
print('\n')
print(df.info())