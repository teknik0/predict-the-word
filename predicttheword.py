import getpass
import random
import time
#gets your username in order to find file
user = getpass.getuser()

wordtxt = open("/Users/{}/Downloads/words1.txt".format(user), encoding='unicode_escape').read()

#turns words.txt into a list (of words)
list_of_words = wordtxt.splitlines()
#turns list into a string
def listToString(s): 
    str1 = ""     
    for ele in s: 
        str1 += ele       
    return str1
#returns false instead of true if an underscore is in the list
def listisnotunderscoresatall(e):
    t=True
    for i in e:
        if i == "_":
            t=False
    return t



#:) random time between messages because i feel like it
print("\nHello " + user + "!")
time.sleep(random.randint(1, 3))
print('\n\nthis game is called predict the word')
time.sleep(random.randint(1, 3))
print('you have to guess the word as it slowly appears on the screen')
time.sleep(random.randint(1, 3))  

#repeats game the amount of times input specifies
for i in range(int(input("Ok, lets start! how many times would you like to play?(One play session is about half a minute)"))):
    #takes a random word from list, lowercases it, and saves it to word variable
    wod = random.choice(list_of_words).lower()
    
    word=wod.strip()
    
    wordlen=len(word)
    
    listword=list(word)
    
    randlistlen=list(range(wordlen))
    
    random.shuffle(randlistlen)
    
    underscores="_"*wordlen
    #gets a list of underscores that gradually become the word
    underscoreslist=list(underscores)
    
    print("Game "+str(i+1)+" Has Started!")
    
    time.sleep(random.randint(1, 5))
    
    for o in range(wordlen):
        #for each cycle changes an underscore in underscores list
        #to a character that is in listword(word in list form)
        underscoreslist[randlistlen[o]] = listword[randlistlen[o]]
        
        print(listToString(underscoreslist))
        #if underscores list has no more underscores i.e. word fully uncovered
        if listisnotunderscoresatall(underscoreslist):
            print("Too late! You haven't guessed the word!")
        time.sleep(random.randint(1, 5))

    



