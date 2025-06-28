#function :store and reused steps
# inbuilt function these all are:
# function all will start with def
# built in function int(), print(), input(),type(), float()
# a function takes some input and produce some an output
# big=max("helloworld")
# print(big)
# def max(inp):
#     blah
#     blah
#     for x in input
#     blah
#     blah
    
# #building our own function
# we create a new function using def keyword followed by optional parameter in paranthesis
# we indent the body of the function
# this define the function but don t execute the body of the function
 
# def print lyrics()
#     print("i am anything")
#     print("i am sleeping all ")

# x=5
# print("hello")
# def print_lyrics():
#     print("i am sleeping")
#     print("i am working all day")#  output hello, yo , 7
# print("yo")
# x=x+2
# print(x)

#defination and uses :
# Once we have define a function we can call or provoke it as many time as we like
# this is the store and reuse the pattern

#arguments is a value we pass into the function as its input  when we call the function
#we use argument so we can direct the function to do different kinds of work when we call it at diffrent times
#we put the argument  in the parenthesis after the names  of the function 

# def greet():
#     print("hello")
#     print("i missed you")

# greet()

# greet()

# def add(x,y):
#     a=x+y
#     print(a)
    
# add(10,20)

# def sub(x,y):
#     a=x-y
#     print(a)
# sub(20,10)
# sub(99,1)
# sub(88,8)

# def add(m,n):
#     o=m+n
#     return o
# add(7,8)

# #sample of function:
# def function():
#     a=functionbody
#     print(a)#or return a
# function()
    
    
# def function():
#     print("md")
#     print("rashid")
# function()
# function()
# function()

# def lyrics():
#     print("md")
#     print("rashid")
# lyrics()

# def add(x1,x2,x3,x4):
#     a=(x1+x2+x3+x4)
#     return a
# add(10,20,30,40)




#1. Write a function called greet_user that takes a named argument 'name' and returns 'Hello,{name}!
# def greet(name):
#     print("name)"
# greet(name,"mdrashid")
# print

# def greet_user(name):
    
# def greet_user(name):
#     return f"Hello, {name}!"
# print(greet_user(name="mdrashid"))

# def add(x1,x2,x3,x4):
#     a=(x1+x2+x3+x4)
#     print(a)

# add(10,20,30,40)

# def add(x,y):
#      c=x+y
#      return c      error
# result=add(5,4)
# print(result1)   error
 
# def add_sub(x,y):
#     c=x+y
#     d=x-y
#     return c,d
# result1,result2=add_sub(5,4)
# print(result1,result2)

# def update(x):
#     x=8
#     print("x",x)
    
# a=10
# print(id(a)) 
# update(a)# 8 update the value with older value of 10 
# print("a",a)


# def update(x):
#     x=9
#     print(x)
# update(11)

# def update(lst):
#     print(id(lst))
#     lst[1]=25
#     print(id(last))
#     print("x",lst)
# lst=[10,20,30]
# print(id(lst))
# update=(lst)
# print("lst",lst)


#actual argument  four type
# position
#keyword
#default
#variable length
# def person(name,age):
#     print(name)#keyword
#     print(age)
# person(age=20,name="md")


# def person (name, age=20):
#     print(name)   #default
#     print(age)
# person("md",30)

# def sum(a,*b): #  *b means multiple value can take 
#     print(a)
#     print(b)
# sum(5,6,34,78) #

# def sum(*b):
#     c=0
#     for i in b:
#         c=c+i # variable length argument
#     print(c)
# sum(5,6,34,78)#123


# def person(name,**data):
#     print(name)    #keyword variable length argument
#     print(data)
    
    
# person(name="md",city="mubai",mob=9347,age=12)

# def person(name,**data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)
# person("madrashid",age=20,city="hyd",mob=9347)

#  

# def cal_product(a=2,b=3):
#     print(a*b)
#     return a*b
# cal_product()

# def prod(a, b=2):
#     print(a*b)
#     return a*b
# prod(4) 

#waf print the len of list(list in the parameter)
# cities=["delhi","gurgao","puna","mumbai","pune",]
# heroes=["sal","leela","zayn","varun","srk","neli"]
# def print_len(list):
#     print(len(list))
# print_len(cities)
# print_len(heroes)

# #waf to print the element of list in single line (list in the parameter)
# cities=["delhi","gurgao","puna","mumbai","pune",]
# heroes=["sal","leela","zayn","varun","srk","neli"]
# print(heroes[0], end=" ")
# print(heroes[1], end=" ")

# def print_len(list):
#     print(len(list))
    
# print_len(cities)
# print_len(heroes)

# def printlen(list):
#     for item in list :
#         print(item, end=" ")
        
# printlen(heroes)


# def printle(list):
#     for item in list:
#         print(item, end="  ")
# printle(cities)

#waf a function to write a factorial of n(n in the parameter)
#4! four factorial 4*3*2*1
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     print(fact)
    
# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# cal_fact(5)
# cal_fact(6)
# cal_fact(7)
# cal_fact(8)
# cal_fact(9)
# cal_fact(10)

# #waf conver usd to ind
# def converter(usd_val):
#     inr_val=usd_val*83
#     print(usd_val,"usd=",inr_val,"inr")
    
# converter(2)

#take input if number odd print odd , if number even print even
# x=5
# print("hello")
# def print_lyrics():
#     print("i am sleeping")
#     print("i am working all day")#  output hello, yo , 7
# print("yo")
# x=x+2
# print(x)

#1. Write a function called greet_user that takes a named argument 'name' and returns 'Hello,{name}
# def greet_user_name():
#     return f"hello, {name}"
# message=greet_user_name(name="mdrashid")
# print(message)

#  
    
# def greet_user(name):
#     return f"Hello, {name}"

# message = greet_user(name="Rashid")
# print(message)

# def user(name):
#     return "hello",name
# a=user(name="md")
# print(a)

# def names(name):
#     return name
# a=names(name="ras")
# print(a)


# def multi(a,b):
#     return a*b
# c=multi(2,4)
# print(c)
#2. Create a function 'check_temperature' that takes a named argument 'temp' and returns 'Fever' if temp > 99 else 'Normal'
# def check_temprature(fever,normal):
#     if fever>99:
#         return "fever"
#     else:
#         return "normal"
# a=check_temprature(99)
# print(a)

# def temprature():
    
    
# def sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# sum(5,10)

# def cal_temprature(*,temp):
#     if cal_temprature>99:
#         print("fever")
#     else:
#         print("normal")
# a=cal_temprature(99)
# a=cal_temprature(90)
# print(a)

# def calc_sum(a,b):
#     return a+b
# a=calc_sum(1,2)
# print(a)

# def sum(v,w):
#     return(v+w)
# a=sum(1,2)
# print(a)

#3. Define a function 'get_last_fruit' that takes a list of fruits as input and returns the last fruit.
# fruits=["mango","banana","apple","kiwi"]

# def get_last_fruit(fruits):
#     #print(fruits[-1])
#     return fruits[-1]
# print(get_last_fruit(fruits))


# cities=["delhi","mumbai","pune","hyd"]
# heros=["sal","srk","allu"]
# def print_len(list):
#     print(len(list))

# print_len(cities)
    






# def cal_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg

# cal_avg(1,2,3)
#waf to find the factorial of n(n is the parameter)

# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     print(fact)
    
# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#         print(fact)
# cal_fact(5)    

#3. Define a function 'get_last_fruit' that takes a list of fruits as input and returns the last fruit
#fruits=["banana","apple","grapes","oange"]

# def get_last_fruit(fruits):
#     print(fruits[-1])
#     return fruits[-1]
# fruits=["banana","apple","grapes","oange"]
# #print(get_last_fruit(fruits))

# def get_last_fruits(fruits):
#     return fruits[-1]
# print(get_last_fruits(fruits))

#4 Create a function 'get_price_tag' that takes a 'price' and returns 'Expensive' if price > 1000 else "affordable"
# def get_price_tag(price):
#     if price >1000:
#         return "expensive"
#     else:
#         return "affordable"

# print(get_price_tag(100))
# print(get_price_tag(2000))

# def get(price):
#     if price >1000:
#         return "expensive"
#     else:
#         return "cheaper"
# print(get(200))
# print(get(2000))

#5 wite a function 'format_user_info' that takes name and age as keyword arguments and returns a formatted string using f-string.
# def user_info(name,age):
#     arguments=name,age
#     return f"name{md}&{"
# print(user_info("md","rash"))

# def format_user_info(name, age):
#     return f"Name: {name}, Age: {age}"
# print(format_user_info(name="Rashid", age=25))
# Output: Name: Rashid, Age: 25
# def formt_user(name,age):
#     return f"name:{name},age:{age}"
# print(formt_user(name="rashid",age=20))

#6 Define a function 'uppercase_if_string' that takes one argument and returns it in uppercase if it's a
#string, else return 'Invalid input'.
# def lower_to_upper(text):
#     return text.upper()

# sentence="i am going to bihar"
# print(lower_to_upper(sentence))    

# def lower_to_upper(t):
#     return t.upper()

# sentence="im back"
# print(lower_to_upper(sentence)) 

# def upper_to_lower(t):
#     return t.lower()

# sentence="I AM GOING TO BIHAR"
# print(upper_to_lower(sentence)) 

#7. Write a function 'safe_divide' that takes two numbers as keyword arguments 'num' and 'den'.
#Return the result if den is not 0, else return 'Cannot divide'
# def safe_divide(*,num,den):
#     if den!=0:
#         return num/den
#     else:
#         return "cannot drive"
# print(safe_divide(num=10, den=2))
# print(safe_divide(num=5, den=0))


# def add2numbers(number1,number2):
#     result=number1+number2
#     print("the sum is ", result)
    
# add2numbers(10,20)#argument10,20 

# default arguments
# def greetings(name="world"):
#     print("hello",name,"!")

#8. Write a function 'check_login' that takes a dictionary with 'username' and 'password'. Return
#'Login successful' if password is not empty.
#def check_login(username,password):

# def check_login(login_data):
#     if login_data.get('password'):
#         return "Login successful"
#     else:
#         return "Login failed"

# print(check_login({'username': 'rashid', 'password': '1234'}))  # ✅ Login successful
# print(check_login({'username': 'rashid', 'password': ''}))      # ❌ Login failed


# def check_login(credentials):
#     try:
#         if credentials['password']:
#             return "Login successful"
#         else:
#             return "Login failed"
#     except KeyError:
#         return "Login failed"



# greetings() # runs wihtout error using defualt value

# def goodmorning(name="good"):
#     print("moring",name)

# goodmorning()
# goodmorning("rashid")

# #arbitary positional arguments
# def add2numbers(a,b):
#     return a+b

# result=add2numbers(10,20)
# print(result)

# def addnumbers(*args):# stores arguments as tuples
#     print(type(args))
#     return sum(args)
# a=addnumbers(10,20,30,40,50)
# print(a)

# def greetings2(*names):
#     for name in names:
#         print(f"hello,{name}!")
# greetings2("md_rashid","monu")

# #arbitrary keyword arguments(**kwargs)
# #store arguments as a dictionary
# def print_details(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")

# print_details(name="d_rashid",age=22, city="bihar")

# def square(a):
#     return a*a
# result=square(5)
# print(result)

# #anonymous function
# f=lambda a,b :a+b
# result=f(5,6)
# print(result)

#even numbers filter###
# def is_even(n):
#     return n%2==0
# nums=[3,2,4,9,7,6,8,12]
# evens=list(filter(is_even,nums))
# print(evens)

# def even_nums(i):
#     return i%2==0
# nums=[10,20,30,35,40,45,50,60,99]
# even=list(filter(even_nums,nums))
# print(even)

# nun=[4,6,7,9,8,10,12,13,17,18,20]
# evo=list(filter(lambda n:n%2==0 ,nun))
# print(evo)

#map
# nums=[3,2,6,8,4,6,2,9]
# even=(list(filter(lambda n:n%2==0,nums)))

# doublees=list(map(lambda n:n*2,even))
# print(doublees)

#9. Create a function 'get_full_name' that takes 'first' and 'last' as named arguments and returns full name in title case.

# def full_name_name(first,last):
#     return full_name_name.title()
# result=full_name_name("titlecase" rashid)
# print(get_full_name(first="john", last="doe"))
# print(result)

 
# def full_name(first,last):
#     name=f"{first}{last}"
#     return name.title()
# print(full_name(first="md", last="rashid"))

#10. Write a function 'get_discounted_price' that takes 'price' and 'is_member'. If is_member is True,return price * 0.9 else return price.
# def get_discounted_price(price,is_member):
#     if is_member :
#         return price *0.9
#     else:
#         return price
    
# print(get_discounted_price(1000,True))
# print(get_discounted_price(1000,False))

#1. Write a function that accepts any number of numbers using *args and returns the sum of all numbers
# def numbers(*args):
#     total=args
#     args=(10+20+30+40)
#     return args
# sum=numbers(10,20,30,40)
# print(sum)

#2. Create a function that accepts any number of keyword arguments (**kwargs) and returns a string of all keys joined by commas.
# def get_keys_string(**kwargs):
#     return " ,".join(kwargs.keys())
# result=get_keys_string(Name="md_rashid",age=20,country="india")
# print(result)

# def get_key_value_string(**kwargs):
#     return",".join(f"{key}={value}"for key,value in kwargs.items())
# result=get_key_value_string(name="MD_RASHID",AGE=33,CITY="punjab")
# print(result)
#3. Write a program that keeps asking for input using input() until the user types 'exit'. Print each input vlue entered.
# def asking_value(**kwargs):
#     #kwargs=input("enter your value")
#     return ",".join(kwargs.value())
# result=asking_value(name="md",age=63,city="kolkata")
# print(result)
# while True:
#     user_input=input("enter something (type exit to quit)")
#     if user_input=="exit":
#         break
#     print("you enter :",user_input)
    
#4. Write a while loop that prints numbers starting from 1. Break the loop if the number reaches 5.
# a=1
# while a <6:
#     print(a)
#     a+=1
# while a<10:
#     print(a,end="$")
#     a+=2
#5 Write a while loop that asks the user to enter a number. If the number is negative, use continue to
#ask again. Stop when a positive number is entered.\
# while True:
#     num=int(input("enter a number:"))
#     if num <0:
#         continue#skip to next loop iteration
#     break# stop the loop if num is positive
# print("enter positive number")
#6.create a function that takes *args and returns the largest value without using max(). Use a while
#loop to find the largest.
# def find_largest(*args):
#     if not args:
#         return None#retrun none if no arguments are given 
#     i=1
#     largest=args[0]
#     while i<len(args):
#         if args[i]>largest:
#             largest=args[i]
#         i+=1
#     return largest
# print(find_largest(10,80,90,30,60,))


# def find_largest(*args):
#     largest = args[0]
#     i = 1
#     while i < len(args):
#         if args[i] > largest:
#             largest = args[i]
#         i += 1
#     return largest

# def find_larger(*args):
#     larger=args[0]
#     i=1
#     while i < len(args):
#         if args[i]>larger:
#             larger=args[i]
#             i+=1
#     return larger
# print(find_larger(3,9,5,7,6,1))

#arbitary
# def abcd(a,b=2):
#     pass
# abcd(2)
# def sdf(*as):
#     return as
# sdf(1,2)
    
# find the intersection (common elements of two list)
# list1=[1,2,3,4,5]
# list2=[4,5,6,7,8]
# #using for loop
# def intersection_loop(list1, list2):
#     common_list=[]
#     for item in list1:
#         if item in list2 and item  not in common_list:
#             common_list.append(item)
#     return common_list 
# print(intersection_loop(list1,list2))
# def intersection_comp(list1,list2):
#     return[item for item in list1 if item in list2]
# print(intersection_comp(list1,list2))
# find the most frequent element in list
# numbers=[1,2,2,3,3,3,4]
# def most_freq(ist):
#     maxcount=0 
#     most_freq=None
#     for item in ist:
#         count=ist.count(item)
#         if count>maxcount:
#             maxcount=count
#             most_freq=item 

#     return most_freq
# print(most_freq(numbers))
# numbers=[1,2,2,3,3,3,4,7,7,7,7]
# def mos_freq(list):
#     max=0
#     mos_freq=None
#     for item in list:
#         count=list.count(item)
#         if count>max:
#             max=count
#             mos_freq=item
#     return mos_freq
# print(mos_freq(numbers)) 

#10. Write a function that asks for user input using input() inside a while loop until a valid age (>0) is entered, then returns the age.
# def valid_age():
#     while True:
#         try:
#             age=int(input("enter your age"))
#             if age>0:
#                 return 0
#             else:
#                 print("age must be greater than 0 try again")
#         except ValueError:
#             print("invalid input please enter your number")
# get_valid_age=valid_age()
# print(f"your age is:{valid_age}")

# find common ele in list
# list1=[1,2,3,4,5]
# list2=[4,5,6,7,8]
# def intersection_loop(list1,list2):
#     common_list=[]
#     for item in list1:
#         if item in list2 and item not in common_list:
#             common_list.append(item)
#     return common_list
# print(intersection_loop(list1,list2))
# #using list comprehension
# def comprehension(list1,list2):
#     return[item for item in list1 if item in list2]
# print(comprehension(list1,list2)) 

# # find the most frequent element in a list
# numbers=[1,2,3,4,4,6,6,6]
# def freq(list):
#     max_count=0
#     freq=None
#     for item in list:
#         count=list.count(item)
#         if count>max_count:
#             max_count=count
#             freq=item
#     return freq
# print(freq(numbers))

# find cumulative sum of a list
number=[1,2,3,4,5]
# def cumulative_sum():
#     cum_sum=[]
#     total=0
#     for num in list:
#         total+=num
#         cum_sum.append(total)
#     return cum_sum

# def cum(list):
#     sum=[]
#     totl=0
#     for num in list:
#         totl+=num
#         sum.append(totl)
#     return sum
# print=(cum(number))
# remove duplicate from list
# fruits=["apple","banana","kela","seb","mango","aam","apple","kela","banana"]
# def remove_ele(list):
#     remove=[]
#     seen=set()
#     for item in list:
#         if item not in seen:
#             remove.append(item)
#             seen.add(item)
#     return remove
# print=(remove_ele(fruits))

# numbers=[1,2,3,3,3,4,4,5]
# def frequent(numbers):git
#     max_count=0
#     frequent=None
#     for number in numbers:
#         count=list.count(number)
#         if count> maxcount:
#             maxcount=count
#             frequent=number
#     return frequent
# print(frequent(numbers))
# num=[1,2,3,4,5]
# def cumulative_sum(lost):
#     cum_sum=[]
#     total=0
#     for num in lost:
#         total+=1
#         cum_sum.append(total)
#     return cum_sum
# print(cumulative_sum(num)) 

#function to convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
#call function
celsius_to_fahrenheit(50)
