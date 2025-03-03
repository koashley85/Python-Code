# Kavion Ashley
# Date: 2-2-2025
# The program calculates the number of calories consumed by a customer
# based on the number of cookies the customer ate.


# Define main function
# Functions are containers for code
# Later in this course we will divide our code into several small managable chunks or functions
# In Python all code must be indented inside a function
def main():
    #Declare constants
    # each cookies is 75 calories
    # each soda have 300 calories
    CALORIES_PER_COOKIE = 70
    CALORIES_PER_SODA = 300

    # Declare and initialize variable
    # String var for name
    userName = ""
    # Whole num var for cookies eaten and calories consumed
    totalCalories=sodaCalories=sodaConsumed=sodaDranked=cookiesEaten = caloriesConsumed = 0

    #numFloat = 0.0
    
    #userName, sodaConsumed, cookiesEaten = "", 0
    
    # Display "WELCOME TO THE CALORIE COUNTER!!"
    print("WELCOME TO THE CALORIE COUNTER!!\n\n")

    # Prompt for name by displaying "Please enter your name:"
    userName = input("Please enter your name: ") #"Bob"
    # Prompt for cookies eaten by displaying "Please enter the number of cookies consumed:"
    # Written like this the input function executes first and returns the 3 as a string
    # The the string 4 is passed to the int function and it return the integer 4
    #cookiesEaten = int(input("Please enter the number of cookies consumed: ")) #"4" -> 4
    
    # Let's add a name to the question
    # The input function only accepts 1 argument - so no comma separated arguments
    # This will not work in input but would in a print    
    #cookiesEaten = int(input("Hi", userName, "Please enter the number of cookies consumed: "))
    # Using concatenation would work if the variable stores a string, but....no fun
    # cookiesEaten = int(input("Hi" + str(userName) + ",Please enter the number of cookies consumed: "))
    # This is why f formatting is so nice - no need to concatenate
    cookiesEaten = int(input(f"Hi {userName}, Please enter the number of cookies consumed: "))
    # sodaDranked = int(input("Hi" + str(userName) + ",Please enter the number of sodas dranked: "))
    sodaDranked = int(input(f"Hi {userName}, Please enter the number of sodas dranked: "))
    
    # We could type cast in a whole 2nd step or in the math - but ....
    #cookiesEaten = int(cookiesEaten) # "4" -> 4
    # Converting to an int here only does it for this moment in time
    # Does not change what is stored in var
    #caloriesConsumed = int(cookiesEaten) * 75
    #print(f"\nOkay {userName}, you consumed {caloriesConsumed} calories!")

    # Calculate calories consumed = cookies eaten * 75 calories per cookie
    
    caloriesConsumed = cookiesEaten * CALORIES_PER_COOKIE
    sodaCalories = sodaDranked * CALORIES_PER_SODA
    totalCalories = caloriesConsumed + sodaCalories

    # Display calories consumbed calling user by name
    print(f"\nOkay {userName}, you consumed {totalCalories} total calories!")
    # print(f"\nOkay", userName, "you consumed", {totalCalories}, "calories!")
    print(f"\nOkay {userName}, you consumed {caloriesConsumed} calories! from cookies")
    # print(f"\nOkay", userName, "you consumed", {caloriesConsumed}, "calories!")
    print(f"\nOkay {userName}, you consumed {sodaCalories} calories! from sodas")
    # print(f"\nOkay", userName, "you consumed", {sodaCalories}, "calories!")

    # Display outro
    print("Thank you for using my program!")



# Call or invoke main function
main()




#--Try this on your own----- Put these steps in the appropriate places above so the program makes sense and add the code under each step
# add a constant to store 300 calories in a soda
# add a variable for sodaConsumed
# ask the user how many sodas they drank
# calculate how many calories they drank
# Display total calories consumed which is cookie calories plus soda calories
