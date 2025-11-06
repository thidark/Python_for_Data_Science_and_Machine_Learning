import pandas as pd
df_titanic=pd.read_csv("titanic.csv")
print("--------------------Identify missing data---------------------")
#1. Check for missing values in each column
missing_values=df_titanic.isnull().sum()
print("Missing values in each column:\n", missing_values)
#impute: for the fare columns (if it has missing values), replave nay null values with the mean of the Fare column
print("--------------------Handling Missing Values---------------------")
#1. Calculate the mean of 'Fare' column
mean_fare=df_titanic['Fare'].mean()
#2. Fill nulls in 'Fare' column with the mean   
df_titanic['Fare'].fillna(mean_fare, inplace=True)
print("Missing values in Fare after filling:", df_titanic['Fare'].isnull().sum())

#Verify: After imputation, re-calculate and print the number of missing values speciccally for the Fare columns to confirm the imputation was successful.
print("--------------------Handling Missing Values---------------------")
print("Missing values in Fare after filling:", df_titanic['Fare'].isnull().sum())

