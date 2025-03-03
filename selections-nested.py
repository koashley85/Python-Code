# Kavion Ashley
# 2-16-2025
# This program shows a multi-way decision. And a nested decision
# This program will display an insurance premium based on age input

# Define main function
def main():
    # Declare constants for insurance premiums
    # 1000 for 40 or under, 2000 for over 40
    # Cut off age of 40
    YOUNGINSCOSTSMOKER = 2000
    YOUNGINSCOSTNONSMOKER = 1000
    MIDINSCOSTSMOKER = 2500
    MIDINSCOSTNONSMOKER = 1500
    OLDINSCOSTSMOKER = 2000
    OLDINSCOSTNONSMOKER = 2000
    CUTOFFAGEYOUNG = 35
    CUTOFFAGEMID = 59
    
    # Declate and initialize string for name and smoker
    # and whole var for user age
    userName = smoker = ""
    userAge = 0
    
    # Display Intro
    print("Welcome to the Insurance Quote Program\n")
    
    # Prompt for name
    userName = input("Please enter your name: ")
    # Prompt for age
    userAge = int(input(f"Hello {userName}, how old are you? "))
    # Prompt user if they smoke
    smoker = input("Do you smoke, yes or no? ") #yea
                      
    # Display premium based on age  
    # If the user is 40 or under display the premium is 1000
    # If the user is 36-59 display the premium is 1500
    # If the user is over 59 display the premium is 2000

    #A nested decision is one decision in the body of another
    #If the user is 35 or under
        #check to see if the smoke
        #if the user smokes display youngsmoker premium
        #if they do not smoke display the youngnonsmoker premium
    #Else id user age is between 36 and 59 check to see if they smoke
        #check to see if the smoke
        #if the user smokes display.....
        #if they do not smoke display....
    #Otherwise they must be over 59
        #but we still have to check to see if they smoke
        #if the user smokes display....
        #if they do not smoke display...

   # This is the outer selection structure
    if userAge <= CUTOFFAGEYOUNG:
        # This is an inner selection structure
        # == means is equal to and is used for comparison
        if smoker == "yes":
            print(f"\nYour insurance premium is ${YOUNGINSCOSTSMOKER}")
        elif smoker == "no":
            print(f"\nYour insurance premium is ${YOUNGINSCOSTNONSMOKER}")
        else:
            print("You must enter yes or no")
    elif userAge <= CUTOFFAGEMID:
        if smoker == "yes":
            print(f"\nYour insurance premium is ${MIDINSCOSTSMOKER}")
        elif smoker == "no":
            print(f"\nYour insurance premium is ${MIDINSCOSTNONSMOKER}")
        else:
            print("You must enter yes or no")
    else:
        if smoker == "yes":
            print(f"\nYour insurance premium is ${OLDINSCOSTSMOKER}")
        elif smoker == "no":
            print(f"\nYour insurance premium is ${OLDINSCOSTNONSMOKER}")
        else:
            print("You must enter yes or no")


    # Display an outro
    print(f"\nThank you {userName} for your business!")

    

# Call or invoke the main function
main()
