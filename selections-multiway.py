# Kavion Ashley
# 2-16-2025
# This program shows a multi-way decision
# This program will display an insurance premium based on age input

# Define main function
def main():
    # Declare constants for insurance premiums
    # 1000 for 40 or under, 2000 for over 40
    # Cut off age of 40
    YOUNGINSCOST = 1000
    MIDINSCOST = 1500
    OLDINSCOST = 2000
    CUTOFFAGEYOUNG = 35
    CUTOFFAGEMID = 59
    
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
    # If the user is 36-59 display the premium is 1500
    # If the user is over 59 display the premium is 2000
    # A multi-way decision has only 1 if, as many elifs as needed
    # and only 1 else
    # If the condition in the if is true the body of the if will execute
    # If the condition in the if is not true the interpreter will move on to
    # the elif and check that condition
    # If the condition if the elif is true the body of the elif will execute
    # This will continure for as many elifs as we have
    # The else will only execute if none of the conditions above it are true
    # Again only 1 can execute 
    if userAge <= CUTOFFAGEYOUNG:
        print(f"\nYour insurance premium is ${YOUNGINSCOST}")
    elif userAge <= CUTOFFAGEMID:
        print(f"\nYour insurance premium is ${MIDINSCOST}")
    else:
        print(f"\nYour insurance premium is ${OLDINSCOST}")


    # Display an outro
    print(f"\nThank you {userName} for your business!")

    

# Call or invoke the main function
main()
