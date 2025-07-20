# # Initialize a list
# my_list = [1, 2, 3, 4, 5]

# # Interchange first and last elements
# my_list[0], my_list[-1] = my_list[-1], my_list[0]

# # Print the modified list
# print("List after swapping first and last elements:", my_list)


# Input : lst1 = ['Hello', 'geeks', 'for', 'geeks']
# lst2 = [1, 2, 3]
# Output : ['geeks', 'for', 'geeks']


# a = [4, 7, 9, 7, 2, 7]

# # Find all indices of the value 7
# indices = [i for i, x in enumerate(a) if x == 7]
# print("Indices", indices)

# # Python program to print pattern G
# def Pattern(line):
#     pat=""
#     for i in range(0,line):    
#         for j in range(0,line):     
#             if ((j == 1 and i != 0 and i != line-1) or ((i == 0 or
#                 i == line-1) and j > 1 and j < line-2) or (i == ((line-1)/2)
#                 and j > line-5 and j < line-1) or (j == line-2 and
#                 i != 0 and i != line-1 and i >=((line-1)/2))):  
#                 pat=pat+"*"   
#             else:      
#                 pat=pat+" "   
#         pat=pat+"\n"   
#     return pat
 
# # Driver Code
# line = 7
# print(Pattern(line))
   
   
   
n = 5
sum = 0

for i in range(1, n + 1):
    s += i ** 3

print(s)


a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)


def fun(lst):
    lst.append(4)
    print("Inside function:", lst)

a = [1, 2, 3]
fun(a)
print("Outside function:", a)

def same_list(list):
    return list

my_list = ["X"]
same_list(my_list)
print(my_list)



def call_by_val(x):
    x = x * 2
    return x

def call_by_ref(b):
    b.append("D")
    return b

a = ["E"]
num = 6

# Call functions
updated_num = call_by_val(num)
updated_list = call_by_ref(a)

# Print after function calls
print("Updated value after call_by_val:", updated_num)
print("Updated list after call_by_ref:", updated_list)



s1 = 'GeeksforGeeks'

s2 = lambda func: func.upper()
print(s2(s1))


keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  

# this line shows dict comprehension here  
d = { k:v for (k,v) in zip(keys, values)}  

# We can use below too
# d = dict(zip(keys, values))  

print (d)



# define a class
class Dog:
    sound = "bark"  # class attribute
    # sound attribute is a class attribute.

class Dog:
    sound = "bark" 

# Create an object from the class
dog1 = Dog()
# instance dog1.
# Access the class attribute
print(dog1.sound)


# Using __init__() Function
# In Python, class has __init__() function. It automatically initializes object attributes when an object is created.


class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Explanation:

# class Dog: Defines a class named Dog.
# species: A class attribute shared by all instances of the class.
# __init__ method: Initializes the name and age attributes when a new object is created.
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)  # Output: Buddy
print(dog1.species)  # Output: Canine

# Explanation:

# dog1 = Dog("Buddy", 3): Creates an object of the Dog class with name as "Buddy" and age as 3.
# dog1.name: Accesses the instance attribute name of the dog1 object.
# dog1.species: Accesses the class attribute species of the dog1 object.




# Self Parameter
# self parameter is a reference to the current instance of the class.
# It allows us to access the attributes and methods of the object.
class Dog:
    def __init__(self, name, age):  
        self.name = name 
        self.age = age

    def bark(self): 
        print(f"{self.name} is barking!")

# Creating an instance of Dog
dog1 = Dog("Buddy", 3)
dog1.bark()






class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."  # Correct: Returning a string
      
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)  
print(dog2)


# Class and Instance Variables in Python
# In Python, variables defined in a class can be either class variables or instance variables,
# and understanding the distinction between them is crucial for object-oriented programming.

# Class Variables
# These are the variables that are shared across all instances of a class. It is defined at the class level,
# outside any methods. All objects of the class share the same value for a class variable unless explicitly overridden in an object.


# Instance Variables
# Variables that are unique to each instance (object) of a class. 
# These are defined within __init__ method or other instance methods. 
# Each object maintains its own copy of instance variables, independent of other objects.

class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)


# Python program to demonstrate instantiating
# a class
class Dog:

    # A simple class attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
        
    def greet(self):
      print("hope you are doing well")


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes and method through objects
print(Rodger.attr1)
print(Rodger.attr2)
Rodger.fun()
Rodger.greet()