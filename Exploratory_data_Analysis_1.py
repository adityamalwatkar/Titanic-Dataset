#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

df= pd.read_csv(r'C:\Users\prach_sxw8up\Downloads\titanic\train.csv')


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df.describe(include="object")


# In[12]:


df['Sex'].value_counts()


# In[13]:


df['Embarked'].value_counts()


# In[14]:


df['Sex'].value_counts(normalize='True')

