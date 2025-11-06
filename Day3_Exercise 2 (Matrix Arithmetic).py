#Define the grades matrix (Student in rows, Assignments in columns)
import numpy as np

grades_matrix = np.array([[90,80,75,95],
                          [85,90,88,92],
                          [70,75,78,80]])

#Define weights for each assignment
weights = np.array([0.2,0.3,0.4,0.5])  #


#Calculate the weighted Score for each student using matrix operations
weighted_scores = grades_matrix.dot(weights)
print("Weighted Scores for each student:", weighted_scores)


