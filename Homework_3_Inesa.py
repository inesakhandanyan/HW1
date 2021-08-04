#!/usr/bin/env python
# coding: utf-8

# # Problem 1. Variable types, Lists

# In[1]:


type(225+2.0)


# In[2]:


type(230*2==2*230)


# In[3]:


type(round(1.056))


# In[4]:


import math


# In[5]:


type(math.ceil(14.56))


# b)

# In[6]:


movie_name=input("What is the name of your favorite movie?")
director_name=input("What is the name of your favorite movie's director?")
prod_year=input("When was your favorite movie produced?")
print(f"My favorite movie is {movie_name} which was directed by {director_name} and it was premiered in {prod_year}")


# c)

# In[7]:


Stocks=[]
print(Stocks)


# In[8]:


Stocks.append("EBAY")


# In[9]:


Stocks.append("A")


# In[10]:


Stocks.append("AHAC")


# In[11]:


Stocks.append("BGS")


# In[12]:


Stocks.append("CEMI")


# In[13]:


print(Stocks)


# # Problem 2. If Condition and For Loop

# a)

# In[14]:


n=25

if n%2==0:
    print("n is even")
else:
    print("n is odd")


# b)

# In[15]:


Wine_list=["Thomas Fogarty 2018 Razorback Vineyard Pinot Noir","Migration 2018 Drum Canyon Vineyard Pinot Noir", "Zorah Voski 2018","Curto Marco 2017 Arborina (Barolo)","Calera 2018 Jensen Vineyard Pinot Noir","Hin Areni Red 2014"]


# In[16]:


Wine_list2=[]


# In[17]:


for i in Wine_list:
    if "Pinot" in i:
        Wine_list2.append(i+": Pinot Noir")
    elif "Areni" in i:
        Wine_list2.append(i+": Areni")
    else:
         Wine_list2.append(i+": Other")


# In[18]:


print(Wine_list2)


# # Problem 4. Dictionaries 

# a)

# In[19]:


dict_stocks={"EBAY":"Ebay","AAPL":"Aplle Inc.","AMZN":"Amazon","MSFT":"Microsoft","FB":"Facebook"}
print(dict_stocks)


# # Problem 5. Functions 

# a)

# In[20]:


def maximum_number(x):
    maximum=x[0]
    for i in x:
        if i>maximum:
            maximum=i
    return maximum


# In[21]:


a=[-10,0,12,3,8,5,6,8,-3]


# In[22]:


print(maximum_number(a))


# b)

# In[23]:


def satisfaction_level(x):
    if x==1:
        print("Strongly dissatisfied")
    elif x==2:
        print("Dissatisfied")
    elif x==3:
        print("Neither dissatisfied nor satisfied")
    elif x==4:
        print("Satisfied")
    elif x==5:
        print("Very satisfied")
    else:
        print("Please use 1-5 range to rate your satisfaction")
try:
        level=int(input("Please rate your satisfaction level of services provided by company X on scale from 1 to 5"))
except ValueError:
        print("Please enter numeric information")


# # Problem 6. Reading data 

# a)

# In[24]:


import pandas as pd


# In[25]:


data_affairs=pd.read_excel('Affairs.xlsx')


# # Problem 7. Data description 

# a)

# In[26]:


data_affairs


# In[27]:


data_affairs.shape


# b)

# In[28]:


data_affairs.isnull().any().sum()


# c)

# In[29]:


data_affairs.isna().sum()


# d)

# In[30]:


print(data_affairs.select_dtypes('number').shape[1])
print(data_affairs.select_dtypes('object').shape[1])


# 7 numeric and 3 non-numeric variables are in the data

# e)

# In[31]:


data_affairs.loc[data_affairs['ID']==904,'gender']


# In[32]:


data_affairs.loc[data_affairs['ID']==904,'years married']


# f)

# In[33]:


print(data_affairs.education.mean())


# g)

# In[34]:


data_affairs.loc[:,'years married'].median()


# h)

# In[35]:


data_affairs.rating.quantile(0.75)


# i)

# In[36]:


data_affairs[data_affairs['affairs']=='Yes'].age.mean()


# j)

# In[37]:


def object_observations():
    objects=data_affairs.select_dtypes(include=['object'])
    for i in objects.columns:
        print(objects[i].value_counts())


# In[38]:


object_observations()


# k)

# In[40]:


for i in objects.columns:
        print(objects[i].unique())


# # Problem 8. Data Transformation

# a)

# In[41]:


data_affairs2=data_affairs.dropna()
print(data_affairs2)


# b)

# In[42]:


data_affairs3=data_affairs2.drop(['ID'],axis=1)


# c)

# In[43]:


data_affairs3.shape


# d)

# In[44]:


data_affairs3.columns= data_affairs3.columns.str.replace(' ','_')


# In[45]:


data_affairs3


# e)

# In[46]:


data_num=data_affairs3.select_dtypes(exclude=['object'])
data_num.info()


# In[47]:


data_obj=data_affairs3.select_dtypes(include=['object'])
data_obj.info()


# # Problem 9. Data Visualization

# In[48]:


import matplotlib.pyplot as plt


# In[49]:


for i in data_num.columns:
    plt.figure(figsize=(13,8))
    plt.title(f'(Relationship between {i} and g')
    sns.scatterplot(data_num[i],
               data_num.g)
    plt.show()


# In[50]:


plt.figure(figsize=(10,6))
plt.bar(data_affairs.affairs.unique(),data_affairs.age.mean(),color=('#a83252'))
plt.xlabel('Affairs')
plt.ylabel('Average Age')
plt.title('Average age by affairs')
plt.show()


# In[51]:


for i in data_num.columns:
    plt.hist(data_num[i],bins=20,color=('#a83252'))
    plt.title(i)
    plt.show()


# In[52]:


country_df[['x','y']].plot(kind='box')
plt.title("x and y")
plt.show()

