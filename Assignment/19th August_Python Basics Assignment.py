#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://drive.google.com/file/d/1jnUYkZvJVV-6pO18EuaFOVv8E2Eb5_SB/view
#PYTHON BASIC VARIABLE

"""Q. Declare two variables, `x` and `y`, and assign them integer values.
Swap the values of these variables without using any temporary variable."""
x=10
y=20
x,y=y,x
print(x,y)


# In[10]:


"""Create a program that calculates the area of a rectangle. Take the length and
width as inputs from the user and store them in variables. Calculate and
display the area"""
x=int(input("Enter the length:"))
y=int(input("Enter the width:"))
Area=x*y
print("Area of the rectangle:", Area )


# In[9]:


"""Write a Python program that converts temperatures from Celsius to
Fahrenheit. Take the temperature in Celsius as input, store it in a variable,
convert it to Fahrenheit, and display the result."""

#Explanation: #Conversion as per the formula c/5=(f-32)/9

c =int(input("Enter the temperature in centigrade:"))
f =((9*c)/5)+32 
print("The temperature in Fahrenheit:",f)


# In[10]:


###STRING BASED QUESTION
""" 1. Write a Python program that takes a string as input and prints the length of
the string."""

a= input("Enter a string")
b=len(a) # b is variable to store the value of input
print("length of the string:", b)


# In[58]:


""" 2. Create a program that takes a sentence from the user and counts the number
of vowels (a, e, i, o, u) in the string."""
# Get input from the user
sentence = input("Enter a sentence: ")

vowel_count = 0

for char in sentence:
    #Convert the character to lowercase to handle both uppercase and lowercase vowels
    char_lower = char.lower()

    # Check if the character is a vowel (a, e, i, o, u)
    if char_lower in "aeiou":
        #If the character is a vowel, increment the vowel_count variable
        vowel_count += 1

#Display the result
print("Number of vowels:", vowel_count)


# In[15]:


""" 3. Given a string, reverse the order of characters using string slicing and print
the reversed string."""

a="pwskills"
b=a[7:-9:-1]
print(b)
#slicing


# In[33]:


""" 4. Write a program that takes a string as input and checks if it is a palindrome
(reads the same forwards and backwards)."""

a=input("Enter a string: ")
b=len(a)
c=a[(b-1):-(b+1):-1] #The logic Back slicing and mathing with the input string
a==c


# In[35]:


""" 5. Create a program that takes a string as input and removes all the spaces from
it. Print the modified string without spaces."""
a= input("Enter a string:")
a.replace(" ", "")


# In[ ]:




