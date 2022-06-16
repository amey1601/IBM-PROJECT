#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
# </center>
# 

# # **Space X  Falcon 9 First Stage Landing Prediction**
# 

# ## Lab 2: Data wrangling
# 

# Estimated time needed: **60** minutes
# 

# Falcon 9 first stage will land successfully
# 

# 
# 

# Several examples of an unsuccessful landing are shown here:
# 

# 
# 

# 

# ## Objectives
# 
# Perform exploratory  Data Analysis and determine Training Labels
# 
# *   Exploratory Data Analysis
# *   Determine Training Labels
# 

# ***
# 

# ## Import Libraries and Define Auxiliary Functions
# 

# We will import the following libraries.
# 

# In[24]:



import pandas as pd
import numpy as np


# ### Data Analysis
# 

# Load Space X dataset, from last section.
# 

# In[2]:


df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
df.head(10)


# In[27]:


df["LaunchSite"].unique()


# Identify and calculate the percentage of the missing values in each attribute
# 

# In[3]:


df.isnull().sum()/df.count()*100


# Identify which columns are numerical and categorical:
# 

# In[4]:


df.dtypes


# ### TASK 1: Calculate the number of launches on each site
# 
# The data contains several Space X  launch facilities: <a href='https://en.wikipedia.org/wiki/List_of_Cape_Canaveral_and_Merritt_Island_launch_sites?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01'>Cape Canaveral Space</a> Launch Complex 40  <b>VAFB SLC 4E </b> , Vandenberg Air Force Base Space Launch Complex 4E <b>(SLC-4E)</b>, Kennedy Space Center Launch Complex 39A <b>KSC LC 39A </b>.The location of each Launch Is placed in the column <code>LaunchSite</code>
# 

# Next, let's see the number of launches for each site.
# 
# Use the method  <code>value_counts()</code> on the column <code>LaunchSite</code> to determine the number of launches  on each site:
# 

# In[5]:


# Apply value_counts() on column LaunchSite
df["LaunchSite"].value_counts()


# Each launch aims to an dedicated orbit, and here are some common orbit types:
# 

# 

# 
# 

# ### TASK 2: Calculate the number and occurrence of each orbit
# 

# Use the method  <code>.value_counts()</code> to determine the number and occurrence of each orbit in the  column <code>Orbit</code>
# 

# In[6]:


# Apply value_counts on Orbit column
# Apply value_counts on Orbit column
df.Orbit.value_counts()


# ### TASK 3: Calculate the number and occurence of mission outcome per orbit type
# 

# Use the method <code>.value_counts()</code> on the column <code>Outcome</code> to determine the number of <code>landing_outcomes</code>.Then assign it to a variable landing_outcomes.
# 

# In[7]:


# landing_outcomes = values on Outcome column
# landing_outcomes = values on Outcome column
landing_outcomes = df.Outcome.value_counts()
landing_outcomes


# <code>True Ocean</code> means the mission outcome was successfully  landed to a specific region of the ocean while <code>False Ocean</code> means the mission outcome was unsuccessfully landed to a specific region of the ocean. <code>True RTLS</code> means the mission outcome was successfully  landed to a ground pad <code>False RTLS</code> means the mission outcome was unsuccessfully landed to a ground pad.<code>True ASDS</code> means the mission outcome was successfully  landed to a drone ship <code>False ASDS</code> means the mission outcome was unsuccessfully landed to a drone ship. <code>None ASDS</code> and <code>None None</code> these represent a failure to land.
# 

# In[8]:


for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)


# We create a set of outcomes where the second stage did not land successfully:
# 

# In[9]:


bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
bad_outcomes


# In[14]:


df.head()


# ### TASK 4: Create a landing outcome label from Outcome column
# 

# Using the <code>Outcome</code>,  create a list where the element is zero if the corresponding  row  in  <code>Outcome</code> is in the set <code>bad_outcome</code>; otherwise, it's one. Then assign it to the variable <code>landing_class</code>:
# 

# In[20]:


# landing_class = 0 if bad_outcome
# landing_class = 1 otherwise

def onehot(item):
    if item in bad_outcomes:
        return 0
    else:
        return 1
landing_class = df["Outcome"].apply(onehot)
landing_class


# This variable will represent the classification variable that represents the outcome of each launch. If the value is zero, the  first stage did not land successfully; one means  the first stage landed Successfully
# 

# In[21]:


df['Class']=landing_class
df[['Class']].head(8)


# In[22]:


df.head(5)


# We can use the following line of code to determine  the success rate:
# 

# In[23]:


df["Class"].mean()


# We can now export it to a CSV for the next section,but to make the answers consistent, in the next lab we will provide data in a pre-selected date range.
# 

# <code>df.to_csv("dataset_part\_2.csv", index=False)</code>
# 
