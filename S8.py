import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
import seaborn as sns

from scipy.stats import kurtosis, skew

plt.style.use('ggplot')

matplotlib.rcParams['figure.figsize'] = (15,10)
pd.options.mode.chained_assignment = None



dfm = pd.read_csv("clienti_leasing.csv")
print(dfm.head().to_string())
print(dfm.describe())
print(dfm.info())
# Return the number of missing values in each column.
print(dfm.isnull().sum())
#view the index
print(dfm.index)
#view the columns
print(dfm.columns)
#drop category columns for easiness


'''A histogram is used to summarize discrete or continuous data. In other words, it provides a visual interpretation 
of numerical data by showing the number of data points that fall within a specified range of values (called “bins”).
 It is similar to a vertical bar graph.'''
dfm.hist()
plt.show()
'''
Kurtosis is a statistical measure that defines how heavily the tails of a distribution differ from the tails of a normal distribution. 
In other words, kurtosis identifies whether the tails of a given distribution contain extreme values.
'''
'''Kurtosis is one of the two measures that quantify shape of a distribution. 
kutosis determine the volume of the outlier'''
df_int = dfm.select_dtypes(include=['int64', 'float64'])

print(df_int.kurtosis())
'''However, the two concepts must not be confused with each other. 
Skewness essentially measures the symmetry of the distribution, 
while kurtosis determines the heaviness of the distribution tails'''


'''Observation:
· If the absolute value of skew<0.5 then very symmetric.
· If the absolute value of skew is in between 0.5 and 1 then slightly skewed
· If the absolute value of skew is greater than 1 then very skewed.'''


'''Correlation coefficients are used to measure the strength of the relationship between two variables.
 Pearson correlation is the one most commonly used in statistics. This measures the strength and direction of a linear relationship between two variables.'''
dfm_corr = df_int.corr()
print(dfm_corr.to_string())

y = dfm['REQUESTED_AMOUNT']
plt.hist(y, bins=60)
print("medie : ", np.mean(y))
print("varianta  : ", np.var(y))
print("skewness : ",skew(y))
print("kurtosis : ",kurtosis(y))
plt.show()


dfm_corrs = df_int.corr(method='spearman')
dfm_corrk = df_int.corr(method='kendall')

'A scatter plot (aka scatter chart, scatter graph) uses dots to represent values for two different numeric variables.' \
' The position of each dot on the horizontal and vertical axis indicates values for an individual data point. ' \
'Scatter plots are used to observe relationships between variables.'
'You will often see the variable on the horizontal axis denoted an independent variable, and the variable on the vertical axis the dependent variable. ' \
'Relationships between variables can be described in many ways: positive or negative, strong or weak, linear or nonlinear.'

dfm.plot(x="FIDELITY", y="DEPOSIT_AMOUNT", kind="scatter")
plt.show()

'''Pair plot is used to understand the best set of features to explain a relationship 
between two variables or to form the most separated clusters'''

'''distributia si relatia dintre coloana varsta si valoarea creditelor pentru cei care au cerut mai mult de 10000'''

'''vad distributia creditelor in functie de varsta'''
sns.pairplot(dfm[dfm['REQUESTED_AMOUNT'] > 100000],
             vars = ['AGE','VAL_CREDITS_RON'],
             hue = 'PRESCORING', diag_kind = 'hist')
plt.show()
sns.pairplot(dfm[dfm['REQUESTED_AMOUNT'] > 100000],
             vars = ['AGE', 'VAL_CREDITS_RON', 'REQUESTED_AMOUNT', 'VENIT_PER_YEAR_RON'],
             hue = 'PRESCORING', diag_kind = 'hist')
plt.show()
'''As noted above, a heatmap can be a good alternative to the scatter plot when there are a lot of data points that need to be plotted
 and their density causes overplotting issues.
However, the heatmap can also be used in a similar fashion to show relationships between variables when one or both variables are not continuous and numeric. If we try to depict discrete values with a scatter plot, all of the points of a single level will be in a straight line. 
Heatmaps can overcome this overplotting through their binning of values into boxes of counts.'''
dfm_numeric = dfm.select_dtypes(include=[np.number])
sns.heatmap(dfm_numeric.corr(),annot=True)
plt.show()

'''PIVOT TABLE si reprezentari grafice: 

Înlocuiți valorile anormale ale profesiei cu valoarea ALTA PROFESIE. Pe baza DataFrame-ul obținut realizați următoarele:
- în funcție de profesie determinați valorile totale pentru coloanele venit anual, valoarea creditelor, suma din depozite și suma solicitată in functie de sexul clientilor. Afișați datele sub forma de box, bar, pie. 
- grupați în funcție de coloana DATA valorile medii pentru coloanele venit anual, valoarea creditelor, suma din depozite și suma solicitată. Ordonați valorile în ordinea crescătoare a datei și reprezentați evoluția valorilor.
- reprezentați sub formă de heatmap valorile medii ale sume solicitate în funcție de profesie și stare civilă. Tratați valorile null
'''

print(dfm['JOB'].value_counts())


listOfJobs  = ['muncitor necalificat', 'profesor' , 'agricultor', 'asistent medical', 'barman', 'economist', 'inginer',
             'medic', 'pensionar']
dfm['JOB']=dfm.loc[dfm['JOB'].str.lower().isin(listOfJobs), ['JOB']]
dfm['JOB'] = dfm['JOB'].fillna('ALTA PROFESIE')

'''https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html'''

df=pd.pivot_table(dfm, values=['REQUESTED_AMOUNT', 'DEPOSIT_AMOUNT', 'VAL_CREDITS_RON','VENIT_PER_YEAR_RON'], index=['JOB'], columns = ['SEX'],
                    aggfunc={'REQUESTED_AMOUNT': 'sum','DEPOSIT_AMOUNT': 'sum', 'VAL_CREDITS_RON': 'sum', 'VENIT_PER_YEAR_RON': 'sum'}).reset_index()

'''pandas. reset_index in pandas is used to reset index of the dataframe object to default indexing (0 to number of rows minus 1) or to reset multi level index.
 By doing so, the original index gets converted to a column.'''
print(df.head())
df.plot(kind='box', figsize=[12,10])
plt.xticks(rotation='vertical')
plt.show()

'''Bar charts'''

df.plot.bar(x='JOB', figsize=[15,12])
plt.show()

'''Stacked bar'''
df.plot.bar(x='JOB',y=['DEPOSIT_AMOUNT','VENIT_PER_YEAR_RON'],stacked=True, figsize=[20,30])
plt.show()

'''Pie chart - este necesara transformarea coloanei PROFESIA in index'''
df.set_index('JOB', inplace=True)
df[['DEPOSIT_AMOUNT','VENIT_PER_YEAR_RON']].plot.pie(subplots=True, figsize=(30, 25))
plt.show()



#pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False, sort=True)
df3=pd.pivot_table(dfm, values=['REQUESTED_AMOUNT'], index=['JOB', 'MARITAL_STATUS'], aggfunc={'REQUESTED_AMOUNT': np.mean}).reset_index()

#DataFrame.pivot(index=None, columns=None, values=None)
df3 = df3.pivot(index='JOB', columns='MARITAL_STATUS', values='REQUESTED_AMOUNT').fillna(0)

sns.heatmap(df3,annot=True,fmt="f")
plt.show()
