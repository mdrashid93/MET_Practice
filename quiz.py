#print the score
#1 what do you need
#score
#2 what do you want from whom
    #question-myself
    #i need each answer from user
#3 order the need with priority same
#4 flow pseudo code
##1 define question ds
##2 iterate and show each question
##3 iterate and show collection each questin from the user
##4 iterate and every correct answer we need to increment score
##5 print the score

# score=0
# questions=[
# {
# "question": "What does strip() method do?",
# "options": ["A. remove left space", "B. remove spaces both end", "C. NA "],
# "answer": "B"
# },
 
# {"question": "what is 2+2?",
# "option":["A.4","B.5","C.6"],  
# "answer":"A"  
# },
 
# {
# "question":"what is 2**2?",
# "option":["A.4444","B.44","c.4"],
# "answer":"C"    
    
# }
# ] 
# for i,q in enumerate(questions):
#     print(f"question{i+1}:{q["question"]}")
    
   # print(q["option"])

# score=0
# questions=[
# {
# "question": "What does strip() method do?",
# "option": ["A. remove left space", "B. remove spaces both end", "C. NA "],
# "answer": "B"
# },
 
# {"question": "what is 2+2?",
# "option":["A.4","B.5","C.6"],  
# "answer":"A"  
# },
 
# {
# "question":"what is 2**2?",
# "option":["A.4444","B.44","c.4"],
# "answer":"C"    
    
# }
# ] 
# for i, q in enumerate(questions):
#     print(f"question{i+1}:{q['question']}")

#     for option in q['option']:
#         print(option)
#         print("")

# score=0
# questions=[
# {
# "question": "What does strip() method do?",
# "option": ["A. remove left space", "B. remove spaces both end", "C. NA "],
# "answer": "B"
# },
 
# {"question": "what is 2+2?",
# "option":["A.4","B.5","C.6"],  
# "answer":"A"  
# },
 
# {
# "question":"what is 2**2?",
# "option":["A.4444","B.44","c.4"],
# "answer":"C"    
    
# }
# ]
# attempt=[] 
# for i, q in enumerate(questions):
#     print(f"question{i+1}:{q['question']}")

#     for option in q['option']:
#         print(option)
#     chioice=input("enter your answer")
#    # attempt.append((i,chioice))
#     attempt_entry=()
#     if chioice.upper()==q['answer']:
#         score+=2.0
#         attempt_entry=(i,chioice,'correct')
#     else:
#         score-=0.5 
#         attempt_entry=(i,chioice,'wrong')
#     attempt.append(attempt_entry)
#     print("")
# print(f"your score:{score}")
# print(attempt)


# attempt=[] 
# for i, q in enumerate(questions):
#     print(f"question{i+1}:{q['question']}")

#     for option in q['option']:
#         print(option)
#     chioice=input("enter your answer")
#     attempt_entry=(i,chioice, q['answer'])
#    # attempt.append((i,chioice))
#     attempt_entry=()
#     if chioice.upper()==q['answer']:
#         score+=2.0
      
#     else:
#         score-=0.5 
      
#     attempt.append(attempt_entry)
#     print("")
# print(f"your score:{score}")
# print(attempt)

# attempt=[]
# for i,w in enumerate(questions):
#     print(f"{i+1}:{w['question']}")
#     for option in w["option"]:
#         print(option)
#     choice=input("enter your answer")
#     attem_ent=(i,choice,w["answer"])
#     attem_ent=()
#     if choice.upper()==w["answer"]:
#         score+2.0
#     else:
#         score-=0.5
        
# print(attempt)
# print(f"your score is:{score}")

# names=['raj ras','reh','riya']
# for c in names:
#     print(c[2])
#     if c=="reh":
#         print("hey i'm rashid")
# numbers=[2,3,5,-2,10]
# squares=[]
# for num in numbers:
#     square= num**2
#     squares.append(square)
#     print(squares,num ,end=" ")
#     squares.pop(squares)

# count=5
# while count>0:
#     print(count,"i love you bebe")
#     count -=1
# for i in range(1,10,2):
#     print(i)

     
# class TV:
#     def turn_on(self):
#         print("The TV is now ON.")
        
#     def turn_off(self):
#         print("The TV is now OFF.")

# class Remote:
#     def __init__(self):
#         self.tv = TV()  # Creating an instance of TV inside Remote

#     def turn_on_tv(self):
#         self.tv.turn_on()

#     def turn_off_tv(self):
#         self.tv.turn_off()

# # Example usage
# remote = Remote()
# remote.turn_on_tv()
# remote.turn_off_tv()


# class TV:
#     def turn_on(self):
#         print("TV is ON.")
        
#     def turn_off(self):
#         print("TV is OFF.")

# class Remote:
#     def turn_on_tv(self, tv):
#         tv.turn_on()
        
#     def turn_off_tv(self, tv):
#         tv.turn_off()

# # Example usage
# my_tv = TV()
# remote = Remote()

# remote.turn_on_tv(my_tv)
# remote.turn_off_tv(my_tv)



# class TB:
#     def turn_on(self):
#         print("tb is on")
#     def turn_off(self):
#         print("tb is off")
# class Remot:
#     def turn_on_tb(self,tb):
#         tb.turn_on()
#     def turn_of_tb(self,tb):
#         tb.turn_on(self,tb)


# mi_tb=TB()
# remot=Remot()

# remot.turn_on_tb(mi_tb)
# remot.turn_of_tb(mi_tb)
 

# out=[[i,j,k] 
# for i in range(0,i+1) for j in range(j+1) for k in range(k+1)if i+j+k !=n]
# print(out)

# out=[[i,j,k] 
# for i in range(i+1) for j in range(j+1) for k in range(k+1)if i+j+k !=n]
# print(out)
# arr=(2,6,6,5)
# arr=lsit(set(arr))
# arr.sort()
# print(arr[-2])

# class Student:
#     def __init__(self,name):
#         self.name=name

# print(s1.name)
# s1=Student("md_rashid")
# del s1

# class Person:
#     __name="anonymous"

#     def __hello(self):
#         print("hello person")
    
#     def welcome(self):
#         self.__hello() #only accessable with internal not in external
# p1=Person()
# print(p1.welcome)
# class Terson:
#     def __mello(self):
#         print("kello peerso")
#     def selcome(self):
#         self.mello()

# p2=Terson()
# print(p2.selcome)


######################### single level inheritence
# class Car:
#     color="blacked"
#     @staticmethod
    
#     def started():
#         print("car started")
    
#     @staticmethod
#     def stop():
#         print("car stopped")

# class Toyotacar(Car):
#     def __init__(self,name):
#         self.name=name
        
# car1=Toyotacar("Fortuner")
# car2=Toyotacar("Porsche")

# print(car2.stop)
# print(car1.started) 
# print(car1.color) 


#################### multi level inheritence#################
# class Car:
#     @staticmethod
#     def started():
#         print("car starting")
    
#     @staticmethod
#     def stop():
#         print("car stopping")

# class Toyotacar(Car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(Toyotacar):
#     def __init__(self, type):
#         self.type=type

# car1=Toyotacar("inova")
# car2=Fortuner("diesel")
# print(car1.started)
# print(car2.stop)
# car1.started()
# # car2.started()
# car2.stop()

######33333333 multiple inheritence~~~~~~~~~~~~~~~~~~
# class A:
#     VarA="welcome to class A"

# class B:
#     VarB="welcome to class B"

# class C(A,B):
#     VarC="welcome to class C"
    
# c1=C()
# print(c1.VarC)
# print(c1.VarB)
# print(c1.VarA)




# class Car:
#     def __init__(self,type):
#         self.type=type
    
#     @staticmethod
#     def start():
#         print("car startedd")
        
#     @staticmethod
#     def stop():
#         print("car stoppingg")

# class Toyotacar(Car):
#     def __init__(self,name, type):
        
#         super().__init__(type)
#         self.name=name
#         super().start()
        

# car1=Toyotacar("prius","electric")
# print(car1.type)

# print(car1.name)
# car2=Toyotacar("prius","electric")
# print(car2.name)
# print(car2.start())

# class Person:
#     name="anonymous"
    
#     def changename(self,name):
#         self.__class__name=name# name change

# p1=Person()
# p1.changename("mdrashid")
# print(p1.name)
# print(Person.name)

# class Verson:
#     name="tonykakkar"
#     def namechange(self,name):
#         Verson.name=name
# d1=Verson()
# d1.namechange("rehan")
# print(d1.name)
# print(Verson.name) # if u want change name both attribute and object then version.name=name in method
# second type change name in both attribute and object (self.__class__.name="name")


    # class Person:
    #     name="anonymous"
    #     @staticmethod
    #     def changename(cls,name):
    #         cls.name=name

    # A1=Person()
    # A1.changename("rajtevari")
    # print(A1.name)
    # print(Person.name)



# class Student:
#     def __init__(self,phy,che,math):
#         self.phy=phy
#         self.che=che
#         self.math=math
#         self.percentage = str((self.phy+self.che+self.math)/3) + "%"
    
#     # def calcPercentage(self):
#     #         self.percentage = str((self.phy+self.che+self.math)/3) + "%"
#     @property
#     def percentage(self):
#         return str((self.phy+self.che+self.math)/3) + "%"
    

# stu1=Student(98,97,99)


# stu1.phy=86
# print(stu1.percentage)



##################### poly morphysm-----------------------

# print(1+2)
# print("md"+"rashid") #concatenate
# print([1,2,3]+[4,5,6])# merge


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def shownumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal,newimg)
    
    def __sub__(self,num2):
        newreal=self.real-num2.real
        newimg=self.img-num2.img
        return Complex(newreal,newimg)
        
    
num1=Complex(1,3)
num1.shownumber()

num2=Complex(4,6)
num2.shownumber()

# num3=num1.add(num2)
# num3.shownumber()
# num3=num1+num2
# num3.shownumber()

num4=num1-num2
num4.shownumber()



# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
        
#     def area(self):
#         return (22/7) * self.radius**2
    
#     def perimeter(self):
#         return 2*(22/7)* self.radius
    
# c1=Circle(21)
# print(c1.area())
# print(c1.perimeter())
