# name="md_rashid"
# age=24
# is_married=False
# fruits=["banana","kiwi","apple"]
# colors=("white","black","yellow")
# user_name={"alex","anny","md_ras"}
# person={"name":"md_rashid"
#         "age":30}
# print(fruits[0][0])#b
# print(fruits[0][2:5])#nan
# print(fruits[1][-4:])#kiwi
# print(fruits[1][2:])#wi

# a=[1,2,3]
# fruit=["banana",True,23,98.5,a]
# print(fruit[-1])

#1 list inside list
fruits=[["jack","apple"],#0
        ["orange","kiwi"],#1
        ["dragon","grapes"]]#3  
#print(fruits[-1][-2])#dragon
fruits[0].append("fruit")
fruits[2].append("water")# third element me last me add water
#print(fruits)#jack,apple,fruits
#a=[len(fruits[0]),len(fruits[1]),len(fruits[2])]
#print(sum(a))#output is 8.
 #3+2+3=8
#a=fruits[1:2][1][2]
#print(a)#error
a=fruits[1:2]
print(a)#orange,kiwi
b=[1,2,3]

#print(b[1:2])
# a=fruits[1:2][0][1][-2]
# print(a)#w

# #tuple inside tuple
# coordinate=((0,1),(2,3),(4,5))
# print(coordinate[2][1])#5

# #tuple inside list
# student=[("alice",23),("bob",21)]
# print(student[1][1])#21
# print(int(21+str(23))/213)#1
# print(213/213)#1
# print(student[1])#error

#list inside tuple
groups=([10,20],[30,40])
print(groups[1][1])#40
print(groups[1][-2])#30
print(groups[1][-2] )
print(int(str(groups[1][-2].replace('3','2'))))
print(int(str(30).replace('3','2')))
print(int("30".replace('3','2')))
print(int("20"))#20

#list of dictionary
students=[{
    "name":"md_rashid"
           "age":23},
          {"name":"raaj"
           "age":28}]
print(students[0]["name"])#md_rashid
print(students[0].get("name"))#md_rashid
print(students[0].get("marks",40))#40 default
