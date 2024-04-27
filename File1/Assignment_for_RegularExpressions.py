#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re

Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.

Sample Text- 'Python Exercises, PHP exercises.'
Expected Output: Python:Exercises::PHP:exercises:
# In[28]:


#Out_put :Approach

text ='Python Exercises, PHP exercises.'
out_put = re.sub(r"\s+",':',text)  
s_final = re.sub(r",",":",out_put)
final_text=re.sub(r".$",":",s_final)
print(final_text)

Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.

Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
Expected output-
0      hello world
1             test
2    four five six

# In[16]:


#Out_put :Approach
dict= {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df = pd.DataFrame(dict)
df
pattern = r'[^a-z\s]'
result = df['SUMMARY'].str.replace(pattern, '', regex=True)
result

Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.
# In[32]:


str = 'Dry fruits are very healty and usefull to consume in the morning time '
pattern = "\w{4}"
regex_pattern = re.compile(pattern)
all_four_char = regex_pattern.findall(str)
print(all_four_char)

Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.
# In[35]:


str = 'Dry fruits are very healty and usefull to consume in the morning time '
pattern = "\w{3,5}"
regex_pattern = re.compile(pattern)
three_four__five_char = regex_pattern.findall(str)
print(three_four__five_char)

Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
Expected Output:
example.com
hr@fliprobo.com
github.com
Hello Data Science World
Data Scientist
# In[ ]:




Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
Note- Store given sample text in the text file and then to remove the parenthesis area from the text.

# In[ ]:




Question 7- Write a regular expression in Python to split a string into uppercase letters.
Sample text: “ImportanceOfRegularExpressionsInPython”
Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]

# In[153]:


text = "ImportanceOfRegularExpressionsInPython"
result = re.findall('[A-Z][^A-Z]*',text)
print(result)

Question 8- Create a function in python to insert spaces between words starting with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

# In[48]:


text ='RegularExpression1IsAn2ImportantTopic3InPython'
pattern = "(\d?[A-Za-z]+)"
result = re.findall(pattern,text)
print (result)

Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython

# In[69]:


text ='RegularExpression1IsAn2ImportantTopic3InPython'
pattern = "(\d+|[A-Z]?[A-Za-z]+)"
result = re.findall(pattern,text)
print (result)

Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv

# In[71]:


df = pd.read_csv('https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv')
df.head()


# In[72]:


df['Country']


# In[94]:


pattern = '(\w{6})'
first_five_letter =df['Country'].str.extract(pattern,expand =True)
first_five_letter


# In[95]:


df['first_five_letter'] = first_five_letter
df

Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
# In[102]:


df['Region']


# In[118]:


pattern = '(\w+)'
result = df['Region'].str.extract(pattern,expand=False)
result.head(15)

Question 12- Write a Python program where a string will start with a specific number. 
# In[18]:


data ={'Happiness Score':['2ndhighest','3rdhighest','4thhighest','3rdlowest','4thhighest']}
d2= pd.DataFrame(data)
d2


# In[38]:


pattern = r'^3\w+'
specific_num = d2['Happiness Score'].str.contains(pattern)
d2[specific_num]

Question 13- Write a Python program to remove leading zeros from an IP address
# In[55]:


ip = "196.03.05.121.1.0,111.34.23.4.0,145.45.47.3.0"
result = re.sub('\.[0]*','.',ip)
print(result)

Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
Expected Output- August 15th 1947
Note- Store given sample text in the text file and then extract the date string asked format.

# In[59]:




Question 15- Write a Python program to search some literals strings in a string. 
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'

# In[28]:


pattern = "fox|dog|horse"
string ='The quick brown fox jumps over the lazy dog.'
result = re.findall(pattern, string)
result

Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'

# In[61]:


str ='The quick brown fox jumps over the lazy dog.'
result = re.search(r'\bfox\b',str)
print(result)
print(result.group())

Question 17- Write a Python program to find the substrings within a string.
Sample text : 'Python exercises, PHP exercises, C# exercises'
Pattern : 'exercises'.

# In[62]:


str1 ='Python exercises, PHP exercises, C# exercises'
result = re.search(r'\bexercises\b',str1)
print(result)

Question 18- Write a Python program to find the occurrence and position of the substrings within a string.
# In[63]:


str ='The quick brown fox jumps over the lazy dog.'
result = re.search(r'\bfox\b',str)
print(result)
print(result.group())

Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
# In[ ]:




Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']

# In[83]:


text ="01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
pattern="(^[0-9]+\.[0-9]{1,2})"
r_pat = re.compile(pattern)
result = r_pat.findall(text)
result

Question 21- Write a Python program to separate and print the numbers and their position of a given string.
# In[85]:


text = 'Create a function in python to find all 10 words that are at least 4 characters long in a string'
result = re.finditer(r"10|4",text)
for match_object in result:
    print(match_object)

Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
Expected Output: 950

# In[147]:



 

Question 23- Create a function in python to insert spaces between words starting with capital letters.
Sample Text: “RegularExpressionIsAnImportantTopicInPython"
Expected Output: Regular Expression Is An Important Topic In Python

# In[ ]:




Question 24- Python regex to find sequences of one upper case letter followed by lower case letters
# In[ ]:




Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
Sample Text: "Hello hello world world"
Expected Output: Hello hello world

# In[142]:


sample ='Hello hello world world'
pattern = '\b(\w+)(?:\W+\1\b)+'
result = re.sub(pattern,'\1',sample)
print(result)

Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.
# In[ ]:




Question 27-Write a python program using RegEx to extract the hashtags.
Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']

# In[ ]:




Question 28- Write a python program using RegEx to remove <U+..> like symbols
Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders

# In[ ]:




Question 29- Write a python program to extract dates from the text stored in the text file.
Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
Note- Store this sample text in the file and then extract dates.

# In[ ]:




Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
The use of the re.compile() method is mandatory.
Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.

# In[ ]:




