#List
#append()===inserrt into tend([group])
my_list=[10,"apple",3.14,True]
print(my_list)
print(my_list[1])#apple
print(my_list[2])#3.14
my_list.append("banana")
print(my_list)#[10, 'apple', 3.14, True, 'banana']
print(len(my_list))#5
print(type(my_list))#<class 'list'>

#insert()===insert into specific index(position)
my_list.insert(2,"orange")
print(my_list)#[10, 'apple', 'orange', 3.14, True

#remove()===remove from tend([group])   
my_list.remove(3.14)
print(my_list)#[10, 'apple', True, 'banana']

#pop()===remove from specific index(position)
my_list.pop(1)
print(my_list)#[10, True, 'banana']
my_list.pop()
print(my_list)#[10, True]

#clear()===remove all elements from list
my_list.clear() 
print(my_list)#[]

#del()===delete entire list
del my_list 
#print(my_list)#NameError: name 'my_list' is not defined

#exit()===exit from program
