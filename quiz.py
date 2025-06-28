#print the score
#1 what do you need
#score
#2 what do you want from whom
    #question-myself
    #i need each answer from user
#3 order the need with priority same
#4 flow pseudo code
##1 define question ds
##2 iterate and show each question
##3 iterate and show collection each questin from the user
##4 iterate and every correct answer we need to increment score
##5 print the score

# score=0
# questions=[
# {
# "question": "What does strip() method do?",
# "options": ["A. remove left space", "B. remove spaces both end", "C. NA "],
# "answer": "B"
# },
 
# {"question": "what is 2+2?",
# "option":["A.4","B.5","C.6"],  
# "answer":"A"  
# },
 
# {
# "question":"what is 2**2?",
# "option":["A.4444","B.44","c.4"],
# "answer":"C"    
    
# }
# ] 
# for i,q in enumerate(questions):
#     print(f"question{i+1}:{q["question"]}")
    
   # print(q["option"])

# score=0
# questions=[
# {
# "question": "What does strip() method do?",
# "option": ["A. remove left space", "B. remove spaces both end", "C. NA "],
# "answer": "B"
# },
 
# {"question": "what is 2+2?",
# "option":["A.4","B.5","C.6"],  
# "answer":"A"  
# },
 
# {
# "question":"what is 2**2?",
# "option":["A.4444","B.44","c.4"],
# "answer":"C"    
    
# }
# ] 
# for i, q in enumerate(questions):
#     print(f"question{i+1}:{q['question']}")

#     for option in q['option']:
#         print(option)
#         print("")

# score=0
# questions=[
# {
# "question": "What does strip() method do?",
# "option": ["A. remove left space", "B. remove spaces both end", "C. NA "],
# "answer": "B"
# },
 
# {"question": "what is 2+2?",
# "option":["A.4","B.5","C.6"],  
# "answer":"A"  
# },
 
# {
# "question":"what is 2**2?",
# "option":["A.4444","B.44","c.4"],
# "answer":"C"    
    
# }
# ]
# attempt=[] 
# for i, q in enumerate(questions):
#     print(f"question{i+1}:{q['question']}")

#     for option in q['option']:
#         print(option)
#     chioice=input("enter your answer")
#    # attempt.append((i,chioice))
#     attempt_entry=()
#     if chioice.upper()==q['answer']:
#         score+=2.0
#         attempt_entry=(i,chioice,'correct')
#     else:
#         score-=0.5 
#         attempt_entry=(i,chioice,'wrong')
#     attempt.append(attempt_entry)
#     print("")
# print(f"your score:{score}")
# print(attempt)


# attempt=[] 
# for i, q in enumerate(questions):
#     print(f"question{i+1}:{q['question']}")

#     for option in q['option']:
#         print(option)
#     chioice=input("enter your answer")
#     attempt_entry=(i,chioice, q['answer'])
#    # attempt.append((i,chioice))
#     attempt_entry=()
#     if chioice.upper()==q['answer']:
#         score+=2.0
      
#     else:
#         score-=0.5 
      
#     attempt.append(attempt_entry)
#     print("")
# print(f"your score:{score}")
# print(attempt)

# attempt=[]
# for i,w in enumerate(questions):
#     print(f"{i+1}:{w['question']}")
#     for option in w["option"]:
#         print(option)
#     choice=input("enter your answer")
#     attem_ent=(i,choice,w["answer"])
#     attem_ent=()
#     if choice.upper()==w["answer"]:
#         score+2.0
#     else:
#         score-=0.5
        
# print(attempt)
# print(f"your score is:{score}")

# names=['raj ras','reh','riya']
# for c in names:
#     print(c[2])
#     if c=="reh":
#         print("hey i'm rashid")
# numbers=[2,3,5,-2,10]
# squares=[]
# for num in numbers:
#     square= num**2
#     squares.append(square)
#     print(squares,num ,end=" ")
#     squares.pop(squares)

# count=5
# while count>0:
#     print(count,"i love you bebe")
#     count -=1
# for i in range(1,10,2):
#     print(i)

     
# class TV:
#     def turn_on(self):
#         print("The TV is now ON.")
        
#     def turn_off(self):
#         print("The TV is now OFF.")

# class Remote:
#     def __init__(self):
#         self.tv = TV()  # Creating an instance of TV inside Remote

#     def turn_on_tv(self):
#         self.tv.turn_on()

#     def turn_off_tv(self):
#         self.tv.turn_off()

# # Example usage
# remote = Remote()
# remote.turn_on_tv()
# remote.turn_off_tv()


# class TV:
#     def turn_on(self):
#         print("TV is ON.")
        
#     def turn_off(self):
#         print("TV is OFF.")

# class Remote:
#     def turn_on_tv(self, tv):
#         tv.turn_on()
        
#     def turn_off_tv(self, tv):
#         tv.turn_off()

# # Example usage
# my_tv = TV()
# remote = Remote()

# remote.turn_on_tv(my_tv)
# remote.turn_off_tv(my_tv)



class TB:
    def turn_on(self):
        print("tb is on")
    def turn_off(self):
        print("tb is off")
class Remot:
    def turn_on_tb(self,tb):
        tb.turn_on()
    def turn_of_tb(self,tb):
        tb.turn_on(self,tb)


mi_tb=TB()
remot=Remot()

remot.turn_on_tb(mi_tb)
remot.turn_of_tb(mi_tb)
print(remot.turn_of_tb)

