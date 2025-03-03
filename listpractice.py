#Kavion Ashley
#March 2 2025
# List Practice

def main():
    #This is a variable storing a single string
    fun = "I Love Python"

    #This is a list containing 3 items, all strings
    animals = ["dog", "cat", "bird"]

    #This is a list containg 3 items, all integers
    nums = [7,2,99]

    #Let's see how each displays
    print(fun)
    print(animals)
    print(nums)
    print("\n")


    #indexed positions
    #To be able to use data from a list we have to be able to access it and pull it out or put it in
    #Every item in a list has a numbered (indexed) positions, items are separated by commas
    #indexed positions start count at 0 from the left
    #So dog in the list of animals is in indexed position 0
    print(animals[0])
    print(animals[1])   #is cat
    print(animals[2])   #is bird

    #We can also access it from the right side or the end of the list using negative indices
    print(animals[-1])    #will display bird - the last item in the list (or first from the right)
    print(animals[-2])    #will display bird - the 2nd item in the list (or second from the right)



    #Now we will practice using various methods on our lists
    #A method changes a list instantly and permanently since lists are mutable
    #This is not the same on a variable storing a single value

    #Some methods cannot be passed any arguments, some must be passed arguments
    #And some can be passed arguments, but do not have to be
    #append adds to the end of a list - takes 1 argument
    animals.append("fish")
    print(animals)
    print("\n")

    #insert adds to a position in a list - must pass 2 arguments
    animals.insert(0,"lizard")
    print(animals)
    print("\n")

    #pop removes from the list - by default the last item if no arguments
    print(animals.pop())
    print(animals)
    print("\n")

    #pop can also remove a location if you pass it 1 argument
    print(animals.pop(0))
    print(animals)
    print("\n")

    #remove will also remove from a list - but a specific item passed to it
    animals.remove("cat")
    print(animals)
    print("\n")

    #del in an instruction not a method - can be used in a list or on a whole list
    del animals[1]
    print(animals)
    print("\n")

    #Let's put 2 things back in our list for the next part
    animals.append("bird")
    animals.append("cat")
    print(animals)
    print("\n")

    #The sort method will make it ascending (a-z) and store it that way
    animals.sort()
    print(animals)
    print("\n")

    # reverse reverses the list so
    # if you want z-a you must first sort it a-z
    animals.reverse()
    print(animals)
    print("\n")

    #We've only been using the list of strings, but it does the same thing with nums
    print(nums)
    nums.sort()  
    print(nums)
    print("\n")

    nums.reverse()
    print(nums)
    print("\n")

    #The sorted function will display A-Z but not store it that way
    print(sorted(animals))
    print(animals)

    print("\n")
    
    #The len function will count items in a list
    print(len(animals))
    print(len(nums))
    print("\n")

    #When you pass len a string - it counts number of characters in a string
    print(len(fun))
    print("\n")

    #The sum function is a fast way to add up a bunch of numbers stored in a list
    print(sum(nums))
    print("\n")

    #We can easily find an average of any amount of numbers stored in a list
    #by combining the sum and len functions
    print(sum(nums)/len(nums))

    print("\n")

    #We often loop through lists to make more effiecient code
    for animal in animals:
        print(f"I love {animal}")

    print("\n")


    for number in nums:
        print(number ** 3)

    print("\n")

    # Here's and example checking items in a list
    for num in nums:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")


    print("\n")

    myPets = ["dog", "dog", "dog", "goat", "cow", "fish", "dog", "fish", "pig", "fox"]

    pet = input("Enter a pet type you are curious about (e.g., cat, dog, hampster): ").lower()

    pet_counter = myPets.count(pet)
    if pet_counter == 0:
        print(f"Im surprised you never had a {pet}. You should give it a chance!")
    elif pet_counter == 1:
        print(f"You’ve had {pet} one time. You should get one more!")
    else:
        print(f"Congrats!!{pet_counter} {pet}'s is a good amount! Clearly, I love {pet}s as well!")



def getScores(): #Does not work this way
    #Declare and initialize empty list
    scores = []

    #print intro
    print("Welcome to my number sorting program!")

    for i in range(5):
       scores[i]= int(input("Please enter a score: ")) #"90" -> 90

    print(scores)
            



def getScores2():
    #Declare and initialize list with 5 ints
    scores = [0] * 5

    #print intro
    print("Welcome to my number sorting program!")

    for i in range(5):
       scores[i]= int(input("Please enter a score: ")) #"90" -> 90

    print(scores)




def getScores3():
    #Declare and initialize whole var to store how many scores
    numScores = 0
    #Declare and initialize empty list
    scores = []

    #print intro
    print("Welcome to my number sorting program!")


    #Prompt for how many scores
    numScores = int(input("How many scores do you have to enter? ")) #3

    for i in range(numScores):
        scores.append(int(input("Please enter a score:"))) #"90" -> [90] -> [90,85,98]

    print(scores)


def getScores4():
    #Declare and initialize whole var to store how many scores
    numScores = 0
    #Declare and initialize empty list
    score = [0] * 3

    #print intro
    print("Welcome to my number sorting program!")
    

    #Prompt for how many scores
    numScores = int(input("How many scores do you have to enter? ")) #3

    for i in range(numScores):
        scores.append(int(input("Please enter a score:"))) #"90" -> [90] -> [0,0,0,90,85,98]

    print(scores)
    

main()

# Add to this to the program inside main before submitting:
# Make a new list of animals you have had in your life in order like
# myPets = ["cat", "bird", "dog", "cat", "cat", "hamster", "dog", "dog", "dog", "dog"]
# Practice using the count method by asking the user to enter a pet type
# then use count to see how many of that type of pet you have had in you life and display
# a fun statement back to the user with the answer
# * if you have never had any pets just use my list
    
