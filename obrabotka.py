#импорты
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ddplot')
plt.rcParams ['figure.figsize'] = (10,5)





# считываем из csv файла подготовленный датасет (Лена) для обучения

data_train = pd.read_csv('data_train.csv')
films [['name', 'rating', 'genre', 'run_time', 'tagline']] [:20]
#films ['raiting'].values_counts() выбор по рейтингу, написать,чтобы выводился фильмец
#films_counts = films['raiting'].value_counts()
#films_counts[:15]
#построение графика самых ужасных фильмов по типу аватар, ну или самых лучших
film_counts[:15].plot(kind = 'bar')
X_train = data_train[['']].values
y_train = data_train[''].values

#загружаем модель МО
from sklearn.linear_model import LogisticRegression
model = LogisticRegresiion(max_iter=100_000).fit(X_train,y_train)

#сохранение модели
