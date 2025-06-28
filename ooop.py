# class User:
#     def __init__(self,name,money):
#         self.name=name
#         self.money=money
#         self.cart=None
        
#     def add_to_cart(self):
#         pass
    
#     def remove_to_cart(self):
#         pass
# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

# class Cart:
#     def __init__(self):
#         self.products=[]

# product1=Product("soap",50)
# product2=Product("dishwasher",70)

# user=User("md",2000)
# cart=Cart()
# user.cart=cart
# user.cart.products.extend([product1,product2])
# print(user.cart.products[0].name)


# print(product1.name)
# products=[product1.name,product2.name]
# print(products)
# user=User("md",2000)
# cart=Cart()
# user.cart=Cart
# user.cart.products.append("vim")
# print(user.cart.products)


######################################################################### encapsulation


# class User:
#     def __init__(self,name,number):
#         self.name=name
#         self.bank_acc=number
# user=User("md",6301478938)
# print(user.name)
# print(user.bank_acc)
# user.bank_acc=960000000  
# print(user.bank_acc)      




# class User:
#     def __init__(self,name,number):
#         self._name=name
#         self.bank_acc=number
        
#     def say_name(self):
#         print(f"{self.__name}")
        
# user=User("md",6301478938)
# print(user._name)
# print(user.__name())




# class User:
#     def __init__(self,name,number):
#         self.__name=name
#         self.__bank_acc=number
        
#     def set_bank_acc(self,new_acc_no):
#         self.__bank_acc=new_acc_no
    
#     def get_bank_acc(self):
#         return self.__bank_acc
       
# user=User("md",6301478938)

# user.set_bank_acc(123456789)

# print(user.get_bank_acc())




# class User:
#     def __init__(self,name,number):
#         self.__name=name
#         self.__bank_acc=number
        
#     def set_bank_acc(self,id,new_acc_no):
#         if id=="1234":
#             self.__bank_acc=new_acc_no
#         else:
#             return "you dont have access"
#     def get_bank_acc(self):
#         return self.__bank_acc
       
# user=User("md",6301478938)

# # user.set_bank_acc("45686", 123456789)# old account 8938
# print(user.set_bank_acc("45686", 123456789))# you dont have access


# print(user.get_bank_acc())





# class User:
#     def __init__(self,name,number):
#         self.__name=name
#         self.__bank_acc=number
        
#     def set_bank_acc(self,new_acc_no):
#         if new_acc_no.isdigit()
#             self.__bank_acc=new_acc_no
#         else:
#             return "you dont have access"
#     def get_bank_acc(self):
#         return self.__bank_acc
       
# user=User("md",6301478938)


#implement encapsulate of name "attribute"
class Dog:
    def __init__(self,name,breed):
        self.__name=name
        self.breed=breed
    
    # def my_dog(self):
    #     self.name=name
    #     print("my kalia")
    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        self.__name=new_name
        
    
        
dog=Dog("kutta","kallu")
dog.set_name("billa")
# print(dog.__name)
print(dog.get_name())


##################################### oops explanation
# Explanation:
#1.Classes: Animal, Dog, and Cat are classes. Dog and Cat inherit from the Animal class.
#2. Encapsulation: The name attribute is encapsulated within the Animal class.
#3. Inheritance: Dog and Cat inherit the properties and methods of the Animal class.
#4. Polymorphism: The speak method is overridden in the Dog and Cat classes.



#base class 
class Animal:
    def __init__(self,name):
        self.name=name #encapsulation
    
    def speak(self):
        raise NotImplementedError("smim")
#derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} say woof!"

#another derived class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

#creating objeccts
dog=Dog("buddy")
cat=Cat("whiskers")

#using the objects
print(dog.speak())#buddy say  woof
print(cat.speak())# whishkers say meow

##########################################  inheritence

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Usage
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Dog barks
print(cat.speak())  # Output: Cat meows

# class Animal:
#     def speak(Self):
#         return"Animal speaks"

# class Dog(Animal):
#     def speak(Self):
#         return "Dog barks"
# class Cat(Animal):
#     def speak(self):
#         return "Cat meows"
# #usage
# dog=Dog()
# cat=Cat()
# print(dog.speak())
# print(cat.speak())


#------------------------------------- encapsulation
# class BankAccount:
#     def __init__(self,account_number,balance=0):
#         self.__account_number=account_number#private attribute
#         self.__balance=balance#private attribute
        
#         #getter for balance
#     def get_blance(self):
#             return self.__balance
#         #setter for balance
#     def deposit(Self,amount):
#             if amount>0:
#                 self.__balance +=amount
#                 print(f"depsited:{amount}")
#             else:
#                 print("deposited amount must be positive.")
#     #method to withdraw amount
#     def withdraw(self,amount):
#         if 0<amount<=self.__balance:
#             self.__balance-=amount
#         else:
#             print("insufficeint funds or invalid amount.")

# #create an object of BankAccount
# account=BankAccount("9347066570")

# #accessing balance usig getter
# print("initial Balance:",account.get_blance())

# #depositing money
# account.deposit(1000)

# #withdraw money
# account.withdraw(500)

# #cheking money
# print("final balance",account.get_blance())

# #trying to access private attribute directly (will rise an error)
# print(account.__balance())
#--------------------------------------------------inheritence--------
# class A:
#        pass
# class B(A):
#        pass
# class C(A):
#        pass
# class D(B, C):  # D inherits from both B and C
#        pass

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def get_name(self):
        return self.name

# # class Student(Person):
# #     pass
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)#person,when u give super no need pas self
#         self.grade="A"

# Student=Student("md",20)
# # print(Student.get_name())
# print(Student.grade)

#________________________________POLY Morphysm______--------------

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
        
#     def move(self):
#         print("drive...")

# class Boat:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
        
#     def move(self):
#         print("sails..")

# class Plane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
    
#     def move(self):
#         print("fly")

# car=Car("ford","v3")
# boat=Boat("boat company","v1")
# plane=Plane("beoing","747")

# for vehicle in (car,boat,plane):
#     vehicle.move()
    
# class Parrot:
#     name=""
#     age=2
# Parrot1=Parrot()

# class Polygon:
#     def draw(self):
#         print("drawing polygon")

# class square(Polygon):
#     def draw(self):
#         print("drawing square")
        
# class Circle(Polygon):
#     def draw(self):
#         print("drawing circle")
        
# # sq1=square()
# # sq1.draw()
# c1=Circle()
# c1.draw()


        
class Phonepay:
    def pay(self):
        print("paying through the phonepay")

class PayTm:
    def pay(self):
        print("paying through the paytm")
        

def get_payment_mode(use_choice):
    if user_choice=="Phonepay":
        payment_mode=Phonepay()
    elif user_choice=="PayTm":
        payment_mode=PayTm()
    
    return payment_mode

user_choice="phonepay"
# user_choice=input("choice:")
payment_mode=get_payment_mode(user_choice)
payment_mode.pay()




# if user_choice=="Phonepay":
#     payment_mode=Phonepay()
# elif user_choice=="PayTm":
#     payment_mode=PayTm()
    