import seaborn as sns    
import matplotlib.pyplot as plt
penguins=sns.load_dataset("penguins")


print("..................Flipper Length Distribution..................")

sns.histplot(data=penguins,x="flipper_length_mm")
plt.title("Distribution of Penguin Flipper Lengths")
plt.show()

#Dataset Names
dataset_names=sns.get_dataset_names()
print("Dataset Names:\n",dataset_names)

print(".......Total bill summary by day and week........")
tips=sns.load_dataset("tips")
sns.boxplot(data=tips,x="day",y="total_bill")
plt.title("Total Bill by Day of Week")
plt.show()




print("..............Iris Pairplot with Hue..................")
iris=sns.load_dataset("iris")
sns.pairplot(iris,hue="species")
plt.show()


print("........................Seaborn Customization......................")

sns.set_theme(style="whitegrid")
sns.boxplot(data=penguins,x="species",y="body_mass_g",palette="flare")
plt.show()


tips=sns.load_dataset("tips")
sns.set_theme(style="darkgrid", context="talk")
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    palette="flare"
)

plt.title("Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
sns.despine()
plt.show()