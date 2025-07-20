# from time import*
# import random as r
# def mistake(partest,usertest):
#     error=0
#     for i in range(len(partest)):
#         try:
#             if partest[i]!=usertest[i]: 
#                 error = error +1
#         except:
#             error = error +1
#     return error

# def speed_time(time_s,time_e,user_input):
#     time_delay=time_e-time_s
#     time_r=round(time_delay,2)
#     speed=len(user_input)/time_r
#     return round(speed)
# if __name__=="__main__":
    
#     while True:
#         ck=input("ready to test(yes/no)")
#         if ck=="yes":
#             test=["a paragraph is self contained unit of discourage is "
#             "my name is md_rashid","a paragraph is self contained unit of discourage is"]
#             test1=r.choice(test)
#             print("*****typing speed*****")
#             print(test1)

#             time_1=time()
#             testinput=input("enter:")
#             time_2=time()

#             print("speed:",speed_time(time_1,time_2,testinput),"w/sec")
#             print("error",mistake(test1,testinput)) 
#         elif ck=="no":
#             print("thk u")
#             break
#         else:
#             print("wrong inye=")



#---------------------------------------- google translator---------------------------------

# from tkinter import*
# from tkinter import ttk
# from googlet_translator import Translator,Language

# def change(text="type",src="english",dest="hindi"):
#     text1=text
#     src1=src
#     dest1=dest
#     trans=Translator()
#     trans1=trans.translate(text,src=src1,dest=dest1)
#     return trans1.text

# def data():
#     s=comb_sor.get()
#     d=comb_dest.get()
#     mes=sor_text.get(1.0,END)
#     textget=change(text=mes,src=s,dest=d)
#     dest_txt.delete(1.0,END)
#     dest_txt.insert(END,textget)
    
# root=Tk
# root.title("Translator")
# root.geometry("500*700")
# root.config(bg="Red")

# lab_txt=Label(root,text="Translator",font=("time new roman",40,"bold"))
# lab_txt.place(x=100,y=40,height=50,width=300)

# frame=Frame(root).pack(side=BOTTOM)

# lab_txt=Label(root,text="source text",font=("time new roman",20,"bold"),fg="black",bg="red")
# lab_txt.place(x=100,y=100,height=200,width=300)

# sor_txt_txt=Label(root,text="Translator",font=("time new roman",40,"bold"))
# sor_txt_txt.place(x=100,y=40,height=50,width=300)

# list_text=list(Language.values())

# comb_sor=Text(root,text="Translator",font=("time new roman",40,"bold"))
# comb_sor.place(x=100,y=40,height=50,width=300)
# comb_sor.set("english")

# button_change=Button(frame,text="Translate",relief=Raised,command=data)
# button_change.place(x=170,y=300,height=40,width=1500)

# comb_dest=ttk.Combobox(frame,value=list_text)
# comb_dest.place(x=330,y=300,height=40,width=150)
# comb_dest.set("english")

# lab_txt=Label(root,text="dest text",font=("Time New Roman",20,"bold"),fg="black",bg="red")
# lab_txt.place(x=100,y=360,height=20,width=300)

# dest_text=Text(frame,font=("Time New Roman",20,"Bold"),wrap=WORD)
# dest_text.place(x=10,y=400,height=150,width=480)

# root.mainloop()

# amount=int(input("enter the amount:"))
# notes=[2000,500,200,100,50,20,10,5,2,1]
# for note in notes:
#     count=amount//note
#     if count>0:
#         print(f"{note}*{count}")
#         amount=amount%note
        
# am=int(input("enter amount:"))
# note=[5000,2000,2000,1000,500,200,100,50,20,10,5,1]
# for n in note:
#     count=am//note
#     if count>0:
#         print(f"{n}*{count}")
#         am=am%n

# x = print("Hello")
# print("Return value of print() is:", x)

# a=print("cel")
# print("ret val of ",a)




# char=input("enter a character:")
# if len(char)==1:
#     print(f"the ascii value of '{char}'is {ord(char)}")
# else:
#     print("please enter only single character")
# char=input("enter a character:")
# print("ascii value is "ord(char))

# char=input("enter a character:")
# print("asxii value of '{}' is {}".format(char,ord(char)) )

# char=input("enter a char:")
# print(f"ascii value of '{char}' is {ord(char)}  ")


# def find_quotient_remainder(x, y):
#     return x // y, x % y

# a = int(input("Enter dividend: "))
# b = int(input("Enter divisor: "))

# q, r = find_quotient_remainder(a, b)

# print("Quotient =", q)
# print("Remainder =", r)



# a=int(input("enter first number(a):"))
# b=int(input("enter second number(b):"))

# temp=a
# a=b
# b=temp
# print(f"after swapping :a={a},b={b}")


# m=int(input("enter 1st"))
# n=int(input("enter 2nd"))
# # tem=m
# # m=n
# # n=tem
# # print(f"swapping m={m},n={n}")

# m=m+n
# n=m-n
# m=m-n

# a,b=b,a
# print(f"swaping : m={m},n={n}")

# num=int(input("enter a number"))
# print(f"\n multiplication of table of {num}:\n")
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")
    


# num1=int(input("enter numer "))
# print(f"{num1}")

# for i in range(1,11):
#     print(f"{num1}*{i}={num1*i}")


# n=int(input("enter the range(up to n):"))


# for num in range(1,n+1):
#     print(f"\n table of {num}:")
#     for i in range(1,11):
#         print(f"{num}*{i}={num*i}")

#function to print multiplication table
# def print_table(n):
#     print(f"\n multiplication table of {n}")
#     print("-*30")
#     for i in range(1,11):
#         print(f"{n:2}*{i:2}={n*i:3}")
#     print("-"*30)
# num=int("ente num")
# print_table(num)

# n=int(input("enter the number of terms:"))
# a,b=0,1
# print("fibonacci series:")
# for i in range(n):
#     print(a, end=" ")
#     a,b=b,a+b
    
# def fib(n):
#     a,b=0,1
#     for _ in range(n):
#         print(a,end="")
#         # a,b=b,a+b
         
# i=int(input("enter num"))
# print("fib")
# fib(i)


# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)

# terms=int(input("enter numbr of ter:"))
# print("fibonacci series")
# for i in range(terms):
#     print(fib(i))
    
# def fib(s):
#     if s<=1:
#         return n
#     else:
#         return fib(n-1)+(n-2)
# i=int("enter")
# for a in range(i):
#     print(fib(a))

# base = int(input("Enter base number: "))
# exponent = int(input("Enter exponent (positive integer): "))

# result = 1
# for _ in range(exponent):
#     result *= base

# print(f"{base} ^ {exponent} = {result}")

# bess=int(input("ent bas"))
# expo=int(input("ent ex"))
# res=1
# for i in range(expo):
#     res*=bess
# print(f"{bess}^{expo}={res}")
# num=int(input("enter a num"))
# rev=0
# while num!=0:
#     digit=num%10
#     rev=rev*10+digit
#     num//=10

# print(f"Reversed number is: {rev}")
# num = input("Enter a number: ")
# reversed_num = num[::-1]

# print(f"Reversed number is: {reversed_num}")
# num=input("e")
# rev=num[::-1]
# print(f"rever{rev}")

# num = input("Enter a number: ")

# if num == num[::-1]:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")


# nu=input("enter number")

# if nu==nu[::-1]:
#     print("this is palin")
# else:
#     print("thi not") 
n = int(input("Enter the value of n: "))

print(f"Prime numbers between 1 and {n} are:")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # efficient check up to √num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')