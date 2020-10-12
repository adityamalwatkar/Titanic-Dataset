#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

df= pd.read_csv(r'C:\Users\prach_sxw8up\Downloads\titanic\train.csv')


# In[2]:


df.head()


# In[3]:


df['Name']


# In[4]:


df['Name'].head()


# In[5]:


df['Age'].max()


# In[6]:


df['Age'].mean()


# In[7]:


df['Fare'].mean()


# In[8]:


df.loc[0:15,'Name']


# In[9]:


df.loc[0:15,'Name':'Embarked']


# In[10]:


df.iloc[0:15,0:4]


# In[11]:


df['Age'].max()


# In[12]:


df['Age']==df['Age'].max()


# In[13]:


df[df['Age']==df['Age'].max()]


# In[14]:


df[df['Age']==df['Age'].max()]['Name']


# In[16]:


df.sort_values(by='Age',ascending=True)


# In[18]:


df.sort_values(by='Age',ascending=True).head()


# In[20]:


df.sort_values(by=['Name','Age'],ascending=[True,False]).head()


# In[24]:


New={'male':0,'female':1}
df['Sex']=df['Sex'].map(New)
df.head()


# In[26]:


old={0:'male',1:'female'}
df=df.replace({'Sex':old})
df.head()


# In[27]:


df.groupby(by='Survived')['Age'].describe()


# In[28]:


pd.crosstab(df['Sex'],df['Survived'],normalize=True)

