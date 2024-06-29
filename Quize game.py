print("Welocme to my Computer Quize game")
#Ask from the user whether he likes to play this game or not 
playing = input("Do you like to play this game? ")
if playing !="yes":
    quit("Quit")
print()
print("Okay let's PLAY !!!")
print()

#asking 04 questions
print("We provide 5 questions and for each correct answer, you will get 5 marks")
print("Please always use simple letters when you answer")
print()

#For count the user's score
marks = 0

qs01 = input("What is GPU stands for? ")
if qs01 == "graphic processing unit":
    print("Your answer is CORRECT")
    marks += 25
else:
    print("Your answer is wrong. Correct answer is Graphic Processing Unit")
print()

qs02 = input("What is CPU stands for? ")
if qs02 == "central processing unit":
    print("Your answer is CORRECT")
    marks += 25
else:
    print("Your answer is wrong. Correct answer is Centra Processing Unit")
print()

qs03 = input("What is RAM stands for? ")
if qs03 == "random access memory":
    print("Your answer is CORRECT")
    marks += 25
else:
    print("Your answer is wrong. Correct answer is Random Access Memory")
print()

qs04 = input("What is ROM stands for? ")
if qs04 == "read only memory":
    print("Your answer is CORRECT")
    marks += 25
else:
    print("Your answer is wrong. Correct answer is Read Only Memory")
print()

#Show the score
if marks >= 50:
    print("Congratulations!!!")
    print("You have successfully complete this quize game")
    print(f"Your score is {marks}/100")
else:
    print("You have complete the quize")