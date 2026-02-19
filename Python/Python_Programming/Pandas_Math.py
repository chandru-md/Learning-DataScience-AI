#!/usr/bin/env python
# coding: utf-8

# In[5]:


def addition(a,b):
    return a+b

def sub(a,b):
    return a-b

def multily(a,b):
    return a*b

try:
    def division(a,b):
        return a/b
except ZeroDivisionError:
    print("Please enter a number greater than 0")


# In[ ]:




