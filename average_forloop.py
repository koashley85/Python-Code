# Kavion Ashley
# 2-23-2025
# This program finds an average of numbers entered by user 
# This version uses a for loop

def main():
    #Initialize variable
    howManyNumbers = 0
    number = average = total = 0.0

    #Display into
    print("Welcome to my average program!\n")
    
    #Prompt user for number of numbers
    howManyNumbers = int(input("How many numbers are there: ")) #3
    
    #Use a counted loop  to ask the user to enter the nubmers for as many times
    #as they said they have numbers
    for i in range(howManyNumbers):
        #Prompt user for a number
        number = float(input("Please enter a number: ")) #5 7 3
        total = total + number #5 12 15
        
    #Calculate the average
    average = total / howManyNumbers
    
    #Display average
    print(f"The average of your nubmers is {average}")
    #could have done math in {} - only if we need the answer only 1 time
    #print(f"The average of your numbers is {total / howManyNumbers}")
    
    #Display outro
    print("\nThanks, bye")


main()

#This version makes the user have to count the numbers in advance
#- not very user friendly
