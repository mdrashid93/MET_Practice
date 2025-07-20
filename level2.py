# # 1. Find maximum of two numbers
# a=int(input("enter first number"))
# b=int(input("enter second number"))

# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")
    
# # 62 program to find length of string
# b=input("enter a sen:-")
# length=len(b)
# print(length)

# a="generater"
# print(len(a))

# # 61. Program to remove all characters in a string except alphabets
# a=input("enter a string:-")
# b=""
# for i in a:
#     if i.isalpha():
#         b+=i
# print(b)

# # program to remove small  character in strings.
# character=input("enter a string:-" )
# stored_value=""
# for b in character:
#     if not b.islower():# condition false
#         stored_value+=b
# print(stored_value)

# 84. Read an array and search for an element

# #read array sizze
# n=int(input("enter number of element in array:"))
# #read ele into array
# arr=[]
# print("enter the element:")
# for i in range(n):
#     element=int(input())
#     arr.append(element)
    
# #input element to search
# search=int(input("enter element to search:"))

# #search for element
# found=False
# for i in range(n):
#     if arr[i]==search:
#         print(f"ele {search} found at position {i}")
#         found=True
#         break
# if not found:
#     print(f"ele {search} not found in the array.")


# 50. Program to calculate average] using arrays

#read number of elements
# n=int(input("enter number of elements:"))
# #read elements into list
# num=[]
# print("enter the number:")
# for i in range(n):
#     nums=float(input())
#     num.append(nums)
# #calculate sum and average
# total=sum(num)
# average=total/n
# #print result
# print("sum:",total)
# print("average:",average)

# m=int(input("enet the number of elements"))
# print("enter the numbers")
# numbers=[]
# for i in range(m):
#     num=int(input())
#     numbers.append(num)
# total=sum(numbers)
# average=total/m
# print("total sum",total)
# print("average:",average)

# # 51. Program to find largest element in an array
# n=int(input("enter number of elements"))
# arr=[]
# print("enter the elements")
# for i in range(n):
#     b=float(input())
#     arr.append(b)
# #print largest ele
# max_ele=arr[0]
# for i in range(1,n):
#     if arr[i]>max_ele:
#         max_ele=arr[i]
# print("largest ele in the array is:",max_ele)


# # 89 Find the reverse of a string
# text=input("enter a string")
# reversed_text=text[::-1]
# print("reversed string is:",reversed_text)

# text=input("enter a string:")
# reversed_text=""
# for char in text:
#     reversed_text=char+reversed_text#add each char to the front
# print("reversed string is",reversed_text)


# 73. Calculate sum of digits# input123456 #output 21
# num=int(input("enter a num:"))
# #initialize sum
# total=0
# #extract and add digits
# while num>0:
#     digit=num%10
#     total+=digit
#     num=num//10
# print("sum of digit is total",total)


# # 43. Program to display factors of a number
# num=int(input("enter a num:-"))
# print(f"factors of {num} are.")
# for u in range(1,num+1):
#     if num%u==0:
#         print(u)

# import math
# n=int(input("enter num"))
# print(f"factors of {n} are")
# for i in range(1,int(math.sqrt(n))+1):
#     if n%i ==0:
#         print(i)
#         if i !=n//i:
#             print(n//i)

# # 52. Program to calculate standard deviation
# #Standard deviation measures how spread out the numbers are from the mean (average).
# numbers=[10,20,30,40,50]
# #calculate the mean(average)
# mean=sum(numbers)/len(numbers)
# # Calculate the squared differences from the mean
# squared_diffs=[(x-mean)**2 for x in numbers]
# #Calculate variance (average of squared differences)
# variance=sum(squared_diffs)/len(numbers)
# #take swuare root of variance to get standard deviation
# std_deviation=variance**0.5
# print("standard deviation is:",std_deviation)

# import geocoder

# # Get current location based on IP
# location = geocoder.ip('me')
# print("Your location:")
# print(location.latlng)  # Latitude and Longitude
# print(location.city, location.state, location.country)


# 88. Find reverse of an array
# # Original array
# arr = [1, 2, 3, 4, 5]

# # Reverse using slicing
# reversed_arr = arr[::-1]

# print("Original array:", arr)
# print("Reversed array:", reversed_arr)
# a=[1,2,3,4,5,6,7,8,9]
# reverseda=a[::-1]
# print(reverseda)

# b=[9,8,7,6,5,4,3,2,1]
# revers=[]
# for i in range(len(b)-1,-1,-1):
#     revers.append([i])
# print(revers)

# 95. Program to Find Sum of Rows and Columns of a Matrix in Python
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# rows=len(matrix)
# cols=len(matrix[0])
# #sum of each row
# print("sum of each row")
# for i in range(rows):
#     row_sum=sum(matrix[i])
#     print(f"row {i+1}:{row_sum}")

# #sum of each column
# print("\n sum of each column:")
# for j in range(cols):
#     cols_sum=0
#     for j in range(rows):
#         cols_sum+=matrix[i][j]
# print(f"clumn{j+1}:{cols_sum}")

#57. programe to swap number in cyclic order using call by refrence
# a=1,b=2,c=3
#after swapping a=3,b=1,c=2
# ini=ab,bc,ca
# def cyclic_swap(numbers):
#     numbers[0],numbers[1],numbers[2]=numbers[2],numbers[0],numbers[1]
# #main program 
# nums=[1,2,3]
# print("before swap:",nums)
# cyclic_swap(nums)
# print("after swap:",nums)

# 59. Program to find frequency(reapeated specific num) of characters in a string
# string="hello world"
# freq={}
# for char in string:
#     if char in freq:
#         freq[char]+=1
#     else:
#         freq[char]=1
# print("char frequency:")
# for key,value in freq.items():
#     print(f"{key}:{value}")
# string="hello world"
# frequency={}
# for ch in string:
#     if ch in frequency:
#         frequency[ch]+=1
#     # else: 
#     #     frequency[ch]=1
# for key, value in frequency.items():
#     print(f"{key} : {value}")

# st="hello world"
# fre={}
# for ch in st:
#     if ch in fre:
#         fre[ch]+=1
#     else:
#         fre[ch]=1
# for ch,fre in fre.items():
#     print(f"{ch} : {fre}") 

# 87. (doubt) Find the number of non-repeated elements in an array
# arr=list(map(int,input("enter array elements seprated by space").split()))
# frequency={}
# for num in arr:
#     frequency[num]=frequency.get(num,0)+1

# # count ele that appear only once
# count=0
# for frequency in frequency.values():
#     if frequency==1:
#         count+=1

# print("num of non reapeated ele:",count)

# a=int(input("enter ary ele:"))
# fre={}
# cnt=0
# for n in a:
#     if n in fre:
#         fre.append(n)
# for fre in fre:
#     if fre==1:
#         cnt+=1
# print(cnt)

# i_str=input("ent ele")
# str_lst=i_str.split()
# arr=[]
# for x in str_lst:
#     arr.append(int(x))
# free={}
# for num in arr:
#     if num in free:
#         free[num]+=1
#     else:
#         free[num]=1
# non_rep_c=0
# for val in free.values():
#     if val==1:
#         non_rep_c+=1
# print("num of n0n repeat ele:",non_rep_c)
    

# 86. Print alternate elements in an array
# arr=list(map(int,input("enter arry ele").split()))
# for i in range(0,len(arr),2):
#     print(arr[i],end="")
# arr=input("ele:")
# for i in range(0,len(arr),2):
#     print(arr[i],end=" ")


# 47. Program to convert binary to decimal number and vice versa
# binary=input("enter a binary number:")
# #convert using with base 2
# decimal=int(binary,2)
# print("decimal value:",decimal)

# decimal=int(input("enter decimal:"))
# #convert using bin() and remove "0b" prefix
# binary=bin(decimal)[2:]
# print(binary)


# 45. Program to find factorial of a number using recursion
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# num=int(input("enter a num:"))
# if num<0:
#     print("factorial not defined for negative number.")
# else:
#     result=fact(num)
#     print(f"factorial of {num} is {result}")
    
    
#     # Program to find factorial using recursion

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Input from user
# num = int(input("Enter a number: "))

# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     result = factorial(num)
#     print(f"Factorial of {num} is {result}")

# 49. Program to reverse a sentence using recursion
# def reverse(sentence):
#     if len(sentence.strip().split())<=1:
#         return sentence
#     else:
#         words=sentence.strip().split()
#     return"".join(words[-1:]) +" "+reverse(" ".join(words[:-1]))
# sentence=input("enter a sentence:")
# reversed=reverse(sentence)
# print("reversed sentence:",reversed)


# # 68. Program to add two complex numbers by passing structures to a function
# # Define a class to represent a complex number
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

# # Function to add two complex numbers
# def add_complex(c1, c2):
#     return Complex(c1.real + c2.real, c1.imag + c2.imag)

# # Input from user
# r1 = float(input("Enter real part of first complex number: "))
# i1 = float(input("Enter imaginary part of first complex number: "))
# r2 = float(input("Enter real part of second complex number: "))
# i2 = float(input("Enter imaginary part of second complex number: "))

# # Create complex number objects
# num1 = Complex(r1, i1)
# num2 = Complex(r2, i2)

# # Add the complex numbers
# result = add_complex(num1, num2)

# # Display the result
# print(f"Sum = {result.real} + {result.imag}i")



# class Complex:
#     def __ini__(self,real,img):
#         self.real=real
#         self.img=img
# def add_com(d1,d2):
#     return complex(d1.real+d2.real,d1.img+d2.img)
# r1 = float(input("Enter real part of first complex number: "))
# i1 = float(input("Enter imaginary part of first complex number: "))
# r2 = float(input("Enter real part of second complex number: "))
# i2 = float(input("Enter imaginary part of second complex number: "))
# num1=complex(r1,i1)
# num2=complex(r2,i2)
# result=add_com(num1,num2)
# print(f"sum={result.real}+{result.img}i")

# # 69. Program to calculate difference between two time periods
# # Class to store time
# class Time:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

# # Function to convert time to total seconds
# def time_to_seconds(t):
#     return t.hours * 3600 + t.minutes * 60 + t.seconds

# # Function to convert seconds back to time format
# def seconds_to_time(total_seconds):
#     hours = total_seconds // 3600
#     total_seconds %= 3600
#     minutes = total_seconds // 60
#     seconds = total_seconds % 60
#     return Time(hours, minutes, seconds)

# # Function to find difference
# def find_time_difference(t1, t2):
#     sec1 = time_to_seconds(t1)
#     sec2 = time_to_seconds(t2)
#     diff_seconds = abs(sec1 - sec2)  # absolute difference
#     return seconds_to_time(diff_seconds)

# # Input times
# print("Enter first time:")
# h1 = int(input("Hours: "))
# m1 = int(input("Minutes: "))
# s1 = int(input("Seconds: "))

# print("Enter second time:")
# h2 = int(input("Hours: "))
# m2 = int(input("Minutes: "))
# s2 = int(input("Seconds: "))

# # Create time objects
# time1 = Time(h1, m1, s1)
# time2 = Time(h2, m2, s2)

# # Find difference
# diff = find_time_difference(time1, time2)

# # Display result
# print(f"Time Difference = {diff.hours} hours, {diff.minutes} minutes, {diff.seconds} seconds")


# # 74. Calculate product of digits
# # Function to calculate product of digits
# def product_of_digits(n):
#     product = 1
#     while n > 0:
#         digit = n % 10
#         product *= digit
#         n //= 10
#     return product

# # Input from user
# num = int(input("Enter a number: "))

# # If number is 0, product is 0
# if num == 0:
#     print("Product of digits = 0")
# else:
#     result = product_of_digits(num)
#     print("Product of digits =", result)

# 76. Find one’s compliment of a number
# Binary of 5 → 0101 → One's complement → 1010 (which is -6 in Python using ~5)

# # Input from user
# num = int(input("Enter a number: "))

# # One's complement using bitwise NOT
# #negative num in binary
# ones_complement = ~num

# print(f"One's complement of {num} = {ones_complement}")
# num=int(input("ent"))
# once_com=~num
# print(f"one com:{num}={once_com}")



# # 77. Find two’s compliment of a number
# # Formula: Two's complement = ~num + 1
# # Input from user
# num = int(input("Enter a number: "))

# # Two's complement using ~num + 1
# twos_complement = ~num + 1

# print(f"Two's complement of {num} = {twos_complement}")
# num=int(input("ent a nu:"))
# tow_com=~num+1
# print(f"tow com{num}={tow_com}")

# def to_co(num,bits=8):
#     if num>=0:
#         return format(num,f'0{bits}b')
#     else:
#         return format((1<<bits)+ num,f'0{bits}b')

# print("two com of 5:", to_co(5))
# print("toe com of -5",to_co(-5))

#90. Swap consecutive elements in an array
# To swap consecutive elements means we swap every pair of adjacent elements:

# [1, 2, 3, 4, 5, 6] → [2, 1, 4, 3, 6, 5]
# arr=[1, 2, 3, 4, 5, 6]
# for i in range(0,len(arr)-1,2):
#     arr[i],arr[i+1]=arr[i+1],arr[i]
#     print("array after swapping consecutive ele:",arr)

# ar=[10,20,30,40,50,60,70]
# for i in range(0,len(ar)-1,2):
#     ar[i],ar[i+1]=ar[i+1],ar[i]
# print(ar)

# 91. Program to insert new value in the array
# arr=[1,2,3,4]
# arr.append(5)
# print(arr)

# arr=[1,3,4]
# arr.insert(1,2)
# print(arr)

# arr=[10,20,30,50]
# pos=3
# value=40
# arr=arr[:pos]+[value]+arr[pos:]
# print(arr)

# 92. Program to delete an element at desired position from an array
# def delete_ele(arr,pos):
#     if pos<0 or pos>=len(arr):
#         print("invalid position")
#         return arr
#     else:
#         #remove ele using slicing
#         new_arr=arr[:pos]+ arr[pos+1:]
#         return new_arr

# arr=[10,20,30,40,50]
# print("original array:",arr)

# position=int(input("enter the position to delete(0 based index):"))

# arr=delete_ele(arr,position)
# print("array after deletion:",arr)
# arr=list(map(int,input("enter array ele seprated by space:").split()))
# print("original array:",arr)
# #input position to delete
# pos=int(input("enter the position(starting from 0):"))
# #check if position is valid
# if pos <0 or pos>=len(arr):
#     print("invalid position")
# else:
#     deleted_element=arr.pop(pos)
#     print(f"deleted ele:{deleted_element}")
#     print("array after deletion:",arr)
# ✅ 93. Program to find sum of right diagonals of a matrix
# for a square matrix:[
#     [a,b,c],
#     [d,e,f],
#     [g,h,i]
# ]
# #formula ele at matrix[i][n-i-1]
# n=int(input("enterr size of square matrix(n*n):"))
# #input matrix
# matrix=[]
# print("enter matrix row-wise:")
# for i in range(n):
#     row=list(map(int,input().split()))
#     matrix.append(row)
# #calculate sum of right diagonal
# right_diagonal_sum=0
# for i in range(n):
#     right_diagonal_sum+=matrix[i][n-i-1]
# print("sum of right (secondary) diagonal:",right_diagonal_sum)

# ✅ 94. Program to find the sum of left diagonals of a matrix
# # Input matrix size
# n = int(input("Enter size of square matrix (n x n): "))

# # Input matrix
# matrix = []
# print("Enter matrix row-wise:")
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# # Calculate sum of left diagonal
# left_diagonal_sum = 0
# for i in range(n):
#     left_diagonal_sum += matrix[i][i]

# # Output
# print("Sum of left (primary) diagonal:", left_diagonal_sum)


# ✅ 95. Program to find sum of rows and columns of a matrix
#row sums:
# row 0:1+2+3=6
# row 1:4+5+6=15
# row 3:7+8+9=24
#column sum:
# Col 0: 1+4+7 = 12
# Col 1: 2+5+8 = 15
# Col 2: 3+6+9 = 18
#input row and column
# rows=int(input("enter number of rows:"))
# cols=int(input("enter number of cols:"))
#input matrix
# matrix=[]
# print("enter matrix row wise:")
# for i in range(rows):
#     row=list(map(int,input().split()))
#     matrix.append(row)
# #calculate row sums
# print("\nsum of each row:")
# for i in range(row):
#     row_sum=sum(matrix[i])
#     print(f"row{i} sum={row_sum}")
# #calculate col sum
# print("\nsum of each cols")
# for j in range(cols):
#     col_sum=0
#     for i in range(rows):
#         col_sum+=matrix[i][j]
#     print(f"column{j} sum={col_sum}")

#96. Program to accept a matrix and determine whether it is a sparse matrix
# def is_sparse_matrix(matrix):
#     rows=len(matrix)
#     cols=len(matrix[0])
#     total_elements=rows*cols
#     zero_counts=0
#     # count number of zero elements
#     for row in matrix:
#         for val in row:
#             if val==0:
#                 zero_counts+=1
#     #if number of zero > number of non-zero, its sparse
#     if zero_counts>total_elements/2:
#         return True
#     else:
#         return False
# #input matrix size
# rows=int(input("enter number of rows:"))
# cols=int(input("enter the number of cols:"))
# #input matrix ele
# matrix=[]
# print("enter matrix ele row-wise:")
# for i in range(rows):
#     row=list(map(int,input(f"row{i+1}").split()))
    
#     matrix.append(row)
# #display matrix
# print("\nthe entered matrix is:")
# for row in matrix:
#     print(row)
# #check and display result
# if is_sparse_matrix(matrix):
#     print("\n the matrix is sparse matrix.")
# else:
#     print("\n the matrix is not sparse matrix.")
       
def is_sparse_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_elements = rows * cols
    zero_count = 0

    for row in matrix:
        for element in row:
            if element == 0:
                zero_count += 1

    return zero_count > total_elements / 2

# Accept matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Accept matrix elements
print("Enter the elements row-wise:")
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    if len(row) != cols:
        print("Invalid number of elements. Please enter exactly", cols)
        exit()
    matrix.append(row)

# Display matrix
print("\nMatrix:")
for row in matrix:
    print(row)

# Check if sparse
if is_sparse_matrix(matrix):
    print("\n✅ The matrix is a sparse matrix.")
else:
    print("\n❌ The matrix is NOT a sparse matrix.")