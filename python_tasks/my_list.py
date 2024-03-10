#empty list
my_list=[]

#Appending empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list) #output:[10, 20, 30, 40]

#Inserting element to list
my_list.insert(1, 15)
print(my_list) #Output:[10, 15, 20, 30, 40]

#Extending list
list=[50,60,70]
my_list.extend(list)
print("list after append:",my_list) #output:[10, 15, 20, 30, 40, 50, 60, 70]

#Remove element from my_list
del my_list[-1] #using del()
print(my_list)

#sort
my_list=[10, 15, 20, 30, 40, 50, 60, 70]
sorted_list= sorted(my_list)
print(sorted_list)

#Finding index
index=my_list.index(30)
print(index) #output: 3

#output summary:
#[10, 20, 30, 40]
#[10, 15, 20, 30, 40]
#list after append: [10, 15, 20, 30, 40, 50, 60, 70]
#[10, 15, 20, 30, 40, 50, 60]
#[10, 15, 20, 30, 40, 50, 60, 70]
#3
