player = input("Enter your name : ")
gender = input("Male/Female :")
total_questions = 4
score = 0
if (gender.lower() == "male"):
    print("Hey,Mr." + player)
else:
    print("Hey,Mrs." + player)     
    
    
q1 = input("Python is a:" )
if(q1.lower()=="programming language"):
    print("your answer is correct!")
    score += 1
else:
    print("Wrong answer.")    

q2 = input("5+10 =" )
if(q2 =="15"):
    print("your answer is correct!")
    score += 1
else:
    print("Wrong answer.")        
    
q3 = input("10 × 10 =" )
if(q3 =="100"):
    print("your answer is correct!")
    score += 1
else:
    print("Wrong answer.")         
    
q4 = input("5+5 =" )
if(q4 =="10"):
    print("your answer is correct!")
    score += 1
else:
    print("Wrong answer.")               
    
    
mark = (score/total_questions)*100
mark = int(mark)
print("your score is:" + str(mark) + "/100")