# import requests

 
# print("***RHYMING WORD GENERATOR*****")
# choice = input('Enter a word:')
# endpoint = f"https://api.datamuse.com/words?sp={choice}"
 
# response = requests.get(endpoint)
 
# data = response.json()
  
# if response.status_code == 200:
#     for item in data:
#         print(item.get('word'))




class Instructor:
    def __init__(self,instructor_name,address):
        self.name=instructor_name
        self.address=address
        self.followers=0
    
    def display(Self):
        print("done")
    def function(self):
        print(f"i'm , {self.name}and your address is {self.address}")
    def function(self,subject_name):
        print(f"i'm {self.name} and teach {subject_name}")
    
    def update_followers(self,followers_name):
        self.followers += 1000

        
i=Instructor("md","paki")
print(i.name)
print(i.address)
print(i.followers)
# i.function("hindi")
i.update_followers("ree")
print(i.followers)


# class Human:
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("i can work")

# class Male(Human):
#     def flirt(self):
#         print(" i can flirt")

# h=Male()
# h.eat()
# h.flirt()
# print(h.flirt)

# class Human:
#     def __init__(self):
#         self.num_eyes=2
#         self.num_eyes=1
    
#     def eat(self):
#         print("i can eat")
    
#     def work(self):
#         print("i can work")

# class Male(Human):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
    
#     def flirt(self):
#         print(" i can do first")
        
# h=Male("md_rashid")
# print(h.name)



# class Human:
#     def __init__(self,num_heart):
#         self.num_eyes=2
#         self.num_eyes=1
#         self.num_heart=num_heart
    
#     def eat(self):
#         print("i can eat")
    
#     def work(self):
#         print("i can work")

# class Male(Human):
#     def __init__(self,name):
#         super().__init__(heart)
#         self.name=name
    
#     def flirt(self):
#         print(" i can do first")
        
# h=Male("md_rashid",1)
# print(h.name)
# print(h.num_heart)

# class Human:
#     def eat(self):
#         print("i can ea")

# class Male:
#     def fill(self):
#         print("i can fill")

# class Boy(Human,Male):
#     def sleep(self):
#         print("i can sleep")
#     def work(self):
#         print("i can test")

# b=Boy()
# b.fill()
# b.eat()
# b.work()


# questions lets practice
# class Order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price
        
#     def __get__(self,order1,order2):
#         return self.price>order2.price

# rder1=Order("apple",80)
# rder2=Order("dell",70)
# print(rder1>rder2)

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
    
#     def area(self):
#         return (22/7)*self.radius**2
    
#     def perimeter(self):
#         return 2*(22/7)*self.radius
    
# c1=Circle(55)
# print(c1.area())
# print(c1.perimeter())

# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary
        
#     def showdetails(self):
#         print("role=",self.role)
#         print("dept=",self.dept)
#         print("salary=",self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer", "IT", 80000)
        
# eng1=Engineer("md_rashid",100)
# eng1.showdetails()

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
        
#     def shownumber(self):
#         print(self.real,"i +",self.img,"j")
    
#     def __add__(self,num2):
#         numreal=self.real+num2.real
#         newimg=self.img+num2.img
#         return Complex(numreal,newimg)

# num1=Complex(1,3)
# num1.shownumber()

# num2=Complex(4,6)
# num2.shownumber()

# num3=num1+num2
# num3.shownumber()
# # num3=num1.add(num2)
# # num3.shownumber()


# def happy_birthday():
#     print("happy birthday to you!")
#     print("you are old")
#     print("happy birth day to you")
#     print()

# happy_birthday()

# def happy_birthday(name,age):
#     print(f"happy birthday to {name}!")
#     print(f"you {age}are old")
#     print("happy birth day to you")
#     print()

# happy_birthday("rehan",40)
# happy_birthday("minn",30)
# happy_birthday("ras",20)

# def divide(x,y):
#     z=x/y
#     return z
# print(divide(1,2))

# def divide(x,y):
#     z=x+y
#     return z
# print(divide(1,2))

# def divide(x,y):
#     z=x*y
#     return z
# print(divide(1,2))

# def divide(x,y):
#     z=x-y
#     return z
# print(divide(1,2))


# def create_name(first,last):
#     first=first.capitalize()
#     last=last.capitalize()
#     return first +"__"+last
# full_name=create_name("md","rashid")
# print(full_name)