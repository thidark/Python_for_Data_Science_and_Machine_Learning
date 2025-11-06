data={
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva','Frank','Grace' ,'Helen'],
    'Maths': [85, 78, 92, 70, 88, 95, 80, 76],
    'English': [90, 82, 85, 88, 91, 87, 84, 80],
    'Science': [88, 79, 94, 72, 86, 93, 81, 77],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F']  
}

#Numerical Data visualization using Matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.DataFrame(data)

#plot histogram for Maths scores
plt.figure(figsize=(10,6))
plt.hist(df['Maths'], bins=5, color='blue', alpha=0.7)
plt.title('Distribution of Maths Scores')
plt.xlabel('Scores')
plt.ylabel('Number of Students')
plt.grid(axis='y', alpha=0.75)
plt.show()
#plot a scatter plot for Maths vs English scores
plt.figure(figsize=(10,6))
plt.scatter(df['Maths'], df['English'], color='green', alpha=0.7)
plt.title('Maths vs English Scores')
plt.xlabel('Maths Scores')
plt.ylabel('English Scores')
plt.grid()
plt.show()

#plot a bar chart showing the number of students by Gender
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(8,5))   
plt.bar(gender_counts.index, gender_counts.values, color=['pink', 'lightblue'], alpha=0.7)
plt.title('Number of Students by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Students')        
plt.show()

#plot a box plot for Science scores by Gender
plt.figure(figsize=(8,5))
df.boxplot(column='Science', by='Gender')
plt.title('Science Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Science Scores')    
plt.show()

#add title and axis labels to the plots
#(Already included in the above plots)
#change colors and styles of the plots
#(Already included in the above plots)
#adjust figure size and number of bins in histogram
#(Already included in the above plots)