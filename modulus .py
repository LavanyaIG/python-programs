#!/usr/bin/env python
# coding: utf-8

# In[10]:


while True:# If the while condition is true if block is executed
    a=input("Do you want to continue or not(y/n)?")
    if a.upper()=='Y':# if the user pass 'Y' the following statement is executed
        break
a=int(input('FIRst number is:')) #first number
b=int(input('second number is:')) #second number
print(a,"%",b,"=",a%b)# perform a % b
print(b,"%",a,"=",b%a) # perform b % a


# In[ ]:




