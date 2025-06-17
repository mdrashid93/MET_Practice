# count=1
# while count<=5:
#     print("hello")
#     count=count+1
# count=1
# while count<=10:
#     print("hell")
#     count=count+1
# a=1
# while a<=8:
#     print("welcome")
#     a=a+2
# b=5
# while b>=1:
#     print("men",b)
#     b=b-1#54321
    
# count=10
# while count>=1:
#     print(count)
#     count=count-1
# count=8
# while count>=-10:
#     print(count)
#     count=count-2
# s=40
# while s>=4:
#     print(s)
#     s=s-4
    
# s=1
# while s<=10:
#     print("goodnight")
#     s +=1
    
# c=100
# while c>=10:
#     print(c)
#     c -=3
# i=1
# while i<=5:
#     print(i)
#     i+=1
# i=5
# while i<4:
#     print(i)
#     i-=1
# #search for a number x in the tuple using loop:
# numbers=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(numbers):
#     print(idx)
#     idx+=1
    
# i=1
# while i<=10:
#     print(3*i)
#     i+=1
# i=3
# while i<=30:
#     print(i)
#     i+=3
# i=1
# while i<=10:
#     print(4*i)
#     i+=1
# n=int(input("enter number"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
    
# x=("mdrashid",65,2.2)
# for i in x:
#     print(i)

# x
# for b in x:
#     print(b)

# for i in range(10):
#     print(i)
    
# for a in range(20):
#     print(a,"hello")
    
# for i in[2,6,"mdras"]:
#     print(i)

# for z in (36,96,85,22,'md'):
#     print(z)

# for i in range(2,4,6,8):#argument expected at most 3 argument print 4 got error
#     print(i)
    
# for i in range(20,11,-1):
#     print(i)

# for i in range(100,80,-5):
#     print(i)
    
# for i in range (100,20,-5):#95.90.85.80to 25
#     print(i)
# for i in range(20,50,+2):
#     print(i)  #22.24.26.28.30.32.34

# for i in range(1,21):
#     if(i%5!=0):# miss 5,10,15,20
#         print(i)

# 5
    
# a=int(input("how much candy you want"))
# b=1                                     #candy needed
# while b<=a:
#     print("candy")
#     b+=1

# x=int(input("how much candy you want?"))
# i=1
# while i <=x:
#     print("chocholate")
#     i+=1

# av=5
# x=int(input("how much candies you want"))
# i=1
# while i<=x:
#     if i>av:
#         break
#     print("candy")
#     i+=1

# av=6
# x=int(input("enter candi"))
# i=1
# while i<=x:
#     if i>av:
#         print("out of stock")
#         break
#     print("candy")
#     i+=1
# print("bye")

# mb=10
# x=int(int(input("how much cnady you want")))
# i=1
# while i<=x:
#     if i>mb:
#         print("out of stock")
#         break
#     print("candy")
#     i+=1
# print("bye")

# for i in range(1,101):
#     if i%3==0:
#         continue
#     print(i)
# print("by")
# for i in range(1,100):
#     if i%3==0 or i%5==0:
#         continue
#     print(i)

# for i in range(1,100):
#     if(i%2!=0):
#         pass          #even number
#     else:
#         print(i)
# print("by")

# i=1
# while i<=5:
#     print("i miss u")
#     i+=1
    
# i=5
# while i>=1:
#     print("i miss u" ,i)
#     i-=1

# i=5
# j=1
# while i>=1:
#     print("telusko")
#     while j<=4:
#         print("rock")
#         j=j+1
#     i=i-1
    
# i=1
# j=1
# while i<=5:
#     print("telu", end=" ")
#     while i<=4:
#         print("rocks", end=" ")
#         j=j+1
#     i=i+1


# j=1
# i=1
# while i<=5:
#     print("md" , end=" ")
#     while i<=4:
#         print("rocks", end=" ")
#         j+=1
# #         i+=1
# i=5
# j=1
# while i>=10:
#     print("teli")
#     while j<=5:
#         print("rock")
#         j=j+1
#     i=i+1

# ja=1
# i=1
# while i <=5:
#     print("telusko", end=" ")
#     while ja<=10:
#         print("rocky", end=" ")
#         ja+=1
#     i+=1
# for i in range(1,101):
#     print(i)
# for i in range(1,101):
#     if(i%5!=0):
#         pass
#     else:
#         print(i)
        
# for i in range(1,100):
#     if i%3==0:
#         continue
#     print(i)

# for j in range(4):
#     print("#",end=" ")
# print()# #### in same line

# for i in range(5):
#     print("#", end=" ")
# print()
# for j in range(5):
#     print("#",end=" ")
#     print()

# for i in range(4):         ####
#     for j in range(4):     ####
#                            ####
#         print("#",end=" ") ####
#     print()
    
for i in range(4):
    for j in range(i+1):
        print("#", end=" ")
    print()
        