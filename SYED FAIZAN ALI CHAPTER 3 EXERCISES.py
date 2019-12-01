#!/usr/bin/env python
# coding: utf-8

# # CHAPTER 3: EXERCISES

# # PRACTICE PROBLEM 3.1:

# In[2]:


fahr = eval(input("Enter the temperature in degree fahrenheit "))
cels = (fahr-32) * 5/9
print('the temperature in degree Celsius is', cels)


# # PRACTICE PROBLEM 3.2:

# # PART (a):

# In[1]:


age = float(input("Enter your age"))
if age > 62:
    print("You can get your pension benefits!")


# # PART(b):

# In[4]:


name = ('Musical','Aaron','Williams','Gehrig','Ruth')
if name in ['Musical','Aaron','Williams','Gehrig','Ruth']:
    print('One of the top 5 baseball players, ever!')


# # PART (c):

# In[2]:


hits  = eval(input('Enter the value'))
shield = 0
if hits > 10 and shield == 0:
    print('You\'re dead...')


# # PART (d):

# In[2]:


north or south or east or west
if north or south or east or west:
    print("I can escape")


# # PRACTICE PROBLEM 3.3:

# # PART (a):

# In[4]:


year = eval(input("Enter the year:"))
if year % 4 == 0:
    print("Could be a leap year:")
else:
    print("Definitely not a leap year")


# # PART (b):

# In[5]:


ticket = lottery
if ticket == lottery:
    print("You won")
else:
    print("Better luck next time!")


# # PRACTICE PROBLEM 3.4:

# In[7]:


users = ['joe', 'sue' , 'hani', 'sophie']
id = input("login: ")
if id in users:
    print('You are in!')
else:
    print('user unknown')
print("done:")    


# In[8]:


users = ['joe', 'sue' , 'hani', 'sophie']
id = input("login: ")
if id in users:
    print('You are in!')
else:
    print('user unknown')
print("done:")    


# # PRACTICE PROBLEM 3.5:

# In[13]:


wordlist = eval(input("Enter the word list: "))
for word in wordlist:
    if len(word) == 4:
        print("word")


# In[ ]:




