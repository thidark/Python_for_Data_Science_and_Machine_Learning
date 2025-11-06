import numpy as np
#Rows=Students(3), Columns=Subjects(4)

scores=np.array([[80,95,70,90],
                 [65,88,92,75],
                 [90,70,85,82]])

#Calculate overall average score for all subjects
overall_average=np.mean(scores)
print("Overall Average Score:", overall_average)

#Find the minimum score achieved by each student
min_scores_per_student=np.min(scores, axis=1)       
print("Minimum Scores per Student:", min_scores_per_student)

#Use boolean indexing to find how many scores are above 90
print("Score above 90",scores>90)