import pandas as pd
data={
    'EmployeeId':[102,103,104],
    'Name':['Alice','Bob','Charlie'],
    'Department':['HR','IT','Finance']
}

df_employees=pd.DataFrame(data)
print(df_employees)

print("-------------------creatting a series-------------------")
# Creating a Pandas Series
series_data = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(series_data)

series1=pd.Series([100,200,300])
print(series1)

print("-------------------DataFrame Operations-------------------")
# DataFrame Operations
print("DataFrame Shape:", df_employees.shape)
print("DataFrame Columns:", df_employees.columns)
print("First Two Rows:\n", df_employees.head(1)) 
print("Last Two Rows:\n", df_employees.tail(1))
#rint("random ",df_employees.random())


print("-------------------Indexing and Slicing-------------------")
# Indexing and Slicing
print("Employee Names:\n", df_employees['Name'])
print("First Two Employees:\n", df_employees.iloc[0:2])

print("---------------------Loading Dataset---------------------")
df_titanic=pd.read_csv("titanic.csv")
df_titanic.head()


print("---------------------REading Data---------------------")

#pd.read_csv("titanic.csv")
#pd.read_excel("titanic.xlsx")
#pd.read_json("titanic.json")
#pd.read_html("titanic.html")
#pd.read_sql("titanic.sql")


print("---------------------Attributes ---------------------")
print(df_titanic.shape)
print(df_titanic.index)    
print(df_titanic.columns)
print(df_titanic.dtypes)

print("---------------------Common Methods---------------------")
print(df_titanic.head())
print(df_titanic.tail())
print(df_titanic.info())
print(df_titanic.describe())
print(df_titanic.sample(5))

print("---------------------Selecting Columns---------------------")
ages=df_titanic['Age']
print(ages.head())

key_cols=df_titanic[['Name','Sex','Age']]
print(key_cols.head())

print("---------------------Indexing by label: loc---------------------")

subset_loc=df_titanic.loc[0:5,['Name','Age']]
print(subset_loc)

print("---------------------Indexing by position: iloc---------------------")
subset_iloc=df_titanic.iloc[0:5, [1,5]]
print(subset_iloc)

print("---------------------Filtering Data (Single Condition)---------------------")

females=df_titanic[df_titanic['Sex']=='female']
print(f"Total females: {females.head()}")
print(f"Total females: {females.shape[0]}")

print("---------------------Filtering Data (Multiple Conditions)---------------------")

survived_first=df_titanic[(df_titanic['Survived']==1) & (df_titanic['Pclass']==1)]
print(f"Survived in First Class: {survived_first.shape[0]}")


print("---------------------Sorting Data---------------------")
most_expensive=df_titanic.sort_values(by='Fare', ascending=False)
print(most_expensive.head(3))


print("---------------------Filtering and sorting data---------------------")
#filter the data create a new data frame with passengers younger than 30 years and in first class
young_first_class=df_titanic[(df_titanic['Age']<30) & (df_titanic['Pclass']==1)]
#sort the new data frame by age in ascending order and display the first 5 rows
sorted_young_first_class=young_first_class.sort_values(by='Age', ascending=True)
print(sorted_young_first_class.head(5))


print("---------------------Identifying MIssing Data (Nulls)---------------------")

missing_counts=df_titanic.isnull().sum()
print("Missing values in each column:\n", missing_counts)

#Removing missing data with dropna()
df_clean_embarked=df_titanic.dropna(subset=['Embarked'])
print("Rows after removing missing Embarked values:", df_clean_embarked.shape[0])

#Drop all rows with any missing values
df_fully_dropna=df_titanic.dropna(how='any')
print("Rows after dropping all rows with any missing values:", df_fully_dropna.shape[0])


print("---------------------Filling missing data with fillna()---------------------")

median_age=df_titanic['Age'].median()
df_titanic['Age'].fillna(median_age, inplace=True)
print("Missing values in Age after filling:", df_titanic['Age'].isnull().sum())


print("--------------------Imputing Missing Categorical Data with fillna()---------------------")

#1. find the mode (most frequent value) of the 'Embarked' column
#mode_embarked=df_titanic['Embarked'].mode()[0]

#2. fill nulls in 'Embarked' column with the mode
#df_titanic['Embarked'].fillna(mode_embarked, inplace=True)

#3. fill 'Cabin' column nulls with 'Unknown'
#df_titanic['Cabin'].fillna('Unknown', inplace=True)
#print("Missing values in Embarked after filling:", df_titanic['Embarked'].isnull().sum())

print("--------------------Handling Duplicates---------------------")
# 1. Check duplicates (returns a count of duplicate rows)
print("Duplicate Rows:", df_titanic.duplicated().sum())
# 2. Remove duplicates
df_no_dupes=df_titanic.drop_duplicates()
print("Rows after removing duplicates:", df_no_dupes.shape[0])




print("--------------------Grouping and Aggregation with grpupby()---------------------")
survival_rate_by_sex=df_titanic.groupby('Sex')['Survived'].mean()
print("Survival rate by sex:\n", survival_rate_by_sex)

print("--------------------Multiple Aggregations with .agg()---------------------")
summary=df_titanic.groupby('Pclass').agg(
    Avg_Age=('Age','mean'),
    Max_Fare=('Fare','max'),
    Count=('PassengerId','count')
    )
print(summary)


print("--------------------Merging DataFrames with pd.merge()---------------------")


df_additional=pd.DataFrame({
    'PassengerId':[1,2,3,892,893],
    'Cabin_Assignment':['X','Y','Z','W','V']
})

#inner join
inner_merged_df2 = pd.merge(df_titanic, df_additional, on='PassengerId', how='inner')
print("Inner Merged DataFrame with additional:\n", inner_merged_df2.head())

#left join
left_merged_df2 = pd.merge(df_titanic, df_additional, on='PassengerId', how='left')
print("Left Merged DataFrame with additional:\n", left_merged_df2.head())
#right join
right_merged_df2 = pd.merge(df_titanic, df_additional, on='PassengerId', how='right')
print("Right Merged DataFrame with additional:\n", right_merged_df2.head())
#outer join
outer_merged_df2 = pd.merge(df_titanic, df_additional, on='PassengerId', how='outer')
print("Outer Merged DataFrame with additional:\n", outer_merged_df2.head())


print("--------------------Exporting Data---------------------")
df_titanic.to_csv("titanic_cleaned.csv", index=False)
print("Data exported to titanic_cleaned.csv")
#Export to Excel
#df_titanic.to_excel("titanic_cleaned.xlsx",sheet_name='Clean Data', index=False)
#print("Data exported to titanic_cleaned.xlsx")


print("--------------------Univariate Analysis (Single Variable--------------------")

#plot the distribution of ages using a histogram
import matplotlib.pyplot as plt

df_titanic['Age'].plot(kind='hist', title='Age Distribution')

df_titanic['Pclass'].value_counts().plot(kind='bar', title='Passenger Class Distribution') 

df_titanic.plot(kind='scatter', x='Age', y='Fare', title='Age vs Fare') 

plt.show()  


print("--------------------Bivariate Analysis (Two Variables)--------------------")
import seaborn as sns
sns.boxplot(x='Pclass', y='Fare', data=df_titanic)
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df_titanic)
plt.show()



print("--------------------Correlation Analysis-------------------")
correlation_matrix=df_titanic[['Age','Fare','Survived']].corr()
print("Correlation Matrix:\n", correlation_matrix)


print("--------------------Visualizing Survival by Gender--------------------")
survival_rate_by_sex=pd.crosstab(df_titanic['Sex'], df_titanic['Survived'])
print(survival_rate_by_sex)



print("-------------------Grouping and Aggregations------------------")
#calculate average age and total fare by passenger class, grouping the results by the Pclass (Passenger class) column.
agg_stats=df_titanic.groupby('Pclass').agg(
    Avg_Age=('Age','mean'),
    Total_Fare=('Fare','sum')
)
print(agg_stats)

#Store the result in a Dataframe named class_summary. Rename the aggregated columns to 'Average_Age' and 'Total_Fare' respectively.
class_summary=agg_stats
print(class_summary)






























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































