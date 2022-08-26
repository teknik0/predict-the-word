import random
import time
import os
import sys


def no_underscores(e):
    t=True
    for i in e:
        if i == "_":
            t=False
    return t

def list_to_string(s): 
    str1 = ""     
    for ele in s: 
        str1 += str(ele)       
    return str1


while True:
    try:
        #finds words1.txt in current directory
        with open(os.path.join(sys.path[0], "words1.txt"), "r") as f:
            wordtxt = (f.read())
    
        global list_of_words
        #turns words.txt into a list (of words)
        list_of_words = wordtxt.splitlines()

        break
    
    except:
            #file not found message
            print("Words file not found. \n Check if \"words1.txt\" is in the same directory as the .py file \n Retrying in 10 seconds")
            time.sleep(10)
            print("Retrying...")


#random time between messages because i feel like it
ee = bool(round(time.time())%2)
print("\n" "Hello! " * ee + "Welcome!" * (not ee))
time.sleep(random.randint(1, 3))
print('\nThis game is called predict the word')
time.sleep(random.randint(1, 3))
print('\nTry and guess the word as it slowly appears on the screen')
time.sleep(random.randint(1, 3))
print('\nTake too long, and you will lose')
time.sleep(random.randint(1, 3))  


#repeats game loop the amount of times input specifies
for i in range(int(input("\nOk, lets start! how many times would you like to play? (One play session is about half a minute) "))):
    #takes a random word from list and fixes it up
    word = random.choice(list_of_words).lower().strip()
    #generates shuffled numbers that are the same length as the word
    #for the randomized revealing of letters
    wordlen = len(word)
    
    randlen = list(range(wordlen))

    random.shuffle(randlen)
    
    #gets a string of underscores that gradually become the word
    underscores=list("_"*wordlen)
    #+1 to compensate for range starting at 0
    print(f"\nGame {i+1} Has Started!")
    
    time.sleep(random.randint(1, 5))
    
    
    #core game loop
    for o in range(wordlen):
        #for each cycle changes a random underscore
        #to the letter that is in the corresponding position
        underscores[randlen[o]] = word[randlen[o]]
        
        print(list_to_string(underscores))
        
        #if word revealed
        if no_underscores(underscores):
            print("Too late! You haven't guessed the word!")
        time.sleep(random.randint(1, 5))
print("GAME END")
