
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # ====== YOUR FACEBOOK LOGIN DETAILS ======
# mobile_number = "8986301198"   # Example: "9876543210"
# password = "aasshiff98."    # Your FB password

# # ====== PATH TO CHROMEDRIVER.EXE ======
# driver_path = "C:/chromedriver/chromedriver.exe"  # 👈 Update if path is different

# # ====== START SELENIUM CHROME DRIVER ======
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.facebook.com")
# time.sleep(3)

# # ====== LOGIN TO FACEBOOK ======
# driver.find_element(By.ID, "email").send_keys(mobile_number)
# driver.find_element(By.ID, "pass").send_keys(password)
# driver.find_element(By.NAME, "login").click()
# time.sleep(5)

# # ====== GO TO FRIENDS PAGE ======
# driver.get("https://www.facebook.com/me/friends")
# time.sleep(5)

# # ====== SCROLL TO LOAD MORE FRIENDS (OPTIONAL) ======
# for i in range(3):  # Load more friends
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

# # ====== UNFOLLOW FIRST 10 FRIENDS ======
# buttons = driver.find_elements(By.XPATH, "//div[@aria-label='Friends']")

# print(f"Found {len(buttons)} friend buttons. Trying to unfollow first 10...")

# count = 0
# for btn in buttons:
#     if count >= 10:  # Limit to 10
#         break
#     try:
#         btn.click()
#         time.sleep(2)

#         # Look for "Unfollow" in popup
#         unfollow = driver.find_element(By.XPATH, "//span[contains(text(),'Unfollow')]")
#         unfollow.click()
#         time.sleep(2)

#         print(f"✅ Unfollowed friend #{count + 1}")
#         count += 1
#     except Exception as e:
#         print(f"⚠️ Skipped one: {e}")
#         time.sleep(2)

# print(" Done. Closed browser.")
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # 1. Facebook login credentials
# phone_number= "8986301198"
# password = "aasshiff98."

# # 2. Setup WebDriver
# driver = webdriver.Chrome(executable_path="https://www.facebook.com/profile.php?id=100008680560752&sk=about")  # Update path here
# driver.get("https://www.facebook.com/profile.php?id=100008680560752&sk=about")
# time.sleep(3)

# # 3. Login to Facebook
# driver.find_element(By.ID, "email").send_keys(email)
# driver.find_element(By.ID, "pass").send_keys(password)
# driver.find_element(By.NAME, "login").click()
# time.sleep(5)

# # 4. Open friends list
# driver.get("https://www.facebook.com/profile.php?id=100008680560752&sk=about")
# time.sleep(5)

# # 5. Scroll to load more friends
# for i in range(5):  # Adjust range as needed
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

# # 6. Find all "Friends" buttons and try unfollowing
# friend_buttons = driver.find_elements(By.XPATH, "//div[@aria-label='Friends']")

# for btn in friend_buttons[:10]:  # Test on first 10 friends
#     try:
#         btn.click()
#         time.sleep(2)

#         # Click "Unfollow" from dropdown
#         unfollow_option = driver.find_element(By.XPATH, "//span[contains(text(),'Unfollow')]")
#         unfollow_option.click()
#         time.sleep(2)

#     except Exception as e:
#         print("Skipped one:", e)

# print("Done")
# driver.quit()

# from instabot import Bot
# bot=Bot()
# bot.login(username="aasshiff",password="password")
# bot.follow("nehaqueen")
# bot.upload_photo("path")
# bot.unfollow("nehaqueen")
# bot.send_message("i'm working",["nehaqueen","and other"])
# followers=bot.get_user_followers("nehaqueen")
# for follower in followers:
#     print(bot.get_user_info(follower))
# following=bot.get.user.following("nehaqueen")
# for Following in following:
#     print(bot.get.user.info(Following))

# import pywhatkit as p
# p.sendwhatmsg("+8986301198","kaha hai abhi",14,50)

# import qrcode as  qr
# img=qr.make("congratulation")
# img.save("r.png")



# import random
# subjects=[
#     "srk",
#     "virat",
#     "salman",
#     "varun",
#     "tiger",
#     "modi",
#     "khesari" 
# ]

# actions=[
#     "launcehe",
#     "dance",
#     "eat",
#     "dance",
#     "doctor",
#     "pm",
#     "celebration"
# ]

# place_of_things=[
#     "mumbai",
#     "delhi",
#     "kolkata",
#     "bihar",
#     "pune",
#     "banglor"
# ]
# #start the headline generation loop
# while True:
    
#     subject=random.choice(subjects)
#     action=random.choice(actions)
#     place_of_thing=random.choice(place_of_things)
    
#     headline=f"breaking news:{subject}{action}{place_of_thing }"
#     print("\n"+headline)
#     user_input=input("\n do you want to another headline (yes/no)").strip().lower()
#     if user_input=="no":
#         break
#     print("\n  thanks for visiting fake news headlines")

# History_file="history.text"
# def show_history():
#     file=open(History_file,"r")
#     line=file.readline()
#     if len(lines)==0:
#         print("no history found")
#     else:
#         for line in reversed(lines):
#             print(line.strip())
#     file.close()

# def clear_history():
#     file=open(History_file,"w")
#     file.close()
#     print("history cleared.")

# def save_to_history(equation,result):
#     file=open(History_file,"a")
#     file.write(equation+"="+ str(result)+ "\n")
#     file.close()

# def calculate(user_input):
#     parts=user_input.split()
#     if len(parts) !=3:
#         print("invalid input. use format number operator")
        
#     num1=float(parts[0])
#     op=parts[1]
#     num2=float(parts[2])
    
#     if op=="+":
#         result=num1+num2
#     elif op=="_":
#         result=num1-num2
#     elif op=="*":
#         result=num1*num2
#     elif op=="/":
#         if num2==0:
#             print("cannot divide by 0")
#             return
#         result=num1/num2
#     else:
#         print("invalid operator use only +-*/")
#         return
#     if int(result)==result:
#         result=int(result)
#     print("result",result)
#     save_to_history( user_input,result)
    
# def main():
#     print("--simple calculator (type history)")
#     while True:
#         user_input=input("enter cal +-*/ or command")
#         if user_input=="exit":
#             print("good bye")
#             break
#         elif user_input=="history":
#             show_history()
#         elif user_input=="clear":
#             clear_history()
#         else:
#             calculate(user_input)
# main()

# user = {"name": "John", "age": 30, "city": "New York"}
# for key in user:
#     print(key)
    
# user = {"name": "John", "age": 30, "city": "New York"}
# for value in user.values():
#     print(value)

# colors = {"red", "green", "blue"}
# for color in colors:
#     print(f"Color: {color}")
    
# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")
    
# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}: {fruit}")
    
# Print a multiplication table
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} × {j} = {i * j}")
#     print("-----")
    
# for a in range(1,11):
#     for b in range(1,11):
#         print(f"{a}*{b}={a*b}")

# # Traditional for loop
# squares = []
# for x in range(10):
#     squares.append(x ** 2)
# print(squares)

# squares=[]
# for a in range(10):
#     squares.append(a**3)
# print(squares)
# x=[]
# for b in range(11):
#     x.append(b**2)
# print(x)
# # Equivalent list comprehension
# squares = [x ** 2 for x in range(10)]
# print(squares)
# s=[a**2 for a in range(10)]
# print(s)

# # Only include even numbers
# even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
# print(even_squares)
# evo=[c**2 for c in range(15) if c%3==0]
# print(evo)


# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)
    

# for i in range(5):
#     if i == 2:
#         pass  # Do nothing special for i=2
#     print(i)
    
    
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = []

# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
        
# print(even_numbers)  # [2, 4, 6, 8, 10]
# n=[]
# for i in numbers:
#     if i %5!=0:
#         n.append(i)

# print(n)



# names = ["alice", "bob", "charlie"]
# capitalized_names = []

# for name in names:
#     capitalized_names.append(name.capitalize())
    
# print(capitalized_names)  # ["Alice", "Bob", "Charlie"]
# na=["md","reh","monu","rashid","ashif"]
# c=[]
# for n in na:
#     c.append(n.capitalize())
# print(c)#['Md', 'Reh', 'Monu', 'Rashid', 'Ashif']


# numbers = [4, 7, 2, 9, 1, 5]
# found = False

# for num in numbers:
#     if num > 8:
#         print(f"Found a number greater than 8: {num}")
#         found = True
#         break
        
# if not found:
#     print("No number greater than 8 found")

# nm=[2,8,3,9,10,15,8,6,12,35,20,22,17,23]
# fd=False
# for n in nm:
#     if n>34:
#         print(f"found number greater than 34:{n}")
#         fd=True
#         break
# if not fd:
#     print("no n  greter than 35:")
    
    
# numbers = [1, 2, 3, 4, 5]
# total = 0

# for num in numbers:
#     total += num
    
# print(f"Sum: {total}")  # Sum: 15


# to=0
# for i in nm:
#     to+=i
# print(to)



# # FizzBuzz using a for loop
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
        
        
        
        
        
# # Assignment 2: Password Validator
# # Create a password validator that:

# # Asks the user to create a password

# # Ensures the password meets these criteria:

# # At least 8 characters long

# # Contains at least one uppercase letter

# # Contains at least one lowercase letter

# # Contains at least one digit

# # Keeps asking until a valid password is entered

# # Solution:

# # Copy
# while True:
#     password = input("Create a password: ")
    
#     # Initialize validations
#     length_valid = len(password) >= 8
#     has_upper = False
#     has_lower = False
#     has_digit = False
    
#     # Check each character
#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
    
#     # Validate the password
#     if length_valid and has_upper and has_lower and has_digit:
#         print("Password is valid!")
#         break
#     else:
#         print("Password must be at least 8 characters and contain:")
#         if not length_valid:
#             print("- At least 8 characters")
#         if not has_upper:
#             print("- At least one uppercase letter")
#         if not has_lower:
#             print("- At least one lowercase letter")
#         if not has_digit:
#             print("- At least one digit")
            
            
            

# # Assignment 3: Dictionary Manipulation
# # Create a program that:

# # Starts with a dictionary of student grades

# # Uses a loop to calculate the average grade for each student

# # Creates a new dictionary with student names as keys and their average grades as values

# # Prints both the original and new dictionaries

# # Solution:

# # Copy
# # Original grades dictionary
# student_grades = {
#     "Alice": [85, 90, 78, 92],
#     "Bob": [76, 88, 95],
#     "Charlie": [82, 89, 75, 81, 90],
#     "David": [92, 95, 88]
# }

# # Calculate average grades
# average_grades = {}

# for student, grades in student_grades.items():
#     # Calculate average for current student
#     total = 0
#     for grade in grades:
#         total += grade
#     average = total / len(grades)
    
#     # Add to new dictionary
#     average_grades[student] = round(average, 2)

# # Print results
# print("Original grades dictionary:")
# for student, grades in student_grades.items():
#     print(f"{student}: {grades}")

# print("\nAverage grades dictionary:")
# for student, average in average_grades.items():
#     print(f"{student}: {average}")
    
    
    
    
# # Assignment 4: Nested Loop Pattern
# # Create a program that uses nested loops to print a pattern of stars (*) in the shape of a right-angled triangle:

# # Solution:

# # Copy
# # Define the height of the triangle
# height = 5

# # Outer loop for rows
# for i in range(1, height + 1):
#     # Inner loop for columns
#     for j in range(i):
#         print("*", end="")
#     # Move to the next line after each row
#     print()
    
    
    
    
    
# # Assignment 5: Data Processing with Loops
# # Create a program that:

# # Has a list of dictionaries representing products (name, price, category)

# # Uses loops to:

# # Find the most expensive product

# # Calculate the average price per category

# # Create a list of products below a certain price threshold

# # Solution:

# # Copy
# # List of product dictionaries
# products = [
#     {"name": "Laptop", "price": 1200, "category": "Electronics"},
#     {"name": "Headphones", "price": 150, "category": "Electronics"},
#     {"name": "Coffee Maker", "price": 80, "category": "Kitchen"},
#     {"name": "Blender", "price": 120, "category": "Kitchen"},
#     {"name": "Desk Chair", "price": 250, "category": "Furniture"},
#     {"name": "Bookshelf", "price": 175, "category": "Furniture"},
#     {"name": "Smart Watch", "price": 300, "category": "Electronics"},
#     {"name": "Toaster", "price": 45, "category": "Kitchen"}
# ]

# # 1. Find the most expensive product
# most_expensive = None
# highest_price = 0

# for product in products:
#     if product["price"] > highest_price:
#         highest_price = product["price"]
#         most_expensive = product

# print(f"Most expensive product: {most_expensive['name']} - ${most_expensive['price']}")

# # 2. Calculate average price per category
# category_totals = {}
# category_counts = {}

# # First collect category data
# for product in products:
#     category = product["category"]
#     price = product["price"]
    
#     if category in category_totals:
#         category_totals[category] += price
#         category_counts[category] += 1
#     else:
#         category_totals[category] = price
#         category_counts[category] = 1

# # Calculate and print the averages
# print("\nAverage price per category:")
# for category in category_totals:
#     average = category_totals[category] / category_counts[category]
#     print(f"{category}: ${average:.2f}")

# # 3. Create a list of affordable products (below $100)
# affordable_products = []
# price_threshold = 100

# for product in products:
#     if product["price"] < price_threshold:
#         affordable_products.append(product["name"])

# print(f"\nProducts under ${price_threshold}:")
# for product_name in affordable_products:
#     print(f"- {product_name}")
    





# while True:
#     pd=input("create password")
#     l_vd=len(pd)>=10
#     h_upper=False
#     h_lower=False
#     h_digit=False

#     for ch in pd:
#         if ch.isupper():
#             h_upper=True
#         elif ch.lower():
#             h_lower=True
#         elif ch.isdigit():
#             h_digit=True

#     if l_vd and h_upper and h_lower and h_digit:
#         print("password is valid")
#     break
# else:
#         print("password must be 10 character")
#     if not l_vd:
#         print("10 char")
#     if not h_upper:
#         print("at least one upper")
#     if not h_lower:
#         print("atleast one lower")
#     if not h_digit:
#         print("at least one digit")
        
        
        
# ct={}
# cc={}
# for pro in products:
#     cat=pro["cat"]
#     pc=pro["pc"]

#     if cat in ct:
#         ct[cat]+=pc
#         cc[cat]+=1
#     else:
#         ct[cat]=pc
#         cc[cat]=1
# print("\n av pc cat")
# for cat in ct:
#     a=ct[cat]/cc[cat]
#     print(f"{cat}: ${a:.2f}")
        
#sort tuple
tom,19,80
john,20,90
people=[]
while True:
    person_data=input()
    if not person_data:
        break
    parts=person_data.split(",")
    name=parts[0]
    age=int(parts[1])
    height=int(parts[2])
    
    people.append((name,age,height))
print(sorted(people))
    