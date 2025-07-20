# import numpy as np
# import cv2
# import imutils
# import datetime

# gun_cascade =cv2.cascadeclassifier('cascade.xml')
# camera=cv2.videocapture(0)

# firstframe=None
# gun_exit=None

# while True:
#     ret, frame=camera.read
#     frame=imutils.reasize(frame,width=500)
# a=[1,2,3,3,4,5,6]
# b=[4,4,5,6,7,8,9]
#  #merged
#  #removed duplicate
#  #sort
#  merged=a+b
#  print(merged)
# a=[1,2,3,3,4,5,6]
# b=[4,4,5,6,7,8,9]
 #merged
 #removed duplicate
 #sort
# merged=a+b
# print(merged)
# ms=set(merged)
# print(ms)
# sort=sorted(ms)
# print(sort)

# def merge_ar(a,b):
#     return sorted(set(a+b))
# print(merge_ar(a,b))

# card_number=8986301198
# number_string=str(card_number)
# star="*"*(len(number_string)-4)
# print(star)
# last_four=number_string[-4:]
# print(last_four)
# masked=star+last_four
# print(masked)


# s="oyo"
# rev=""
# for c in s:
#     rev=c+rev
# if s==rev:
#     print("pali")
# else:
#     print("no")
# a="madam"
# reverse=""
# for i in a:
#     reverse=i+reverse
# if i==reverse:
#     print("p")
# else:
#     print("n")
    
# print("palindrome"if a==a[::-1] else"not")
# a="palindrome"
# b=a[6:]
# print(b)


# print("".join(map(str,range(1,6))))

# items=["a","b","c","d","e"]
# # for itm in items:
# #     if itm=="b":
# #         items.remove(itm)
# #     else:
# #         print(itm)
# new_items=[]
# for itm in items:
#     if itm!="b":
#         print(itm)
#         new_items.append(itm)

# print(new_items)
# items=new_items 

# name=input("enter name")
# if (name =="rashid") or (name=="md") or (name=="md_rashid"):
#     print("unlocked")

# else:
#     print("denid")
    
# my_input="mdrashid@123"
# password="mdrashid@123"
# print(my_input==password)#true
# print(compare_digest(my_input,password))

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
