#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.linear_model import LinearRegression


# In[4]:


X = np.array([
    [1,5],[2,6],[3,6],[4,7],
    [5,7],[6,8],[7,6],[8,7]

])
y = np.array([35,45, 52, 60, 68, 78, 82,90])

model = LinearRegression()
model.fit(X,y)
study = float(input("Daily Studying Hours "))

sleep = float(input ("Daily Slepping Hours"))

predicated = model.predict([[study, sleep]])[0]
predicated = max(0,min(100, predicated))

print (f"\n Predicated Marks:{predicated:.1f}/100")

if predicated >=80:
    print("Great Work Keep up it ")
elif predicated >=60:
    print("Good But Need to Improve")
else: 
    print("Increase Your study hours You can do anything and you will !")


# In[ ]:




