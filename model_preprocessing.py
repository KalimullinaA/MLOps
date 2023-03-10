#импорты
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split


#загрузка данных

DF_train = pd.read_csv('data_train.csv', delimiter =',', index_col = 0)
X_train = DF_train[['year', 'genre', 'run_time', 'casts']].values
y_train = DF_train['rating'].values


DF_test = pd.read_csv('data_test.csv', delimiter =',', index_col = 0)





#удаление дубликатов, объединение DF

DF_train.drop_duplicates(inplace = True)

DF_total = pd.concat([DF_train, DF_test])
# DF_total = DF_total.join(DF_train)


# Разделение столбцов на категориальные и числовые

categ_columns = []
num_columns = []

for column_name in DF_total.columns:
    if(DF_total[column_name].dtypes == object):
        categ_columns +=[column_name]
    else:
        num_columns +=[column_name]

print('categorical columns:\t', categ_columns, '\n len = ', len(categ_columns))
print('numerical columns:\t', num_columns, '\n len = ', len(num_columns))


#Применим OneHotEncoder к категориальным признакам
qwer = pd.get_dummies(DF_total[categ_columns])
DF_total = DF_total.join(qwer)
print(DF_total)

#Применим также OneHotEncoder к колонке
qwe = pd.get_dummies(DF_total['rating'])
DF_total = DF_total.join(qwe)
#
# DF_total.drop(columns=['year', 'genre', 'run_time', 'casts'], inplace=True)
# print(DF_total)

#Разделение на тренировочную и тестовую выборку
train = DF_total.iloc[0:DF_train.shape[0],:]
test = DF_total.iloc[DF_train.shape[0]:,:]
print(DF_train.shape[0], train.shape[0], DF_test.shape[0], test.shape[0])

#Разбиваем тренировочные данные на тренировочную и валидационную
X, y = train.drop(columns = ['rating']).values,train['rating'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


#загрузка модели МО


# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression(max_iter=100_000).fit(X_train,y_train)
# import pickle
# pickle.dump(model,open('model.pkl', 'wb'))




