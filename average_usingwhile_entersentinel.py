# Kavion Ashley
# 2-23-2025
# This program finds an average of numbers entered by user
# This verison uses a while loop
# and a enter as a sentinel


def main():
    #Initialize variable
    count = 0
    number = average = total = 0.0
    playagain="yes"

    #Display into
    print("Welcome to my average program!\n")

    while playagain == "yes":
        #Loop as long as user say yes they have more numbers
        #must seed the loop - must be true the first time
        number = "0"
        count = 0
        total = 0.0
        
        while number != "":
            #Prompt user for a number
            number = (input("Please enter a number <Enter to quit>: ")) #5 7 3 -1

            #selection structure to make sure only positive numbers get added
            if number != "":
                total = total + float(number) #"5" -> 5
                count = count + 1


        #Calculate the average
            average = total / count

        #Display average
        print(f"The average of your numbers is {average}")

      
        playagain = (input("Do you want to play again? yes or no ")) #5 7 3 -1


#Display outro
print("\nThanks, bye")


main()


#Try this
#Add a loop that asks the user if they want to start all over and if they say yes
#it starts over asking them to enter a number

