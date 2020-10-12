#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

df= pd.read_csv(r'C:\Users\prach_sxw8up\Downloads\titanic\train.csv')


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# In[3]:


sns.countplot(x='Survived',data=df)


# In[4]:


sns.countplot(x='Survived',data=df,hue='Sex')


# In[6]:


sns.lineplot(x='Age',y='Fare',data=df)


# In[7]:


df.plot.scatter('Age','Fare')


# In[8]:


df.plot.scatter('Age','Survived')


# In[10]:


df['Age'].hist(bins=8)


# In[13]:


import matplotlib.pyplot as plt
sizes= df['Survived'].value_counts()
fig1,ax1 = plt.subplots()
ax1.pie(sizes,labels=['Not Survived','Survived'],autopct='%1.1f%%',shadow=True)
plt.show()

