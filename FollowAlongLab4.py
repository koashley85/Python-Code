# Kavion Ashley
# 2-16-2025
# This program shows a two-way decision
# This program will display an insurance premium based on age input

# Define main function
def main():
    # Declare constants for insurance premiums
    # 1000 for 40 or under, 2000 for over 40
    # Cut off age of 40
    YOUNGINSCOST = 1000
    OLDINSCOST = 2000
    CUTOFFAGE = 40
    
    # Declate and initialize string for name
    # and whole var for user age
    userName = ""
    userAge = 0
    
    # Display Intro
    print("Welcome to the Insurance Quote Program\n")
    
    # Prompt for name
    userName = input("Please enter your name: ")
    # Prompt for age
    userAge = int(input(f"Hello {userName}, how old are you? "))
                  
    # Display premium based on age  
    # If the user is 40 or under display the premium is 1000
    # If the user is over 40 display the premium is 2000
    # A 2 way decision has an if and an else only
    # Create a condition tobe evaluated as true or false
    # If the condition is true the body of the if will execute
    # If the condition is not true the body of the else will execute
    # But only 1 or the other can execute, never both
    if userAge <= CUTOFFAGE:
        print(f"\nYour insurance premium is ${YOUNGINSCOST}")
    else:
        print(f"\nYour insurance premium is ${OLDINSCOST}")


    
    # Display an outro
    print(f"\nThany you {userName} for your business!")

    

# Call or invoke the main function
main()
