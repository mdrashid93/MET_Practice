#1. IF
# if True:
#     print("works")

#2. IF ELSE
# if True:
#     print("One")
# else:
#     print("two")

#3. IF-ELIF-ELSE
# a, b = 1, 3
# if a > b:
#     print("One")
# elif a == b:
#     print("Two")
# else:
#     print("Done")

#4. IF-ELIF
# a, b = 1, 3
# if a<b:
#     print("one")
# elif b>a:
#     print("Two")


#1. Check if it is a valid combo
#2. For every if, else, elif block, indentation must be at same level
#3. At any point, only block will be executed in a given combo


# a, b, c = 1, 2, 3

# if b > c:
#     print("Hello")
# elif c > b:
#     print("Hello 1")
#     if b > a:
#         print("Hello 2")
#         print("Hello 3")
#     elif c > a:
#         print("Hello 4")
#         print("Hello 5")
#     else:
#         print('No Hello')
# else:
#     print("Not Hello")
    
    
# practice module 2:
#loop
# total_bill=250
# print("receive google paymenet")
# print("receive pay phone ")
 
# a=3
# if True:
#      print(a)
     
# if False:
# #     print(a)#didnot see anything, if it is false it is not going to inside and not execute , it true then go inside and execute
#      print(a+1)
#      print(a+2)
#      print(a+3)
# print(a+3) #6

# choice=input("choose gateway:")
# total_bill=250
# if True:
#     print("receved payment")

# choice=input("choice gateway ")
# total_bill=250
# if choice=="phonepay":
#     print("receving payment phonepay")
# else:
#     print("receing payment googlepay")

# elif choice ==  "gpay":                # when u chose if u have to make single decision and when u choose elif u have double decision
#     print("receving payment of gpay")
# elif choice == "credits":
#     print("credit card payment")
    
# else:#by default
#     print("not supported")

# #1 if 
# if True:
#     print("work")

# #2 if else
# if True:
#     print("one")
# else:
#     ("two")
    
#3 if elif else
# a,b=1,2
# if a>b:
#     print("one")
# elif a==b:
#     print("two")
# else:
#     print("done")

# a,b=10,20
# if b<a:
#     print("a") 
# elif a==b:
#     print("b")
# elif a<b:
#     print("c")#c
# else:
#     print("c")
  
  
  
#a<b,b>a=a less than b, b greater than a
  

#4 if-elif
# a,b=1,3
# if a<b:# A less than B
#     print("one")#one
# elif b>a:# B greater than A
#     print("too")
    
# a=2
# if a>0:
#     print("one")
#     print("two")
#     print("three")
#     print("four")
#     if a>2:
#         print("one")
#     elif b>a:
#         print("two") 
        
        
# a=-1
# if a>0:
#     print("one")
#     print("two")
#     print("three")
#     print("four")
#     if a>2:
#         print("one")
#     elif b>a:
#         print("two") 
# print("done with flow")


# #check if it is valid combo
# #for every if , else, elif block indentation must be same level
# #at any point only one block will be executed in given combo

# a,b,c=1,2,3
# if b>c:
#     print("hello1")
# elif c>b:
#     print("helo1")
#     print("hello2")
#     if b>a:
#         print("hello2") #any given combination single block be executed it will not go any block
#         print("hello3")
#     elif c>b:
#         print("hello4")
#         print("hello5")
#     else:
#        print("no hello")
        
# else:
#     print("not hello")
    

#1 any customer will order two dishes
#2 any customer will enter quantity for each dishes
#3 calculate the total bill for the use

#1 what do u want to achieve
   ### total bill
#2 what do you need to achieve that 
   #dishes and their prices
   #what user wants
   #how many user wants
#3 arrange the order
   #dishes and their prices
   #what user wants
   #how many the user wants
#4 write the code

# menu={
#     "dosa":35,
#     "itly":45,
#     "wada":50,
#     "puri":40,
#     "upma":60,
# }
# _dish_1choices=input("what do you wants")
# _dish_1quantity=int(input("howmany")) 

# _dish_2choices=input("what do you wants")
# _dish_2quantity=int(input("howmany"))

# _total_bill=(_dish_1quantity*menu.get(_dish_1choices))+(_dish_2quantity*menu.get(_dish_2choices))
# print(f"your bill is RS{_total_bill}")
# a="hello"
# print("hello")



n=int(input("enter number of row needed"))
for i in range(n):      #row
   for j in range(i+1): #column
      print(j+1, end=" ")
   print()
   
      