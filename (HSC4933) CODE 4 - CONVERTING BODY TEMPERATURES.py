#!/usr/bin/env python
# coding: utf-8

# In[1]:


# celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# In[8]:


# setting dictionary to mapping the user input to the function
conversion_features = {
    'c': celsius_to_fahrenheit,
    'f': fahrenheit_to_celsius
}

print("Choose the conversion direction.")
print("Put C for celsius to fahrenheit or F for fahrenheit to celsius.")

choice = input("Enter your choice: ").lower()

if choice in conversion_features:
    temperature = float(input("Enter the temperature: "))
    
    # conversion
    converted_temperature = conversion_features[choice](temperature)
    
    print(f"{temperature} degrees {'celsius' if choice == 'c' else 'fahrenheit'} is {converted_temperature} degrees {'fahrenheit' if choice == 'c' else 'celsius'}") 

else: 
    print("This is not a valid input. Please enter a C or F.")
          
    


# In[9]:


# setting dictionary to mapping the user input to the function
conversion_features = {
    'c': celsius_to_fahrenheit,
    'f': fahrenheit_to_celsius
}

print("Choose the conversion direction.")
print("Put C for celsius to fahrenheit or F for fahrenheit to celsius.")

choice = input("Enter your choice: ").lower()

if choice in conversion_features:
    temperature = float(input("Enter the temperature: "))
    
    # conversion
    converted_temperature = conversion_features[choice](temperature)
    
    print(f"{temperature} degrees {'celsius' if choice == 'c' else 'fahrenheit'} is {converted_temperature} degrees {'fahrenheit' if choice == 'c' else 'celsius'}") 

else: 
    print("This is not a valid input. Please enter a C or F.")


# In[10]:


# setting dictionary to mapping the user input to the function
conversion_features = {
    'c': celsius_to_fahrenheit,
    'f': fahrenheit_to_celsius
}

print("Choose the conversion direction.")
print("Put C for celsius to fahrenheit or F for fahrenheit to celsius.")

choice = input("Enter your choice: ").lower()

if choice in conversion_features:
    temperature = float(input("Enter the temperature: "))
    
    # conversion
    converted_temperature = conversion_features[choice](temperature)
    
    print(f"{temperature} degrees {'celsius' if choice == 'c' else 'fahrenheit'} is {converted_temperature} degrees {'fahrenheit' if choice == 'c' else 'celsius'}") 

else: 
    print("This is not a valid input. Please enter a C or F.")

