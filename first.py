import pandas as pd
from sklearn.model_selection import train_test_split

dataframe = pd.read_csv(r"C:\Users\Admin\Documents\GitHub\MLOps\data\IMDB Top 250 Movies.csv")
print(dataframe)

train, test = train_test_split(dataframe, test_size=0.2)
# train, val = train_test_split(train, test_size=0.2)
# print(len(train), 'train examples')
# print(len(val), 'validation examples')
# print(len(test), 'test examples')

train[['name','year','rating','genre','run_time','casts']].to_csv('data_train.csv',index=False)
test[['name','year','genre','run_time','casts']].to_csv('data_test.csv',index=False)