#function definition and calling
#arguments and parameters
#arbitrary arguments
#return values and scope

#function definition
def greet(name):
    print(f"Hello, {name}!")    

#function calling
greet("Alice") #Hello, Alice!

#--------------------------------
#function with parameters
def add(a,b):
    return a+b
result=add(5,10)
print(result) #15
#--------------------------------
#function with positional arguments
def multiply(x,y):
    return x*y
prod=multiply(4,5)
print(prod) #20
#--------------------------------
#function with arbitrary arguments
def fruits(*args):
    for fruit in args:
        print(fruit)
fruits("Apple","Banana","Cherry")
#Apple  
#Banana
#Cherry

def profile_user(**data):
    print(f"Name: {data.get('name','N/A')}")
    print(f"Role: {data.get('role','Guest')}")
profile_user(name="Alice", role="Admin")
#Name: Alice
#Role: Admin

#--------------------------------
#function with keyword arguments
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
person_info(name="John", age=30, city="New York")
#name: John
#age: 30
#city: New York
#--------------------------------
#function with return value and scope
def square(num):
    return num * num
result = square(6)
print(result) #36
#--------------------------------
#function with default value
def greet(name,greeting="Hello"):
    print(f"{greeting}, {name}!")
greet("Bob") #Hello, Bob!
greet("Bob","Hi") #Hi, Bob!
#--------------------------------
#Variable Scope: Local vs Global

#Global variable
x = 10
def modify_global():
    global x
    x = 20
modify_global()
print(x) #20

print("----------------------")
x=100
def my_function(y):
    z=5 #local variable
    print(f"Inside: x={x}, y={y}, z={z}")

my_function(20)

#--------------------------------
#function with lambda
multiply_lambda = lambda a, b: a * b
result = multiply_lambda(3, 4)
print(result) #12

#Lambda Use Case: Sorting
students=[
    {"name":"John","age":25},
    {"name":"Alice","age":22},
    {"name":"Bob","age":23} 
]
students.sort(key=lambda s: s["age"])
print(students)

#--------------------------------