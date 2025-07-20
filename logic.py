# # 1. Remove all non-alphabet characters from 'H3ll0_Wor!ld#2025'.
# #  Expected Output: 'HllWorld'
# ab='H3ll0_Wor!ld#2025'
# l=[]
# for i in ab:
#     if i.isalpha():
#         l.append(i)
# print(l)

# l=[]
# for i in ab:
#     if i.isalpha():
#         l+=str(i)
# print(l)



# ab='H3ll0_Wor!ld#2025'
# ba=str(ab)
# l=[]
# for i in ba:
#     if i.isalpha():
    
#         l.append(i)
# print(l)



# # 2.find sum of digit in this strings
# s="abc12def34gh5"
# total=0
# for ch in s:
#     if ch.isdigit():
#         total+=int(ch)
# print(total) 

# s="abc12def34gh5"
# temp=""
# total=0
# for ch in s:
#     if ch.isdigit():
#         temp += ch
#     else:
#         if temp !="":
#             total +=int(temp)
#             temp =""
# if temp:
#     total+=int(temp)
# print(total)



# # 3.. character common in both the string
# a="apple"
# b="plead"
# co=[]
# for ch in a:
#     if ch in b!=a:
#         co.append(ch) 
# c=set(a)
# d=set(b)
# common=c&d
# print(common)
# print(ch)


# #find max num
# a,b,c=10,25,15
# if a>b:
#     print(" a is gr")
# elif b>c:
#     print("b is gt")
# else:
#     print("c is gt") 
    



# s="swiss"
# #find the first non reapeating char in string
# for i in s:
#     if s.count(i)==1:
#         print(i)
#         break

# # counter balance
# s="((()))"
# balance=0
# for i in s:
#     if i=="(":
#         balance+=1
#     elif i==")":
#         balance-=1
    
#     if balance<0:
#         print("un")
#         break
# else:
#     print("balanced" if balance==0 else"unbalace")





# """2. Find the most frequent word in the sentence: 'cat dog dog bird cat cat'.
#  Expected Output: 'cat'"""
 
# sentence="cat","dog","dog","bird","cat","cat"
# for a in sentence:
#     if sentence.count(a)!=1:
#         print(a)
#         break



# # 3. Return the index of the first vowel in the string 'crypt'.
# #  Expected Output: -1 (no vowels found)
# a="crypt"
# b="a","e","i","o","u"
# for i in a :
#     if b in i:
#         print(i)



# # u have a list of integer
# # i need a function of 2nd largest number in list
# numbers=[10,20,5,8,40]
# numbers.sort(reverse=True)
# print(numbers[1])


# for  num in numbers:
#     if numbers.max(num):
#         print(num)




# # print even number from a list without using loop
# nums=[1,2,8,68,9,45,9,4]
# word="beautiful"

# def print_char(word,i):
#     if i>=len(word):
#         return
    
#     print(word[i])
#     print_char(word,i+1)

# print_char(word,0)
    
# def print_even(nums,i):
#     if i>=    len(nums):
#         return
#     if nums[i]%2==0:
#         print(nums[i])
#     print_even(nums,i+1)

# print_even(nums,0)


# x,y=0,0
# while True:
#     movement=input().strip()
#     if not movement:
#         break 
    
#     parts=movement.split()
#     direction=parts[0]
#     steps=int(parts[1])
    
#     if direction=="UP":
#         y+=steps
#     elif direction=="DOWN":
#         y-=steps
#     elif direction=="LEFT":
#         x-=steps
#     elif direction=="RIGHT":
#         x+=steps
        
# # print(x,y) 
# squared=x*x+y*y
# distance=squared**0.5
# print(distance)

# # sort tuples
# # tom,19,80
# # john,20,90
# # jony,17,91
# # anton,17,93
# # json,21,85








# # 8. count the vowel in string
# count=0
# vowel=set("aeiou")
# words="geourgeous"
# for char in words:
#     if char in vowel:
#         count+=1
# print(count)

# #9  count upper and lower case in strings
# text="Service Based Companies Morgo ham ban Non"
# count=0
# for char in text:
#     if char.isupper():
#         count+=1
# print(count)

# def count_cases_in_string(text):
#     upper=0
#     lower=0
#     # upper=lower=0
    
#     for char in text:
#         if char.isupper():
#             upper+=1
#         elif char.islower():
#             lower +=1
#     return upper, lower
    
# lower,upper=count_cases_in_string(text)
# print(f"lower:{lower}, upper:{upper}")

#     # check anagram in string \
# word1="listen"
# word2="silent"

# def check_anagram(w1,w2):
#     return sorted(w1)==sorted(w2)
# print(check_anagram(word1,word2))
            
# # check missing number form  in a list given 1 to n
# number=[1,2,3,4,6]
# def find_missing_number(nums,n):
#     expected_sum=n*(n+1)//2
#     actual_sum=sum(nums)
#     return expected_sum-actual_sum
    
    
# print(find_missing_number(number,6))




# # move all zero to end while maintaing order non zero elements
# num=[0,1,0,3,12]
# for n in num:
#     if n==0:
#         num.remove(n)
#         num.append(0)

# print(num)

# # find duplicate number in a list
# numb=[1,3,4,2,2,2]
# def find_duplicate(numb):
#     items=set()
#     for n in numb:
#         if n in numb:
#             return n
#         items.add(n)

# print(find_duplicate(numb))


# # find if a string in a palindrome
# word="malayalam"


 
 
# for i in range(1,6):
#      print("1"*i)
     
     
     
# n=5
# for i in range(1,n+1):
#     print(" "*(n-1)+"*"*(2*i-1))



# n=5 

# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))
    
# v=7

# for a in range(1,v+1):
#     print(""*(v-a)+"*"*(2*a-1))#


# # *
# # ***
# # *****
# # *******
# # *********
# # ***********
# # *************

# a=[1,2,3]
# b=a
# a.append(4)
# print(b)

# a=1
# b=a
# a+=1
# print(b)


# x=0.1+0.2==0.3     #0.1+0.2=0.30000000000004

# print(x)#false 0.3000000004!=0.3 = false


# def func(val,lst=[]):
#     lst.append(val)
#     return lst

# print(func(1))
# print(func(2))
# print(func(3))

     
# def ab(c,d=["a"]):
#     d.append(c) #  items=set()
#     return d

# print(ab(2))
# print(ab(4))
# print(ab(6))


# x=[1,2,3]
# y=x
# x+=[4]
# print(x)
# print(y)

# x=1000
# y=1000
# print(x==y)
# # print(x is y) True True

# print((False==False)==False)# False

# a="python"
# print(a[3:3])

# x=[0]
# print(x*5==[0,0,0,0,0])
# print(x*5 is [0,0,0,0,0])


# print("5"+3)#error
# print([5]*3)

# print("5"*3)#555
# print([5]*3)#[5,5,5]


# print(bool("abcd"))#true
# print(bool(""))#false

# x="python"
# print(x[0:3]+x[-1:-4:-1])#pytnoh

# x=10
# def f():
#     print(x)
#     x=5
# f()#error


# for i in range(1,6):
#     print("*"*i)

# n=5
# for i in range(1,n+1):        #n=5, i=1
#     print(" "*(n-i)+"*"*(2*i-1))
#         #    (5-1=4)          (2*1-1=1)
# #   " " * 4 + "*" * 1         
# # "    "+ *
# # "   "+ *
# # "  "+ *



# find the intersection common element of two list.
# list1=[1,2,4,5,6]
# list2=[4,5,6,7,8]
# def intersection(lst1,lst2):
#     common_list=[]
#     for i in lst1:
#         if i in lst2 and i not in common_list:
#             common_list.append(i)
#     return common_list

# print(intersection(list1,list2))

# def intersection_comprehension(lis1,lis2):
#     return[item for item in lis1 if item in lis2]

# print(intersection_comprehension(list1,list2))


# # find most frequent element in list.
# numbers=[1,2,3,4,5,2,2,3,3,4,4,4]
# def most_frequent(lst):
#     max_count=0
#     most_frequent=None
#     for item in lst:
#         count=lst.count(item)
#         if count>max_count:
#             max_count=count
#             most_frequent=item 
#     return most_frequent
# print(most_frequent(numbers))

# find cumulative sum of list
# number=[1,2,3,4] 
# def cumulative_sum(lst):
#     cum_sum=[]
#     total=0
#     for num in lst:
#         total +=num
#         cum_sum.append(total)
#     return cum_sum

# print(cumulative_sum(number))

# # find missing number
# def find_missing_number(lst, n):
#     for i in range(1, n + 1):
#         if i not in lst:
#             return i

# # Example usage
# lst = [1, 2, 4, 5]
# n = 5
# print("Missing number:", find_missing_number(lst, n))  # Output: 3

# def find_missing_number(lst, n):
#     total = n * (n + 1) // 2
#     return total - sum(lst)

# # Example:
# lst = [1, 2, 4, 5, 6]  # Missing number is 3
# n = 6
# print("Missing number:", find_missing_number(lst, n))



# #remove duplicate from a list
# fruits=["apple","banana","cherry","apple","banana"]
# # def remove_duplicate(lst):
# #     uni=[]
# #     seen=set()
# #     for i in lst:
# #         if i not in seen:
# #             uni.append(i)
# #             seen.add(i)
# #     return uni
# # print(remove_duplicate(fruits))

# print(list(set(fruits)))

# # find the index of element in a tuple
# my_tuple=(1,2,3,4)
# def find_index(tup,ele):
#     return tup.index(ele) if ele in tup  else -1

# print(find_index(my_tuple,3))

# #find the most frequent value in a list
# data={"a":1, "b":2,"c":3,"d":1,"e":1}
# def most_frequent(dct):
#     frequency={}
#     for val in dct.values():
#         if val not in frequency:
#             frequency[val]=0
#         frequency[val]+=1
#     max_val=max(frequency, key=frequency.get)
#     return max_val

# print(most_frequent(data))    



# # merge dictionary with summation
# dict1={"a":10,"b":20,"c":30}
# dict2={"b":15,"c":35,"d":25}

# def merge_dictionary(dict1,dict2):
#     result=dict1.copy
#     for key,value in dict2.items():
#         if key in result:
#             result[key]+=value
#         else:
#             result[key]=value
#     return result

# print(merge_dictionary(dict1,dict2))

# # find the missing num from a list
# def find_missing_num(arr,n):
#     xor1=0
#     xor2=0
    
#     for i in range(1,n+1):
#         xor1^=i
    
#     for num in arr:
#         xor2^=num
#     return xor1^xor2
# arr=[1,2,4,5]
# n=5
# print("missing num is:",find_missing_num(arr,n))
# #xor works as: x^x=0 , x^0=x


# def find_missing_number(arr,n):
#     for i in range(1,n+1):
#         if i not in arr:
#             return i
# arr=[1,2,3,4,5,6,7,8,9,10,11,13,15,17]
# n=17
# print("missing num is:",find_missing_number(arr,n))

# numb=[1,2,3,4,5,6,7,8,9,10,11,13,15,17]
# def find_missing(nums,n):
#     es=n*(n+1)//2
#     ac=sum(nums)
#     return es-ac
# print("find missing",find_missing(numb,17))

# arr=[1,2,3,4,5,6,7,8,9,10,11,13,15,17]
# n=17
# def find_all_missing(arr,n):
#     full_set=set(range(1,n+1))
#     arr_set=set(arr)
#     missing=sorted(full_set-arr_set)
#     return missing
# print("missing num are:",find_all_missing(arr,n))


# def find_m(arr,n):
#     missing=[]
#     for i in range(1,n+1):
#         if i not in arr:
#             missing.append(i)
#     return missing
# arr=[1,2,3,4,5,6,7,8,9,10,11,13,15,17]
# n=17
# print("missing numbers are;",find_m(arr,n))

#find duplicate ele in list
nums=[1,2,3,2,2]
def find_duplicate(nums):
    itmes = set()
    for i in nums:
        if i in itmes():
            return i
        itmes.add(i)

print(find_duplicate(nums)) 