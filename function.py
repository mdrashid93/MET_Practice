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
 
