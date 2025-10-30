#symbol:{} (curly braces)
#key characteristics:
#1. unordered
#2. mutable(changeable)
#3. no duplicate values
#4. faster: compared to list
#5. used to store multiple items in a single variable

#Creation
my_set={10,20,30,40,50} #curly braces
print(my_set)#{50, 20, 40, 10, 30}

number_list=[10,20,30,20,40,10,50]
unique_numbers=set(number_list) #convert list to set to remove duplicates
print(unique_numbers)#{50, 20, 40, 10, 30}]

#Add elements
my_set.add(60)
print(my_set)#{50, 20, 40, 10, 60, 30}

#Union
set_a={1,2,3}
set_b={3,4,5}
set_c=set_a.union(set_b)
print(set_c)#{1, 2, 3, 4, 5}

#intersection
set_d=set_a.intersection(set_b) #OR
set_d=set_a & set_b
print(set_d)#{3}

#Difference
set_e=set_a.difference(set_b)
print(set_e)#{1, 2}