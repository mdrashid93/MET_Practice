

#1. Any customer will order two dishes
#2. ANy customer will enter quantity for each dish
#3. Calculate the total bill for the user.


#1. what you want to acheive?
   ## Total Bill
#2. What do u need to acheive that?
   # Dishes and their prices
   # What user wants 
   # how many the user wants
#3. Arrange the order
   # Dishes and their prices - Done
   # What user wants - DOne
   # how many the user wants
   #Total Bill

#4. write the code

# total_bill = 0
# menu = {
#     "dosa": 40,
#     "idly": 35,
#     "poori": 45,
#     "wada": 50,
#     "upma": 30
# }

# dish_one_choice = input("What do you want?") #idly
# dish_one_quantity = int(input("How many?")) #20

# dish_two_choice = input("What do you want?")
# dish_two_quantity = int(input("How many?"))

# dish_one_bill = (dish_one_quantity * menu.get(dish_one_choice))
# dish_two_bill = (dish_two_quantity * menu.get(dish_two_choice))

# total_bill =  dish_one_bill + dish_two_bill

# detailed_bill = f"""

# #####WELCOME TO SO AND SO HOTEL######
# BILL ID: {total_bill * 32}

# {dish_one_choice} X {menu.get(dish_one_choice)} = {dish_one_bill}
# {dish_two_choice} X {menu.get(dish_two_choice)} = {dish_two_bill}
# -------------------------------------------------------------------
# GST: 0%
# TAXES: 0%
# ------------------------------------TOTAL BILL: Rs.{total_bill}/----

# THANKS FOR VISITING US

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)


# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

# tuple1 = ('a', 'b' , 'c')
# tuple2 = (1, 2, 3)
# tuple3 = tuple2 + tuple1
# print(tuple3)

# simple note taking app
def add_note():
   note=input("enter your notes")
   with open("notes.txt","a") as f:
      f.write(note +"\n")
   print("note saved")

def read_note():
   with_open("note.txt","r")  
   notes=f.readlines()
   print("your notes")
   for note in notes:
      print(f"- {note.strip()}")

      
   

while True:
   print("\n1. add notes \n2. read notes \n3 exit")
   choice=input("choice")
   if choice=="1":
      add_notes()
   elif choice=="2":
      read_notes()
   elif choice=="3":
      break
   else:
      print("invalid choice")
       
   """hiichi
   lj  zsdlk
   lbzjds
   """


