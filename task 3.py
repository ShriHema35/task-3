#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('C:\\Users\\Shri Hema\\OneDrive\\Desktop\\task 3\\householdtask3.csv')


# In[3]:


(data.head(10))


# In[4]:


#scatter plot
plt.scatter(data['year'],data['own'])

#adding title to scatter plot
plt.title("scatter plot")

#setting the x and y label
plt.xlabel('year')
plt.ylabel('own')

#showing the chart
plt.show()


# In[5]:


#line chart with  year against own
plt.plot(data['year'])
plt.plot(data['own'])

#adding title to line chart
plt.title("line chart")

#setting the x and y label
plt.xlabel('year')
plt.ylabel('own')

#showing the chart
plt.show()


# In[6]:


#bar chart
plt.bar(data['year'],data['own'])

#adding title to bar chart
plt.title("bar Chart")

#setting the x and y label
plt.xlabel('year')
plt.ylabel('own')

#showing the chart
plt.show()


# In[7]:


#Histogram

plt.hist(data['income'])

#adding title to histogram
plt.title("Histogram")


#showing the histogram
plt.show()


# In[ ]:





# In[ ]:




