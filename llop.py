# 1. Print numbers from 1 to 5 using range()
for i in range(1, 6):
    print(i)

# 2. Print all even numbers between 10 and 20
for i in range(10, 21):
    if i % 2 == 0:
        print(i)

# 3. Ask the user for 3 names and store them in a list
names = []
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    names.append(name)
print("Names list:", names)

# 4. Print the square of each number in a list
numbers = [2, 4, 6, 8]
for num in numbers:
    print(f"Square of {num} is {num ** 2}")

# 5. Loop through list of dictionaries and print name and age
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
for person in people:
    print(f"Name: {person['name']}, Age: {person['age']}")

# 6. Print all fruits from a nested list
fruits = [['apple', 'banana'], ['grape', 'mango']]
for sublist in fruits:
    for fruit in sublist:
        print(fruit)

# 7. Print characters of a string entered by the user
user_string = input("Enter a string: ")
for char in user_string:
    print(char)

# 8. Print numbers from 5 to 1 in reverse order
for i in range(5, 0, -1):
    print(i)

# 9. Input 3 subjects and 3 marks, then print each subject with its mark
subjects = []
marks = []
for i in range(3):
    subject = input(f"Enter subject {i+1}: ")
    mark = input(f"Enter marks for {subject}: ")
    subjects.append(subject)
    marks.append(mark)
for i in range(3):
    print(f"{subjects[i]}: {marks[i]}")

# 10. Loop through list of tuples and print product with price
products = [('Pen', 10), ('Notebook', 40), ('Eraser', 5)]
for item in products:
    print(f"{item[0]}: {item[1]}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # 1. Electronic Devices

class TV:
    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size

    def turn_on(self):
        print(f"{self.brand} TV is now ON.")

    def reset(self):
        print(f"{self.brand} TV has been reset.")

class Laptop:
    def __init__(self, brand, color, ram):
        self.brand = brand
        self.color = color
        self.ram = ram

    def turn_on(self):
        print(f"{self.brand} Laptop is booting up.")

    def reset(self):
        print(f"{self.brand} Laptop is restarting.")

class Fan:
    def __init__(self, brand, color, speed_levels):
        self.brand = brand
        self.color = color
        self.speed_levels = speed_levels

    def turn_on(self):
        print(f"{self.brand} Fan is spinning.")

    def reset(self):
        print(f"{self.brand} Fan settings reset.")

# Instances
tv = TV("Samsung", "Black", "42 inch")
laptop = Laptop("Dell", "Silver", "16GB")
fan = Fan("Usha", "White", 3)

tv.turn_on()
laptop.reset()
fan.turn_on()

# ------------------------------------------------------------

# 2. Vehicles

class Car:
    def __init__(self, model, speed, fuel_type):
        self.model = model
        self.speed = speed
        self.fuel_type = fuel_type

    def accelerate(self):
        print(f"{self.model} is accelerating.")

    def honk(self):
        print(f"{self.model} says Honk Honk!")

class Bike:
    def __init__(self, model, speed, fuel_type):
        self.model = model
        self.speed = speed
        self.fuel_type = fuel_type

    def accelerate(self):
        print(f"{self.model} is zooming ahead.")

    def stop(self):
        print(f"{self.model} has stopped.")

class Truck:
    def __init__(self, model, speed, fuel_type):
        self.model = model
        self.speed = speed
        self.fuel_type = fuel_type

    def honk(self):
        print(f"{self.model} goes HOOONK!")

    def stop(self):
        print(f"{self.model} is parked.")

# Instances
car = Car("Honda City", 180, "Petrol")
bike = Bike("Yamaha FZ", 120, "Petrol")
truck = Truck("Tata Ace", 80, "Diesel")

car.accelerate()
bike.stop()
truck.honk()

# ------------------------------------------------------------

# 3. School System

class Student:
    def __init__(self, name, grade, roll_no):
        self.name = name
        self.grade = grade
        self.roll_no = roll_no

    def study(self):
        print(f"{self.name} is studying.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

class Teacher:
    def __init__(self, name, subject, emp_id):
        self.name = name
        self.subject = subject
        self.emp_id = emp_id

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def take_attendance(self):
        print(f"{self.name} is taking attendance.")

class Classroom:
    def __init__(self, room_no, capacity, section):
        self.room_no = room_no
        self.capacity = capacity
        self.section = section

    def start_class(self):
        print(f"Class in room {self.room_no} has started.")

    def clean_room(self):
        print(f"Room {self.room_no} is being cleaned.")

# Instances
student = Student("Rahul", "10th", 23)
teacher = Teacher("Mrs. Sharma", "Math", 101)
classroom = Classroom("A1", 40, "10A")

student.study()
teacher.teach()
classroom.start_class()

# ------------------------------------------------------------

# 4. Shopping App

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def view_details(self):
        print(f"{self.name} - ₹{self.price} [{self.category}]")

    def apply_discount(self, percent):
        discounted_price = self.price * (1 - percent / 100)
        print(f"Discounted price of {self.name}: ₹{discounted_price}")

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")

    def view_cart(self):
        print("Cart contains:")
        for item in self.items:
            print(f"- {item.name} ₹{item.price}")

class User:
    def __init__(self, username, email, address):
        self.username = username
        self.email = email
        self.address = address

    def login(self):
        print(f"{self.username} logged in.")

    def view_profile(self):
        print(f"User: {self.username}, Email: {self.email}, Address: {self.address}")

# Instances
p1 = Product("Shoes", 1500, "Footwear")
p2 = Product("T-Shirt", 700, "Clothing")
cart = Cart()
user = User("md_user", "md@example.com", "Hyderabad")

user.login()
p1.view_details()
cart.add_product(p1)
cart.add_product(p2)
cart.view_cart()

# ------------------------------------------------------------

# 5. Library System

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

    def get_summary(self):
        print(f"'{self.title}' is a {self.genre} book.")

class Librarian:
    def __init__(self, name, emp_id, shift):
        self.name = name
        self.emp_id = emp_id
        self.shift = shift

    def issue_book(self):
        print(f"{self.name} issued a book.")

    def return_book(self):
        print(f"{self.name} processed a return.")

class Member:
    def __init__(self, name, member_id, membership_type):
        self.name = name
        self.member_id = member_id
        self.membership_type = membership_type

    def borrow_book(self):
        print(f"{self.name} borrowed a book.")

    def return_book(self):
        print(f"{self.name} returned a book.")

# Instances
book = Book("The Alchemist", "Paulo Coelho", "Fiction")
librarian = Librarian("Mr. Khan", 501, "Morning")
member = Member("Ayesha", 1001, "Premium")

book.read()
librarian.issue_book()
member.borrow_book()














# 1. Remote and TV

class TV:
    def turn_on(self):
        print("TV is now ON.")

    def turn_off(self):
        print("TV is now OFF.")

class Remote:
    def __init__(self):
        self.tv = TV()

    def press_power_on(self):
        self.tv.turn_on()

    def press_power_off(self):
        self.tv.turn_off()

# Usage
remote = Remote()
remote.press_power_on()
remote.press_power_off()

# ------------------------------------------------------------

# 2. Engine and Car

class Engine:
    def start_engine(self):
        print("Engine has started.")

class Car:
    def __init__(self):
        self.engine = Engine()

# Usage
car = Car()
car.engine.start_engine()

# ------------------------------------------------------------

# 3. Room and Light

class Light:
    def switch_on(self):
        print("Light is switched ON.")

class Room:
    def __init__(self):
        self.light = Light()

# Usage
room = Room()
room.light.switch_on()

# ------------------------------------------------------------

# 4. Laptop and Battery

class Battery:
    def check_charge(self):
        print("Battery is at 85% charge.")

class Laptop:
    def __init__(self):
        self.battery = Battery()

# Usage
laptop = Laptop()
laptop.battery.check_charge()

# ------------------------------------------------------------

# 5. Mobile and Camera

class Camera:
    def take_picture(self):
        print("Picture taken with 108MP Camera.")

class Mobile:
    def __init__(self):
        self.camera = Camera()

# Usage
mobile = Mobile()





















import math

# Q1: Compute Q using formula Q = sqrt[(4 * C * D)/H]
C = 40
H = 20
D_values = input("Enter comma-separated D values: ").split(',')
for D in D_values:
    D = int(D)
    Q = int(math.sqrt((4 * C * D) / H))
    print(f"D={D} => Q={Q}")

# ------------------------------------------------------------

# Q2: Create 2D list with element at (i,j) = i^2 + j^2
X = int(input("Enter number of rows (X): "))
Y = int(input("Enter number of columns (Y): "))
matrix = [[i**2 + j**2 for j in range(Y)] for i in range(X)]
print("2D Matrix:")
for row in matrix:
    print(row)

# ------------------------------------------------------------

# Q3: Print binary numbers divisible by 7
binary_list = input("Enter comma-separated 4-digit binary numbers: ").split(',')
valid_binaries = [b for b in binary_list if int(b, 2) % 7 == 0]
print("Binary numbers divisible by 7:", ', '.join(valid_binaries))

# ------------------------------------------------------------

# Q4: Bank balance from transactions
transactions = input("Enter transactions (e.g., 'D 300,W 200'): ").split(',')
balance = 0
for txn in transactions:
    action, amount = txn.strip().split()
    amount = int(amount)
    if action == 'D':
        balance += amount
    elif action == 'W':
        balance -= amount
print("Final Balance:", balance)

# ------------------------------------------------------------

# Q5: Robot movement and final distance
moves = input("Enter moves (e.g., 'FORWARD 10,LEFT 5'): ").split(',')
x = y = 0
for move in moves:
    direction, steps = move.strip().split()
    steps = int(steps)
    if direction == 'FORWARD':
        y += steps
    elif direction == 'BACKWARD':
        y -= steps
    elif direction == 'LEFT':
        x -= steps
    elif direction == 'RIGHT':
        x += steps
distance = int(math.sqrt(x**2 + y**2))
print("Final Distance from Origin:", distance)

# ------------------------------------------------------------

# Q6: Count unique words (case-insensitive), sorted alphabetically
text = input("Enter text: ")
words = text.lower().split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
for word in sorted(word_count):
    print(f"{word}: {word_count[word]}")

# ------------------------------------------------------------

# Q7: Sort employee tuples by name, experience, salary
employees = [
    ("Alice", 5, 50000),
    ("Bob", 3, 45000),
    ("Alice", 2, 40000),
    ("Charlie", 4, 60000)
]
sorted_employees = sorted(employees, key=lambda x: (x[0], x[1], x[2]))
print("Sorted Employees:")
for emp in sorted_employees:
    print(emp)

# ------------------------------------------------------------

# Q8: Generator for numbers divisible by 3 but not by 9
class DivisibleGenerator:
    def __init__(self, n):
        self.n = n

    def generate(self):
        for i in range(self.n + 1):
            if i % 3 == 0 and i % 9 != 0:
                yield i

gen = DivisibleGenerator(50)
print("Numbers divisible by 3 but not 9:")
for num in gen.generate():
    print(num, end=' ')

# ------------------------------------------------------------

# Q9: List comprehension for factorials up to n, filter > 1000
n = int(input("\nEnter n for factorials: "))
factorials = [math.factorial(i) for i in range(n + 1)]
filtered = [f for f in factorials if f <= 1000]
print("Filtered Factorials (<=1000):", filtered)

# ------------------------------------------------------------

# Q10: Generator for numbers divisible by both 4 and 6
def divisible_by_4_and_6(n):
    for i in range(1, n + 1):
        if i % 4 == 0 and i % 6 == 0:
            yield i

print("Numbers divisible by both 4 and 6:")
for num in divisible_by_4_and_6(100):
    print(num, end=' ')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import math

# Q1: Evaluate Q = sqrt[(3 * C * D)/H] for comma-separated D values
C = 60
H = 20
D_values = input("Enter comma-separated D values: ").split(',')
for D in D_values:
    D = int(D)
    Q = int(math.sqrt((3 * C * D) / H))
    print(f"D={D} => Q={Q}")

# ------------------------------------------------------------

# Q2: Generate 2D array with (i+j)^2
X = int(input("Enter number of rows (X): "))
Y = int(input("Enter number of columns (Y): "))
matrix = [[(i + j)**2 for j in range(Y)] for i in range(X)]
print("2D Array:")
for row in matrix:
    print(row)

# ------------------------------------------------------------

# Q3: Print 4-digit binary numbers divisible by 3
binary_list = input("Enter comma-separated 4-digit binary numbers: ").split(',')
valid = [b for b in binary_list if int(b, 2) % 3 == 0]
print("Binary numbers divisible by 3:", ', '.join(valid))

# ------------------------------------------------------------

# Q4: Compute net account balance from transaction log
transactions = input("Enter transactions (e.g., 'D 200,W 150'): ").split(',')
balance = 0
for txn in transactions:
    action, amount = txn.strip().split()
    amount = int(amount)
    if action == 'D':
        balance += amount
    elif action == 'W':
        balance -= amount
print("Net Balance:", balance)

# ------------------------------------------------------------

# Q5: Robot movement and final distance from origin
moves = input("Enter moves (e.g., 'UP 5,LEFT 3'): ").split(',')
x = y = 0
for move in moves:
    direction, steps = move.strip().split()
    steps = int(steps)
    if direction == 'UP':
        y += steps
    elif direction == 'DOWN':
        y -= steps
    elif direction == 'LEFT':
        x -= steps
    elif direction == 'RIGHT':
        x += steps
distance = int(math.sqrt(x**2 + y**2))
print("Final Distance from Origin:", distance)

# ------------------------------------------------------------

# Q6: Word frequency count, sorted by frequency desc then alphabetically
text = input("Enter paragraph: ")
words = text.lower().split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
print("Word Frequencies:")
for word, count in sorted_freq:
    print(f"{word}: {count}")

# ------------------------------------------------------------

# Q7: Sort tuples by name, score (desc), age
data = [
    ("Alice", 85, 25),
    ("Bob", 90, 22),
    ("Alice", 90, 23),
    ("Charlie", 70, 30)
]
sorted_data = sorted(data, key=lambda x: (x[0], -x[1], x[2]))
print("Sorted Tuples:")
for item in sorted_data:
    print(item)

# ------------------------------------------------------------

# Q8: Class with generator for even numbers divisible by 4
class EvenDivBy4:
    def __init__(self, n):
        self.n = n

    def generate(self):
        for i in range(2, self.n + 1, 2):
            if i % 4 == 0:
                yield i

gen = EvenDivBy4(50)
print("Even numbers divisible by 4:")
for num in gen.generate():
    print(num, end=' ')

# ------------------------------------------------------------

# Q9: List comprehension for squares up to n, filter not divisible by 3
n = int(input("\nEnter n for squares: "))
squares = [i**2 for i in range(1, n + 1) if (i**2) % 3 != 0]
print("Filtered Squares:", squares)

# ------------------------------------------------------------

# Q10: Generator for numbers divisible by both 6 and 9
def divisible_by_6_and_9(n):
    for i in range(n + 1):
        if i % 6 == 0 and i % 9 == 0:
            yield i

print("Numbers divisible by both 6 and 9:")
for num in divisible_by_6_and_9(100):
    print(num, end=' ')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import re

# 1. Remove all non-alphabet characters
s = 'H3ll0_Wor!ld#2025'
result = ''.join([c for c in s if c.isalpha()])
print("Q1:", result)  # Output: HllWorld

# ------------------------------------------------------------

# 2. Most frequent word
sentence = 'cat dog dog bird cat cat'
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
most_common = max(freq, key=freq.get)
print("Q2:", most_common)  # Output: cat

# ------------------------------------------------------------

# 3. Index of first vowel
s = 'crypt'
vowels = 'aeiou'
index = next((i for i, c in enumerate(s) if c in vowels), -1)
print("Q3:", index)  # Output: -1

# ------------------------------------------------------------

# 4. Move vowels to end
s = 'education'
vowels = 'aeiou'
consonants = ''.join([c for c in s if c not in vowels])
vowel_part = ''.join([c for c in s if c in vowels])
print("Q4:", consonants + vowel_part)  # Output: dctneuaio

# ------------------------------------------------------------

# 5. Character frequency dictionary
s = 'banana'
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
print("Q5:", freq)  # Output: {'b':1, 'a':3, 'n':2}

# ------------------------------------------------------------

# 6. Replace vowels with uppercase
s = 'hello world'
vowels = 'aeiou'
result = ''.join([c.upper() if c in vowels else c for c in s])
print("Q6:", result)  # Output: hEllO wOrld

# ------------------------------------------------------------

# 7. Check continuous ascending digits
s = '12345'
is_continuous = all(int(s[i]) + 1 == int(s[i+1]) for i in range(len(s)-1))
print("Q7:", is_continuous)  # Output: True

# ------------------------------------------------------------

# 8. Count words longer than 4 letters
sentence = 'This is a beautiful sunny day'
count = sum(1 for word in sentence.split() if len(word) > 4)
print("Q8:", count)  # Output: 2

# ------------------------------------------------------------

# 9. Mask all but last 4 characters
s = 'mysecretpassword1234'
masked = '*' * (len(s) - 4) + s[-4:]
print("Q9:", masked)  # Output: ****************1234

# ------------------------------------------------------------

# 10. Staircase pattern
s = 'python'
staircase = '\n'.join([' ' * i + s[i] for i in range(len(s))])
print("Q10:\n" + staircase)
# Output:
# p
#  y
#   t
#    h
#     o
#      n

# ------------------------------------------------------------

# 11. Reverse words
s = 'open ai builds tools'
reversed_words = ' '.join(s.split()[::-1])
print("Q11:", reversed_words)  # Output: tools builds ai open

# ------------------------------------------------------------

# 12. Characters at even indices
s = 'a1b2c3'
even_chars = ''.join([s[i] for i in range(0, len(s), 2)])
print("Q12:", even_chars)  # Output: abc
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# 🏫 Medha Edutech | Quiz Game Project

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["A. 90°C", "B. 100°C", "C. 120°C", "D. 80°C"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "Which gas do plants absorb?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Picasso", "B. Van Gogh", "C. Da Vinci", "D. Michelangelo"],
        "answer": "C"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["A. Yen", "B. Won", "C. Dollar", "D. Rupee"],
        "answer": "A"
    }
]

score = 0

print("\n🎓 Welcome to the Quiz Game - Powered by Medha Edutech (M-E-T)\n")

for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")
    for option in q['options']:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q['answer']:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect. Correct answer is: {q['answer']}\n")

print(f"🏁 Final Score: {score} out of {len(questions)}")

































# 1. Greet user
def greet_user(name):
    return f"Hello, {name}!"

print("Q1:", greet_user(name="Ayesha"))

# ------------------------------------------------------------

# 2. Check temperature
def check_temperature(temp):
    return "Fever" if temp > 99 else "Normal"

print("Q2:", check_temperature(temp=101))

# ------------------------------------------------------------

# 3. Get last fruit from list
def get_last_fruit(fruits):
    return fruits[-1] if fruits else None

print("Q3:", get_last_fruit(['apple', 'banana', 'cherry']))

# ------------------------------------------------------------

# 4. Get price tag
def get_price_tag(price):
    return "Expensive" if price > 1000 else "Affordable"

print("Q4:", get_price_tag(price=750))

# ------------------------------------------------------------

# 5. Format user info
def format_user_info(name, age):
    return f"Name: {name}, Age: {age}"

print("Q5:", format_user_info(name="Rahul", age=22))

# ------------------------------------------------------------

# 6. Uppercase if string
def uppercase_if_string(value):
    return value.upper() if isinstance(value, str) else "Invalid input"

print("Q6:", uppercase_if_string("hello"))
print("Q6:", uppercase_if_string(123))

# ------------------------------------------------------------

# 7. Safe divide
def safe_divide(num, den):
    return num / den if den != 0 else "Cannot divide"

print("Q7:", safe_divide(num=10, den=2))
print("Q7:", safe_divide(num=10, den=0))

# ------------------------------------------------------------

# 8. Check login
def check_login(credentials):
    return "Login successful" if credentials.get("password") else "Login failed"

print("Q8:", check_login({"username": "user1", "password": "pass123"}))
print("Q8:", check_login({"username": "user2", "password": ""}))

# ------------------------------------------------------------

# 9. Get full name in title case
def get_full_name(first, last):
    return f"{first.title()} {last.title()}"

print("Q9:", get_full_name(first="john", last="doe"))

# ------------------------------------------------------------

# 10. Get discounted price
def get_discounted_price(price, is_member):
    return price * 0.9 if is_member else price

print("Q10:", get_discounted_price(price=1200, is_member=True))
print("Q10:", get_discounted_price(price=1200, is_member=False))










































# 1. First fruit of last pair
fruits = [['jack', 'apple'], ['orange', 'kiwi'], ['dragon', 'grape']]
print("Q1:", fruits[-1][0])  # Output: dragon

# ------------------------------------------------------------

# 2. Second number in last coordinate
coordinates = ((0, 1), (2, 3), (4, 5))
print("Q2:", coordinates[-1][1])  # Output: 5

# ------------------------------------------------------------

# 3. Bob's age
students = [('Alice', 23), ('Bob', 21)]
print("Q3:", students[1][1])  # Output: 21

# ------------------------------------------------------------

# 4. Last number in tuple of lists
data = ([10, 20], [30, 40])
print("Q4:", data[1][-1])  # Output: 40

# ------------------------------------------------------------

# 5. Name of first student
student_dicts = [{'name': 'Alice', 'age': 23}, {'name': 'Bob', 'age': 21}]
print("Q5:", student_dicts[0]['name'])  # Output: Alice

# ------------------------------------------------------------

# 6. Second mark for Math
subject_marks = {
    'Math': [88, 92, 75],
    'Science': [90, 85, 80]
}
print("Q6:", subject_marks['Math'][1])  # Output: 92

# ------------------------------------------------------------

# 7. Full profile for 'alice'
profiles = {
    'alice': {'age': 23, 'email': 'alice@example.com'},
    'bob': {'age': 21, 'email': 'bob@example.com'}
}
print("Q7:", profiles['alice'])  # Output: {'age': 23, 'email': 'alice@example.com'}

# ------------------------------------------------------------

# 8. Status of second transaction
billing_history = [
    {'id': 1, 'amount': 500, 'status': 'paid'},
    {'id': 2, 'amount': 300, 'status': 'pending'}
]
print("Q8:", billing_history[1]['status'])  # Output: pending

# ------------------------------------------------------------

# 9. Amount from first transaction in tuple
billing_data = (
    {'id': 1, 'amount': 250},
    {'id': 2, 'amount': 400}
)
print("Q9:", billing_data[0]['amount'])  # Output: 250

# ------------------------------------------------------------

# 10. Temperature of last city
cities = [('Delhi', 35), ('Mumbai', 30), ('Chennai', 33)]
print("Q10:", cities[-1][1])  # Output: 33

# ------------------------------------------------------------

# 11. Last score of a user
user_scores = {
    'alice': [85, 90, 95],
    'bob': [70, 75, 80]
}
print("Q11:", user_scores['alice'][-1])  # Output: 95

# ------------------------------------------------------------

# 12. Product name from second dictionary
products = [
    {'product': 'Pen', 'price': 10},
    {'product': 'Notebook', 'price': 40}
]
print("Q12:", products[1]['product'])  # Output: Notebook

# ------------------------------------------------------------

# 13. Second mark for any subject
subject_data = [
    ('Math', [88, 92]),
    ('Science', [85, 90])
]
print("Q13:", subject_data[0][1][1])  # Output: 92

# ------------------------------------------------------------

# 14. First task of Monday
weekly_tasks = {
    'Monday': ('Meeting', 'Report'),
    'Tuesday': ('Call', 'Presentation')
}
print("Q14:", weekly_tasks['Monday'][0])  # Output: Meeting

# ------------------------------------------------------------

# 15. Math marks for first student
students_info = [
    {'name': 'Alice', 'marks': {'Math': 90, 'Science': 85}},
    {'name': 'Bob', 'marks': {'Math': 80, 'Science': 88}}
]
print("Q15:", students_info[0]['marks']['Math'])  # Output: 90





















# 1. Favorite programming languages
languages = {'Python', 'JavaScript', 'C++'}
print("Q1:", languages)

# ------------------------------------------------------------

# 2. User hobbies as set
hobbies = set(input("Enter 3 hobbies separated by spaces: ").split())
print("Q2:", hobbies)

# ------------------------------------------------------------

# 3. Add 'yellow' to colors set
colors = {'red', 'blue', 'green'}
colors.add('yellow')
print("Q3:", colors)

# ------------------------------------------------------------

# 4. Update first set with second
set1 = {'apple', 'banana'}
set2 = {'banana', 'cherry'}
set1.update(set2)
print("Q4:", set1)  # Output: {'apple', 'banana', 'cherry'}

# ------------------------------------------------------------

# 5. Union of cities visited
personA = {'Delhi', 'Mumbai', 'Chennai'}
personB = {'Bangalore', 'Mumbai', 'Kolkata'}
print("Q5:", personA.union(personB))

# ------------------------------------------------------------

# 6. Intersection of name sets
setA = {'alex', 'john', 'mike'}
setB = {'john', 'mike', 'lisa'}
print("Q6:", setA.intersection(setB))  # Output: {'john', 'mike'}

# ------------------------------------------------------------

# 7. Discard 'pencil'
items = {'pen', 'pencil', 'eraser'}
items.discard('pencil')
print("Q7:", items)  # Output: {'pen', 'eraser'}

# ------------------------------------------------------------

# 8. Remove 'marker' using remove()
tools = {'pen', 'pencil', 'eraser'}
try:
    tools.remove('marker')  # Raises KeyError
except KeyError:
    print("Q8: 'marker' not found in set")

# ------------------------------------------------------------

# 9. Pop from weekdays
weekdays = {'Monday', 'Tuesday', 'Wednesday'}
removed = weekdays.pop()
print("Q9: Removed:", removed)
print("Updated set:", weekdays)

# ------------------------------------------------------------

# 10. Clear car brands
cars = {'Toyota', 'Honda', 'Ford'}
cars.clear()
print("Q10:", cars)  # Output: set()

# ------------------------------------------------------------

# 11. Delete tools set
tools = {'hammer', 'screwdriver', 'wrench'}
del tools
try:
    print("Q11:", tools)
except NameError:
    print("Q11: Set no longer exists (NameError)")

# ------------------------------------------------------------

# 12. Set from string 'hello'
letters = set('hello')
print("Q12:", letters)  # Output: {'h', 'e', 'l', 'o'}

# ------------------------------------------------------------

# 13. Unique words from user input
words = set(input("Enter five words: ").split())
print("Q13:", words)

# ------------------------------------------------------------

# 14. Difference between sets A and B
A = {'a', 'b', 'c'}
B = {'c', 'd', 'e'}
print("Q14:", A.difference(B))  # Output: {'a', 'b'}

# ------------------------------------------------------------

# 15. Items in room
room_items = {'chair', 'table', 'lamp'}
room_items.add('fan')
print("Q15: Total items:", len(room_items))

























# 1. Favorite fruits
fruits = ['Mango', 'Apple', 'Banana', 'Grapes', 'Orange']
print("Q1: First fruit:", fruits[0])
print("Q1: Last fruit:", fruits[-1])

# ------------------------------------------------------------

# 2. User input: cities visited
cities = input("Enter 3 cities you visited recently (space-separated): ").split()
print("Q2:", cities)

# ------------------------------------------------------------

# 3. Prices above 900 using slicing
prices = [1200, 850, 950, 720]
filtered = [price for price in prices if price > 900]
print("Q3:", filtered)

# ------------------------------------------------------------

# 4. First 5 even numbers + append 12
evens = [2, 4, 6, 8, 10]
evens.append(12)
print("Q4:", evens)

# ------------------------------------------------------------

# 5. Insert 'Python' at second position
languages = ['Java', 'C++', 'Go']
languages.insert(1, 'Python')
print("Q5:", languages)

# ------------------------------------------------------------

# 6. Split sentence into words
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Q6:", words)

# ------------------------------------------------------------

# 7. Remove last month
months = ['Jan', 'Feb', 'Mar', 'Apr']
months.pop()
print("Q7:", months)

# ------------------------------------------------------------

# 8. Copy, sort, reverse
vehicles = ['car', 'bus', 'train']
copy_vehicles = vehicles.copy()
copy_vehicles.sort()
copy_vehicles.reverse()
print("Q8:", copy_vehicles)

# ------------------------------------------------------------

# 9. Count 'apple'
items = ['apple', 'banana', 'apple', 'cherry']
count = items.count('apple')
print("Q9: 'apple' appears", count, "times")

# ------------------------------------------------------------

# 10. Use .format()
name = "Tom"
apples = 3
bananas = 5
print("Q10:", "{} has {} apples and {} bananas".format(name, apples, bananas))

# ------------------------------------------------------------

# 11. List of characters in 'Hello'
chars = list('Hello')
print("Q11:", chars)

# ------------------------------------------------------------

# 12. Sum and average of 3 integers
numbers = [10, 20, 30]
total = sum(numbers)
average = total / len(numbers)
print("Q12: Sum =", total, ", Average =", average)

# ------------------------------------------------------------

# 13. Name to reversed character list
user_name = input("Enter your name: ")
char_list = list(user_name)
char_list.reverse()
print("Q13:", char_list)

# ------------------------------------------------------------

# 14. Check if 'Bob' is in list
names = ['Alice', 'Bob', 'Charlie']
print("Q14: Is 'Bob' in list?", 'Bob' in names)

# ------------------------------------------------------------

# 15. Clear list
words = ['one', 'two', 'three']
words.clear()
print("Q15:", words)  # Output: []































































# 1. First name from full name
full_name = input("Enter your full name: ").strip()
first_name = full_name.split()[0]
print("Q1: First name:", first_name)

# ------------------------------------------------------------

# 2. City name in different cases
city = input("Enter a city name: ").strip()
print("Q2: Uppercase:", city.upper())
print("Q2: Lowercase:", city.lower())
print("Q2: Title case:", city.title())

# ------------------------------------------------------------

# 3. Reverse 'Technology'
word = 'Technology'
print("Q3:", word[::-1])  # Output: ygolonhceT

# ------------------------------------------------------------

# 4. Combine 'Data' and 'Science'
combined = 'Data' + '-' + 'Science'
print("Q4:", combined)  # Output: Data-Science

# ------------------------------------------------------------

# 5. Format product price
price = float(input("Enter product price: "))
print("Q5: ₹{:.2f}".format(price))  # Output: ₹1200.00

# ------------------------------------------------------------

# 6. Name and age with f-string
name = "Rahul"
age = 25
print(f"Q6: My name is {name} and I am {age} years old.")

# ------------------------------------------------------------

# 7. Check if 'Python' is in sentence
sentence = "Python is awesome"
print("Q7:", 'Python' in sentence)  # Output: True

# ------------------------------------------------------------

# 8. Character count excluding spaces
user_sentence = input("Enter a sentence: ").strip()
print("Q8: Character count:", len(user_sentence))

# ------------------------------------------------------------

# 9. Add 5% tax to price
price = 200
price += price * 0.05
print("Q9: Final price with tax:", price)  # Output: 210.0

# ------------------------------------------------------------

# 10. Check characters in name
name = 'Alice'
print("Q10: 'i' in name?", 'i' in name)
print("Q10: 'z' not in name?", 'z' not in name)

# ------------------------------------------------------------

# 11. Average of test scores
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
average = (score1 + score2 + score3) / 3
print("Q11: Average score:", round(average, 2))

# ------------------------------------------------------------

# 12. BMI calculation
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))
bmi = weight / (height ** 2)
print("Q12: Your BMI is:", round(bmi, 2))

# ------------------------------------------------------------

# 13. Print 'love' from string
text = "I love Python!"
print("Q13:", text[2:6])  # Output: love

# ------------------------------------------------------------

# 14. Replace 'bad' with 'good'
sentence = "This is a bad idea."
print("Q14:", sentence.replace("bad", "good"))

# ------------------------------------------------------------

# 15. Identity operator
a = 1000
b = 1000
print("Q15: a is b?", a is b)  # Output may vary (True or False depending on memory optimization)










































































































