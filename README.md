Description of thougts during project creation.
This Python project calculates the total time a person has lived in various time units (months, weeks, days, etc....) based on their age. This program takes in  the user's age and the time unit they want to use and then it returns the duration of survival in that  unit.
Thought Process:
I started by writing the code which helps me convert the user's age into different time units. For example, if someone is 10 years old, they have lived for 120 months or 3650 days.
I created the Function survival_duration that would calculate the duration. I wanted the function to be flexible enough to handle different time units (months, weeks, days, etc.) so I used if-elif statements to check which time unit the user selected. 
I choose only lowercase timeunit because it converts all the entries into lowercase which will simplify my code.
For each unit (ex: months), I multiplied the age by the correct factor (ex: age * 12 for months since 1 year = 12 months).
I also added an option to handle invalid inputs in case the user enters a unit that doesn’t exist.
Taking Input From the User: used the input() function to ask the user for their age and time unit. Since the user might use either the full name of the time unit (like “months”) or just the first letter (like “m”), I made sure to account that both options by converting the input to lowercase.
i used different conditions which can detect errors in age or invalid entries of age. 
After calculating the duration in the chosen time unit, I used the print() function to display the result. I also converted the time unit input to lowercase for consistency.
I then mentioned the print function where i added f string which helps in formatting the texet which gives the final output. 
