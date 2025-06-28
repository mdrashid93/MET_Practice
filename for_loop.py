# # for loop in python
# names=["jas","raj","shaan"]
# for name in names:
#     print(name)
# #
# names=["md","rashid","raj"]
# for name in names:
#     print(name)
#     if name=="rashid":
#         print("hey, its me")
# #
# numbers=[2,3,5,-2,10]
# for number in numbers:
#     square= number**2 #square
#     print(square)
# for i in numbers:
#     cube=i**3# cube
#     print(square)
# #
# squares=[]
# for i in numbers:
#     square=i**2
#     squares.append(square)
#     print(square,end=" ")
# #
# for i in range(5,10):
#     print(i)
# for i in range(1,10,3):
#     print(i)
# #
# count=5
# while count>0:
#     if count ==3:
#         pass
#     else:
#         print(count)
#     count-=1
# #
# for i in range(5):
#     if i==3:
#         break#012
#     print(i)
# # #
# for i in range(11):
#     if i==9:
#         continue
#     print(i)
# #
# count=15
# while count>0:
#     if count ==8:
#         continue
#     else:
#         print(count)  
#     count -=1
# #
# while True:
#     user_input=input("enter exit to stop")
#     if user_input=="exit":
#         print("conngrats! you guesed it rigt")
#         break
#     print("sorry, you entered:", user_input)

# count=1
# while count<6:
#     print(count,end=" ")
#     count+=1
# #9 Write a program using while loop that counts down from 10 to 1, but skips number 5 using continue.
# count=10
# while count >0:
#     if count==5:
#         continue
#     print(count)
#     count-=1
# #10. Write a function that asks for user input using input() inside a while loop until a valid age (>0) is entered, then returns the age.
# def user_input(input):
#     a=input("enter your valid age")
    
#     b=a
#     while i in a>=b:
#         c=age<0
#         b=input
#         if age<0:
#             print("you are invalid")
#             return b
# d=user_input()
            
# i=0
# while True:
#     print("hello")
#     i+=1
#     if i==4:
#         break
    
# i=0
# while i+10 <6:
#     i+=1
#     print(i)
    
# else:
#     print(" i is no more greater than 6")
    
# i=0
# while i <6:
#     i+=1
#     print(i)
#     if i==4:
#         break
    
# else:
#     print(" i is no more greater than 6")
    
    
# i=0
# while i <6:
#     i+=1
#     print(f"{i}all email sent!!!")
     
# else:
#     print(" all email sent")

    
    
# i=0
# while i <6:
#     i+=1
#     print(f"{i}all email sent!!!")
#     if i==4:
#       break
# else:
#     print(" all email sent")

# for loop
# fruits=[ "apple","banaana","cherry"]
# for fruit in fruits:
#     print(fruit)
    
# fruits=[ "apple","banaana","cherry"]
# for fruit in fruits:
#     print(fruit[0])#abc

# name="rashid"
# for character in name:
#     print(character)


# name="rashid"
# for character in name:
#     print(character)
# print(character)#rashidd

# details={
#      "name":"md rashid",
#      "age":50
# }
# for item in details:
#     print(item)# name , age

# details={
#      "name":"md rashid",
#      "age":50
# }
# for item in details:
#     print(details[item])# md rashid, 50
    
# details={
#      "name":"md rashid",
#      "age":50
# }
# for item in details.values():
#     print(item)# md rashid, 50
    
    
# details={
#      "name":"md rashid",
#      "age":50
# }
# for item in details.items():
#     print(item)# (name, mdrashid, age,50)
    
# vowels=['a','e','i','i','o','u']
# vowels_count=0
# sentence= input("enter a sentence")
# for character in sentence:
#     if character in vowels:
#         vowels_count+=1
# print(f"vowel count:{vowels_count}")

# vovel=['a','e','i','i','o','u']
# vowe=0
# sen=input("enter sentence")
# for char in sen:
#     if char in vovel:
#         vovel +=1
# print(f" cout:{vowe}")

# password criteria
# one uppercase,one lowercase,one special charter,one number
# def validate_password(password):
#     pass
# password=input("enter your pas")
# result=validate_password(password)
# if result:
#     print("strong password")
# else:
#     print("weak password")
     



# def validate_password(password):
#     return True#,false
# password=input("enter your pas")
# result=validate_password(password)
# if result:
#     print("strong password")
# else:
#     print("weak password")

# def validate_password(password):
#     is_number=False
#     is_uppercase=False
#     is_lowercase=False
#     is_special=False
#     for character in password:
#         if character.isupper():
#             is_uppercase=True
#         elif character.islower():
#             is_lowercase=True
#         elif character.isdigit():
#             is_number=True
#         elif character in string.punctuation:
#             is_special=True
#     return is_uppercase and is_lowercase and is_number and is_special
# password=input("enter your pas")
# result=validate_password(password)
# if result:
#     print("strong password")
# else:
#     print("weak password")
         

# students=[
#     {
#         "name":"md",
#         "age":50 
#     },
#     {
#         "name":"raj",
#           "age":60       
#     },  
#     {
#         "name":"ras",
#         "age":80
#     }
# ]
# for details in students:
#     print(students)

# for details in students:
#     print(details.get("name"))#md raj ras


# students=[
#     {
#         "name":"md",
#         "mark":50 
#     },
#     {
#         "name":"ran",
#           "mark":60       
#     },  
#     {
#         "name":"ras",
#         "mark":80
#     }
# ]
# for details in students:
#      print(details.get("name"))
# for details in students:
#     name=details.get("name")
#     mark=details.get("mark")
#     if mark >50:
#         print(f"{name}pass")
#     else:
#         print(f"{name}fail")
            
 # for details in students:
#     i = details.get("mark")
#     if i >50:
#         print("pass")
#     else:
#         print("fail")

#

# remove duplicate from the list
#fruits=["apple","banana","cherry","apple","banana"]
#duplicate=[]
#for f in fruits:
# def remove_duplicate(lst):
#     unique=[]
#     seen=set()
#     for i in lst:
#         if i not in seen:
#             unique.append(i)
#             seen.add(i)
#     return unique
# print(remove_duplicate(fruits))

# def remove_duplicat(fruits):
#     unique=[]
#     seen=set()
#     for fruit in fruits:
#         if fruit not in seen:
#             unique.append(fruit)
#             seen.add(fruit)
#     return unique
# print(remove_duplicate(fruits))

# without seen but not good for large dataset
# def remove_duplica(fruits):
#     unique=[]
#     for fruit in fruits:
#         if fruit not in unique:
#             unique.append(fruit)
#     return unique
# print(remove_duplica(fruits))
#print(list(set(fruits)))
  
  
# find the index of element in tuple
# my_tuple=(1,2,3,4)     

# def find_index(tuple,element):
#     return tuple.index(element) if element in tuple else -1 
# print(find_index(my_tuple,20))    
        
        
# find the most frequent value in dictionary:-
# data={'a':1,'b':2,'c':1,'d':3,'e':1}
# def most_frequent(dct):
#     frequency={}
#     for value in dct.values():
#         if value not in frequency:
#             frequency[value]=0
#         frequency[value]+=1
#     max_value=max(frequency, key=frequency.get)
#     return max_value
# print(most_frequent(data))


#1 Write a for loop that prints numbers from 1 to 5 using range().
#number=[1,2,3,4,5]
# for a in number :
#     print(a, number) 
#     a+=1    
# num=0
# for a in num:
#     if num<=-10:
#      print(a,num)
#     a+=1
    
# for a in range(1,11):
#     if a==8:
#         continue
#     print(a,"i love you")

#2. Use a for loop with range() to print all even numbers between 10 and 20.

# for a in range(10,22):
#     if a%2==0:
#         print(a)
#3.Ask the user for 3 names using input() in a loop. Store them in a list and print the list.
# b=[user_input=input("enter your name1")
# user_input=input("enter your name2")
# user_input=input("enter your name3")]
# loop=[]
# leap=[]
# for a in b:             this is wrong code
#     if b in loop:
#         loop.append(b)
    
#     else:
#         print("false")

# names = []

# for i in range(3):
#     name = input(f"Enter name {i + 1}: ")
#     names.append(name)

# print("The list of names is:", names)

# named=[]
# for name in range(5):
#     name=input(f"enter your name{name+1}:")
#     named.append(name)
# print("this list of named is :",named)
 
 
# names=[]
# for i in range(8):
#     name=input(f"enter name{i+1}:")
#     names.append(name)
#     print("the name",names)

#4. Given a list of numbers, use a for loop to print the square of each number.
# numbers=[1,2,3,4,5,6,7,8,9]
# for num in numbers:
#     num+=0
#     print(num,num*num)

#5. Loop through a list of dictionaries with keys 'name' and 'age'. Print each name and age
# people = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 30},
#     {'name': 'Charlie', 'age': 22}
# ]

# # for person in people:
# #     print(f"Name: {person['name']}, Age: {person['age']}")
# for person in people:
#     print(f"name:{person['name']},age:{person['age']}")

#6. Given a nested list of fruits like [['apple', 'banana'], ['grape', 'mango']], use a for loop to print all
#fruits.
#fruits = [['apple', 'banana'], ['grape', 'mango']]

# for sublist in fruits:
#     for fruit in sublist:
#         print(fruit)
# for sublist in fruits:
#     for furit in sublist:
#         print(fruit)
# for sublist in fruits:
#     for fruit in sublist:
#         print(fruit)
#7. Write a for loop that prints characters of a string entered by the user.
# user=input("say something")
# for i in user:
#     print(i, end="")

#8. Use range() to print numbers from 5 to 1 in reverse order
# for i in range(5,0,-1):
#     print(i)
# for b in range(1000,1,-50):
#     print(b)
#9. Write a program that asks the user to input 3 subjects and 3 marks each, then print each subject
#with its mark
# subjects=[]
# 
     
# for i in range(3):
#     subject=input(f"enter your subject{i+1}:")
#     mark=input(f"enter mark for {subject}:")
#     subjects.append((subject,mark))
# print("\nsubjects and mark")
# for subject, mark in subjects():
#     print(f"{subject}:{mark}")
# subject=[]
# subject_marks={}#empty dictionary to store subject and marks
# for i in range(3):# loop to get 3 subject and their marks 
#     subject=input(f"enter the name of subject{i+1}")
#     marks=int(input(f"enter marks for {subject}: "))
#     subject_marks[subject]=marks
# #print the subject and marks
# print("\nsubjeccts and marks")
# for subject,marks in subject_marks.items():
#     print(f"{subject}:{marks}")

#10.Loop through alist of tuples containing(product,price)and print 'product: price' for each.
#list of (product , price )tuples
# products=[("laptop",7500),("phone",30000),("headphone",1500)]

# #loop through the list and print each item
# for product, price in products:
#     print(f"{product}:{price}")

#11 sorting method:
# numbers=[5,2,1,9,6,3]
# numbers.sort()
# print(numbers)

#12
# sorted_numbers=sorted(numbers)
# print(sorted_numbers)
#13
# sorted(numbers,reverse=True)
# print(sorted)
# or numbers.sort(reverse=True)

# 13 total=0
# for i in range(1,6):
#     total+=i
# print(f"total:{total}")

# total=1
# for i in range(10,20):
#     total+=i
# print(f"total sum 10 to20:{total}")
#14 nested loop
# for i in range(1,5):
#     for j in range(i):
#         print("*")
#     print()

#nested loop
# for i in range(0,6):
#     for j in range(i):
#         print("#",end=" ")
#     print()

# for i in range (1,6):
#     print(f"{i} ka square:{i**2}")
#.15 shopping cart calculator
#cart = [("Apple", 30, 2), ("Banana", 10, 5), ("Mango", 50, 1)]
# total=0
# for itme, price,qty in cart:
#     total+=price*qty
# print(f"total bill:{total}")
# for itme,price,qty in cart:
#     total=qty*price
# price(f"bil:{total}")

# #16.student ke mark anlyze karna average nikalna 
# students = [("Ali", [80, 75, 90]), ("Riya", [60, 85, 88])]
# for name, marks in students:
#     avg = sum(marks) / len(marks)
#     print(f"{name} ka average: {avg:.2f}")
# for nam,mark in students:
#     av=sum(mark)/len(mark)
#     print(f"{nam}:{av:.2f}")
    
# #17.- Loop Use: Folder ke andar sabhi files ko rename karna (e.g. img1.jpg, img2.jpg, ...)

# import os

# files = os.listdir("photos")
# for i, file in enumerate(files):
# #     new_name = f"image_{i+1}.jpg"
# #     os.rename(f"photos/{file}", f"photos/{new_name}")
    
# #18.- Loop Use: Har task ke liye alert ya reminder dikhana.

# tasks = ["Email boss", "Finish project", "Call mom"]
# for i, task in enumerate(tasks, start=1):
#     print(f"Task {i}: {task}")
# # taask=["Email boss", "Finish project", "Call mom"]
# for i, task in enumerate(taask, start1=2):
#     print(f"taask{i}:{taask}")

# #19.- Loop Use: Questions loop mein poochhna, score track karna.

# quiz = [("Capital of India?", "Delhi"), ("2 + 2?", "4")]
# score = 0
# for q, a in quiz:
#     ans = input(q + " ")
#     if ans.lower() == a.lower():
#         score += 1
# print(f"You scored {score}/{len(quiz)}")

# #201. ATM Simulator
# #Purpose: User se input lena jaise balance check, deposit, withdrawal.
# #Loop Use: Tab tak options dikhana jab tak user exit nahi karta.

# balance = 1000

# while True:
#     print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
#     choice = input("Choose option: ")

#     if choice == '1':
#         print(f"Balance: ₹{balance}")
#     elif choice == '2':
#         amt = int(input("Enter deposit amount: "))
#         balance += amt
#         print("Amount deposited.")
#     elif choice == '3':
#         amt = int(input("Enter withdrawal amount: "))
#         if amt <= balance:
#             balance -= amt
#             print("Amount withdrawn.")
#         else:
#             print("Insufficient balance.")
#     elif choice == '4':
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid option.")
        
        
# #21📈 3. Expense Tracker App
# #Purpose: Har din ke kharche track karna, aur month-end par total ya category-wise breakup dekhna.
# #Loop Use: User ke entered expenses ko process karna aur total calculate karna.


# expenses = []

# while True:
#     item = input("Enter expense item (or 'done' to finish): ")
#     if item.lower() == 'done':
#         break
#     amount = float(input("Amount spent: "))
#     expenses.append((item, amount))

# print("\nYour Expenses:")
# total = 0
# for item, amount in expenses:
#     print(f"{item}: ₹{amount}")
#     total += amount
# print(f"Total Spent: ₹{total}")

# #22

# #📈 3. Expense Tracker App
# # Purpose: Har din ke kharche track karna, aur month-end par total ya category-wise breakup dekhna.
# # Loop Use: User ke entered expenses ko process karna aur total calculate karna.
# import time

# seconds = int(input("Enter countdown time in seconds: "))
# for i in range(seconds, 0, -1):
#     print(f"Time left: {i} sec", end="\r")
#     time.sleep(1)
# print("\nTime’s up! Take a break or switch task. ✅")

# balance=1000
# while True:print("\n1.check balance\n2.deposit\n3.withdraw.\n4 exit")
# choice=input("choose option:")

# if choice=="1":
#     print(f"balance:{balance}")
# elif choice=="2":
#     amt=int(input("enter deposit amount:"))
#     balance+=amt
#     print("amount deposited.")
# elif choice=="3":
#     amt=int(int("enter withdral amount:"))
#     if amt<=balance:
#         balance-=amt
#         print("amount withdrawn.")
#     else:
#         print("insufficient balance.")
# elif choice =="4":
#     print("goodbye!")
#     break
    
# else:
#     print("invalid option")
 
        
        
        
# def show_menu():
#     print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")

# def check_balance(balance):
#     print(f"Balance: ₹{balance}")
#     return balance

# def deposit(balance):
#     try:
#         amt = int(input("Enter deposit amount: "))
#         if amt <= 0:
#             print("Amount must be greater than 0.")
#         else:
#             balance += amt
#             print("Amount deposited.")
#     except ValueError:
#         print("Please enter a valid number.")
#     return balance

# def withdraw(balance):
#     try:
#         amt = int(input("Enter withdrawal amount: "))
#         if amt <= 0:
#             print("Amount must be greater than 0.")
#         elif amt <= balance:
#             balance -= amt
#             print("Amount withdrawn.")
#         else:
#             print("Insufficient balance.")
#     except ValueError:
#         print("Please enter a valid number.")
#     return balance

# 🔸 Main Program Loop
balance = 1000

# while True:
#     show_menu()
#     choice = input("Choose option: ")

#     if choice == '1':
#         balance = check_balance(balance)
#     elif choice == '2':
#         balance = deposit(balance)
#     elif choice == '3':
#         balance = withdraw(balance)
#     elif choice == '4':
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid option.")