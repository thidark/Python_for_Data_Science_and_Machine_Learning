#Creating Dictionary
student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Science", "History"],
    "is_enrolled": True
}
print(student)
#Accessing Values
print(student["name"])  # John Doe
print(student.get("age"))  # 21
print(student["courses"])  # ['Math', 'Science', 'History']

#Modifying Values
student["age"] = 22
student["courses"].append("Art")
print(student)

#Adding New Key-Value Pairs 
student["graduation_year"] = 2023
print(student)  

#Removing Key-Value Pairs
del student["is_enrolled"]
print(student)

student.pop("graduation_year", None)
print(student)

student.popitem()  # removes the last inserted key-value pair
print(student)

#Iterating Through a Dictionary
for key in student:
    print(f"{key}: {student[key]}")
    
#creating nested data
employee=[
    {"id":1,"name":"Jane","dept":"HR"},
    {"id":2,"name":"Mark","dept":"IT"},
     {"id":3,"name":"Sue","dept":"HR"}
]
mark_dept=employee[1]["dept"]
print(f"Mark is in: {mark_dept}")

print("\nHR Staff:")

for person in employee:
    if person["dept"]=="HR":
        print(person["name"])

#List Complehension
square=[]
for x in range(1,6):
    square.append(x**2)
print(square)
#[1, 4, 9, 16, 25]

evens=[x for x in range(1,11)if x%2==0]
print(evens)
#[2, 4, 6, 8, 10]

#........................................
# enumerate() Function
#When iterating over an iterable (like a list), enumerate() returns both the index and the value at
#the same time.

data=["setup","process","result"]
for index,item in enumerate(data):
    print(f"Step {index+1}: {item}")
    
#Step 1: setup
#Step 2: process
#Step 3: result

#zip() Function
#The zip() function takes multiple iterables and aggregates elements from each into tuples.

names=["Anya","Ben","Chloe"]
scores=[95,88,92]
grades=["A","B+","A"]

report_card=list(zip(names,scores,grades))
print(report_card)