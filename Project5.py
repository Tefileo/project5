# Assignment for post class.
# Learning outcome: [variables, print, different data types]
# ask and store the following in variables.
# Name, last_name, age, age_of_mother, 3 skills.
# Print out the information in a formated manor.
# Calculate age difference between response and mother.
# Store skills in a list.
# Print each skill in a formated way.
# Definition of formated.
# a little context text.
# appropriate string formating like lower case or upper case, or other.
# assignment to variable.

name = input('What is your first name: ').strip().capitalize()
last_name = input('What is your last name: ').strip().capitalize()
age = int(input('What is your age: '))
age_of_mother  = int(input('What is the age of your mother: '))
print("i'm going to ask you for three skills")
skill1 = input('What is your first skill? : ').strip().lower()
skill2 = input('What is your second skill? : ').strip().lower()
skill3 = input('What is your third skill? : ').strip().lower()

print (f'We have stored your first name as {name}, your last name as {last_name}, your age as {age},\n the age of your mother as {age_of_mother}, and your three skills to be {skill1}, {skill2} and {skill3}.')

# The definition of formatted is 'To modify the appearance of the string to suit the program requirements'