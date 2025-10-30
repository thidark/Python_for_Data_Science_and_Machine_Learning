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