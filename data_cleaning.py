import pandas as pd
import numpy as np
df = pd.read_csv('GooglePlayStore_wild.csv')


#df['Size']=df['Installs'].apply(lambda x: float(x.replace('M', '').replace('K', '')))
print(df.info())

# Выведи информацию о всем DataFrame, чтобы узнать какие столбцы нуждаются в очистке
# Выведи информацию о всем DataFrame, чтобы узнать, какие столбцы нуждаются в очистке
# Сколько в датасете приложений, у которых не указан ('NaN') рейтинг ('Rating')?
print('\n')
#вывод колличества пустых значений
print(df['Rating'].isna().sum())


# Замени пустое значение ('NaN') рейтинга ('Rating') для таких приложений на -1.

#Замена пустых значений с помощью метода fillna
df['Rating'] = df['Rating'].fillna(-1)
print('После замены пустых значений')
print(df['Rating'].isna().sum())

# Определи, какое ещё значение размера ('Size') хранится в датасете помимо Килобайтов и Мегабайтов, замени его на -1.
# Преобразуй размеры приложений ('Size') в числовой формат (float). Размер всех приложений должен измеряться в Мегабайтах.
def convert_size(size_str):
    
    # обрезка ненужных пробелов
    size_str = size_str.strip()
    #Если в конце строки стоит символ болбшая M
    if size_str.endswith('M'):
        try:
            #смнеа типа с помощью float и среза по последний символ
            return float(size_str[:-1])
        #в случае ошибки возращать значение -1
        except ValueError:
            return -1        
    #Если в конце строки стоит символ k или больша K
    elif size_str.endswith('k') or size_str.endswith('K'):
        try:
            #Перевод в тип float и срез по послдний символ и умножение на 1024(Количество килобайт в мБ)
            return float(size_str[:-1]) / 1024
        #в случае ошибки возращать значение -1
        except ValueError:
            return -1
    #в случае ошибки возращать значение -1
    else:
        return -1
#Конвертация значений в столбце Size с помощью самописной функции и apply
df['Size'] = df['Size'].apply(convert_size)

# Чему равен максимальный размер ('Size') приложений из категории ('Category') 'TOOLS'?
print('\n')
#Фильтрация и вывод максимального элемента в стобце
print(df[df['Category'] == 'TOOLS']['Size'].max())

# Бонусные задания
# Замени тип данных на целочисленный (int) для количества установок ('Installs').
# В записи количества установок ('Installs') знак "+" необходимо игнорировать.
# Т.е. если в датасете количество установок равно 1,000,000+, то необходимо изменить значение на 1000000

#конвертация с помощью apply и replace
print('\n')
df['Installs']=df['Installs'].apply(lambda x: int(x.replace(',','').replace('+', '')))
print(df['Installs'].dtypes)

# Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом,
# посчитай среднее количество установок ('Installs') в каждой группе. Результат округли до десятых.
# В полученной таблице найди ячейку с самым большим значением. 
# К какой возрастной группе и типу приложений относятся данные из этой ячейки?

#Группирует и возращает среднее
grouped = df.groupby(['Category', 'Content Rating'])['Installs'].mean().round(1)
grouped_df = grouped.reset_index()

#Возращает максимальное категорию и возрастную группу максимальногоо значения
max_idx = grouped.idxmax()
max_value = grouped.max()

print(max_value)
print(f"Категория '{max_idx[0]}' возрастная группе '{max_idx[1]}'")


# У какого приложения не указан тип ('Type')? Какой тип там необходимо записать в зависимости от цены?

#Устанавливает тип в зависимости от цены
mask = df['Type'].isna()
df.loc[mask, 'Type'] = df.loc[mask, 'Price'].apply(lambda x: 'Free' if x == 0 else 'Paid')
print(df)

# Выведи информацию о всем DataFrame, чтобы убедиться, что очистка прошла успешно
print('\n')
print(df.info())