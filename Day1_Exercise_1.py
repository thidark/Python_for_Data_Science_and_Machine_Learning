num_students=int(input("Enter the number of students: "))
names=[]
totals=[]
avgs=[]
grades=[]
for i in range(num_students):
    name=input("Enter student name: ")
    names.append(name)

    marks=[]
    for j in range(3):
        mark=int(input("Enter marks for subject (0-100) :"))
        marks.append(mark)
    total=sum(marks)
    avg=total/3
    format_avg=f"{avg:.2f}"
    totals.append(total)
    avgs.append(format_avg)

    if(avg>89):
        grades.append("A+")
    elif(avg>79):
        grades.append("B")
    elif(avg>69):
        grades.append("C")
    elif(avg>59):
        grades.append("D")
    else:
        grades.append("E")
print("Name\tTotal\tAverage\tGrade")
print("-----------------------------------")
for i in range(num_students):
    print(names[i]+"\t"+str(totals[i])+"\t"+str(avgs[i])+"\t"+str(grades[i]))