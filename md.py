student_1=['rashid',10]#name,grade
student_2=['md',12]
print(f"{student_1[0]} is in class{student_1[1]}")

#using oops creating student records
#class-blueprints or template
class Student:
#     name="md_rashid"
#     grade=10
# #object- instance of class
# student1=Student()
# print(student1.name,student1.grade)
# # print(student1.grade)
#self parameter- reference or connection build bw class and object
#__init__ method cunstructor initialized
#attribute (name,grade) prooerties
       
#     def __init__(self,name,grade,percentage):
#         self.grade=grade#attribute
#         self.name=name#attribute
#         self.percentage=percentage#attribute
    
#     def student_details(self):# this is method
#         print(f"{self.name} is in class{self.grade} with {self.percentage}%")
# student1=Student("md",200,96)
# # print(student1.name,student1.grade)

# student2=Student("ras",400,99)
# # print(student2.name, student2.grade)
# # print(student1.percentage)
# student1.student_details()
# student2.student_details()
# print(student1.__dict__)# dictionary form


#modify object property or attribute
# student1.percentage=100
# print(student1.percentage)

# delete object properties
# del student1.percentage
# print(student1.__dict__)

#delete object
# del student1
# print(student1)# did you mean student1   

    def __init__(self,name,grade,percentage,team):
        self.grade=grade#attribute
        self.name=name#attribute
        self.percentage=percentage#attribute
        self.team=team
    
    def student_details(self):# this is method
        print(f"{self.name} is in class{self.grade} with {self.percentage}%, in team {self.team}")
team1="a"
team2="b"
student1=Student("md",200,96,team1)
# print(student1.name,student1.grade)

student2=Student("ras",400,99,team2)
print(student1.team)

#4 features in OOPs
#abstraction
#encapsulation
#inheritance
#polymorphism

#********************************************ABSTRACTION****************************************************************************
# HIDING UNNECESSARY DETAILS FR0M USERS THROUGH CLASS, METHODS
class Student:
    def __init__(self,name,grade,percentage,team):
        self.grade=grade#attribute
        self.name=name#attribute
        self.percentage=percentage#attribute
        self.team=team
    
    def student_details(self):# this is method -ABSTRACTION
        print(f"{self.name} is in class{self.grade} with {self.percentage+2}%, in team {self.team}")#HIDDEN FROM USERS  
team1="a"
team2="b"
student1=Student("md",2000,96,team1)
student2=Student("raa",800,95,team2)
student1.student_details()



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ENCAPSULATION @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# RESTRICT ACCESS TO CERTAIN ATTRIBUTES OR METHODS TO PROTECT DATA AND ENFORCE CONTROLLED ACCESS 
class Student:
    def __init__(self,name,grade,percentage):
        self.grade=grade#attribute
        self.name=name#attribute
        self.__percentage=percentage# DOUBLE UNDERSCORE LIMITS ACCESS
    
    def get_percentage(self):
        return self.__percentage
        
    
    def student_details(self):# this is method -ABSTRACTION
        print(f"{self.name} is in class{self.grade} with {self.__percentage}% ")#HIDDEN FROM USERS  

student1=Student("md",2000,96)
student2=Student("raa",800,95)
student1.student_details()

# print(student1.__percentage)#got error , dont have attribute percentage
print(student1.get_percentage())


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(INHERITENCE)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#ALLOW ONE CLASS (CHILD) TO REUSE THE PROP AND METHOD OF ANOTHER CLASS (PARENT).
#BAAP
class Student:
    def __init__(self,name,grade,percentage):
        self.grade=grade#attribute
        self.name=name#attribute
        self.percentage=percentage# DOUBLE UNDERSCORE LIMITS ACCESS
    
    def get_percentage(self):
        return self.percentage
        
    
    def student_details(self):# t
        print(f"{self.name} is in class{self.grade} with {self.percentage}% ")#HIDDEN FROM USERS  

student1=Student("md",2000,96)
student2=Student("raa",800,95)
# student1.student_details()

# print(student1.__percentage)#got error , dont have attribute percentage
#print(student1.getpercentage())
# BETA

class GraduateStudent(Student):#graduate students child class inherit properties form student parent class
    def __init__(self, name, grade, percentage,stream):# parameters from parents class and new parameter child class
        super().__init__(name, grade, percentage) #call parent class init
        self.stream=stream# this is new attribute in child class
    def student_details(self):
        super().student_details()#method inherit fom parent class
    
    
#object
grad_student1=GraduateStudent("apple",12,96,"pcm")
print(grad_student1.stream)
print(student2.percentage)

grad_student1.student_details()


#++++++++++++++++++++++++++++++++++++++++++++++++++ POLYMORPHISM ++++++++++++++++++++++++++++++++++++++++++++++++++++
# ALLOW METHOD IN DIFFERENT CLASSESS TO HAVE SAME NAME BUT DIFFERENT BEHAVIOUR DEPENDING ON OBJECTES=
        
class Student:
    def __init__(self,name,grade,percentage):
        self.grade=grade#attribute
        self.name=name#attribute
        self.percentage=percentage# 
    
    def get_percentage(self):
        return self.percentage
        
    
    def student_details(self):# this is method -ABSTRACTION 
        print(f"{self.name} is in class{self.grade} with {self.percentage}% ")#HIDDEN FROM USERS  

student1=Student("md",2000,96)
student2=Student("raa",800,95)

class GraduateStudent(Student):
    def __init__(self, name, grade, percentage,stream):# 
        super().__init__(name, grade, percentage) 
        self.stream=stream# 
        
    def student_details(self):
        # print(f"{self.name}is in class{self.grade} with {self.percentage} and stream{self.stream}")
        print("same method with different output")

#object student class
student1=Student("reshid",15,88)
# graduate student class
grad_student1=GraduateStudent("apple",12,96,"pcm")

student1.student_details()
grad_student1.student_details()