#importing the time module

import time
from getpass import getpass

secret_word = getpass("Input the name of a fruit and Enter. It will be masked.. ")
print("")
#welcoming the user
print("******* Hangman *******")
print("")
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

#wait for 1 second
time.sleep(1)

print ("Start guessing the name of a fruit...")
time.sleep(0.5)

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in secret_word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char,end=""),    

        else:
    
        # if not found, print a dash
            print ("_",end=""),     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("You won")
    # exit the script
        break            
    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in secret_word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Wrong")  
 
    # how many turns are left
        print ("You have", + turns, 'more guesses' )
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose"  )
            print("The secret word is ", secret_word)