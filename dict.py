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

fruits[0].index
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
# print(groups[1][1])#40

# print(groups[0][1])#20
# print(groups[0][0])
# print(groups[1][0])
#print(groups[1][-2])#30
# print(groups[1][-2] )
#print(int(str(groups[1][-2].replace('3','2'))))
# print(int(str(30).replace('3','2')))
# print(int("30".replace('3','2')))
# print(int("20"))#20

# #list of dictionary
# students=[{
#     "name":"md_rashid"
#            "age":23},
#           {"name":"raaj"
#            "age":28}]
# print(students[0]["name"])#md_rashid
# print(students[0].get("name"))#md_rashid
# print(students[0].get("marks",40))#40 default


# #.8 You have a list called billing_history with dictionaries for each transaction. Print the status of the second transaction
# billing_history = [
#     {'transaction_id': 'T001', 'amount': 1000, 'status': 'Completed'},
#     {'transaction_id': 'T002', 'amount': 500, 'status': 'Pending'},
#     {'transaction_id': 'T003', 'amount': 750, 'status': 'Failed'}
# ]

# # Print the status of the second transaction
# print(billing_history[1]['status'])

# #9. Create a tuple containing two billing dictionaries. Print the amount from the first transaction.
# billing_data = (
#     {'transaction_id': 'T001', 'amount': 1200, 'status': 'Completed'},
#     {'transaction_id': 'T002', 'amount': 800, 'status': 'Pending'}
# )

# #10 Print the amount from the first transaction
# print(billing_data[0]['amount']) #1200

        # #10city_temps = [
        #     ('Delhi', 40),
        #     ('Mumbai', 35),
        #     ('Kolkata', 38)
        # ]

        # # Print the temperature of the last city
        # print(city_temps[-1][1])

# #11. Given a dictionary with user names as keys and list of scores as values, print the last score of a user
# user_scores = {
#     'alice': [78, 85, 90],
#     'bob': [65, 70, 75],
#     'charlie': [88, 92, 85]
# }

# # Print the last score of a specific user, for example 'bob'
# print(user_scores['bob'][-1])

# #12 Make a list of two dictionaries: each dictionary should have keys 'product' and 'price'. Print the
# #product name from the second dictionary.
# products = [
#     {'product': 'Laptop', 'price': 60000},
#     {'product': 'Smartphone', 'price': 25000}
# ]

# # Print the product name from the second dictionary
# print(products[1]['product'])

# #13. Create a list of tuples where each tuple contains (subject, [marks]). Print the second mark for
# #any subject.
# subject_marks = [
#     ('Math', [78, 85, 90]),
#     ('Science', [80, 88, 84]),
#     ('English', [70, 75, 72])
# ]

# # Print the second mark for Math
# print(subject_marks[0][1][1])

# #14. Define a dictionary with days of the week as keys and a tuple of 2 tasks as values. Print the first
# #task of Monday.
# weekly_tasks = {
#     'Monday': ('Write report', 'Attend meeting'),
#     'Tuesday': ('Review code', 'Call client'),
#     'Wednesday': ('Design UI', 'Team stand-up')
# }

# # Print the first task of Monday
# print(weekly_tasks['Monday'][0])

# #15. Create a list of dictionaries, where each dictionary contains a student's name and another
# #dictionary with subjects and marks. Print Math marks for the first student.
# students = [
#     {
#         'name': 'Alice',
#         'marks': {
#             'Math': 90,
#             'Science': 85
#         }
#     },
#     {
#         'name': 'Bob',
#         'marks': {
#             'Math': 78,
#             'Science': 80
#         }
#     }
# ]

# # Print Math marks for the first student
# print(students[0]['marks']['Math'])




# #7. Define a dictionary inside a dictionary for a user profile. Print the full profile for 'alice'.
# user_profiles = {
#     'alice': {
#         'age': 25,
#         'city': 'Delhi',
#         'email': 'alice@example.com'
#     },
#     'bob': {
#         'age': 30,
#         'city': 'Mumbai',
#         'email': 'bob@example.com'
#     }
# }

# # Print the full profile for 'alice'
# print(user_profiles['alice'])

# user={
#         "raj":{"age":25,
#                "city":"delhi",
#                "phone":8986302010},
#         "monu":{"age":89,
#                 "address":"mumbai"}
        
# }
# print(user["monu"])

# # You have a list called billing_history with dictionaries for each transaction. Print the status of the second transaction
# billing_his=[{"transaction":"abcde", "amout":899, "status":"paid"},
#                {'transaction_id': 'T002', 'amount': 800, 'status': 'Pending'}]

# billing_history = [
#     {'transaction_id': 'T001', 'amount': 1000, 'status': 'Completed'},
#     {'transaction_id': 'T002', 'amount': 500, 'status': 'Pending'},
#     {'transaction_id': 'T003', 'amount': 750, 'status': 'Failed'}
# ]
# print(billing_his[0]["status"])
            
            
# #9. Create a tuple containing two billing dictionaries. Print the amount from the first transaction
# bill=({"transaction_id":1234, "amount":800, "status":"completed"},
#       {"transaction_id":4567, "amount":1000, "status":"pending"})
# # print(bill[0]["status"])

# #10. Define a list of 3 tuples, each with a city name and a temperature. Print the temperature of the last city
# city_temps = [
#     ('Delhi', 40),
#     ('Mumbai', 35),
#     ('Kolkata', 38)
# ]

# # # Print the temperature of the last city
# # print(city_temps[-1][1])
# city_name_temp=[
#         ("delhi":100),
#         ("mumbai":80),
#         ("pune":50)
         
# ]
# print(city_name_temp[1][1])

#11 Given a dictionary with user names as keys and list of scores as values, print the last score of a user
# user_name=[{"raaj":35,
#            "ras":48,
#            "ham":89,}]
# print(user_name[2])

# Sample dictionary
# user_scores = {
#     'alice': [85, 90, 88],
#     'bob': [78, 82, 91],
#     'charlie': [92, 87, 95]
# }

# # Enter the username
# user = 'bob'

# # Print the last score of that user
# if user in user_scores:
#     print(f"Last score of {user}: {user_scores[user][-1]}")
# else:
#     print("User not found.")

# iser={
#         "md":[90,35,52],
#         "ras":[63,61,72],
#         "rashid":[36,63,9]
# }

# #used="rashid"
# if used in iser:
#         print(f"last of marks of {used}:{iser[used][-1]}")
        
        
#12 Make a list of two dictionaries: each dictionary should have keys 'product' and 'price'. Print the
# #product name from the second dictionary.
# one= [
#         {"iphone":140000,
#      "oneplus":90000,
#      "samsung:":"20k",
#      "realme":10000, },
# two={"google":400,
#      "amazon":5000,
#      "dell":6000,
#      "lenovo":4000,
#         }]
# print(two[1]["lenovo"])
# {'product': 'Laptop', 'price': 60000},

# products = [
#     {'product': 'Laptop', 'price': 60000},
#     {'product': 'Smartphone', 'price': 25000}
# ]

# # Print the product name from the second dictionary
# print(products[1]['product'])

# produc=[
# {"produc":"laptop","price":50000},
# {"produce":"iphone","price":40000}
# #print product of iphone
# ]
# print(produc[1]["produce"])

#13. Create a list of tuples where each tuple contains (subject, [marks]). Print the second mark for
# #any subject.

 #14. Define a dictionary with days of the week as keys and a tuple of 2 tasks as values. Print the first
# #task of Monday.
# weekly_tasks = {
#     'Monday': ('Write report', 'Attend meeting'),
#     'Tuesday': ('Review code', 'Call client'),
#     'Wednesday': ('Design UI', 'Team stand-up')
# }

# # Print the first task of Monday
# print(weekly_tasks['Monday'][0])

# task={"monday":("write report","attend meeting"),
#       "tuesday":("review code","call client"),
#       "wednesday":("design UI","Team stand up")
# print=(task["monday"][1])
      
      
      
      
      #}




# #15. Create a list of dictionaries, where each dictionary contains a student's name and another
# #dictionary with subjects and marks. Print Math marks for the first student.
# students = [
#     {
#         'name': 'Alice',
#         'marks': {
#             'Math': 90,
#             'Science': 85
#         }
#     },
#     {
#         'name': 'Bob',
#         'marks': {
#             'Math': 78,
#             'Science': 80
#         }
#     }
# ]

# # Print Math marks for the first student
# print(students[0]['marks']['Math'])
# bachhe=[{"name":"rashid",
#        "marks":{"math":90, "science":99,"urdu":88} },
      
#       {"name":"md",
#        "mark":{"hindi":85,
#        "gk":77}}  ]
# print(bachhe[1]["name"])


student=["mdrashid",980.00,"delhi"]
print(student[2])
student[2]="mumbai"
print(student)        
        
        
marks=[2,6,8,10,12]
print(marks[:5])#2681012
print(marks[0:5])#2681012
print(marks[1:])#681012
print(marks[0:])#2681012
print(marks[-3:-1])