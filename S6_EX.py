import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StoresPrep.csv")

# Display the first five rows of the dataset
print(df.head())

"""
This dataset contains information about different stores, including various features associated with each store.

Here's a breakdown of the columns:
Store_Number: A numerical identifier for each store.
AreaStore: The area of the store.
Property: Indicates whether the property is owned, rented, or a cooperation.
Type: Describes the type of store (e.g., Hyper, Extra, Express).
Old/New: Indicates whether the store is old or new.
Checkout Number: The number of checkout counters in the store.
Revenue: The revenue generated by the store.

"""

# Display basic information about the dataset
print(df.info())


# Display descriptive statistics
print(df.describe())
print(df.describe(include="all").to_string())


# Check for missing values
print(df.isna())
print(df.isna().sum())
print(df.isnull().sum())
print(df.notnull().sum())

# Display number of unique values in Property column
print(df['Property'].value_counts())
print(df['Property'].nunique())
print(df['Property'].unique())


# Display number of unique values in each column

print(df.columns)

for i in list(df.columns):
    print(f"Column {i} has a number of {df[i].nunique()} unique values.")

# Display unique values in each column
for i in df.columns:
    print(f"Unique values in column {i}: {df[i].unique()}")


'''
Selecting Rows
Using loc: Select the rows where Store_Number is 3.
Using iloc: Select the row at the third position (keep in mind Python is 0-indexed).
'''
print(df.loc[df['Store_Number'] == 3])
print(df.iloc[2,:])



'''
Selecting Columns
Using loc: Select the Revenue column for all rows.
Using iloc: Select the last column for all rows.
'''

print(df.loc[:,'Revenue'])
print(df.iloc[:,-1])

'''
Selecting Rows and Columns
Using loc: Select Store_Number and Revenue columns for stores 1 and 4.
Using iloc: Select the first and last columns for the first and fourth rows.
'''

print(df.loc[df["Store_Number"].isin([1,4]), ["Revenue","Store_Number"]])
print(df.iloc[[0,3], [0,-1]])

'''
Conditional Selection
Using loc: Select all rows where the Type is 'Hyper'.
Using iloc:  iloc does not directly support conditional selection based on column values.
'''

print(df.loc[df.Type=='Hyper',['Store_Number','Type']])


'''
Updating a Value
Using loc: Change the Type of store 2 to 'Super'.
'''
print(df.loc[df['Store_Number'] == 2, 'Type'])
df.loc[df['Store_Number'] == 2, 'Type'] = 'Super'
print(df.loc[df['Store_Number'] == 2, 'Type'])

'''
Slicing Rows
Using loc: Selected rows 1 through 3 (inclusive of both ends).
Using iloc: Selected the first three rows.
'''



'''Calculate the total Revenue across all stores.'''


'''Calculate the average AreaStore size.'''



'''Find the maximum Checkout Number across all stores. '''



'''Identify the store with the smallest AreaStore.'''


'''------------------Group BY ----------------------------'''

'''
The groupby operation in pandas is used for aggregating data, allowing you to group your data by one or more 
columns and then perform calculations or transformations on those groups.
This operation is similar to the SQL GROUP BY statement and is extremely useful for data analysis, 
allowing you to break down complex datasets into more manageable pieces or to perform calculations on subsets
of your data based on certain criteria.

How It Works
The groupby operation can be broken down into three steps:

Splitting: The data is divided into groups based on one or more keys. This is done on a specific axis of the DataFrame or Series, 
typically rows (axis=0).
Applying: A function is applied to each group independently. This function could be an aggregation (returning a single value per group), 
a transformation (returning a version of the data), or a filtration (returning a subset of the data).
Combining: The results of the function applications are combined into a new DataFrame or Series.


Syntax
The basic syntax of a groupby operation in pandas is:
df.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=NoDefault.no_default, observed=False, dropna=True)


by ->  can be a single column, a list of columns, or even mappings (like dictionaries or series) that define the grouping.
axis  -> specifies the axis to group on. By default, it's set to 0, which means the operation is performed on rows.
as_index ->is a boolean indicating whether to group by the index (default is True).
'''

'''Calculate the total revenue for each Type of store. '''



'''Find the average Checkout Number for each Old/New category.'''



'''----------------------'Aggregation'---------------------------'''
'''
The agg function in pandas is used for performing aggregation operations on DataFrame or Series objects.
It allows you to apply one or more operations across a specified axis of the DataFrame or Series, 
making it highly versatile for data summarization tasks. '''

'''Find the total, average, and maximum revenue for each Type of store.'''


'''Identify the store with the highest revenue for each Type.'''
'''-involves two steps: first, using groupby and idxmax to find the index of the row with
the highest revenue for each store type, 
and second, using loc to retrieve the complete information for these rows.'''

# First, find the index of the max revenue per Type
# Then, use loc to get the rows corresponding to these indices


'''For each Type of store, find the revenue of the store with the highest AreaStore, and its respective Store_Number.'''

# Group by 'Type' and then apply a custom function to each group


'''_______________Graphics_________________'''

# Plot the distribution of Revenue

'''
plt.hist() is a Matplotlib function that creates a histogram.
df['Revenue'] specifies the data to be used for the histogram, in this case, the Revenue column from the DataFrame df.
bins=20 sets the number of bins (or bars) in the histogram to 20. The range of Revenue values will be divided into 20 intervals.
color='blue' sets the color of the bars in the histogram to blue.
edgecolor='black' sets the color of the edge of the bars to black, enhancing visual distinction between them.
'''

plt.hist(df['Revenue'], bins=20, color='blue', edgecolor='black')
plt.title('Distribution of Revenue')  # Adds a title "Distribution of Revenue" to the histogram.
plt.xlabel('Revenue')  # Labels the x-axis as "Revenue"
plt.ylabel('Frequency')  # Labels the y-axis as "Frequency", indicating the number of occurrences within each bin
plt.show()  # Displays the histogram. This function must be called to actually render the plot.

# Pie chart to visualize the distribution of Property types

property_counts = df['Property'].value_counts()  # Counts the occurrences of each unique value in the Property column
# of the DataFrame df and assigns the result to property_count
# The value_counts() function returns a Series where the index contains the unique values
# and the values are the counts of those unique values in the dataset.

plt.pie(property_counts, labels=property_counts.index, autopct='%1.1f%%', startangle=90)
'''plt.pie() is a Matplotlib function that creates a pie chart.

The first argument, property_counts, is the data for the pie chart, representing the counts of each property type.

labels=property_counts.index uses the index of property_counts (which are the unique property types) as labels for the pie chart slices.

autopct='%1.1f%%' formats the percentage value of each slice to one decimal place. 
It automatically calculates the percentage of each slice and displays it on the chart.

startangle=90 rotates the start of the pie chart by 90 degrees. This means the first slice will start at the top of the chart.'''

plt.title("Distribution of Property Types")
plt.show()

'''Bar Plot of Average Revenue by Store Type'''

# Step 1: Group by 'Type' and calculate mean revenue
average_revenue_by_type = df.groupby('Type')['Revenue'].mean()

# Step 2: Plot directly from the DataFrame
average_revenue_by_type.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Average Revenue by Store Type')
plt.xlabel('Store Type')
plt.ylabel('Average Revenue')
plt.xticks(rotation=45)  # Rotate labels to improve readability
plt.show()
