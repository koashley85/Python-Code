# Kavion Ashley
# 2-23-2025
# This program presents a option with 4 possible states
# then tells the capital of their choice

# Define main funtion
def main():
    # Declare and initialize variables
    # strings for name and menuchoice
    userName = menuChoice = ""

    # Display Intro
    print("WELCOME TO THE CAPITAL PROGRAM!!\n")

    # Prompt for name
    userName = input("First, let me get your name: ")

    while menuChoice != "A" and menuChoice != "B" and menuChoice != "C" and menuChoice != "D":
        # Display state options
        print("\nPlease choose from the following menu: ")
        print("A) PA\nB) SC \nC) GA \nD) FL")

        # Prompt for menuchoice
        menuChoice = input("\nEnter your choice here: ")

        # Selection structure to determine which capital to display to user
        if menuChoice == "A" or menuChoice == "a" or menuChoice == "PA":
            print("The capital of Pennsylvania is Harrisburg")
        elif menuChoice =="B" or menuChoice == "b" or menuChoice == "SC":
            print("The capital of Pennsylvania is Harrisburg")
        elif menuChoice =="C" or menuChoice == "c" or menuChoice == "GA":
            print("The capital of Georgia is Atlanta")
        elif menuChoice =="D" or menuChoice == "d" or menuChoice == "FL":
            print("The capital of Florida is Tallahassee")
        else:
            print("Sorry, you must choose A, B, C, or D.")

    # Display outro
    print(f"\nThank you {userName} for playing my state capitals game!")



# Call main function
main()
