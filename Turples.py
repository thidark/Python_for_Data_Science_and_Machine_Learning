# symbol: () (parentheses )
#key characteristics:
#1. ordered
#2. immutable(unchangeable)
#3. allow duplicate values  
#4. faster: compared to list
#5. used to store multiple items in a single variable

#Creation and Immutability
my_tuple=(10,20,30,40,50) #parentheses
person="John",25,"Engineer"  #omitting parentheses
print(my_tuple)#(10, 20, 30, 40, 50)
print(person)#('John', 25, 'USA')

#Immutability
try:
    my_tuple=(10,20,30)
    my_tuple[1]=25 #TypeError: 'tuple' object does not support item assignment
except TypeError as e:
    print("error:", e)
#print(my_tuple)#

#Tuple Unpacking
name,age,job=person
print(name)#John
print(age)#25   
print(job)#Engineer
print(f"Name: {name}, Age: {age}, Job: {job}")#Name: John, Age: 25, Job: Engineer       

#Slicing and Ite
rgb_colors=(255,165,0,"Orange",(0,0,0),"Black",(255,255,255),"White")
print(rgb_colors[0:4])#(255, 165, 0, 'Orange')
print(rgb_colors[-4:])#((0, 0, 0), 'Black', (255, 255, 255), 'White')

#Iterate through a tuple
for color in rgb_colors:
    print(color)    
#255
#165
#0
#Orange
#(0, 0, 0)
#Black
#(255, 255, 255)
#Count and Index Methods


