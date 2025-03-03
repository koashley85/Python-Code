#Kavion Ashley
# 2-23-2024
# For Loop Examples


def main():
    #This will be a counted loop
    #Also known as a for loop
    #A counted loop always execues a predetermined number of times
    #Range is built in function in python that allows us to repeat a loop a specific number of times
    #1 argument passed to range means repeat that many times
    #argument must be an integer
    for i in range(10):
        #anthing indented is the body of the loop
        #and what will repeat
        print("Happy Birthday")
        print("to you")

    print("\n")

    
    #Count out loud to 3 ---- You said 1, 2, 3 rigt? Of course you did, that is what we do as humans
    #The range function starts count at 0 though by default - and increments by 1 by default
    #The i is a placeholder variable that basically keeps track of each times the loop iterates
    #It doesn't have to be an i, it can be anything really. We will use other things later
    for i in range(3):
        print(i)  #This will display from 0 - 2 which is looping 3 times


    print("\n")


    #Now you can really see how useful the end keyword is that we learned earlier
    #When used in a loop it can allow every iteration of the loop to go on the same line
    for i in range(10):
        print(i, end = " ")


    print("\n\n")


    #Passing 2 arguments to the range function
    # - 1st is start position, 2nd stop position
    #it will count from and including the start, up to but not including the stop
    #This is 1-10 displayed
    for i in range(1,11):
        print(i, end = " ")

    print("\n")

    #Class try 5-23 on one line separated by tabs
    for i in range(5,24):
        print(i, end = "\t")

    print("\n\n")

    #Passing 3 arguments to the range function
    #1st is start position, 2nd is still the stop,
    #the third is now the step - or what to increment by instead of the default of 1
    #This will count by 2's
    for i in range(2,11,2):
        print(i)


    print("\n")
    
    #Class - display 5 a tab 10 a tab 15
    for i in range(5,16,5):
        print(i, end = "\t")


    print("\n")


    #What if we want to count backwards from 10 to 1, like a count down
    #If we use the only 2 arguments telling it to start at 10 and end on 1 (stop if 0) nothing will happen
    for i in range(10,0):
        print(i)

    print("\n")

    #Any time you want to count backward, even by only 1, you must add a negative step
    for i in range(10,0,-1):
        print(i)

    print("\n")


    #Class - display 10 tab 7 tab 4
    for i in range (10,3,-3):
        print(i, end ="\t")

    print("\n\n")




    #The for loop can also be used to iterate though a list
    #We will learn more about lists soon, but for now know what lists are items placed inside square brackets in Python
    #When we want to iterate through each item in a list we do not use the range function - we use the list
    for i in [-2,3,4,5]:  
        print(i**2)


    print("\n")


    #Usually the list is already in the program though like this
    numbers = [2,4,6,8]

    #To make the loop more readable we often use the words that make sense instead of just the generic i
    for num in numbers:
        print(num)

    print("\n")

    animals = ["cat", "dog", "bird"]

    for animal in animals:
        print(f"I love {animal}s")



    print("\n")



    #We often use loops to accumulate totals
    total = 0

    print(total) #0

    for i in range(5):
        #total += 10 is more common
        total = total + 10   #10 20 30 40 50
        print(total)


    print("\n")


    for i in range(5):
        #total +=i could also be used
        total = total + i
        print(total) #50 51 53 56 60


    print("\n")

    for i in range(1,6):
        print(total+i) #61 62 63....

    print("\n")


    #The arguments passed to the range function can be integers, or variables that store integers
    #Here we can use the users answers to questions as the start and stop positions

    start = int(input("What number do you want to start on?")) #1
    stop = int(input("What number do you want to end on?")) #10

    for i in range (start,stop+1):
        print(i)

    print("\n")

    for i in range (1,4,1):
        print("This is line",i) #This will print "This is Line i" value of i will change

    print("\n")


    for i in range (5,30,5):
        print(i,"\t||\t",i**2)  #This will print value of i then sqare the number

    print("\n")


               
    
main()



# Try this after the last print statement above and before calling main
# Use a for loop to display the example below (you cannot type the 1,2,3, you must use the i):
"""
This is line 1
This is line 2
This is line 3
"""
# Next add a for loop that will display the example below(hint, it displays from 5 to 25 by 5's and each of thos values that store integers

               
"""
5            ||          25
10           ||          100
15           ||          225
20           ||          400
25           ||          625
"""
