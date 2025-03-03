# Sammy Seahawk
# Date
# This program will explain various math operations and variables

# Programming languages follow the same math order of operations you already know
# PEMDAS - Parenthesis, exponents, multiplication, division, addition, subtraction, left to right

# Operators include +, -, *, /, //, % , **
# Anything in quotation marks remember is a string literal and will be output as typed
print("2 + 2") # will display 2 + 2

# So + between 2 numbers adds them  (the spaces do not matter - typed to make the code more readble)
# As you can see numbers are not placed inside quoation marks
print(2 + 2)
print("2 + 2") #A plus sign between 2 string concatenates them or merges them together into 1 string

# - means subtract
print(2 - 1) # will display 1

# * is for multiplication (Note that you cannot type an x for times)
print(2 * 3) # will display 6

# / is division - division will always return a float by default
print(11 / 5) # will display 2.2

# // is for integer division and will only return the integer value of the answer
print(11 // 5)  # will display 2 not 2.2

# % is known as remainder division and will return the remainder only
print (11 % 5)  # will display 1 (5 goes into 11 2 times with a remainder of 1)

# ** is to the power of
print(2 ** 3) # means 2 to the 3rd power so will display 8

# Order of operations
# what is in parenthesis happens first
print(2*(3+2)) # will display 10 because 3+2 happens first
print(2*3*2) # will display 8 because 2*3 happens first - multiplication before addition

# these would both be the same answer because the 3 *2 happens first in both -so no need for the ()
print(2+(3*2))
print(2+3*2)


# Important to note is that when all arguments are integers the result will also be an integer
print(2+3*2)
# But if even 1 argument is a float the result will be a float
print(2.0+3*2)


print()
print()


# Variables:
# Variables are like virtual containers that store data for use later in the program
# Variables names have rules:
# Cannot start with a number or special character other than an _ which is considered a character (can have a number in the name)
# Cannot contain spaces
# They are case sensitive, so Age is not the same as age
# Must not be the same as any Python reserved word
# Each variable in a program must have a unique name - if you had 2 players maybe player1Name and player2Name not playerName twice
# An unwritten rule is that variable names should represent the data they store
# I would never call a variable name and store an age in it or call it age and store a user name

# To create a variable we first decide on a name and then put a value in it -
# the variable always comes first, then an = which means to assign a value, then the value to be assigned to the variable
# So here the value Sammy is now assigned to the variable userName
userName = "Sammy"
userAge = 21

#  The way I named the variable uses something we call camel case - many believe it makes it more readable
# But you could also write user_name or username - all are acceptable variable names (never user name as spaces are not allowed)
# Choose a style that you prfer and name all of your variables that way

# The data stored in a variable can change throughout a program (even change data type)
myVariable = 5
# Since myVariable is not in "" it will not print literally
# Instead what displays is the value stored in the variable myVariable which is 4
print(myVariable)

print()
# I can then change what is stored in myVariable
myVariable = "Now it's a phrase"
print(myVariable)
print()

# to display multiple variables you can use comma separated arguments, concatenation, or f formatting
print(userName, "is", userAge)

# Using concatenation only works if the variables contain strings
print(userName + " is " + myVariable) #Sammy is
# If the variables contain numbers the program will crash unless you convert the number ro a string
# print(userName + " is " + userAge) this crashes because you cannot concatenate a word and a number
print(userName + " is " + str(userAge)) #21 -> "21"

# If using f formatting for output put the variable inside curly braces and any data type can be used
print(f"{userName} is {userAge}")

print()
print("2 + 2 = ", 2+2)
print()
# We can even do math inside the curly braces in f formatting
print(f"2 + 2 = {2+2}")


# Try theses on you own before submitting this lab
# Create a variable called myName and store your first name in it
myName = "Kavion Ashley"
# Create a variable called myPhrase and store in it a silly saying like apples and bananas
myPhrase = "To Make Money"
# Using comma separated arguments, display your name then the word likes and then the silly
# phrase (using the variables except for the word likes)
print(myName, "likes", myPhrase)
# Now use f formatting to display the same output
print(f"{myName} likes {myPhrase}")
# Next, create theses 4 variables A = 3, B = 4, C =2, D=5
#Now use print statements to display the correct answers to the equations (keep in mind the proper math order of operations)
A = 3
B = 4
C = 2
D = 5
# Display the answer to this equation 4A-2BC
y = (4*A)-(2*B*C)
print(y)
# Display the answer to this equation -> D plus B, divided by, A minus C
x= (D+B)/(A-C)
print(x)
