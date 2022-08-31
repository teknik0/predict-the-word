#os/sys for word1.txt locating, keyboard/threading for dynamic input
import random, time, os, sys, keyboard, threading

#thread function to let guesses be made asynchronously to word revealing
def guess_daemon():
    #when thread started, create a global guess variable
    global guess

    guess = ""
    #time.sleep used to limit usage
    #essentially, until ordered to terminate, do guess procedure if space is pressed
    while True:
        time.sleep(0.001)
        if end_thread.is_set():
            break
        #using space instead of enter because key inputs are queued in the terminal
        if keyboard.is_pressed("space"):
            daemon_turn.wait()  #"If it is not my turn yet, I will wait"
            not_questioning.clear() #"I am questioning now"
            guess = input(random.choice(awaiting)).strip() #calls for input, strips spaces because of the terminal input queue
            daemon_turn.clear() #"It is no longer my turn"
            not_questioning.set() #"I am done with my questioning"
            daemon_turn.wait() #"I will wait for my turn before doing more work"

#checks if containing underscores
def no_underscores(e):
    t=True
    for i in e:
        if i == "_":
            t=False
    return t

#returns list in str form
def stringed_list(s): 
    str1 = ""     
    for ele in s: 
        str1 += str(ele)       
    return str1

#sleep for a random number in a range, default 2-5
def reep(lower = 2, upper = 5):
    time.sleep(random.randint(lower, upper))

#words1.txt file locating procedure
while True:
    try:
        #searches for words1.txt in current directory, then reads to wordtxt variable
        with open(os.path.join(sys.path[0], "words1.txt"), "r") as f:
            wordtxt = (f.read())

        #formats wordtxt to a global list
        global list_of_words
        list_of_words = wordtxt.splitlines()
        #exits file locating procedure
        break
    
    #if file cannot be found
    except FileNotFoundError:
        #error text, retries loop after 10 seconds
        print("\nWords file not found. \n Check if the \"words1.txt\" is in the same directory as the .py file \n Retrying in 10 seconds")
        time.sleep(10)
        print("Retrying...")

#types of text, formatted into lists to allow random picking
greetings=["Hello!", "Welcome!", "HUMAN DETECTED", "Salutions!", "Welcome to Tasking Inc."]
assignments=["Your assignment today is to predict the word(s).", "As a new employee, you will need to undergo word prediction training.", "PREDICT WORDS, NOW!", "Our main event for the rest of time is word prediction"]
descriptions1=["Press space to freeze the word for a guess", "If you think you know the answer, press space, and then type it in.", "THINK YOU KNOW THE WORD? TO TYPE IT IN, PRESS SPACE"]
descriptions2=["and once you're done, hit enter to submit your guess.", "and once you're done, press enter to submit your guess.", "when you've got your answer laid out, all that's left to do is press enter.", "HITTING ENTER WILL SUBMIT YOUR WRITTEN GUESS", "after you've typed it out, just hit enter to unfreeze the word and submit your guess."]
guiding_stone=["The words will not always be fair to you, so watch out!", "Don't tell anyone I told you this, but you can queue your keyboard inputs.", "You can never know what's going to happen next, so always keep a finger over your space bar!"]
etc=["Take too long, and you will fail the task.", "Know better than to dally about, the words do not wait for no one!", "Remember, patience is virtue and good things come to those who wait... I think.", "There's no punishment for a wrong guess, so Predict away!"]
nope=["WRONG!", "that was... completely wrong", "Seriously? Why did we hire humans?", "Soooo close yet sooooo far", "Someone should take your keyboard away", ]
awaiting=["Your prediction?\n", "What do you think it is?\n", "Make this one count!\n", "INPUT:  ", "Guess:  ", "You think you got it? Give it your best shot\n", "All eyes on you!\n"]
trashed=["Too late! You haven't guessed the word! It was: {}", "The was word {}...", "Have you never seen the word {} before?", "OBLIVIOUS HUMAN! THE MOST PROBABLE OUTCOME WAS OBVIOUSLY {u}!!!", "the word was {}. That's right, {u}!!!"]
finish=["An astonishing success!", "Finally, a master of the letters!", "Pure Bliss", "Employee of the month!", "Thinking in the fourth dimension!", "A task completion to mark the new day!", "Congratulations!", "Masterful", "A professional indeed! Almost like we've paid you to be here...", "Terrific execution!", "Way to go!", "Everyone in the office knows your name! Exceptional work!"]
prescriptive_prescriptor=[" {} letters remaining", "This word has {} letters", "there are {} underscores here, go figure", "Uhh, im just the intern. There are {} letters in this word.", "this word is a measly * {} * underscores long", "Double credit for any {} letter long words!", "\nLucky you! last time I got a word anywhere near {} underscores was years ago!\n"]
today=["How many tasks do you have time for today? (one task takes about 20 seconds)", "How many tasks can you take on today? Please note 3 tasks take about a minute.", "HOW MANY TASKS TODAY, HUMAN?", "How many tasks do you have time for? 1 would take you no longer than half a minute!"]
value_error=["Please input a number, and only a number", "Sorry little trick, isn't it? Just put in a positive whole number please.", "Maybe your finger missed one of the keys? Next time input a whole positive number.", "SILLY HUMAN! CAN NOT EVEN INPUT A POSITIVE INTEGER.", "There are keys on your keyboard with numbers on them. Please use those keys"]
task_start=["task {} has started", "TASK {} COMMENCED", "here we go again, task {} starting", "task {}", "now task {}", "STARTING TASK #{}"]
assertion_error=["No tricks! Put in a positive number.", "Woah, what's happening? \n TIME REVERTING...", "Sorry, you can't undo a task", "The completed tasks are sent away. You can't take them back"]
ditched=["oh, so you just didn't want to play?", "Why would you do this?", "I pray you meant to input \"1\"", "No tasks??! They are a fun, I promise...", "Your loss"]

#random time between messages because i feel like it
print(f"\n{random.choice(greetings)}")
reep()
print(f"\n{random.choice(assignments)}")
reep()
print(f"\n{random.choice(descriptions1)}\n{random.choice(descriptions2)}")
reep()  
print(("\n" + random.choice(guiding_stone)) * random.randint(0,1))
reep()
print(f"\n{random.choice(etc)}")
reep()  

#create objects
#event objects for communication between threads
#thread object for asychronous process
end_thread=threading.Event()
not_questioning=threading.Event()
daemon_turn=threading.Event()
guess_taker=threading.Thread(target = guess_daemon)

#asks for how many times to run the main game, except blocks for invalid inputs
while True:
    try:
        
        loops = int(input(f"\n{random.choice(today)}\n"))
        assert loops >= 0
        repetitions = range(loops)
        break
    
    except ValueError:
        print(f"\n{random.choice(value_error)}")
        time.sleep(random.random()*random.randint(1,2))
        time.sleep(random.choice([random.random(), random.randint(1,2)]))

    except AssertionError:
        print(f"\n{random.choice(assertion_error)}")
        time.sleep(random.random()*random.randint(1,2))
        time.sleep(random.choice([random.random(), random.randint(1,2)]))
    

#repeats game loop the amount of times input specifies
#this primary loop is the setup loop
for i in repetitions:
    
    #creates word variable from a word from list_of_words
    word = random.choice(list_of_words).lower().strip()
    
    #length of the word for ease of access
    wordlen = len(word)
    
    #random list of numbers used for randomly revealing the word
    randlen = list(range(wordlen))
    random.shuffle(randlen)
    
    #gets a string of underscores that will gradually become the word
    underscores=list("_"*wordlen)
    
    #if this is the first time setup is being run, start guess_taker thread and no questioning is being done
    if i == 0:
        guess_taker.start()
        not_questioning.set()
    
    #reset guess and recent_guess for detecting new guesses
    guess = ""

    recent_guess = ""

    print(f"\n{random.choice(task_start).format(i+1)}")
    time.sleep(random.random() * random.randint(1,2))
    
    print(f"\n{stringed_list(underscores)} {random.choice(prescriptive_prescriptor).format(wordlen)}")
    
    #core game loop
    #loop being broken out of either leads to another repetition or program terminating
    for o in range(wordlen):
        #sleep allows time for guess to be made
        reep(1, 5)
        
        #closes questioning to halt accidental cheating
        daemon_turn.clear()        

        #"If you are questioning, I will wait for you to finish"
        not_questioning.wait()

        #for each cycle changes a random underscore
        #to the letter that is in the corresponding position
        #randlen (randomized list range of word length) allows for random picked each cycle
        underscores[randlen[o]] = word[randlen[o]]
        
        #if guess is word, break out of this loop
        if guess.lower() == word:
            
            print(f"\n{random.choice(finish)}")

            time.sleep(random.random())

            break
        
        #if not won, print if guess has changed
        elif guess != recent_guess:
            recent_guess = guess
            print(random.choice(nope) * random.randint(0,1))

        #if all underscores revealed (i.e. lost), break from this loop
        if no_underscores(underscores):
            print(random.choice(trashed).format(word, u = word.upper()))
            break
        
        #print the current state of the underscores (1 gets revealed each cycle)
        print(stringed_list(underscores))

        #reopens for questioning,
        #guess_taker thread will wait for reopening if word was frozen while questioning was closed
        daemon_turn.set()


try:
    #terminate guess_taker thread and notify of complete termination
    end_thread.set()
    daemon_turn.set()
    guess_taker.join()
    time.sleep(random.random()*random.randint(1,4))
    print("\nGAME END\n")
except RuntimeError:
    #if threads have not started/0 input as how many tasks to do
    print(f"\n{random.choice(ditched)}\n")
