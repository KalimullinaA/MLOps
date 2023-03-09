#импорты
import pandas as pd
import matplotlib.pyplot as plt


#загрузка данных

DF_train = pd.read_csv('data_train.csv', delimiter =',', index_col = 0)
X_train = DF_train[['year', 'genre', 'run_time', 'casts']].values
y_train = DF_train['rating'].values

DF_test = pd.read_csv('data_test.csv', delimiter =',', index_col = 0)




#удаление дубликатов, объединение DF

DF_train.drop_duplicates(inplace = True)

DF_total = pd.concat([DF_train, DF_test])
# DF_total = DF_total.join(DF_films)


# Разделение столбцов на категориальные и числовые

categ_columns = []
num_columns = []

for column_name in DF_total.columns:
    if (DF_total[column_name].dtypes == object):
        categ_columns +=[column_name]
    else:
        num_columns +=[column_name]

print('categorical columns:\t', categ_columns, '\n len = ', len(categ_columns))
print('numerical columns:\t', num_columns, '\n len = ', len(num_columns))

#загрузка модели МО


from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=100_000).fit(X_train,y_train)
import pickle
pickle.dump(model,open('model.pkl', 'wb'))




