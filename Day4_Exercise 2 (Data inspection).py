import pandas as pd
data_frame=pd.read_csv("titanic.csv")
print("Data Frame: \n",data_frame)
print("Columns in dataset: \n",data_frame.columns)
print("Shape : \n",data_frame.shape)
print("Data types of each column: \n",data_frame.dtypes)
print("First 5 rows: \n",data_frame.head())
print("Last 5 rows:\n",data_frame.tail())
print("Summary Statistics:\n",data_frame.describe())