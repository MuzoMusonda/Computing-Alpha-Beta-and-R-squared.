#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm

import matplotlib.pyplot as plt


# In[2]:


data = pd.read_excel('Downloads/MUZO/DATA_ANALYTICS/Housing.xlsx')


# In[3]:


data


# In[4]:


data[['House Price', 'House Size (sq.ft.)']]


# In[5]:


#Univariate Regression


# In[6]:


X = data['House Size (sq.ft.)']
Y = data['House Price']


# In[7]:


X


# In[8]:


Y


# In[9]:


#scatter plot will have all data points scatter on the chart


# In[10]:


plt.scatter(X,Y)
plt.show()


# In[11]:


plt.scatter(X,Y)
plt.axis([0, 2500, 0 , 1500000])
plt.show()


# In[12]:


#Adding plt.ylabel and plt.xlabel will as a label to the x and y axis accordingly


# In[13]:


plt.scatter(X,Y)
plt.axis([0, 2500, 0 , 1500000])
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft.)')
plt.show()


# In[14]:


#Running a regression.


# In[15]:


X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()


# In[16]:


reg.summary()


# In[18]:


260800 + 402 * 1000


# In[19]:


#ALPHA, Beta, R^2:


# In[20]:


slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)


# In[ ]:


#The slope = Beta


# In[21]:


slope


# In[ ]:


#The intercept = Alpha


# In[22]:


intercept


# In[23]:


r_value


# In[24]:


p_value


# In[25]:


std_err


# In[ ]:


#Don't forget to raise the r value to the power of 2
#to obtain the well known R^2 statistics


# In[26]:


r_value ** 2


# In[ ]:




