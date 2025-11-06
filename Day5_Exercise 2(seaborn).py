#choose a dataset from seaborn's built=in datasets
import seaborn as sns
import matplotlib.pyplot as plt
#load the dataset
df = sns.load_dataset('tips')
#choose one numerical column for visualization
#plot histogram for total_bill
plt.figure(figsize=(10,6))
plt.hist(df['total_bill'], bins=10, color='blue', alpha=0.7)
plt.title('Distribution of Total Bill') 
plt.xlabel('Total Bill')
plt.ylabel('Number of Bills')
plt.grid(axis='y', alpha=0.75)
plt.show()

#plot a scatter plot with two numerical columns: total_bill vs tip
plt.figure(figsize=(10,6))
plt.scatter(df['total_bill'], df['tip'], color='green', alpha=0.7)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.grid()
plt.show()

#choose one categorical column
#plot a countplot
plt.figure(figsize=(8,5))
sns.countplot(x='day', data=df, palette='pastel')
plt.title('Number of Bills by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Bills')
plt.show()

#plot a boxplot to compare a numerial column across categories of the categorical column
plt.figure(figsize=(8,5))
sns.boxplot(x='day', y='total_bill', data=df, palette='Set2')
plt.title('Total Bill by Day')  
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()