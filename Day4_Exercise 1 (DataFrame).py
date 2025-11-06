#Dataframe Creation
import pandas as pd
data={
    'ProductId':[102,103,104],
    'Name':['Laptop','Tablet','Smartphone'],
    'Price':[800,400,600]
}
df_products=pd.DataFrame(data)
print(df_products)