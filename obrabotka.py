#импорты
import pandas as pd
import matplotlib.pyplot as plt

#загрузка данных

DF_train = pd.read_csv('', delimiter =',', index_col = 0)
DF_test = pd.read.csv('',delimiter =',', index_col = 0)
Target = pd.read_csv('',delimiter =',', index_col = 0)

#удаление дубликатов, объединение DF

DF_train.drop_duplicates(inplace = True)

DF_total = pd.concat([DF_train, DF_test])
DF_films = pd.concat([Target, Submission])
DF_total = DF_total.join(DF_films)

#Анализ данных

DF_total.info() #просмотр данных

# Разделение столбцов на категориальные и числовые

сateg_columns = []
num_columns = []

for column_name in DF_total.columns:
    if (DF_total[columns_name].dtypes == object):
        categ_columns +=[column_name]
    else:
        num_columns +=[column_name]

print ('categorical columns:\t',categ_columns, '\n len = ', len(categ_columns))
print ('numerical columns:\t',num_columns, '\n len = ', len(num_columns))





