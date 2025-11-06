#Filtering and sorting data
import pandas as pd
df_titanic=pd.read_csv("titanic.csv")
young_first_class=df_titanic[(df_titanic['Age']<30) & (df_titanic['Pclass']==1)]
sorted_young_first_class=young_first_class.sort_values(by='Age', ascending=True)
print(sorted_young_first_class.head(5))