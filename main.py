import pandas as pd
import matplotlib.pyplot as matplot


series = pd.Series(['Coast Redwood', 'Yellow Meranti',
                    'Mountain Ash', 'Coast Douglas Fir', 'Sitka Spruce'])
series.index = (['a', 'b', 'c', 'd', 'e'])

series2 = pd.Series({'a': 380.3, 'b': 331, 'c': 329.7, 'd': 327, 'z': 317})

# df = pd.DataFrame({'name': series, 'height': series2})

# df = pd.DataFrame(index=['a', 'b', 'c', 'd', 'e'],
#                   data={'name': ['Coast Redwood', 'Yellow Meranti', 'Mountain Ash', 'Coast Douglas Fir', 'Sitka Spruce'],
#                         'height': [380.3, 331, 329.7, 327, 317]})

df = pd.read_csv('./titanic.csv')

pd.set_option('display.max_rows', None)

df.drop(['Embarked', 'Cabin', 'SibSp', 'Parch',
         'Ticket'], inplace=True, axis='columns')
df.dropna(inplace=True)
df.reset_index(inplace=True)
df.drop(['index'], inplace=True, axis='columns')

# first = df[df['Pclass'] == 1].reset_index()

# print(df.groupby(['Pclass', 'Sex']).corr())


# print(df.describe())

# print(df.corr())

# df.hist(column='Age', by='Pclass')


# df.plot.scatter(x='Age', y='Fare')

weather = pd.read_csv('./weather.csv')
weather.dropna(inplace=True)
weather.reset_index(inplace=True)
weather.drop(['index'], inplace=True, axis='columns')

weather.iloc[0:50].plot.line(x='datetime', y='station_london')

# print(weather)


matplot.show()
