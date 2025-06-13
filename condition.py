#1. IF
# if True:
#     print("works")

#2. IF ELSE
# if True:
#     print("One")
# else:
#     print("two")

#3. IF-ELIF-ELSE
# a, b = 1, 3
# if a > b:
#     print("One")
# elif a == b:
#     print("Two")
# else:
#     print("Done")

#4. IF-ELIF
# a, b = 1, 3
# if a<b:
#     print("one")
# elif b>a:
#     print("Two")


#1. Check if it is a valid combo
#2. For every if, else, elif block, indentation must be at same level
#3. At any point, only block will be executed in a given combo


a, b, c = 1, 2, 3

if b > c:
    print("Hello")
elif c > b:
    print("Hello 1")
    if b > a:
        print("Hello 2")
        print("Hello 3")
    elif c > a:
        print("Hello 4")
        print("Hello 5")
    else:
        print('No Hello')
else:
    print("Not Hello")
    
    
