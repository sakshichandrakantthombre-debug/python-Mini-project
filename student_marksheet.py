#!/usr/bin/env python
# coding: utf-8

# In[1]:


name=input("Enter student name:")
roll_no=input("Enter Roll number: ")
# subject of marks:
marathi=int(input("enter the marks marathi:"))
math=int(input("enter the marks math:"))
Biology= int(input("enter the marks Biology: "))
physics=int(input("enter the marks physics:"))
psycology=int(input("enter the marks psycology:"))
# Totle
totle=marathi+math+Biology+physics+psycology
# percentage
percentage=totle/5
#Grade
if percentage>=98:
    grade= "A+"
elif percentage>=87:
    grade= "A"
elif percentage>=78:
    grade="B"
elif percentage>=67:
    grade="C"
elif percentage>=57:
    grade="D"
else:
    grade ="F"
    if marathi >= 35 and maths >= 35 and Biology >= 35 and physics >= 35 and psycology>= 35:
        result = "PASS"
else:       
    result="FAIL"

# Print marksheet:
print("===\nSTUDENT MARKSHEET===")
print("Name:", name)
print("Roll No:", roll_no)
print("Totle:", totle,"/500")
print("percentage:", percentage)
print("Grade:", grade)
print("Result:", result)


# In[7]:


##### name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
marathi = int(input("Enter Marathi Marks: "))
maths = int(input("Enter Maths Marks: "))
english = int(input("Enter English Marks: "))
geography = int(input("Enter Geography Marks: "))
biology = int(input("Enter Biology Marks: "))
total = marathi + maths + english + geography + biology
percentage = total / 5
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
if marathi >= 45 and maths >= 45 and english >= 45 and geography >= 45 and biology >= 45:
    result = "PASS"
else:
    result = "FAIL"
print("\n===== STUDENT MARKSHEET =====")
print("Roll No:", roll_no)
print("Total:", total, "/500")
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:")


# In[ ]:




