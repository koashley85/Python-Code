#Kavion Ashley
#2-23-2025
#This program calculates a fine for speeding
#$50 fee plus $5 for every mph over speed limit
#Additional flat fee of $200 for over 90 mph
#This version uses a multi-way selection structure and a nested selection structure

def main():
    #declare constants for FLATFEE of 50, MPHOVER or 5, and OVER90FEE of 200
    FLATFEE = 50
    MPHOVER = 5
    OVER90FEE = 270
    MAXSPEED = 90
    #declare and intialize variables
    #ints for speedlimit, speed, totalFee  
    speedLimit = speed = totalFee = 0
    
    #Display Intro
    print("Welcome to my speed calculator program")
    print("You will enter a speed limit and speed the traveler was going")
    print("Then you will see the fine incurred\n\n")
 
    #Prompt for speed limit
    speedLimit = 70
    #int(input("Please enter the speed limit: "))
    #prompt for speed
    speed = int(input("Please enter the speed you were traveling: "))

    #use selection structure to determine if speeding or not
    #compare speedlimit to speed going
    #and display fine if speeding
    #if over limit but <= 90 set totalFee = (speed - speedlimit) * MPHOVER + FLATFEE
    #if over 90 mph set total fee = (speed - speedlimit) * MPHOVER + FLATFEE + OVER90FEE
    if speed > 0 and speed <= speedLimit:
        print("\n\nYou were not speeding, you are a safe driver!")        
    elif speed > speedLimit:
        if speed > MAXSPEED:
            print("\n\nWHAT, over 90! SLOW DOWN!")
            totalFee = (speed - speedLimit) * MPHOVER + FLATFEE + OVER90FEE
        else:
            totalFee = (speed - speedLimit) * MPHOVER + FLATFEE
        print(f"\nYou were speeding and your fee will be ${totalFee:,.2f}")
    else:
        print("The car isn't even mioving")
        
    #Display outro
    print("\n\nThank you for using my fine calculator")

main()

