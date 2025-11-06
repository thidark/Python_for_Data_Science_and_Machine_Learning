import pandas as pd
df_titanic=pd.read_csv("titanic.csv")

#calculate average age and total fare by passenger class, grouping the results by the Pclass (Passenger class) column.
agg_stats=df_titanic.groupby('Pclass').agg(
    Avg_Age=('Age','mean'),
    Total_Fare=('Fare','sum')
)
print(agg_stats)

#Store the result in a Dataframe named class_summary. Rename the aggregated columns to 'Average_Age' and 'Total_Fare' respectively.
class_summary=agg_stats
print(class_summary)