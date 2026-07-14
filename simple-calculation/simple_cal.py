#!/usr/bin/env python
# coding: utf-8

# ## Simple Calculator Mini Project:=

# In[8]:


# simple calculator:

print("Simple Calculator")
print("1. Addition")
print("1. Subtraction")
print("1. Multiplication")
print("1. Division")


user_choice= int(input("Enter your user_choice (1-6): "))


num1= int(input("Enter the your choice: "))
num2=int(input("Enter the your choice: "))


if user_choice ==1:
    print("Addition", num1+num2)
elif user_choice ==2:

    print("Subtraction", num1-num2)
elif user_choice ==3:
    print("Multiplication", num1*num2)
elif user_choice ==4:
    print("Division", num1/num2)
elif user_choice ==5:
    print("Module", num1%num2)
elif user_choice ==6:
    print("Totle", num1+num2)
else:
    print("Invalid user_choice")






# In[ ]:




