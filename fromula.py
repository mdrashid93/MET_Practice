# mydict.keys()return all keys
# mydict.value()return all value
# mydict.itmes()return all(key,value)pair as tuple
# mydict.get("key")return the key according to value
# mydict.update(newdict)insert specific items to dict
# mydict.len()return all length
# mydict.pop()remove random ele

# set.add(el)add on element
# set.remove(el)remove the ele an
# set.clear()empty the set
# set.pop()remove an random ValueError
# set.union(set)combine both set value and return new
# set.intersection(set)combine common value and return new


# write a programme to enter marks of three subject from the user and store them  in a dict start with an empty dict and add one by one use sub 
# name as key mark as value.
# marks={}
# a=int(input('enter hindi'))
# marks.update({"hindi":a})
# a=int(input("enter urdu"))
# marks.update({"urdu":a})
# a=int(input("enter eng"))
# marks.update({"eng":a})
# print(marks)
# my_class="student"

# for student in my_class:
#     if student.is_present_today:
#         say_hello(student.name)
#         print(student)

#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found

# tupel=("aple","banana","cherry","mango")
# print(tupel)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# thistup=("apple", "banana", "cherry")
# if "cherry" in thistup:
#     print("yes","cherry ",is in the fruits tuple")

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

# x=("apple","banana","cherry")
# y=list(x)
# y[1]="amrood"
# x=tuple(y)
# print(x)


# thistuple=("apple", "banana","cherry")
# y=list(thistuple)
# y.append("orange")
# thistuple=tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# tup=("apple", "banana", "cherry","guava","amrood")
# y=("dahi",)
# tup+=y
# print(tup)

# day = 4
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")


# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# x = input("Type a number: ")
# y = input("Type another number: ")

# sum = int(x) + int(y)

# print("The sum is: ", sum)

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)
# def m_f(fn):
    
#     print(fn+ "i love you")

# m_f("babe")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
