# Data Analysis in Python

## Data Analysis

Data analysis is the practice of taking raw data and tranforming and modeling the data to extract meaningful information.  It is the process of interpreting data in a way that allows us to understand the underlying trends and causes that determine the data, and/or  allowing us to determine future decision-making.

Data analysis is something we do automatically in our everyday lives. We use it to determine our optimal routes to places, based on how long each route took us in the past.  We use it to determine what foods we should eat in what amounts, based on how these meals made us feel in the past.  We use it to determine what movies we should watch, based on how much we liked similar and dissimilar movies in the past and which actors and directors we enjoyed.

Our brains can process tremendous amounts of information in a variety of ways, and data analysis aims to recreate the system manually.

### Stages of Data Analysis

The process of data analysis consists of a few stages:

#### Data Collection

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR365QYtsNjKL9LcL10XHjclGH32Q_rAtaFdw&usqp=CAU)

Collecting the data is the process of aggregating data points into a single set.

#### Data Cleaning

![](https://media.geeksforgeeks.org/wp-content/uploads/datacleaning.jpg)

Cleaning data is the process of detecting and correcting incomplete, corrupt, or inaccurate data points in our sets, and ensuring that data types are consistent and correct throughout our records.

#### Data Transformation

![](https://cdn.sanity.io/images/nosafynr/watershed-production/15a19d757b82ee30725db4f29303c05e44ea9650-1200x675.jpg?w=800&h=450&fit=crop)

Data must often be transformed from one format to another, so that we can process it with the tools we have.

#### Data Modelling

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTInB9sJuZFYOa3ROgljAw5uFZB-GIO1QbAQ&usqp=CAU)

Data modelling is the process of transforming our data into a form from which trends can be identified.  This involves grouping and organizing the data so that certain relationships can be illustrated.  This is often a visual format.

### Types of Data Analysis

There are different types of data analysis

#### Descriptive Analysis

Descriptive analysis aims to describe what happened. Descriptive analysis is the simplest form of data analysis, and is the basis of more advanced forms of analysis. It's a summary of the data we are analyzing. In business, this can take the form of a revenue report.

#### Diagnostic Analysis
Diagnostic analysis aims to describe why something happened. We take what we see in descriptive analysis, and drill down into specific aspects of the data to try to determine what causes the trends we see. A company might use diagnostic analysis to figure out what factors affect their delivery speeds, or what advertising campaigns drive sales.

#### Predictive Analysis

Predictive analysis aims to describe what is going to happen. This takes the data we gleaned from descriptive analysis, and uses it to make logical guesses about what will happen. This can involve simulations of the environments our data comes from and comparisons to similar times in history.  This type of data analysis is complex and approximate.

#### Prescriptive Analysis

Presciptive analysis aims to describe what we should do to achieve a certain goal based on what we think is going to happen and how our actions will affect that. This is an extension of predictive analysis, and involves complex mathematics and computer science.  Prescriptive analysis is the goal of AI, and is highly sought after.

## Data Analysis with Pandas

Pandas is a popular, powerful, and flexible data science library. It allows us clean, transform, and model data from a variety of sources. Pandas is basically a python version of Excel that allows us to do complex data manipulation easily, and works well with data visualization packages. We need to install pandas with

	pip install pandas
	
and import it into our file with

	import pandas as pd
	
Remember that the `as pd` is just a renaming convenience for us.

Check out the [pandas cheatsheet](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf) and the [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)

### Series

Series are the fundamental building block of pandas.  They are columns of data, and each series has a set of values and an index. They can be created in a variety of ways.  The simplest:

```
series = pd.Series(['Coast Redwood', 'Yellow Meranti', 'Mountain Ash', 'Coast Douglas Fir', 'Sitka Spruce'])
```

If we don't define an index, pandas will default to numerical values starting from 0.  We can define another index if we want, using

	series.index=(['a', 'b', 'c', 'd', 'e'])
	
We can combine those two steps into one by defining the series using a dictionary, like so

```
series = pd.Series({'a':'Coast Redwood', 'b':'Yellow Meranti', 'c':'Mountain Ash', 'd':'Coast Douglas Fir', 'e':'Sitka Spruce'})

series2 = pd.Series({'a': 380.3, 'b': 331, 'c': 329.7, 'd': 327, 'e': 317})
```

### Dataframes

Dataframes in pandas are the equivalent of tables in databases or spreadsheets.  They are made up of series, and can constructed in several different ways.  We can defined them all explicitly:

```
df = pd.DataFrame(index=['a', 'b', 'c', 'd', 'e'], 
					data={'name': ['Coast Redwood', 'Yellow Meranti', 'Mountain Ash', 'Coast Douglas Fir', 'Sitka Spruce'], 
					'height': [380.3, 331, 329.7, 327, 317]})
```

We could also create a dataframe using series that we've created:

	df = pd.DataFrame({'name': series, 'height': series2})

But most often, we'll create dataframes from data files that we already have.  These files are usually of the type csv, JSON, SQL, xlxs, or others.

	df = pd.read_csv('./weather.csv')

This creates a dataframe from the data in the weather.csv file.  If we want to take a look at our data, all we need to do is `print(df)`.  This will show us the first and last 5 rows of data.  This can be useful if we want to confirm that our df works and is created correctly.  If we want to view the full dataframe, we can add

	pd.set_option('display.max_rows', None)

somewhere in our file, then print it.

### Cleaning Data

As we mentioned above,  cleaning our data is an important part of data analysis, and pandas can do this for us. The most common type of dirty data is missing values, which can skew our data.  We can look for these null values using

	print(df.isnull().sum())
	
which will show us how many null values exist in each of our columns.  We can delete these records with null values using

	df.dropna(inplace=True)
	
Setting inplace to True saves the result to the original variable, df.

We can also delete entire columns using commands like this:

	df.drop(['Embarked'], inplace=True, axis='columns')


### Transforming and Modelling Data

Pandas gives us lots of methods to transform and model our data. We can filter our records to meet certain conditions. Running

	df[df['Sex'] == 'male']

shows us the records of the male passengers. If we want to create a new dataframe eith just the records of the male passengers with fresh indexes, we could run

	first = df[df['Pclass'] == 1].reset_index()

We can also order records by largest or smallest.  If we wanted to find the records of the 100 passengers with the highest fares, we could run

	print(df.nlargest(100, 'Fare'))

Grouping is one of the most powerful standard data analysis tools we have.  We can see how mnay recorded belong to each group using

	print(df.groupby(['Pclass']).count())

To make the result more readable, we can run

	print(df.groupby(['Pclass'])['PassengerId'].count())

instead.  This just shows the PassengerId column, instead of each column.

We can also use 

	print(df.groupby(['Pclass']).mean())

to glean other data.

We can group by more than 1 column at a time, and examine pertitent columns..  Let's take a look at this:

	print(df.groupby(['Pclass', 'Sex'])['Survived'].mean())

Other important methods are `.describe` and `.corr`

#### Data Visualization

We can also use pandas to create graphs, which can help us to view trends.  To be able to view these graphs, we need to install a library called matplotlib.  We install the package by running

	pip install matplotlib
	
and import matplotlib.pyplot it into our files with something like

	import matplotlib.pyplot as matplot

One of the most useful graphs we can create is a histogram. We can run `df.hist()` to create one, though it can be confusing to look at without some specification.  We can use the `column` property to choose whats columns to display, and the `by` property to create seperate histograms for different column groups.

	df.hist(column='Age', by='Pclass')
	
This will show us 3 histograms showing passengers by age, one for each of the seperate classes. To see the plots we create, we run

	matplot.show()

To see more customization option for our histograms, check out [the histogram docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html).

Another useful plot we can use is a scatter plot.  We can create a scatter plot by using

	df.plot.scatter(x='Pclass', y='Fare')

For the docs on pandas scatter plots, [read this](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html).