#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: Function to calculate duration.
def survival_duration(age, time_unit):
    if time_unit.lower() == 'months' or time_unit.lower() == 'm':
        return age * 12
    elif time_unit.lower() == 'weeks' or time_unit.lower() == 'w':
        return age * 52
    elif time_unit.lower() == 'days' or time_unit.lower() == 'd':
        return age * 365
    elif time_unit.lower() == 'hours' or time_unit.lower() == 'h':
        return age * 365 * 24
    elif time_unit.lower() == 'minutes' or time_unit.lower() == 'min':
        return age * 365 * 24 * 60
    elif time_unit.lower() == 'seconds' or time_unit.lower() == 's':
        return age * 365 * 24 * 60 * 60
    else:
        return "Invalid time unit"

# Step 2: Take input from user
age = input("What's your age? ")

# Check if input is a valid number
while not age.isdigit():
    print("Invalid input. Please enter a numeric value for age.")
    age = input("What's your age? ")

# Convert input to integer after checking
age = int(age)

if age < 0:
    print("Age cannot be negative. Please enter a valid age.")
else:
    print(f"Your age is {age}.")
time_unit = input("Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds.\nNote: You can write the first letter or the full name of the time unit: ")

# Step 3: Output
result = survival_duration(age, time_unit)
print(f"You lived for {result} {time_unit.lower()}.")

