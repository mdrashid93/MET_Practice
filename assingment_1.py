# print("Enter assingment")
# info={"name":"md_rashid",
#       "sub":["hindi","english","math","urdu"],
#       "topic":("dic","set"),
#       "age":35,
#       "is adult":True,
#        "marks":98,}
# print(info)
# print(type(info))
# print(info["name"])
# print(info["topic"])
# print(info["age"])
# print(info["marks"])
# info["name"]="shar"#change name update
# info["age"]="22"#update age
# info["marks"]=88
# print(info)

# null_dict={}
# null_dict["name"]="raaj"
# print(null_dict)

# student={"name":"raaaz",
#          "sub":{"hindi":99,
#                 "urdu":89,
#                 "math":78,
#                 }}

# student1={"name":"raas",
#          "sub":{"hindi":72,
#                 "urdu":80,
#                 "math":79,
#                 }}
# a=student.keys()
# b=student.values()
# c=student.get("sub")#returm to specific value
# print(student["sub"])#print value
# print(student["sub"]["urdu"])
#student.update({"city":"hyd", "name":"rashid","age":99,})#add specific items and update multiplekey vale pair
#remove_age=student.pop("age")#remove age specifiec item
# remove_item=student.popitem()#remove last item like subject 
# print(student)
# a=remove_item=student.popitem()#remove form front
# n=student["name"]
# s=student["sub"]
# print(n)
# student.update({"marks":10000,})
# print(student)
# a=student.update({"city":"hyud","marks":{"teli":83,}})
# print(student)
# student.clear()#clear dict
# print(student)
# value_list=student.values()
# print(value_list)
# item_list=student.items()
# print(item_list)
# user_copy=student.copy()
# print(user_copy)#create shallow capy
# merged_dict=student=student|student1
# print(merged_dict)#update with new value dictionary1(student1)
# merged_dic={**student,**student1}
# print(merged_dic)


# #set
# numbers={1,2,3,4,5,6}#set of integer
# mixed={1,"hello",3.14,True}#mixed data type
# print(mixed)
# #set methods-adding elements
# numbers.add(6)#add single element
# print(numbers)
# numbers.update([7,8,9,10])#add multiple elements
# print(numbers)
# numbers.remove(5)#remove single elements and error if element no found
# print(numbers)
# numbers.discard(10)#remove single elements and no error if elements not found
# print(numbers)
# poped=numbers.pop()#remove and return random elements
# print(print)
# numbers.clear()
# print(numbers)
# student={"name":"raaaz",
#          "sub":{"hindi":99,
#                 "urdu":89,
#                 "math":78,
#                 }}
# # b=student.values()
# # pair=(student.items())

# # print(pair[1])

# marks={}
# x=int(input("enter phy val:"))
# marks.update({"phy":x})
# x=int(input("enter math val:"))
# marks.update({"math":x})
# x=int(input("enter chem val:"))
# marks.update({"chem":x})
# print(marks)

# students=["md",99,"delhi"]
# str="hello"
# print(str[1])
# str[1]="o"
# print(students)
# student={"name":"raaaz",
#          "sub":{"hindi":99,
#                 "urdu":89,
#                 "math":78,
#                 }}


# #1 list inside list
# fruits=["jace","apple"],
#         ["orange","kiwi"],
#         ["dragon","grapes"]
        
# fruits[0].append("fruit")
# print(fruits)
# a=fruits[1:2][0][1][-2]
# print(a)

# #tuple oinside a list
# stidemt =[("alice",23,("bob",21))]
# print(studemt[1.pop()])#erroe

# #list inside tuple g
# grup={[10,20],[30,40]}
# print(int(str(grup[1][-2].replace9(3,2)))
      
#       #tuple inside list  list inside tple
#       ptirny(studenty[0].get("markds","40"))
#        )
# print(student[0].updat({"markds":len(student[1])}))


# #creation
# a={}
# person={"name":"alex", "age":25,}
# a=person["name"]
# b=person.get("address","hyd")
# print(a,b)

# #modification
# person["age"]=355
# person.update({"age":35,"address":"hyderabad"})
# print(person)

# # ATM SYSTEM
# def check_balance(balance):
#     print(f"your current balance is {balance}")
    
# def atm():
#     balance=10000
#     print("welcome to ATM ")

# def withdraw(balance,amount):
#     if amount>balance:
#         print("insufficient balnce")
#     else:
#         balance=balance-amount
#         print(f"withdraw successful and new balance : Rupees{balance}")
# def deposit(balance, amount):
#     balnce=balnce+amount
#     print(f"deposit successful and new balance: rupees{balance}")
#     return balance
    
# while True:
#         print("\n choice option")
#         print("1 check balance")
#         print("2 withdraw money")
#         print("3 deposit money")
#         print("4 exit")
        
#         choice=input("enter your choice(1-4)")
        
#         if choice=="1":
#             check_balance(balance)
#         elif choice=="2":
#             amount=float(input("enter enter amount of withdraw rupees"))
#             balnce=withdraw(balance,amount)
#         elif choice=="3":
#             amount=float(input("enter amount to deposit rupees"))
#             balnce=deposit(balance,amount)
#         elif choice=="4":
#             print("exit")
#             break
#         else:
#             print("invalid choice")
            
# atm()
        
        
#----------------------------------------------------------------------------
#define the menu of restuarant
# menu={
#     'Pizza':40,
#     'Pasta':50,
#     'Burger':60,
#     'Salad':70,
#     'Coffee':80,  
# }
# # print(menu)
# print("Welcome to Pi restuarant")
# print( "Pizza:RS40 \n Pasta:RS50\n Burger:RS60\n Salad:RS70\n Coffee:80")

# order_total=0
# item_1=input("Enter the name of order you want to order=")
# if item_1 in menu:
#     order_total+=menu[item_1]#0+50
#     print(f"your item{item_1}has been added in your order")
# else:
#     # print("please order something else we can serve you")
#     print(f"order item {item_1}is not available yet")

# another_order=input("do you want to another item? (yes/no)")
# if another_order=="yes":
#     item_2=input("enter the name of second item")
#     if item_2 in menu:
#         order_total+=menu[item_2]
#         print(f"itme{item_2}has been addded to order")
#     else:
#         print(f"order{item_2}not available")
# print(f"total amount of item is to pay{order_total}")




#---------------------------------------------------------------
# password generator

import random
import string 
def generate_password(min_length,numbers=True,special_character=True):
    #generate_password(10,False,False)
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    # print(letters,digits,special)
    character=letters
    if numbers:
        character+=digits
    if special_character:
        character+=special
    pwd=""
    meet_criteria=False
    has_number=False
    has_special=False
    
    while not meet_criteria or len(pwd)< min_length:
        new_char=random.choice(character)
        pwd+= new_char
        
        if new_char in digits:
            has_number=True
        elif new_char in special:
            
        

generate_password(10)
    
    

        
        




