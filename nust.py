# class Coffee:
#     #inititalize coffee with name and price
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

# class Order:
#     #initialize order with empty list
#     def __init__(self):
#         self.items=[]
        
#     #add coffee to order
#     def add_item(self,coffee):
#         self.itmes.append(coffee)
#         print(f"added {coffee.name} to your order")
        
#     #calculate total price
#     def total(self):
#         return sum(item.price for item in self.items)
    
#     def show_order(self):
#         if not self.items:
#             print("no item in order")
#             return
#         print("\n your order:")
#         for i, item in enumerate(self.items,1):
#             print(f"{i}.{item.name}.${item.price}")
#         print(f"Total:${self.total()}\n")
#         #handle checkout process
        
#     def checkout(self):
#         if not self.items:
#              print("your cart is empty")
#              return
#         self.show_order()
#         confirm=input( "proceed to checkout (yes/no)").strip.lower()
#         if confirm=="yes":
#             print("order confirmed thank you")
#             self.items.clear()
#         else:
#             print("checkout cancelled")
            
            
#         #display menu and handle user input
# def main():
#     menu=[
#         Coffee("espresso",2.5),
#         Coffee("lattee",3.5),
#         Coffee("cappuccino",3.0),
#         Coffee("americano",2.0)
#     ]
    
#     order=Order()
#     #user interaction
#     while True:
#         print("\n--coffee menu")
#         for i,Coffee in enumerate(menu,1):
#             print(f"{i}.{Coffee.name}-${Coffee.price}")
#         print("5.view order")
#         print("6.chekout")
#         print("7. exit")
#         choice=input ("choose opetion")
#         if choice in [1,2,3,4]:
#             order.add_item(menu[int(choice)-1])
#         elif choice=="5":
#             order.show_order()
#         elif choice=="6":
#             order.checkout()
#         elif choice=="7":
#             print("thank u for visiting")
#             break
#         else:
#             print("invalid choice try again")
#             break

# if __name__=="__main__":
#     main()
        
strings=["my","world","apple","pear"]
# lengths=map(len,strings)
# print(list(lengths))

# strings=["my","world","apple","pear"]
# lengths=map(lambda x:x+"sd",strings)
# print(list(lengths))


# def add_s(strings):
#     return strings+"s"
# lengths=map(add_s,strings)
# print(list(lengths))

# def longer_than(string):
#     return len(string)>4
# strings=["my","world","apple","pear"]
# filtered=filter(longer_than,strings)
# print(list(filtered))

# filtered=filter(lambda x:len(x)>=4,strings)
# print(list(filtered))


# def longer_than4(string):
#     return len(string)>3
# strings=["my","world","apple","pear"]
# filtered=filter(longer_than4,strings)
# print(list(filtered))


# numbers={1,4.5,5,23,2}
# # print(sum(numbers,start=-10))

# sorted_nums=sorted(numbers,reverse=True)
# print(sorted_nums)

# people=[
#     {"name":"alice","age":30},
#     {"name":"md","age":22}
# ]
# sorted_pep=sorted(people, key=lambda person:person["age"],reverse=True)
# print(sorted_pep)

# tasks=["write report","attempt meeting","review code"]
# for index in range(len(tasks)):
#     task=tasks[index]
#     print(f"{index+1}.{task}")

# for index,task in enumerate(tasks):
#     print(f"{index+1}.{task}")
# print(list(enumerate(tasks)))

# file=open("test.txt","w")
# file.write("hello world \nmy nameis md")

# def greetings(name):
#     print("hello",name,)

# greetings("md")

# def intro(course_name,instructor_name):
#     print("welcome to",course_name,"course by",instructor_name)

# intro("python","md")
# def gre(name="world"):
#     print("welcome to",name)
# gre()
# def divide(a,b):
#     return a/b
# a=divide(100,50)
# print(a)

# def multi(c,d):
#     return c*d
# multiplication=multi(4,10)
# print(multiplication)

# def add3num(a,b,c):
#     return a+b+c
# add=add3num(10,20,30)
# print(add)

# def add_num(*args):
#     return sum(args)
# a=add_num(2,6,5,6,8,9,22)
# print(a)

# def greet(*name):
#     for n in  name:
#         print(f"hello,{name}")
# greet("md","rashid","reha")

# def print_details(**kwargs):
#     for key ,value in kwargs.items():
#         print(f"{key}:{value}")
# print_details(name="md",age=22,city="mum")

# def add2nm(x,y):
#     result=(x-y)
#     print("the sum is",result)
# add2nm(50,50000)
# add2nm(y=50000,x=50)
#


# #to check a prime num
# num=int(input("enete a prime num"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count=count+1
# if count==2:
#     print(num,"is prime numb" )
# else:
#     print(num,"is not a prime num")


# def Employee:
    
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
        
#     def show(self):
#         print( "Employee name:",self.name)
#         print("salary:",self.salary)

# emp1=Employee("john",1000)
# emp2=emeployye(ali)


#sorted array
# arr=[64,34,25,12,11,90]
# n=len(arr)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if arr[j]>arr[j+1]:
#             temp=arr[j]
#             arr[j]=arr[j+1]
#             arr[j+1]=temp
# print("sorted arry:",arr)

#factorial num
# eg.. 5*4*3*2*1=120
# num=int(input("enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("factorial of ",num,"is",fact)

# n=int(input("e:"))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print("f",n,f)

# #fabonacci series in python
# num=int(input("enter a number:"))
# num1=0
# num2=1
# count=0
# print(num1,end=" ")
# print(num2,end=" ")
# while count<num:
#     result=num1+num2
#     print(result,end=" ")
#     num1=num2
#     num2=result
#     count=count+1
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# # Print first 8 terms
# for i in range(8):
#     print(fibonacci(i), end=" ")
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
for i in range(3):
    print(f(i),end="")
    