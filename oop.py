# class car:
#     color="blue"
#     brand="bmw"

# car1=car()
# print(car1.color)
# print(car1.brand)

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding new student in database")
        
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#             print("hi", self.name, "your avg socre is:" ,sum/3)

# s1=student("md_rashid",[99,98,97])
# s1.get_avg()

# s2=student("md_ras",100)
# print(s2.name,s2.marks)

# del keyword:-
#used to delete object properties or object itself.
#del s1.name
#del s1
# class student:
#     def __init__(self,name):
#         self.name=name
# s1=student("mdrashid")
    
# print(s1)
# del s1     
# print(s1)
# class account:
#     def __init__(self,acc_no, acc_pass):
#         self.acc_no=acc_no
#         self.acc_pass=acc_pass
# acc1=account("12345","abc de")
# print(acc1.acc_no) 
# print(acc1.acc_pass)

# class account:
#     def __init__(self,acc_no, acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass#private password(__)
#     def reset_pass(self):
#         print(self.__acc_pass)
# acc1=account("12345","abc de")
# print(acc1.acc_no) 
# #print(acc1.__acc_pass)
# print(acc1.reset_pass())

# class person:
#     __name="anonymous"
    
#     def __hello(self):
#         print("hello person!")
#     def welcome(self):
#         self.__hello()
# p1=person()
##print(p1.__hello())# cant access this is private account
#print(p1.welcome())

# inheritance single level
#when one class(children) drive the properties from other class
# class car:
#     #color="black"
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped.")
# class toyotacar(car):
#     def __init__(self,name):
#         self.name=name 
# car1=toyotacar("fortuner")
# car2=toyotacar("prius")

#print(car1.name)
#print(car1.start())
#print(car1.color)

# Inheritance type
# single, multilevel, multiple

# class car:
#     #color="black"
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped.")
# class toyotacar(car):
#     def __init__(self,brand):
#         self.brand=brand

# class fortuner(toyotacar):
#     def __init__(self,type):
#         self.type=type

# car1 = fortuner("diesel")
# car1.start()

# # multiple inheritance:-
# class a:
#     vara="welcome to calss a"
# class b:
#     varb="welcome to class b"
# class c(a,b):
#     varc="welcome to class c"
# c1=c()
# print(c1.varc)
# print(c1.varb)
# print(c1.vara)

#super method:-
# super method used to access methods of the parent class
# class car:
#     def __init__(self, type):
#         self.type=type
    
#     @staticmethod
#     def start():
#         print("car started..")
    
#     @staticmethod
#     def stop():
#         print("car stopped")
        
# class toyotacar(car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()
        
# car1=toyotacar("prius","electric")
# print(car1.type)

# class person:
#     name="nonoymous"
#     def changename(self,name):
#         self.name=name

# p1=person()
# p1.changename("mdrashid")
# print(p1.name)  
#print(person.name)

# class person:
#     name="nani"
#     def changename(self,name):
# c1=person()
# c1.changename("mdrs")
# print(c1.name)


# class person:
#     name="nonoymous"
#     def changename(self,name):
#         #self.name=name
#         # person.name=name#class attribute change
#         self.__class__.name="mdrashid"
        
#         @calssmethod
#         def changename(cls,name):
#             cls.name=name # directly we can chage object

# p1=person()
# p1.changename("mdrashid")
# print(p1.name)  
# print(person.name)

  
# class student:
#     def __init__ (self,phy,chen,math):
#         self.phy=phy
#         self.chen=chen
#         self.math=math
# #         self.percentage=str((self.phy+self.chen+self.math)/3)+"*"

#     @property
#     def percentage(self):
#     return str((self.phy+self.chen+self.math)/3)+"%"
            
# stu1=student(98,97,99)
# print(stu1.percentage)
# stu1.phy=86
# # print(stu1.phy)
# print(stu1.percentage )


# class AC:
#     brand="samsung"
#     color="white"
#     type_of_ac="central AC"
    
#     def turn_on(self):
#         print("Turning on AC..")
    
#     def turn_off(self):
#         print("Turn off AC..")

# ac=AC()
# print(ac.brand)


# class car:
#     brand="lg"
#     color="black"
    
#     def turn_on(self):
#         print("turn on ac")
    
#     def turn_off(self):
#         print("turn off ac")

# cat=car()
# print(cat.brand)
# print(cat.color)


# class AC:
#     brand="samsung"
#     color="white"
#     type_of_ac="central ac"
    
#     def turn_on(self):
#         print("turing on ac...")
    
#     def turn_off(self):
#         print("turning off ac")

# ac=AC()
# print(ac.color)
# ac2=AC()
# print(ac2.color)
# print(ac is ac2)

# ac.color="blue"
# print(ac.color)
# # ac=AC("apple","white")
# # print(ac.brand)

# class AC:

#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
    
#     def turn_on(self):
#         print(f"turning on {self.brand}  ac...")

#     def turn_off(self):
#         print("turing off ac..")

# ac=AC("samsung","white")
# print(ac.brand)
# ac=(ac.turn_on())

######
# class Dog:
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed
#     def bark(self):
#         return f"{self.name} say woof!"
#     def bek(self):
#         return f"{self.name} say aooo!"
    
# my_dog=Dog("buddy","golden retriever")
# your_dog=Dog("lucy","labrador")

# print(my_dog.bark())
# # print(your_dog.breed())
# print(your_dog.bek())

########
class User:
    def __init__(self,name,money):
        self.name=name
        self.money=money
        self.cart=None
    
    def add_to_cart(self):
        pass
    
    def remove_from_cart(self):
        pass

class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
class cart:
    def __init__(self):
        self.product=[]
        
    
#user=User("md",5000) 
# user.money=-100
# user2=User("rashid",6)
# print(f"{user2.name} had {user2.money}")
# user.name="rehan"
# print(user.name)

user=User("md",200)
cart=cart()
user.cart=cart
#user.cart.products.append("vim")
#print(user.cart.product)
user.cart.product.append("vim")
print(user.cart.product)

 
 
######

class Animal:
    def __init__(self,name):
        self.name=name
    

class Zoo:
    def __init__(self):
        self.animals=[]


animal=Animal("cat")
animal_1=Animal("donkey")
animal_2=Animal("dog")
animal_4=Animal("kutta")
# animal.name="billi"
        
# print(animal.name)

zoo=Zoo()
zoo.animals.append(animal)
zoo.animals.append(animal_1)
zoo.animals.append(animal_4)
zoo.animals.append(animal_2)
print(zoo.animals)
# print(zoo.animals[0].name)
print(zoo.animals[3].name)


########

# class TV:
        
    
#     def __init__(self,brand,remote):
#         self.brand=brand
#         # self.remote=remote
    
#     def show_picture(self):
#         pass
    
#     def show_blank(self):
#         pass
    
# class Remote:
#     def __init__(self,tv):
#         self.tv=tv
        
#     def turn_on(Self):
#         print(f"{self.tv.brand} is turning on")
    
#     def turn_off(self):
#         print("turning off...")
 
# remote=Remote(tv)
# tv=TV("samsung",remote)

# tv.remote.turn_on()
# tv.remote.turn_off()

# remote.tv.turn_on

# tv=TV("samsung")
# Remote=Remote(tv)
# remote.turn_on()       
        
# 1. Identify three electronic devices in your home. For each device, list 3 properties (like brand, color,
# etc.) and 2 actions (like turn_on, reset, etc.). Then, create a class for each device with these
# attributes and methods. Create instances and call some methods.


# class Electronic:
    
#     def __init__(self,brand,color,year):
#     self.brand=brand
#     self.color=color
#     self.year=year
    
#     def
    


# ele=Electronic(self)


# # #1. Create a class Remote and a class TV. Add a method turn_on() in TV. Inside Remote, create an
# # instance of TV and call tv.turn_on() from Remote. Now write similar code for turn_off().
# class Remote:
#     def __init__(self,tv,remote):
#         self.tv=tv
#         self.remote=Remote
    
#     def turn_on(tv,remote):
#         tv=tv()

# class TV:
#     def __init__(self,brand):
#         self.brand=brand
#         # self.remote=Remote
    
#     def show_picture(self):
#         pass
    
#     def show_blank(self):
#         pass
    
# class Remote:
#     def __init__(self,tv):
#         self.tv=tv
    
#     def turn_on(self):
#         print("turning on...")
    
#     def turn_off(self):
#         print(f"turning off...")
# remote=Remote()
# tv=TV("samsung")
# remote=Remote(tv)
# tv.remote.turn_on()


#  2. Model a class Engine and a class Car. Let Car have an instance of Engine. Define a method in
#  Engine called start_engine(), and call it using car.engine.start_engine().
# class Engine:
#     def start_engine(self):
#         print("Engine has started.")

# class Car:
#     def __init__(self):
#         self.engine = Engine()  # Car contains an Engine instance

# # Example usage
# car = Car()
# car.engine.start_engine()

class Engine:
    def start_engine(self):
        print("engine start")

class Car:
    def __init__(self):
        self.engine=Engine() # car contains an engine instance

car=Car()
car.engine.start_engine()




#  3. Design a class Room and a class Light. Let each Room object contain a Light object. Define a
#  method in Light called switch_on(). From a Room instance, call room.light.switch_on().

class Light:
    def switch_on(self):
        print("The light is now ON.")

class Room:
    def __init__(self):
        self.light = Light()  # Room has a Light object

# Example usage
room = Room()
room.light.switch_on()


class Light:
    def __init__(self):
        self.is_on = False

    def switch_on(self):
        self.is_on = True
        print("Light is now ON.")

class Room:
    def __init__(self):
        self.light = Light()  # Containing a Light object

# Create a Room instance
room = Room()

# Call switch_on() from Room instance
room.light.switch_on()

class Lit:
    def __init__(Self):
        self.is_on=False
    
    def swithc_on(self):
        self.is_on=True
        print("lisht is now on")
        
class Room():
    def __init__(self):
        self.light=Light()
room.light.switch_on()

room=Room()

room.light.switch_on()

#  4. Create a class Laptop and a class Battery. Let Laptop have a Battery instance. Add a method in
#  Battery called check_charge(). Call it from Laptop like laptop.battery.check_charge().

class Battery:
    def __init__(self, charge_level=100):
        self.charge_level = charge_level  # percentage (0 to 100)

    def check_charge(self):
        print(f"Battery charge is at {self.charge_level}%.")

class Laptop:
    def __init__(self):
        self.battery = Battery()  # Contain a Battery instance

# Create a Laptop object
laptop = Laptop()

# Call the check_charge method via Laptop instance
laptop.battery.check_charge()

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started..")

car=Car()
car.start()


#create a class called "dog"
#name, breed
# implementation encapsulation for "name" attribute

class Dog:
    def __init__(self,name,breed):
        self.__name=name
        self.breed=breed
    
    

dog=Dog("jimy","labour")
print(dog.__name())
