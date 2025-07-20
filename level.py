# 1..Find maximum of two numbers 
# a=100
# b=200
# if a>b :
#     print("a is greater")
# elif a<b:
#     print("b is greater")

 
# if a>b:
#     max=a
# else:
#     max=b
    
# print("max num is",max)

# a=int(input("enter 1st num"))
# b=int(input("enter 2nd num"))

# if a>b:
#     max=a
# else:
#     max=b
    
# print("max num is",max)
 
 
 
 # 2..Find maximum of three numbers 
# a=100
# b=80
# c=90



# if a>b:
#     max=a
# elif b>a:
#     max=b
# else:
#     max=c
# print(max)

# a = 10
# b = 25
# c = 15

# if a >= b and a >= c:
#     print("Maximum is:", a)
# elif b >= a and b >= c:
#     print("Maximum is:", b)
# else:
#     print("Maximum is:", c)



#3..Check whether given number is positive, negative or zero
# a=int(input("enter numbr"))
# if a>0:
#     print("number is positive")
# elif a<0:
#     print("number is negative")
# else:
#     print("zero")




# 4.. check wheter geive nm even or odd
# num=13
# # for i in num:
# if num%2==0:
#     print("even")
# elif num%2!=0:
#      print("odd")
# else:
#     print("negatie")


#5.. Check whether a number is leap year or not 
# year=[1000,1100,1900,1200,2000,1600,1800]
# year=int(input("entr y"))

# # for y in year:
# if year%4==0:
#     print("leap")
# else:
#     print("not leap year")


# #6 Check whether a character is alphabet or not 
# a=input("enter something")
# if a.isalpha():
#     print("its alphabet")
# else:
#     print("not alpha")



# 7..Input any alphabet and check whether it is vowel or consonant 
# vowel=set("aeiou")
# user=input("entr word:")
# if user in vowel:
#     print("v")
# else:
#     print("c")

# ch = input("Enter any alphabet: ")

# if len(ch) == 1 and ch.isalpha():
#     if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
#         print(ch, "is a vowel")
#     else:
#         print(ch, "is a consonant")
# else:
#     print("Invalid input. Please enter a single alphabet.")
    


# 8.. Input any character and check whether it is alphabet, digit or special character 
# user=input("enter something:(click y to exit)")
# # while True:
# if user.isalpha():
#     print("a")
# elif user.isdigit():
#     print("d")
# # elif user==y:
# #     print("exit")
# #     break
# else:
#     print("s")










# 11...Input month number and print number of days in that month 
# month=input('enter month number(1-12)')
# if month==1:
#     print("jan:30 day")
# elif month==2:
#     print("feb: 30 day")    
# elif month==3:
#     print("march: 30 day")
# elif month==4:
#     print("april: 30 day")
# elif month==5:
#     print("may: 30 day")
# elif month==6:
#     print("june: 30 day")
# elif month==7:
#     print("july: 30 day")
# elif month==8:
#     print("aug: 30 day")
# elif month==9:
#     print("sep: 30 day")
# elif month==10:
#     print("oct: 30 day")
# elif month==11:
#     print("nov: 30 day")
# elif month==12:
#     print("dec: 30 day")
# # else:
# #     print("invalid")


# import signal

# class MyTimeout(Exception):
#     pass

# def handler(signum, frame):
#     print('Signal handler called with signal', signum)
#     raise MyTimeout

# try:
#     signal.signal(signal.SIGALRM, handler)
#     signal.alarm(5)
#     number = input("Divide by (5 sec):")
#     signal.alarm(0)   
#     print(42/int(number))
# except MyTimeout:
#     print('timeout')
# except Exception as e:
#     print(e)
#     #raise

# print("Still working")

# def my_sum(*numbers):
#     s = 5
#     for number in numbers:
#         s += int(number)
#     return s
# my_sum()

# 12.. count total number of note in given amount
# amount=[10,20,30,40,50,60,70,80,90,100,200,500,1000,2000]
# total=[]
# for i in amount:
#     total.append(i)
    
# print(total)

# amount = int(input("Enter the amount: "))

# notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# print("Currency Note Count:")
# for note in notes:
#     count = amount // note
#     if count > 0:
#         print(f"{note} x {count}")
#         amount = amount % note
#  Explanation:
# We divide the amount starting from the highest note.

# amount // note gives how many notes we can use.

# Then we reduce amount = amount % note.

# Let me know if you want the total number of notes used or to skip coins (1, 2 ₹).

# word="md rashid"
# word2="me k","is s","bety"

# print(len(word))

# print(word.count("d"))
# print(word.find("a"))
# print(word.split(","))
# print(word.split())
# print(word.replace("md","mm"))
# print(word.rstrip())
# print(" ".join(word2))

# 13..input all angles of triagl e and check whether triagle
# valid or not

# Input all three angles of the triangle
# angle1 = float(input("Enter first angle of the triangle: "))
# angle2 = float(input("Enter second angle of the triangle: "))
# angle3 = float(input("Enter third angle of the triangle: "))

# # Check if the sum of angles is 180 and all angles are greater than 0
# if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
#     print("The triangle is valid.")
# else:
#     print("The triangle is not valid.")


#14..input all side of triagle and check wherthr triagle is
# equilatral,isoscele or scalene triagle or not




#15.. find all root of quadric equation
# ax**+bx+c=0
# import math

# a=float(input("enter coefficient a:"))
# b=float(input("enter coefficient b:"))
# c=float(input("enter coefficient c:"))

# #calculate discriminant
# d=b**2-4*a*c

# #check conditions
# if a==0:
#     print("this is not a quadratic equation.")
# elif d>0:
#     root1=(-b + math.sqrt(d))/(2*a)
#     root2=(-b -math.sqrt(d))/(2*a)
#     print("two real and distinct roots:",root1,"and",root2)
# elif d==0:
#     root=-b/(2*a)
#     print("two real and equal roots",root,"and",root)
# else:
#     real_part=-b/(2*a)
#     imag_part=math.sqrt(-d)/(2*a)
#     print("two complex root:")
#     print(f"{real_part}+{imag_part}i")
#     print(f"{real_part}-{imag_part}i")



#16..addition of tow number without addition operator
# def add(x,y):
#     while y!=0:
#         carry=x&y
#         x=x^y
#         y=carry<<1
#     return x
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# result=add(num1,num2)
# print(result)


#17..programe to print how many input are given by user
# Input a line of numbers or words separated by space
# user_input = input("Enter values separated by space: ")

# # Split the input string into list elements
# values = user_input.split()

# # Count the number of inputs
# count = len(values)

# # Display the result
# print("Number of inputs given by user:", count)


# userr_inputt=input("dog")
# values=userr_inputt.split()
# count=len(values)
# print("number of input given by user",count)

#18..programe to find return value of print f and scan f
x = print("Hello")
print("Return value of print() is:", x)

#19.. c program to find ascii value of a character
ch = input("Enter a character: ")

# Check if input is a single character
if len(ch) == 1:
    print(f"The ASCII value of '{ch}' is {ord(ch)}")
else:
    print("Please enter only a single character.")


ch = input("Enter a character: ")
print("ASCII value is:", ord(ch))


ch = input("Enter a character: ")
print("ASCII value of '{}' is {}".format(ch, ord(ch)))



ch = input("Enter a character: ")
print(f"ASCII value of '{ch}' is {ord(ch)}")

#20.. c program to complete quotient t remainder
# Take two numbers as input
dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

# Calculate quotient and remainder
quotient = dividend // divisor
remainder = dividend % divisor

# Display the result
print("Quotient =", quotient)
print("Remainder =", remainder)

# // gives the quotient (integer division).

# % gives the remainder (modulus operator).


a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

q, r = divmod(a, b)

print("Quotient =", q)
print("Remainder =", r)



def find_quotient_remainder(x, y):
    return x // y, x % y

a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

q, r = find_quotient_remainder(a, b)

print("Quotient =", q)
print("Remainder =", r)




#21.. programm to find the size of int , float double and char
import sys

# Define sample variables
i = 0              # int
f = 0.0            # float
c = 'a'            # char
d = 0.0            # double (Python float is equivalent to C double)

# Print their sizes
print("Size of int:", sys.getsizeof(i), "bytes")
print("Size of float:", sys.getsizeof(f), "bytes")
print("Size of char:", sys.getsizeof(c), "bytes")
print("Size of double:", sys.getsizeof(d), "bytes")

# Size of int: 28 bytes
# Size of float: 24 bytes
# Size of char: 50 bytes
# Size of double: 24 bytes


import sys

# Define sample variables
i = 0              # int
f = 0.0            # float
c = 'a'            # char
d = 0.0            # double (Python float is equivalent to C double)

# Print their sizes
print("Size of int:", sys.getsizeof(i), "bytes")
print("Size of float:", sys.getsizeof(f), "bytes")
print("Size of char:", sys.getsizeof(c), "bytes")
print("Size of double:", sys.getsizeof(d), "bytes")


#22 program to demonstrate the working of keyword long
# Small integer (like normal int in C)
a = 100
print("a =", a)
print("Type of a:", type(a))

# Very large integer (like long or long long in C)
b = 98765432101234567890123456789012345678901234567890
print("b =", b)
print("Type of b:", type(b))

# Check size in bytes
import sys
print("Size of a in bytes:", sys.getsizeof(a))
print

#23..program to swap two nnumbersw
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping using temp variable
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# 24..Program to generate multiplication table 
num = int(input("Enter a number: "))

print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")



num = int(input("Enter a number: "))
i = 1

print(f"Multiplication Table of {num}:")
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1


# 25..Program to display Fibonacci series 
n = int(input("How many terms? "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b


def fibonacci_list(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

n = int(input("Enter number of terms: "))
print(fibonacci_list(n))



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("How many terms? "))
for i in range(terms):
    print(fibonacci(i), end=' ')



# 26..Program to find GCD of two number 
import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = math.gcd(a, b)
print(f"GCD of {a} and {b} is {gcd}")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(f"GCD of {a} and {b} is {gcd}")


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"GCD of {a} and {b} is {find_gcd(a, b)}")


# # 27..Program to find LCM of two numbers 📌 Formula:
# LCM(a, b) = (a × b) / GCD(a, b)
import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = (a * b) // math.gcd(a, b)
print(f"LCM of {a} and {b} is {lcm}")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

max_num = max(a, b)

while True:
    if max_num % a == 0 and max_num % b == 0:
        lcm = max_num
        break
    max_num += 1

print(f"LCM of {a} and {b} is {lcm}")


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"LCM of {a} and {b} is {lcm(a, b)}")



#28.. Program to display characters from A to Z using loop 
print("Alphabets from A to Z:")

for i in range(65, 91):  # ASCII value of 'A' is 65, 'Z' is 90
    print(chr(i), end=' ')


import string

print("Alphabets from A to Z:")
for ch in string.ascii_uppercase:
    print(ch, end=' ')

# 29..Program to calculate the power of a number using loop 
base = int(input("Enter base number: "))
exponent = int(input("Enter exponent (positive integer): "))

result = 1
for _ in range(exponent):
    result *= base

print(f"{base} ^ {exponent} = {result}")



base = float(input("Enter base number: "))
exponent = int(input("Enter exponent: "))

result = 1
for _ in range(abs(exponent)):
    result *= base

if exponent < 0:
    result = 1 / result

print(f"{base} ^ {exponent} = {result}")


# 30..Program to reverse a number 
num = int(input("Enter a number: "))
rev = 0

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(f"Reversed number is: {rev}")


num = input("Enter a number: ")
reversed_num = num[::-1]

print(f"Reversed number is: {reversed_num}")

num=int(input("enter a num"))
rev=0
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num//=10

print(f"Reversed number is: {rev}")

#31.. Program to check whether a number is palindrome or not 
# A palindrome number reads the same forward and backward.
# 📌 Examples: 121, 1331, 12321 are palindromes; but 123, 1245 are not. 
num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")



num = input("Enter a number: ")

if num == num[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")


# 32..Program to display prime numbers between 1 to n 
# A number greater than 1 that has no positive divisors other than 1 and itself.
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


#33.. Program to check whether number is prime or not 
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # Only check up to √num
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")


#34 Program to check whether number is Armstrong or not 
# An Armstrong number (also known as a narcissistic number) 
# of n digits is a number such that the sum of its digits each
# raised to the power n equals the number itself.
# 153 → 1³ + 5³ + 3³ = 153 ✅

# 9474 → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 ✅

# 123 → 1³ + 2³ + 3³ = 36 ❌
num = int(input("Enter a number: "))
digits = str(num)
power = len(digits)

sum_of_powers = sum(int(digit) ** power for digit in digits)

if num == sum_of_powers:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
    
    
    
    
    num = int(input("Enter a number: "))
temp = num
power = len(str(num))
sum_of_digits = 0

while temp > 0:
    digit = temp % 10
    sum_of_digits += digit ** power
    temp //= 10

if num == sum_of_digits:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")



num = int(input("Enter a number: "))
digits = str(num)
power = len(digits)
sum_of_digits = 0

for d in digits:
    sum_of_digits += int(d) ** power

if num == sum_of_digits:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")



def is_armstrong(n):
    power = len(str(n))
    temp = n
    result = 0
    while temp > 0:
        digit = temp % 10
        result += digit ** power
        temp //= 10
    return result == n

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")



# 35..Program to check Armstrong numbers between two intervals 
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

print(f"Armstrong numbers between {lower} and {upper} are:")

for num in range(lower, upper + 1):
    power = len(str(num))
    sum_of_digits = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit ** power
        temp //= 10

    if num == sum_of_digits:
        print(num, end=' ')


#36.. Program to check whether given number is strong or not 
# A Strong number is a number for which the sum of the factorial of its digits is equal to the number itself.

# 📌 Examples:

# 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145 ✅

# 123 → 1! + 2! + 3! = 1 + 2 + 6 = 9 ❌
import math

num = int(input("Enter a number: "))
temp = num
sum_of_factorials = 0

while temp > 0:
    digit = temp % 10
    sum_of_factorials += math.factorial(digit)
    temp //= 10

if sum_of_factorials == num:
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")




def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
temp = num
sum_of_fact = 0

while temp > 0:
    digit = temp % 10
    sum_of_fact += factorial(digit)
    temp //= 10

if sum_of_fact == num:
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")



import math

def is_strong(n):
    return n == sum(math.factorial(int(d)) for d in str(n))

num = int(input("Enter a number: "))

if is_strong(num):
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")



#  Program to check strong number between two intervals 
#  A Strong number is a number in which the sum of the factorial of its digits is equal to the number itself.

# Example: 145 → 1! + 4! + 5! = 145 ✅


import math

# Input range
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

print(f"Strong numbers between {lower} and {upper} are:")

for num in range(lower, upper + 1):
    sum_of_fact = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_of_fact += math.factorial(digit)
        temp //= 10

    if sum_of_fact == num:
        print(num, end=' ')



# 38..Program to check prime or Armstrong number using user defined function 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    power = len(str(n))
    sum_of_powers = sum(int(digit) ** power for digit in str(n))
    return sum_of_powers == n

# Input from user
num = int(input("Enter a number: "))

# Check prime
if is_prime(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is not a Prime number.")

# Check Armstrong
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")



# 39*..Program to check a number can be expressed as sum of two prime numbers or not 
# A number n can be expressed as the sum of two prime numbers if there exist two primes p1 and p2 such that:
 def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input number
num = int(input("Enter a number: "))

found = False
print(f"Checking if {num} can be expressed as sum of two prime numbers:")

for i in range(2, num // 2 + 1):
    if is_prime(i) and is_prime(num - i):
        print(f"{num} = {i} + {num - i}")
        found = True

if not found:
    print(f"{num} cannot be expressed as the sum of two prime numbers.")




def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def can_be_expressed_as_sum_of_two_primes(n):
    for i in range(2, n):
        if is_prime(i):
            if is_prime(n - i):
                return (i, n - i)
    return None

# --- Main Program ---
number = int(input("Enter a number: "))

result = can_be_expressed_as_sum_of_two_primes(number)

if result:
    print(f"{number} can be expressed as the sum of two prime numbers: {result[0]} + {result[1]}")
else:
    print(f"{number} cannot be expressed as the sum of two prime numbers.")





# 40..Program to find sum of natural numbers using recursion 
# ✅ Key Points:
# Natural numbers are positive integers (no decimals or fractions).

# They are used for counting things (like apples, students, etc.).

# 0 is not a natural number in most definitions.

# They do not include negative numbers.

def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

# Input from user
num = int(input("Enter a positive number: "))

if num <= 0:
    print("Please enter a positive integer.")
else:
    total = sum_natural(num)
    print(f"Sum of first {num} natural numbers is: {total}")



# Function to calculate sum using recursion
def find_sum(n):
    return 0 if n == 0 else n + find_sum(n - 1)

# Main program starts here
def main():
    num = int(input("Enter a positive integer: "))
    
    if num < 0:
        print("Invalid input! Please enter a positive number.")
    else:
        total = find_sum(num)
        print(f"Sum of first {num} natural numbers is: {total}")

# Calling main function
main()
